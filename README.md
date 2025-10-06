# 🧮 Professional CLI Calculator

A **professional-grade command-line calculator** built in Python with a modular design, complete test coverage, and continuous integration (CI) via GitHub Actions.

---

## 🚀 Features

- **REPL Interface:** Interactive “Read–Eval–Print” loop for continuous calculations.
- **Arithmetic Operations:** Addition, subtraction, multiplication, and division.
- **Robust Error Handling:**
  - LBYL (Look Before You Leap) for input validation.
  - EAFP (Easier to Ask Forgiveness than Permission) for safe exception handling.
- **Calculation History:** View all calculations performed during a session.
- **Special Commands:**
  - `help` — shows instructions  
  - `history` — shows session history  
  - `exit` or `quit` — exits gracefully  
- **Comprehensive Unit Tests:** 100% test coverage verified by `pytest` and `pytest-cov`.
- **Automated CI Pipeline:** GitHub Actions run all tests and enforce full coverage on every push.

---


## Setup Instructions

### Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # macOS/Linux
# venv\Scripts\activate        # Windows

### Install dependencies
pip install -U pip
pip install pytest pytest-cov

### Run the Calculator
python -m app.calculator

Example usage inside the REPL:
calc> add 2 3
= 5
calc> 9 / 3
= 3
calc> history
1. 2 add 3 = 5
2. 9 / 3 = 3
calc> exit
Goodbye!

---

## Run Tests and Check Coverage

pytest --cov=app --cov-report=term-missing

To enforce 100% coverage:
pytest --cov=app --cov-fail-under=100

Output example:
---------- coverage: platform darwin, python 3.11 ----------
Name                          Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------
app/calculator/__init__.py        51      0     12      0   100%
app/calculation/__init__.py       33      0     10      0   100%
app/operation/__init__.py         25      0      2      0   100%
---------------------------------------------------------------
TOTAL                            109      0     24      0   100%

---

## Continuous Integration (CI)

This project uses **GitHub Actions** to automatically:
- Run all unit tests.
- Verify code coverage.
- Fail the build if coverage < 100%.

Workflow file:  
.github/workflows/python-app.yml

---

