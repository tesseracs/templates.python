"""Helpers that turn template data into console output."""

from app.project import ProjectSnapshot


def format_summary(project: ProjectSnapshot) -> str:
    completed = sum(task.status == "done" for task in project.tasks)
    return "\n".join(
        [
            f"Project: {project.name}",
            f"Goal: {project.goal}",
            f"Progress: {completed}/{len(project.tasks)} tasks completed",
        ]
    )


def format_next_steps(project: ProjectSnapshot) -> str:
    lines = ["Next steps:"]
    for task in project.tasks:
        if task.status != "done":
            lines.append(f"- {task.title} ({task.owner})")
    return "\n".join(lines)
