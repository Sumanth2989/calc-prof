import builtins
from io import StringIO
from contextlib import redirect_stdout
from app.calculator import Calculator, main as calc_main


def run_scripted_session(inputs):
    """Feed inputs to the REPL and capture output safely (no print recursion)."""
    calc = Calculator()
    it = iter(inputs)

    def fake_input(prompt=""):
        try:
            return next(it)
        except StopIteration:
            # End the session gracefully by simulating Ctrl-D
            raise EOFError

    out = StringIO()
    orig_input = builtins.input
    try:
        builtins.input = fake_input
        with redirect_stdout(out):
            calc.run()
    finally:
        builtins.input = orig_input

    return out.getvalue()


def test_help_and_exit():
    output = run_scripted_session(["help", "exit"])
    assert "Commands:" in output
    assert "Goodbye!" in output


def test_basic_calculations_and_history():
    output = run_scripted_session(["add 2 3", "history", "quit"])
    assert "= 5" in output
    assert "1. 2 add 3 = 5" in output


def test_infix_and_errors():
    output = run_scripted_session(["2 / 0", "2 ^ 3", "", "exit"])
    assert "Error: Cannot divide by zero" in output
    assert "Input error: Unsupported operator" in output


# ---- New tests to close coverage gaps ----

def test_ctrl_d_immediately_exits():
    """Cover the EOFError branch at the first input call."""
    out = StringIO()

    def raise_eof(_prompt=""):
        raise EOFError

    orig_input = builtins.input
    try:
        builtins.input = raise_eof
        with redirect_stdout(out):
            Calculator().run()
    finally:
        builtins.input = orig_input

    s = out.getvalue()
    assert "Welcome to the Professional CLI Calculator!" in s
    assert "Goodbye!" in s


def test_keyboard_interrupt_path():
    """Cover the KeyboardInterrupt branch."""
    out = StringIO()

    def raise_kbi(_prompt=""):
        raise KeyboardInterrupt

    orig_input = builtins.input
    try:
        builtins.input = raise_kbi
        with redirect_stdout(out):
            Calculator().run()
    finally:
        builtins.input = orig_input

    s = out.getvalue()
    assert "Welcome to the Professional CLI Calculator!" in s
    assert "Goodbye!" in s


def test_unexpected_error_branch(monkeypatch):
    """Force an unexpected exception to cover the catch-all except block."""
    from app import calculator as calc_mod

    def boom(_tokens):
        raise RuntimeError("boom")

    monkeypatch.setattr(calc_mod.CalculationFactory, "from_tokens", boom)
    output = run_scripted_session(["anything", "exit"])
    assert "Unexpected error: boom" in output


def test_main_function_path():
    """Execute main() directly to cover the main wrapper line(s)."""
    out = StringIO()

    # Feed a quick 'exit' so main() returns immediately after greeting.
    it = iter(["exit"])

    def fake_input(_prompt=""):
        try:
            return next(it)
        except StopIteration:
            raise EOFError

    orig_input = builtins.input
    try:
        builtins.input = fake_input
        with redirect_stdout(out):
            calc_main()
    finally:
        builtins.input = orig_input

    s = out.getvalue()
    assert "Welcome to the Professional CLI Calculator!" in s
    assert "Goodbye!" in s

def test_history_when_empty():
    # Immediately ask for history, then exit. This covers the "no history yet" branch.
    output = run_scripted_session(["history", "exit"])
    assert "(no calculations yet)" in output

