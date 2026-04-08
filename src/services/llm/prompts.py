from __future__ import annotations

import json

from src.types.contracts import CoachingOutput


SYSTEM_PROMPT = """You are LeetCode Coach, an interview-focused DSA coach.

Your job is to help a coding interview candidate reason about a LeetCode-style problem.
You are not primarily a code generator.
You should coach how to think through the problem from brute force to optimal.

Rules:
- Return JSON only.
- Do not wrap the JSON in markdown.
- Do not include commentary outside the JSON object.
- Focus on interview reasoning, tradeoffs, and edge cases.
- Do not provide full code unless the user explicitly asks for code.
- Keep the explanation concrete and practical for a live interview.
- Recommended patterns should use common DSA terms like BFS, DFS, DP, Graph, Heap, Two Pointers, Sliding Window, Binary Search, Greedy, Backtracking, Trie, Union Find.
- Hint sequence must go from subtle to more direct.
"""


def build_problem_analysis_prompt(problem_text: str) -> str:
	schema = CoachingOutput.model_json_schema()
	compact_schema = json.dumps(schema, indent=2)
	return f"""Analyze the following coding interview problem and return a JSON object that matches the schema exactly.

Problem:
{problem_text}

Return requirements:
- Produce valid JSON only.
- Every field in the schema must be present.
- Keep problem_summary concise.
- pattern_reason should connect the input constraints or structure to the recommended patterns.
- brute_force_approach and optimal_approach should explain reasoning, not code.
- time_complexity and space_complexity should be short strings such as O(n log n).
- Provide 3 to 5 progressive hints.
- Provide 3 to 5 likely follow-up questions.
- Provide 3 to 6 common mistakes or edge cases.

JSON schema:
{compact_schema}
"""
