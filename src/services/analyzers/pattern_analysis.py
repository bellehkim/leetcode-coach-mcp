from __future__ import annotations

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.services.llm.claude_client import ClaudeClient


def classify_patterns(problem_text: str, client: ClaudeClient | None = None) -> dict[str, object]:
    response = analyze_problem_text(problem_text, client=client)
    return {
        "recommended_patterns": response.coaching.recommended_patterns,
        "pattern_reason": response.coaching.pattern_reason,
    }