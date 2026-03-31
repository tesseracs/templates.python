"""Small OOP example imported by `main.py`."""


class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f"Hello from {self.name} (Python template)"
