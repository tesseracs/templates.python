# Tesseracs - Python Template

A small but real Python starter for [Tesseracs](https://github.com/tesseracs) chat sessions.

Clone URL: `https://github.com/tesseracs/templates.python`

## What this template shows

- A tiny package layout in `app/` instead of keeping all logic in one file.
- A simple domain model plus rendering helpers.
- A `run.sh` entry point that still works for quick experiments.

## Layout

- `app/__main__.py` - application entry point for `python -m app`.
- `app/project.py` - sample project/task data model used by the template.
- `app/rendering.py` - formatting helpers for summaries and next steps.
- `main.py` - thin compatibility wrapper for direct `python main.py` runs.
- `requirements.txt` - optional dependencies; safe to leave empty.
- `run.sh` - installs `requirements.txt` when needed and runs the app.

## Run

```sh
./run.sh
```

Or run it directly:

```sh
python -m app
```

## Suggested next edits

- Rename `ProjectSnapshot` fields to match your project.
- Replace the sample tasks with real work items.
- Add tests once the template becomes project-specific.
