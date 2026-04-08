from __future__ import annotations

from src.services.analyzers.followup_analysis import generate_followups as generate_followups_service


def generate_followups(problem_text: str) -> dict[str, object]:
	return generate_followups_service(problem_text)
