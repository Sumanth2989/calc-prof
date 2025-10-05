import pytest
from app.calculation import Calculation, CalculationFactory


@pytest.mark.parametrize(
    "tokens,expected",
    [
        ("add 2 3".split(), 5.0),
        ("2 + 3".split(), 5.0),
        ("7 - 2".split(), 5.0),
        ("multiply 3 4".split(), 12.0),
        ("9 / 3".split(), 3.0),
    ],
)
def test_factory_and_execute(tokens, expected):
    calc = CalculationFactory.from_tokens(tokens)
    assert isinstance(calc, Calculation)
    assert calc.execute() == expected


def test_unsupported_operator():
    with pytest.raises(ValueError):
        Calculation("^", 2, 3).execute()


@pytest.mark.parametrize("inp", [[], ["add", "2"], ["2", "+"], ["2", "+", "3", "4"]])
def test_bad_token_counts(inp):
    with pytest.raises(ValueError):
        CalculationFactory.from_tokens(inp)


def test_non_numeric_operands():
    with pytest.raises(ValueError):
        CalculationFactory.from_tokens(["add", "a", "1"])
