"""Calculator REPL and history management."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from app.calculation import Calculation, CalculationFactory


@dataclass
class Calculator:
    history: List[Calculation] = field(default_factory=list)

    def add_to_history(self, calc: Calculation, result: float) -> None:
        self.history.append(calc)

    def get_history_lines(self) -> List[str]:
        if not self.history:
            return ["(no calculations yet)"]
        return [f"{i+1}. {c.a:g} {c.operator} {c.b:g} = {c.execute():g}" for i, c in enumerate(self.history)]

    def run(self) -> None:
        print("Welcome to the Professional CLI Calculator! Type 'help' for instructions.")
        while True:
            try:
                line = input("calc> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

            if not line:
                continue

            lower = line.lower()
            if lower in {"exit", "quit"}:
                print("Goodbye!")
                break
            if lower == "help":
                self._print_help()
                continue
            if lower == "history":
                for h in self.get_history_lines():
                    print(h)
                continue

            tokens = line.split()
            try:
                calc = CalculationFactory.from_tokens(tokens)
                result = calc.execute()
                print(f"= {result:g}")
                self.add_to_history(calc, result)
            except ZeroDivisionError as zde:
                print(f"Error: {zde}")
            except ValueError as ve:
                print(f"Input error: {ve}")
            except Exception as exc:
                print(f"Unexpected error: {exc}")

    @staticmethod
    def _print_help() -> None:
        print(
            """
Commands:
  help                 Show this message
  history              Show prior calculations for this session
  exit / quit          Exit the calculator

You can enter expressions in two styles:
  1) Verb-first:       add 2 3      | subtract 7 2 | multiply 3 4 | divide 9 3
  2) Infix (spaced):   2 + 3        | 7 - 2        | 3 * 4        | 9 / 3
            """.strip()
        )


def main() -> None:
    Calculator().run()


if __name__ == "__main__":  # pragma: no cover
    main()
