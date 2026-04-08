from __future__ import annotations

from src.types.contracts import CoachingOutput


def render_markdown_summary(coaching: CoachingOutput) -> str:
	sections = [
		"# LeetCode Coach Output",
		f"## Problem Summary\n{coaching.problem_summary}",
		"## Recommended Patterns\n" + "\n".join(f"- {pattern}" for pattern in coaching.recommended_patterns),
		f"## Why These Patterns Fit\n{coaching.pattern_reason}",
		f"## Brute Force Approach\n{coaching.brute_force_approach}",
		f"## Optimal Approach\n{coaching.optimal_approach}",
		f"## Time Complexity\n{coaching.time_complexity}",
		f"## Space Complexity\n{coaching.space_complexity}",
		"## Progressive Hints\n" + "\n".join(f"- {hint}" for hint in coaching.hint_sequence),
		"## Follow-up Questions\n" + "\n".join(f"- {question}" for question in coaching.follow_up_questions),
		"## Common Mistakes\n" + "\n".join(f"- {mistake}" for mistake in coaching.common_mistakes),
	]
	return "\n\n".join(sections)
