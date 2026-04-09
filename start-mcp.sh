#!/bin/zsh
set -a
source /Users/belle/leetcode-coach-mcp/.env
set +a

cd /Users/belle/leetcode-coach-mcp
exec ./venv/bin/python -m src.main
