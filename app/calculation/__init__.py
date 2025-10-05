"""Calculation objects and factory.

- Calculation: immutable record of an operation and its operands.
- CalculationFactory: creates Calculation from user input.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, List

from app.operation import add, subtract, multiply, divide

OperationFn = Callable[[float, float], float]


@dataclass(frozen=True)
class Calculation:
    operator: str
    a: float
    b: float

    def execute(self) -> float:
        mapping: Dict[str, OperationFn] = {
            "add": add,
            "+": add,
            "subtract": subtract,
            "-": subtract,
            "multiply": multiply,
            "*": multiply,
            "divide": divide,
            "/": divide,
        }
        if self.operator not in mapping:
            raise ValueError(f"Unsupported operator: {self.operator}")
        return mapping[self.operator](self.a, self.b)


class CalculationFactory:
    """Factory to build Calculations from user input tokens."""

    @staticmethod
    def from_tokens(tokens: List[str]) -> Calculation:
        if not tokens:
            raise ValueError("Empty input")

        if tokens[0] in {"add", "subtract", "multiply", "divide", "+", "-", "*", "/"}:
            if len(tokens) != 3:
                raise ValueError("Expected format: <op> <a> <b>")
            op, a_str, b_str = tokens
        else:
            if len(tokens) != 3:
                raise ValueError("Expected format: <a> <op> <b>")
            a_str, op, b_str = tokens

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError as exc:
            raise ValueError("Operands must be numbers") from exc

        return Calculation(op, a, b)
