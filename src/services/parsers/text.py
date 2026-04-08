from __future__ import annotations

import json
from typing import Any


def parse_json_text(raw_text: str) -> dict[str, Any]:
	text = raw_text.strip()
	if not text:
		raise ValueError("Response text cannot be empty.")
	return json.loads(text)
