#!/bin/sh
set -e
# Install deps when present (Tesseracs Python image has uv + venv on PATH)
if [ -f requirements.txt ] && [ -s requirements.txt ]; then
  uv pip install -q -r requirements.txt
fi
python main.py
