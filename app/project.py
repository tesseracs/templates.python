"""Sample domain objects for the Python template."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    title: str
    status: str
    owner: str


@dataclass(frozen=True)
class ProjectSnapshot:
    name: str
    goal: str
    tasks: list[Task]


def build_sample_project() -> ProjectSnapshot:
    return ProjectSnapshot(
        name="Tesseracs template refresh",
        goal="Turn the repository into a practical starting point",
        tasks=[
            Task("Improve README guidance", "done", "docs"),
            Task("Add reusable modules", "done", "template"),
            Task("Replace sample data", "next", "you"),
        ],
    )
