"""Tesseracs Python session starter — imports a sibling module."""

from greeting import Greeter


def main() -> None:
    g = Greeter("Tesseracs")
    print(g.greet())


if __name__ == "__main__":
    main()
