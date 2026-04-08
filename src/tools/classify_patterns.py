from __future__ import annotations

from src.services.analyzers.pattern_analysis import classify_patterns as classify_patterns_service


def classify_patterns(problem_text: str) -> dict[str, object]:
	return classify_patterns_service(problem_text)
