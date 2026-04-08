from __future__ import annotations

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.services.llm.claude_client import ClaudeClient


def generate_followups(problem_text: str, client: ClaudeClient | None = None) -> dict[str, object]:
    response = analyze_problem_text(problem_text, client=client)
    return {
        "hint_sequence": response.coaching.hint_sequence,
        "follow_up_questions": response.coaching.follow_up_questions,
        "common_mistakes": response.coaching.common_mistakes,
    }