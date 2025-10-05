"""Operation functions for the calculator.


Demonstrates EAFP (divide) and keeps simple, pure functions for testability.
"""
from typing import Union


Number = Union[int, float]




def _coerce_number(value: object) -> float:
"""LBYL-style helper: validate input is numeric, raise TypeError if not."""
if isinstance(value, (int, float)):
return float(value)
# LBYL guard: not numeric -> raise consistently
raise TypeError(f"Non-numeric value: {value!r}")




def add(a: Number, b: Number) -> float:
a = _coerce_number(a)
b = _coerce_number(b)
return a + b




def subtract(a: Number, b: Number) -> float:
a = _coerce_number(a)
b = _coerce_number(b)
return a - b




def multiply(a: Number, b: Number) -> float:
a = _coerce_number(a)
b = _coerce_number(b)
return a * b




def divide(a: Number, b: Number) -> float:
"""EAFP-style divide: attempt then handle ZeroDivisionError."""
a = _coerce_number(a)
b = _coerce_number(b)
try:
return a / b
except ZeroDivisionError as exc: # EAFP showcase
raise ZeroDivisionError("Cannot divide by zero") from exc