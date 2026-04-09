# LeetCode Coach MCP

LeetCode Coach MCP is a Python MCP server that turns LeetCode-style problem statements into structured interview coaching output. It is designed for candidates who want help reasoning about a problem in an interview, not for blindly generating code.

The MVP focuses on one strong workflow: take a problem description, classify the right DSA patterns, explain why they fit, walk from brute force to optimal, surface hints, propose likely follow-ups, and warn about common mistakes.

## Project Overview

- Python MCP server using Claude through the Anthropic SDK
- Pydantic contracts for stable structured output
- Thin MCP tool wrappers over a modular service layer
- Local `run.py` flow for testing before MCP integration
- Namespace-package layout under `src/` with no required `__init__.py` files
- Architecture that leaves room for future skills usage

## Architecture

```text
src/
  config.py                         Environment-based configuration
  main.py                           MCP server entry point
  server.py                         Shared MCP server builder
  types/contracts.py                Stable Pydantic response models
  services/
    analyzers/problem_analysis.py   Main orchestration service
    analyzers/pattern_analysis.py   Pattern-specific projection
    analyzers/followup_analysis.py  Hint/follow-up projection
    cleaners/problem_cleaner.py     Problem text cleanup
    formatters/markdown.py          Human-readable local output
    formatters/json_bundle.py       JSON serialization helper
    llm/prompts.py                  JSON-only coaching prompt builder
    llm/claude_client.py            Claude API communication only
    llm/mock_client.py              Deterministic mock client for demos
  tools/
    analyze_problem.py              Full-analysis MCP wrapper
    classify_patterns.py            Pattern MCP wrapper
    generate_hints.py               Hint MCP wrapper
    generate_followups.py           Follow-up MCP wrapper
run.py                              Local CLI runner
tests/                              Unit and MCP smoke tests
```

The project uses Python namespace packages under `src/`, so package marker files are intentionally omitted.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add environment variables in `.env`:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
CLAUDE_MODEL=claude-haiku-4-5-20251001
MCP_SERVER_NAME=leetcode-coach-mcp
```

## Usage

Run locally with inline text:

```bash
./venv/bin/python run.py --text "Given an array of integers nums and a target, return indices of the two numbers that add up to target."
```

Run locally without Anthropic using mock mode:

```bash
./venv/bin/python run.py --mock --format markdown --text "Given an array of integers nums and a target, return indices of the two numbers that add up to target."
```

Run locally with a file and markdown output:

```bash
./venv/bin/python run.py --file path/to/problem.txt --format markdown
```

Start the MCP server over stdio:

```bash
./venv/bin/python -m src.main
```

## MCP Tools

- `analyze_problem_tool`: full coaching output
- `classify_patterns_tool`: recommended patterns plus reasoning
- `generate_hints_tool`: hint sequence only
- `generate_followups_tool`: follow-up questions and common mistakes

## Example Output

```json
{
  "ok": true,
  "result": {
    "problem_summary": "Find two array values whose sum equals the target and return their indices.",
    "recommended_patterns": ["Hash Map"],
    "pattern_reason": "You need fast complement lookup while scanning the array once.",
    "brute_force_approach": "Check every pair of indices and test whether the values sum to the target.",
    "optimal_approach": "Track prior values in a hash map and look up the needed complement at each step.",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "hint_sequence": [
      "Start by thinking about the simplest way to check all pairs.",
      "Ask what information would let you avoid rechecking old numbers.",
      "A map from seen value to index gives constant-time complement lookup."
    ],
    "follow_up_questions": [
      "What changes if the input array is sorted?",
      "How would you handle multiple valid pairs?",
      "Can you return the values instead of the indices?"
    ],
    "common_mistakes": [
      "Reusing the same element twice.",
      "Returning values instead of indices.",
      "Dropping duplicate handling when values repeat."
    ]
  },
  "cleaned_problem": "Given an array of integers nums and a target, return indices of the two numbers that add up to target."
}
```

## Testing

Run:

```bash
./venv/bin/python -m pytest
```

The service-layer tests use the mock client, so they do not need a live API key.
The suite also includes an MCP smoke test that verifies the real server entrypoint registers the expected tools and starts with stdio transport.
The local CLI supports `--mock` for demoing the project without an Anthropic key.

## Future Improvements

- Add response caching for repeated local experiments
- Add richer prompt variants for specific interview styles
- Add optional code-generation mode behind an explicit flag
- Add first-class `.claude/skills` integration once the workflows stabilize
