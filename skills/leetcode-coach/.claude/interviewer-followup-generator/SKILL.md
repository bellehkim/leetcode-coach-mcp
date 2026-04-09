---
name: interviewer-followup-generator
description: "Use when generating interviewer-style follow-up questions, pitfalls, and deeper discussion prompts for a coding problem."
---

# Interviewer Follow-up Generator

Use this skill when the goal is to simulate the next questions an interviewer might ask after the candidate explains an approach.

## Responsibilities

- Generate realistic follow-up questions tied to the original problem and chosen solution direction
- Cover likely extensions around constraints, scalability, alternative data structures, and implementation tradeoffs
- Include common mistakes, edge cases, and failure modes the candidate should be prepared to discuss
- Keep the follow-ups relevant to technical interview prep rather than turning them into generic brainstorming

## Output Style

- Favor short, natural interviewer-style prompts
- Ask questions that pressure-test reasoning, not just recall
- Include edge cases and pitfalls alongside follow-up prompts
- Keep the tone practical and specific to the problem at hand

## Alignment With This Project

- This skill maps most directly to `follow_up_questions`, `common_mistakes`, and often `hint_sequence`
- It should support the behavior exposed by `generate_followups_tool`
- It should make the candidate think one layer deeper instead of handing them the final answer
