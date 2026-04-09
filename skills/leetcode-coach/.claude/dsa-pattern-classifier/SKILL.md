---
name: dsa-pattern-classifier
description: "Use when identifying the best DSA patterns for a LeetCode-style problem and explaining why they fit."
---

# DSA Pattern Classifier

Use this skill when the goal is to identify the best interview patterns for a LeetCode-style problem before diving into implementation details.

## Responsibilities

- Restate the problem shape in practical interview language
- Select the top one to three relevant patterns such as DFS, BFS, DP, Graph, Heap, Sliding Window, Two Pointers, Binary Search, Greedy, Backtracking, Trie, Union Find, or Hash Map
- Explain why those patterns fit the constraints, input structure, and search space
- Distinguish between plausible patterns and the strongest recommended pattern
- Avoid jumping directly to full code unless the user explicitly asks for it

## Output Style

- Keep the answer concise and interview-oriented
- Prefer concrete pattern names over vague descriptions
- Surface tradeoffs when multiple patterns are viable
- Mention edge cases or input constraints that could change the best pattern choice

## Alignment With This Project

- This skill maps most directly to `recommended_patterns` and `pattern_reason`
- It should support the behavior exposed by `classify_patterns_tool`
- It should help the user reason about the problem, not just label it mechanically
