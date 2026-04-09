# LeetCode Coach Skills

This folder holds Claude skill definitions that match the current LeetCode Coach MCP product direction.

## Purpose

These skills are meant to reinforce the same coaching behavior used by the application:

- classify the right DSA patterns
- guide the user from brute force to optimal
- generate interviewer-style follow-up questions and likely mistakes
- stay interview-focused instead of defaulting to full code generation

## Skill Set

- `dsa-pattern-classifier`: focuses on pattern selection and justification
- `brute-to-optimal-coach`: focuses on reasoning from naive to strong solution design
- `interviewer-followup-generator`: focuses on follow-up questions, hints, and pitfalls

## Project Alignment

These skills align with the main structured coaching fields used by the server:

- `recommended_patterns`
- `pattern_reason`
- `brute_force_approach`
- `optimal_approach`
- `hint_sequence`
- `follow_up_questions`
- `common_mistakes`

They are designed to stay compatible with the current architecture in `src/services/` and with future `.claude/skills` usage.
