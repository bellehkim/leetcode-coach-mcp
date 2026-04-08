from __future__ import annotations

from src.types.contracts import AnalysisResponse


def build_json_bundle(response: AnalysisResponse) -> dict:
	return response.model_dump()
