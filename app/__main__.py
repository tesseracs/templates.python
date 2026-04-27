"""Package entry point used by `python -m app`."""

from app.project import build_sample_project
from app.rendering import format_next_steps, format_summary


def main() -> None:
    project = build_sample_project()
    print(format_summary(project))
    print()
    print(format_next_steps(project))


if __name__ == "__main__":
    main()
