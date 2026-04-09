---
name: brute-to-optimal-coach
description: "Use when coaching a candidate from a brute-force idea toward an interview-ready optimal approach."
---

# Brute to Optimal Coach

Use this skill when the goal is to coach a candidate from an initial correct idea toward an interview-ready optimal approach.

## Responsibilities

- Start from a plausible brute-force or naive baseline
- Explain why the brute-force approach is valid before criticizing it
- Identify the bottleneck or repeated work that makes the baseline too slow or too expensive
- Guide the candidate toward the right optimization insight, pattern, or data structure
- Explain the resulting optimal approach in reasoning terms, not as a code dump
- Include time and space complexity for the optimal direction and mention brute-force complexity when it helps the coaching narrative

## Output Style

- Move in clear steps from baseline to improved solution
- Keep the explanation practical for a live interview conversation
- Emphasize the insight that unlocks the optimization
- Avoid full code unless the user explicitly asks for implementation

## Alignment With This Project

- This skill maps most directly to `brute_force_approach`, `optimal_approach`, `time_complexity`, and `space_complexity`
- It should reinforce the product principle of coaching reasoning instead of solving the problem by default
- It should fit the output expected from the main `analyze_problem_tool`
