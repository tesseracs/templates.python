#!/bin/sh
set -e

# Install deps only when the template actually needs them.
if [ -f requirements.txt ] && [ -s requirements.txt ]; then
  python -m pip install -q -r requirements.txt
fi

python -m app
