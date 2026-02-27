"""pytest content module — pytest testing from beginner to mid-level."""

from __future__ import annotations

from generator.models import NotebookSpec, PracticeProblem, TopicSection


def get_pytest_spec() -> NotebookSpec:
    """Return a complete NotebookSpec for the pytest notebook."""
    return NotebookSpec(
        title="pytest — Testing from Beginner to Mid-Level",
        filename="05_pytest_testing.ipynb",
        strategy_tips=_strategy_tips(),
        sections=_beginner_sections() + _mid_level_sections(),
        mock_test=_mock_test(),
        cheat_sheet=_cheat_sheet(),
    )


# ---------------------------------------------------------------------------
# Strategy tips
# ---------------------------------------------------------------------------

def _strategy_tips() -> str:
    return (
        "## Strategy Tips for pytest\n\n"
        "**Start simple:** Write plain `assert` statements first. pytest's "
        "assertion rewriting gives you detailed failure messages for free — "
        "no need for `assertEqual`, `assertTrue`, etc.\n\n"
        "**One concept per test:** Each test function should verify exactly "
        "one behaviour. Short, focused tests are easier to debug.\n\n"
        "**Name tests descriptively:** `test_divide_by_zero_raises_value_error` "
        "is better than `test_divide_2`. The name is your documentation.\n\n"
        "**Use parametrize early:** When you find yourself copy-pasting a test "
        "with different inputs, reach for `@pytest.mark.parametrize`.\n\n"
        "**Fixture scope matters:** Use `scope='session'` for expensive setup "
        "(DB connections, compiled models). Use the default `scope='function'` "
        "when tests must be isolated.\n\n"
        "**Run fast, fail fast:** Use `pytest -x` to stop on the first failure "
        "during development. Use `pytest -v` for verbose output when debugging."
    )


# ---------------------------------------------------------------------------
# Beginner sections
# ---------------------------------------------------------------------------

def _beginner_sections() -> list[TopicSection]:
    return [
        _first_tests(),
        _assertions_and_exceptions(),
        _test_organisation(),
        _basic_fixtures(),
    ]


# ---------------------------------------------------------------------------
# Beginner section implementations
# ---------------------------------------------------------------------------

def _first_tests() -> TopicSection:
    explanation = (
        "### Your First pytest Tests\n\n"
        "pytest is the standard Python testing framework. It discovers and "
        "runs tests automatically — no boilerplate classes or imports needed "
        "for simple cases.\n\n"
        "**Installation:** `pip install pytest`\n\n"
        "**Discovery rules:**\n"
        "- Files named `test_*.py` or `*_test.py`\n"
        "- Functions named `test_*`\n"
        "- Classes named `Test*` (no `__init__` method)\n\n"
        "**Running tests:**\n"
        "```bash\n"
        "pytest                     # run everything\n"
        "pytest test_math.py        # run one file\n"
        "pytest test_math.py::test_add  # run one test\n"
        "pytest -v                  # verbose — show each test name\n"
        "pytest -x                  # stop on first failure\n"
        "pytest -q                  # quiet — minimal output\n"
        "```\n\n"
        "**The key insight:** pytest rewrites `assert` statements to show "
        "exactly what the left and right values were when a test fails. "
        "You get rich failure messages without any extra code."
    )

    examples = [
        (
            "# --- test_math.py: your first test file ---\n"
            "# No imports needed for basic tests!\n\n"
            "def add(a, b):\n"
            "    return a + b\n\n"
            "def multiply(a, b):\n"
            "    return a * b\n\n"
            "# pytest finds these because they start with 'test_'\n"
            "def test_add_two_positives():\n"
            "    assert add(2, 3) == 5\n\n"
            "def test_add_negative():\n"
            "    assert add(-1, 4) == 3\n\n"
            "def test_add_zero():\n"
            "    assert add(0, 0) == 0\n\n"
            "def test_multiply():\n"
            "    assert multiply(3, 4) == 12\n\n"
            "# Run: pytest test_math.py -v\n"
            "# Output:\n"
            "# test_math.py::test_add_two_positives PASSED\n"
            "# test_math.py::test_add_negative      PASSED\n"
            "# test_math.py::test_add_zero          PASSED\n"
            "# test_math.py::test_multiply          PASSED\n"
            "# 4 passed in 0.01s"
        ),
        (
            "# --- What a failure looks like ---\n"
            "# pytest rewrites assert to show actual vs expected values\n\n"
            "def test_that_fails():\n"
            "    result = [1, 2, 3]\n"
            "    assert result == [1, 2, 4]  # wrong!\n\n"
            "# pytest output:\n"
            "# FAILED test_math.py::test_that_fails\n"
            "# AssertionError: assert [1, 2, 3] == [1, 2, 4]\n"
            "#   At index 2 diff: 3 != 4\n"
            "#   Full diff:\n"
            "#   - [1, 2, 3]\n"
            "#   ?        ^\n"
            "#   + [1, 2, 4]\n"
            "#   ?        ^\n\n"
            "# You can add a custom message to any assert:\n"
            "def test_with_message():\n"
            "    value = 42\n"
            "    assert value > 100, f'Expected > 100, got {value}'"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Write Tests for a Temperature Converter",
            statement=(
                "Write at least 4 pytest test functions for the `celsius_to_fahrenheit` "
                "function below. Cover: freezing point (0°C → 32°F), boiling point "
                "(100°C → 212°F), body temperature (37°C → 98.6°F), and absolute "
                "zero (-273.15°C → -459.67°F).\n\n"
                "```python\n"
                "def celsius_to_fahrenheit(c: float) -> float:\n"
                "    return c * 9 / 5 + 32\n"
                "```"
            ),
            function_signature=(
                "def test_freezing_point():\n"
                "def test_boiling_point():\n"
                "def test_body_temperature():\n"
                "def test_absolute_zero():"
            ),
            examples=[
                {"input": "celsius_to_fahrenheit(0)", "output": "32.0"},
                {"input": "celsius_to_fahrenheit(100)", "output": "212.0"},
            ],
            solution_code=(
                "def celsius_to_fahrenheit(c: float) -> float:\n"
                "    return c * 9 / 5 + 32\n\n"
                "def test_freezing_point():\n"
                "    assert celsius_to_fahrenheit(0) == 32.0\n\n"
                "def test_boiling_point():\n"
                "    assert celsius_to_fahrenheit(100) == 212.0\n\n"
                "def test_body_temperature():\n"
                "    assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.01\n\n"
                "def test_absolute_zero():\n"
                "    assert abs(celsius_to_fahrenheit(-273.15) - (-459.67)) < 0.01\n\n"
                "def test_negative_temp():\n"
                "    assert celsius_to_fahrenheit(-40) == -40.0  # same in both scales"
            ),
            test_code=(
                "def celsius_to_fahrenheit(c: float) -> float:\n"
                "    return c * 9 / 5 + 32\n\n"
                "assert celsius_to_fahrenheit(0) == 32.0\n"
                "assert celsius_to_fahrenheit(100) == 212.0\n"
                "assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.01\n"
                "assert abs(celsius_to_fahrenheit(-273.15) - (-459.67)) < 0.01\n"
                "assert celsius_to_fahrenheit(-40) == -40.0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use abs(result - expected) < tolerance for floating-point comparisons.",
                "-40 is the same in both Celsius and Fahrenheit — a useful sanity check.",
            ],
        ),
        PracticeProblem(
            title="Test a String Utility Module",
            statement=(
                "Write tests for the three functions below. Each function "
                "should have at least 2 test cases including an edge case.\n\n"
                "```python\n"
                "def truncate(s: str, max_len: int) -> str:\n"
                "    return s if len(s) <= max_len else s[:max_len] + '...'\n\n"
                "def count_words(s: str) -> int:\n"
                "    return len(s.split()) if s.strip() else 0\n\n"
                "def title_case(s: str) -> str:\n"
                "    return ' '.join(w.capitalize() for w in s.split())\n"
                "```"
            ),
            function_signature=(
                "def test_truncate_short_string():\n"
                "def test_truncate_long_string():\n"
                "def test_count_words_normal():\n"
                "def test_count_words_empty():\n"
                "def test_title_case():"
            ),
            examples=[
                {"input": "truncate('hello', 10)", "output": "'hello'"},
                {"input": "truncate('hello world', 5)", "output": "'hello...'"},
                {"input": "count_words('')", "output": "0"},
            ],
            solution_code=(
                "def truncate(s: str, max_len: int) -> str:\n"
                "    return s if len(s) <= max_len else s[:max_len] + '...'\n\n"
                "def count_words(s: str) -> int:\n"
                "    return len(s.split()) if s.strip() else 0\n\n"
                "def title_case(s: str) -> str:\n"
                "    return ' '.join(w.capitalize() for w in s.split())\n\n"
                "def test_truncate_short_string():\n"
                "    assert truncate('hello', 10) == 'hello'\n\n"
                "def test_truncate_long_string():\n"
                "    assert truncate('hello world', 5) == 'hello...'\n\n"
                "def test_truncate_exact_length():\n"
                "    assert truncate('hello', 5) == 'hello'  # boundary: no truncation\n\n"
                "def test_count_words_normal():\n"
                "    assert count_words('the quick brown fox') == 4\n\n"
                "def test_count_words_empty():\n"
                "    assert count_words('') == 0\n\n"
                "def test_count_words_whitespace_only():\n"
                "    assert count_words('   ') == 0\n\n"
                "def test_title_case():\n"
                "    assert title_case('hello world') == 'Hello World'\n\n"
                "def test_title_case_already_titled():\n"
                "    assert title_case('Hello World') == 'Hello World'"
            ),
            test_code=(
                "def truncate(s, max_len):\n"
                "    return s if len(s) <= max_len else s[:max_len] + '...'\n\n"
                "def count_words(s):\n"
                "    return len(s.split()) if s.strip() else 0\n\n"
                "def title_case(s):\n"
                "    return ' '.join(w.capitalize() for w in s.split())\n\n"
                "assert truncate('hello', 10) == 'hello'\n"
                "assert truncate('hello world', 5) == 'hello...'\n"
                "assert truncate('hello', 5) == 'hello'\n"
                "assert count_words('the quick brown fox') == 4\n"
                "assert count_words('') == 0\n"
                "assert count_words('   ') == 0\n"
                "assert title_case('hello world') == 'Hello World'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Test the boundary: a string exactly at max_len should NOT be truncated.",
                "Whitespace-only strings should count as 0 words.",
            ],
        ),
    ]

    return TopicSection(
        title="Your First pytest Tests",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "No imports needed for basic tests — just write `def test_*():` functions.",
            "pytest rewrites `assert` to show actual vs expected values on failure.",
            "Name tests descriptively: `test_divide_by_zero_raises` > `test_divide_2`.",
            "Run `pytest -v` for verbose output, `-x` to stop on first failure.",
            "Test boundary values (empty string, zero, max length) — they catch most bugs.",
        ],
    )


def _assertions_and_exceptions() -> TopicSection:
    explanation = (
        "### Assertions and Testing Exceptions\n\n"
        "pytest provides several ways to make assertions beyond simple equality.\n\n"
        "**Floating-point comparisons:**\n"
        "```python\n"
        "import pytest\n"
        "assert result == pytest.approx(0.1 + 0.2)  # handles float imprecision\n"
        "assert result == pytest.approx(3.14, abs=0.01)  # within 0.01\n"
        "assert result == pytest.approx(100, rel=0.01)   # within 1%\n"
        "```\n\n"
        "**Testing exceptions with `pytest.raises`:**\n"
        "```python\n"
        "with pytest.raises(ValueError):\n"
        "    int('not a number')\n\n"
        "# Check the exception message\n"
        "with pytest.raises(ValueError, match='invalid literal'):\n"
        "    int('abc')\n\n"
        "# Capture the exception for further inspection\n"
        "with pytest.raises(KeyError) as exc_info:\n"
        "    {}['missing']\n"
        "assert 'missing' in str(exc_info.value)\n"
        "```\n\n"
        "**Testing warnings:**\n"
        "```python\n"
        "with pytest.warns(DeprecationWarning):\n"
        "    old_function()\n"
        "```\n\n"
        "**Checking collections:**\n"
        "```python\n"
        "assert 'key' in my_dict\n"
        "assert result is None\n"
        "assert isinstance(result, list)\n"
        "assert len(result) == 3\n"
        "```"
    )

    examples = [
        (
            "# --- pytest.approx for floats ---\n"
            "import pytest\n\n"
            "def average(nums):\n"
            "    return sum(nums) / len(nums)\n\n"
            "def test_average_floats():\n"
            "    # Direct == fails due to floating-point representation\n"
            "    result = average([0.1, 0.2, 0.3])\n"
            "    assert result == pytest.approx(0.2)  # passes\n\n"
            "def test_average_with_tolerance():\n"
            "    result = average([1, 2, 3, 4, 5])\n"
            "    assert result == pytest.approx(3.0, abs=1e-9)\n\n"
            "# pytest.approx also works with lists and dicts\n"
            "def test_vector_approx():\n"
            "    result = [0.1 + 0.2, 1.0 / 3.0]\n"
            "    assert result == pytest.approx([0.3, 0.333], rel=1e-3)"
        ),
        (
            "# --- pytest.raises: testing exceptions ---\n"
            "import pytest\n\n"
            "def parse_positive_int(s: str) -> int:\n"
            "    value = int(s)  # raises ValueError if not a number\n"
            "    if value <= 0:\n"
            "        raise ValueError(f'Expected positive integer, got {value}')\n"
            "    return value\n\n"
            "def test_valid_input():\n"
            "    assert parse_positive_int('42') == 42\n\n"
            "def test_non_numeric_raises():\n"
            "    with pytest.raises(ValueError):\n"
            "        parse_positive_int('abc')\n\n"
            "def test_negative_raises_with_message():\n"
            "    with pytest.raises(ValueError, match='Expected positive'):\n"
            "        parse_positive_int('-5')\n\n"
            "def test_zero_raises():\n"
            "    with pytest.raises(ValueError):\n"
            "        parse_positive_int('0')\n\n"
            "def test_exception_details():\n"
            "    with pytest.raises(ValueError) as exc_info:\n"
            "        parse_positive_int('-10')\n"
            "    assert '-10' in str(exc_info.value)"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Test a Stack Implementation",
            statement=(
                "Write tests for the `Stack` class below. Cover: push and pop, "
                "peek without removing, popping from an empty stack raises "
                "`IndexError`, and checking if the stack is empty.\n\n"
                "```python\n"
                "class Stack:\n"
                "    def __init__(self): self._data = []\n"
                "    def push(self, item): self._data.append(item)\n"
                "    def pop(self): return self._data.pop()\n"
                "    def peek(self): return self._data[-1]\n"
                "    def is_empty(self): return len(self._data) == 0\n"
                "    def __len__(self): return len(self._data)\n"
                "```"
            ),
            function_signature=(
                "def test_push_and_pop():\n"
                "def test_peek_does_not_remove():\n"
                "def test_pop_empty_raises():\n"
                "def test_is_empty():\n"
                "def test_len():"
            ),
            examples=[
                {"input": "s = Stack(); s.push(1); s.pop()", "output": "1"},
                {"input": "s = Stack(); s.is_empty()", "output": "True"},
            ],
            solution_code=(
                "import pytest\n\n"
                "class Stack:\n"
                "    def __init__(self): self._data = []\n"
                "    def push(self, item): self._data.append(item)\n"
                "    def pop(self): return self._data.pop()\n"
                "    def peek(self): return self._data[-1]\n"
                "    def is_empty(self): return len(self._data) == 0\n"
                "    def __len__(self): return len(self._data)\n\n"
                "def test_push_and_pop():\n"
                "    s = Stack()\n"
                "    s.push(10)\n"
                "    s.push(20)\n"
                "    assert s.pop() == 20  # LIFO\n"
                "    assert s.pop() == 10\n\n"
                "def test_peek_does_not_remove():\n"
                "    s = Stack()\n"
                "    s.push(42)\n"
                "    assert s.peek() == 42\n"
                "    assert len(s) == 1  # still there\n\n"
                "def test_pop_empty_raises():\n"
                "    s = Stack()\n"
                "    with pytest.raises(IndexError):\n"
                "        s.pop()\n\n"
                "def test_is_empty():\n"
                "    s = Stack()\n"
                "    assert s.is_empty() == True\n"
                "    s.push(1)\n"
                "    assert s.is_empty() == False\n\n"
                "def test_len():\n"
                "    s = Stack()\n"
                "    assert len(s) == 0\n"
                "    s.push(1)\n"
                "    s.push(2)\n"
                "    assert len(s) == 2"
            ),
            test_code=(
                "import pytest\n\n"
                "class Stack:\n"
                "    def __init__(self): self._data = []\n"
                "    def push(self, item): self._data.append(item)\n"
                "    def pop(self): return self._data.pop()\n"
                "    def peek(self): return self._data[-1]\n"
                "    def is_empty(self): return len(self._data) == 0\n"
                "    def __len__(self): return len(self._data)\n\n"
                "s = Stack()\n"
                "assert s.is_empty()\n"
                "s.push(10); s.push(20)\n"
                "assert s.pop() == 20\n"
                "assert s.peek() == 10\n"
                "assert len(s) == 1\n"
                "try:\n"
                "    Stack().pop()\n"
                "    assert False\n"
                "except IndexError:\n"
                "    pass\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use pytest.raises(IndexError) to verify popping an empty stack fails.",
                "Test peek separately from pop — peek should not change the stack size.",
            ],
        ),
        PracticeProblem(
            title="Float Assertions with pytest.approx",
            statement=(
                "Write tests for the `circle_area` and `hypotenuse` functions "
                "using `pytest.approx` for floating-point comparisons.\n\n"
                "```python\n"
                "import math\n\n"
                "def circle_area(radius: float) -> float:\n"
                "    return math.pi * radius ** 2\n\n"
                "def hypotenuse(a: float, b: float) -> float:\n"
                "    return math.sqrt(a ** 2 + b ** 2)\n"
                "```"
            ),
            function_signature=(
                "def test_circle_area_unit():\n"
                "def test_circle_area_known():\n"
                "def test_hypotenuse_345():\n"
                "def test_hypotenuse_isoceles():"
            ),
            examples=[
                {"input": "circle_area(1)", "output": "≈ 3.14159"},
                {"input": "hypotenuse(3, 4)", "output": "5.0"},
            ],
            solution_code=(
                "import math\n"
                "import pytest\n\n"
                "def circle_area(radius: float) -> float:\n"
                "    return math.pi * radius ** 2\n\n"
                "def hypotenuse(a: float, b: float) -> float:\n"
                "    return math.sqrt(a ** 2 + b ** 2)\n\n"
                "def test_circle_area_unit():\n"
                "    assert circle_area(1) == pytest.approx(math.pi)\n\n"
                "def test_circle_area_known():\n"
                "    # radius=2 → area = 4π ≈ 12.566\n"
                "    assert circle_area(2) == pytest.approx(4 * math.pi)\n\n"
                "def test_hypotenuse_345():\n"
                "    assert hypotenuse(3, 4) == pytest.approx(5.0)\n\n"
                "def test_hypotenuse_isoceles():\n"
                "    # 1-1-√2 right triangle\n"
                "    assert hypotenuse(1, 1) == pytest.approx(math.sqrt(2))"
            ),
            test_code=(
                "import math\n\n"
                "def circle_area(r): return math.pi * r ** 2\n"
                "def hypotenuse(a, b): return math.sqrt(a**2 + b**2)\n\n"
                "assert abs(circle_area(1) - math.pi) < 1e-9\n"
                "assert abs(circle_area(2) - 4 * math.pi) < 1e-9\n"
                "assert abs(hypotenuse(3, 4) - 5.0) < 1e-9\n"
                "assert abs(hypotenuse(1, 1) - math.sqrt(2)) < 1e-9\n"
                "print('All tests passed!')"
            ),
            hints=[
                "pytest.approx(expected) handles floating-point imprecision automatically.",
                "The 3-4-5 right triangle is a classic: hypotenuse(3, 4) == 5.0 exactly.",
            ],
        ),
    ]

    return TopicSection(
        title="Assertions and Testing Exceptions",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Use pytest.approx() for all floating-point comparisons — never use ==.",
            "pytest.raises() as a context manager tests that an exception is raised.",
            "Add match='pattern' to pytest.raises() to also check the error message.",
            "Capture exc_info to inspect the exception object after the block.",
            "assert isinstance(x, T) and assert x is None are common assertion patterns.",
        ],
    )


def _test_organisation() -> TopicSection:
    explanation = (
        "### Organising Tests\n\n"
        "As your test suite grows, organisation becomes critical. pytest "
        "supports grouping tests into classes and using marks to categorise them.\n\n"
        "**Test classes:**\n"
        "```python\n"
        "class TestUserAuth:\n"
        "    def test_login_valid(self): ...\n"
        "    def test_login_wrong_password(self): ...\n"
        "    def test_logout(self): ...\n"
        "```\n"
        "- Class name must start with `Test`\n"
        "- No `__init__` method\n"
        "- Each method is a separate test\n\n"
        "**Marks — tagging tests:**\n"
        "```python\n"
        "import pytest\n\n"
        "@pytest.mark.slow\n"
        "def test_large_dataset(): ...\n\n"
        "@pytest.mark.skip(reason='Not implemented yet')\n"
        "def test_future_feature(): ...\n\n"
        "@pytest.mark.skipif(sys.platform == 'win32', reason='Linux only')\n"
        "def test_linux_command(): ...\n\n"
        "@pytest.mark.xfail(reason='Known bug #123')\n"
        "def test_known_broken(): ...\n"
        "```\n\n"
        "**Running by mark:**\n"
        "```bash\n"
        "pytest -m slow          # only slow tests\n"
        "pytest -m 'not slow'    # skip slow tests\n"
        "pytest -m 'slow or gpu' # slow OR gpu tests\n"
        "```\n\n"
        "**pytest.ini / pyproject.toml — register custom marks:**\n"
        "```ini\n"
        "[pytest]\n"
        "markers =\n"
        "    slow: marks tests as slow\n"
        "    gpu: requires GPU hardware\n"
        "    integration: integration tests\n"
        "```"
    )

    examples = [
        (
            "# --- Test classes for grouping related tests ---\n"
            "import pytest\n\n"
            "class BankAccount:\n"
            "    def __init__(self, balance=0):\n"
            "        self.balance = balance\n\n"
            "    def deposit(self, amount):\n"
            "        if amount <= 0:\n"
            "            raise ValueError('Deposit must be positive')\n"
            "        self.balance += amount\n\n"
            "    def withdraw(self, amount):\n"
            "        if amount > self.balance:\n"
            "            raise ValueError('Insufficient funds')\n"
            "        self.balance -= amount\n\n"
            "class TestBankAccount:\n"
            "    \"\"\"All tests for BankAccount grouped together.\"\"\"\n\n"
            "    def test_initial_balance(self):\n"
            "        account = BankAccount(100)\n"
            "        assert account.balance == 100\n\n"
            "    def test_deposit_increases_balance(self):\n"
            "        account = BankAccount(100)\n"
            "        account.deposit(50)\n"
            "        assert account.balance == 150\n\n"
            "    def test_deposit_negative_raises(self):\n"
            "        account = BankAccount(100)\n"
            "        with pytest.raises(ValueError, match='positive'):\n"
            "            account.deposit(-10)\n\n"
            "    def test_withdraw_reduces_balance(self):\n"
            "        account = BankAccount(100)\n"
            "        account.withdraw(30)\n"
            "        assert account.balance == 70\n\n"
            "    def test_overdraft_raises(self):\n"
            "        account = BankAccount(50)\n"
            "        with pytest.raises(ValueError, match='Insufficient'):\n"
            "            account.withdraw(100)"
        ),
        (
            "# --- Marks: skip, xfail, custom ---\n"
            "import pytest\n"
            "import sys\n\n"
            "@pytest.mark.skip(reason='Feature not yet implemented')\n"
            "def test_export_to_csv():\n"
            "    pass  # will be skipped, shown as 's' in output\n\n"
            "@pytest.mark.skipif(\n"
            "    sys.platform != 'linux',\n"
            "    reason='Linux-specific test'\n"
            ")\n"
            "def test_proc_filesystem():\n"
            "    import os\n"
            "    assert os.path.exists('/proc/cpuinfo')\n\n"
            "@pytest.mark.xfail(reason='Bug #42: rounding error in edge case')\n"
            "def test_known_rounding_issue():\n"
            "    assert 0.1 + 0.2 == 0.3  # fails — but marked as expected\n\n"
            "# Custom mark — register in pytest.ini to avoid warnings\n"
            "@pytest.mark.slow\n"
            "def test_process_million_records():\n"
            "    result = sum(range(1_000_000))\n"
            "    assert result == 499_999_500_000\n\n"
            "# Run only slow tests: pytest -m slow\n"
            "# Skip slow tests:     pytest -m 'not slow'"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Organise Tests into a Class",
            statement=(
                "Refactor the following standalone test functions into a "
                "`TestShoppingCart` class. Also add a `@pytest.mark.skip` "
                "test for a `apply_coupon` method that doesn't exist yet.\n\n"
                "```python\n"
                "class ShoppingCart:\n"
                "    def __init__(self): self.items = []\n"
                "    def add(self, name, price): self.items.append({'name': name, 'price': price})\n"
                "    def total(self): return sum(i['price'] for i in self.items)\n"
                "    def count(self): return len(self.items)\n"
                "```"
            ),
            function_signature=(
                "class TestShoppingCart:\n"
                "    def test_empty_cart_total(self):\n"
                "    def test_add_item(self):\n"
                "    def test_multiple_items_total(self):\n"
                "    @pytest.mark.skip(reason='not implemented')\n"
                "    def test_apply_coupon(self):"
            ),
            examples=[
                {"input": "cart = ShoppingCart(); cart.total()", "output": "0"},
                {"input": "cart.add('apple', 1.5); cart.total()", "output": "1.5"},
            ],
            solution_code=(
                "import pytest\n\n"
                "class ShoppingCart:\n"
                "    def __init__(self): self.items = []\n"
                "    def add(self, name, price): self.items.append({'name': name, 'price': price})\n"
                "    def total(self): return sum(i['price'] for i in self.items)\n"
                "    def count(self): return len(self.items)\n\n"
                "class TestShoppingCart:\n"
                "    def test_empty_cart_total(self):\n"
                "        cart = ShoppingCart()\n"
                "        assert cart.total() == 0\n\n"
                "    def test_add_item(self):\n"
                "        cart = ShoppingCart()\n"
                "        cart.add('apple', 1.5)\n"
                "        assert cart.count() == 1\n"
                "        assert cart.total() == 1.5\n\n"
                "    def test_multiple_items_total(self):\n"
                "        cart = ShoppingCart()\n"
                "        cart.add('apple', 1.5)\n"
                "        cart.add('bread', 2.0)\n"
                "        cart.add('milk', 1.2)\n"
                "        assert cart.total() == pytest.approx(4.7)\n\n"
                "    @pytest.mark.skip(reason='apply_coupon not implemented yet')\n"
                "    def test_apply_coupon(self):\n"
                "        cart = ShoppingCart()\n"
                "        cart.add('item', 10.0)\n"
                "        cart.apply_coupon('SAVE10')\n"
                "        assert cart.total() == 9.0"
            ),
            test_code=(
                "class ShoppingCart:\n"
                "    def __init__(self): self.items = []\n"
                "    def add(self, name, price): self.items.append({'name': name, 'price': price})\n"
                "    def total(self): return sum(i['price'] for i in self.items)\n"
                "    def count(self): return len(self.items)\n\n"
                "cart = ShoppingCart()\n"
                "assert cart.total() == 0\n"
                "cart.add('apple', 1.5)\n"
                "assert cart.count() == 1\n"
                "assert cart.total() == 1.5\n"
                "cart.add('bread', 2.0)\n"
                "assert abs(cart.total() - 3.5) < 1e-9\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Test class methods take `self` as the first argument.",
                "Each test method creates its own ShoppingCart — tests should be independent.",
            ],
        ),
    ]

    return TopicSection(
        title="Organising Tests",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Group related tests in a `Test*` class — no `__init__` needed.",
            "@pytest.mark.skip skips a test; @pytest.mark.xfail marks expected failures.",
            "Register custom marks in pytest.ini to avoid PytestUnknownMarkWarning.",
            "Run tests by mark: `pytest -m slow`, skip them: `pytest -m 'not slow'`.",
            "Test classes are just for organisation — each method is still independent.",
        ],
    )


def _basic_fixtures() -> TopicSection:
    explanation = (
        "### Basic Fixtures\n\n"
        "Fixtures are pytest's mechanism for reusable setup and teardown. "
        "They replace `setUp`/`tearDown` from unittest with something more "
        "flexible and composable.\n\n"
        "**Defining a fixture:**\n"
        "```python\n"
        "@pytest.fixture\n"
        "def my_list():\n"
        "    return [1, 2, 3]  # returned value is injected into the test\n"
        "```\n\n"
        "**Using a fixture:**\n"
        "```python\n"
        "def test_length(my_list):  # pytest injects by name\n"
        "    assert len(my_list) == 3\n"
        "```\n\n"
        "**Fixtures with teardown (yield):**\n"
        "```python\n"
        "@pytest.fixture\n"
        "def temp_file(tmp_path):\n"
        "    path = tmp_path / 'data.txt'\n"
        "    path.write_text('hello')\n"
        "    yield path          # test runs here\n"
        "    path.unlink()       # teardown after yield\n"
        "```\n\n"
        "**Built-in fixtures:**\n"
        "- `tmp_path` — a temporary directory (pathlib.Path), cleaned up automatically\n"
        "- `capsys` — capture stdout/stderr\n"
        "- `monkeypatch` — temporarily replace attributes, env vars, functions\n\n"
        "**Fixture scope:**\n"
        "```python\n"
        "@pytest.fixture(scope='module')  # created once per test file\n"
        "def expensive_resource(): ...\n"
        "```\n"
        "Scopes: `function` (default), `class`, `module`, `session`"
    )

    examples = [
        (
            "# --- Fixtures: setup and teardown ---\n"
            "import pytest\n\n"
            "class Database:\n"
            "    \"\"\"Simulated in-memory database.\"\"\"\n"
            "    def __init__(self):\n"
            "        self._store = {}\n"
            "        self.connected = True\n\n"
            "    def insert(self, key, value):\n"
            "        self._store[key] = value\n\n"
            "    def get(self, key):\n"
            "        return self._store.get(key)\n\n"
            "    def close(self):\n"
            "        self.connected = False\n\n"
            "@pytest.fixture\n"
            "def db():\n"
            "    \"\"\"Provide a fresh database for each test.\"\"\"\n"
            "    database = Database()\n"
            "    yield database          # test runs here\n"
            "    database.close()        # teardown: always runs after test\n\n"
            "def test_insert_and_get(db):\n"
            "    db.insert('user:1', {'name': 'Alice'})\n"
            "    assert db.get('user:1') == {'name': 'Alice'}\n\n"
            "def test_missing_key_returns_none(db):\n"
            "    assert db.get('nonexistent') is None\n\n"
            "def test_db_is_fresh(db):\n"
            "    # Each test gets a new db — no leftover data from other tests\n"
            "    assert db.get('user:1') is None"
        ),
        (
            "# --- Built-in fixtures: tmp_path and capsys ---\n"
            "import pytest\n\n"
            "def write_report(path: str, data: list[str]) -> None:\n"
            "    \"\"\"Write a list of strings to a file, one per line.\"\"\"\n"
            "    with open(path, 'w') as f:\n"
            "        f.write('\\n'.join(data))\n\n"
            "def test_write_report(tmp_path):\n"
            "    # tmp_path is a pathlib.Path to a unique temp directory\n"
            "    report_file = tmp_path / 'report.txt'\n"
            "    write_report(str(report_file), ['PASS: test_a', 'FAIL: test_b'])\n"
            "    content = report_file.read_text()\n"
            "    assert 'PASS: test_a' in content\n"
            "    assert 'FAIL: test_b' in content\n"
            "    # tmp_path is cleaned up automatically after the test\n\n"
            "def greet(name: str) -> None:\n"
            "    print(f'Hello, {name}!')\n\n"
            "def test_greet_output(capsys):\n"
            "    greet('World')\n"
            "    captured = capsys.readouterr()  # capture stdout/stderr\n"
            "    assert captured.out == 'Hello, World!\\n'\n"
            "    assert captured.err == ''"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Fixture for a User Registry",
            statement=(
                "Write a `registry` fixture that returns a fresh `UserRegistry` "
                "instance for each test. Then write 3 tests using it: adding a "
                "user, looking up a user, and verifying a duplicate raises `ValueError`.\n\n"
                "```python\n"
                "class UserRegistry:\n"
                "    def __init__(self): self._users = {}\n"
                "    def add(self, username, email):\n"
                "        if username in self._users:\n"
                "            raise ValueError(f'{username} already exists')\n"
                "        self._users[username] = email\n"
                "    def get_email(self, username): return self._users.get(username)\n"
                "    def count(self): return len(self._users)\n"
                "```"
            ),
            function_signature=(
                "@pytest.fixture\n"
                "def registry():\n\n"
                "def test_add_user(registry):\n"
                "def test_get_email(registry):\n"
                "def test_duplicate_raises(registry):"
            ),
            examples=[
                {"input": "registry.add('alice', 'alice@example.com'); registry.count()", "output": "1"},
                {"input": "registry.get_email('alice')", "output": "'alice@example.com'"},
            ],
            solution_code=(
                "import pytest\n\n"
                "class UserRegistry:\n"
                "    def __init__(self): self._users = {}\n"
                "    def add(self, username, email):\n"
                "        if username in self._users:\n"
                "            raise ValueError(f'{username} already exists')\n"
                "        self._users[username] = email\n"
                "    def get_email(self, username): return self._users.get(username)\n"
                "    def count(self): return len(self._users)\n\n"
                "@pytest.fixture\n"
                "def registry():\n"
                "    return UserRegistry()\n\n"
                "def test_add_user(registry):\n"
                "    registry.add('alice', 'alice@example.com')\n"
                "    assert registry.count() == 1\n\n"
                "def test_get_email(registry):\n"
                "    registry.add('bob', 'bob@example.com')\n"
                "    assert registry.get_email('bob') == 'bob@example.com'\n"
                "    assert registry.get_email('nobody') is None\n\n"
                "def test_duplicate_raises(registry):\n"
                "    registry.add('alice', 'alice@example.com')\n"
                "    with pytest.raises(ValueError, match='already exists'):\n"
                "        registry.add('alice', 'other@example.com')"
            ),
            test_code=(
                "import pytest\n\n"
                "class UserRegistry:\n"
                "    def __init__(self): self._users = {}\n"
                "    def add(self, username, email):\n"
                "        if username in self._users:\n"
                "            raise ValueError(f'{username} already exists')\n"
                "        self._users[username] = email\n"
                "    def get_email(self, username): return self._users.get(username)\n"
                "    def count(self): return len(self._users)\n\n"
                "r = UserRegistry()\n"
                "r.add('alice', 'alice@example.com')\n"
                "assert r.count() == 1\n"
                "assert r.get_email('alice') == 'alice@example.com'\n"
                "assert r.get_email('nobody') is None\n"
                "try:\n"
                "    r.add('alice', 'other@example.com')\n"
                "    assert False\n"
                "except ValueError as e:\n"
                "    assert 'already exists' in str(e)\n"
                "print('All tests passed!')"
            ),
            hints=[
                "A simple fixture just returns a new instance: `return UserRegistry()`.",
                "Each test gets its own fresh registry — no shared state between tests.",
            ],
        ),
        PracticeProblem(
            title="Using tmp_path to Test File I/O",
            statement=(
                "Write tests for the `save_results` and `load_results` functions "
                "using the `tmp_path` built-in fixture. Test that data survives "
                "a round-trip (save then load), and that loading a missing file "
                "returns an empty list.\n\n"
                "```python\n"
                "import json\n\n"
                "def save_results(path: str, results: list) -> None:\n"
                "    with open(path, 'w') as f:\n"
                "        json.dump(results, f)\n\n"
                "def load_results(path: str) -> list:\n"
                "    try:\n"
                "        with open(path) as f:\n"
                "            return json.load(f)\n"
                "    except FileNotFoundError:\n"
                "        return []\n"
                "```"
            ),
            function_signature=(
                "def test_round_trip(tmp_path):\n"
                "def test_load_missing_file(tmp_path):"
            ),
            examples=[
                {"input": "save then load [{'name': 'test_a', 'passed': True}]", "output": "[{'name': 'test_a', 'passed': True}]"},
                {"input": "load non-existent file", "output": "[]"},
            ],
            solution_code=(
                "import json\n"
                "import pytest\n\n"
                "def save_results(path: str, results: list) -> None:\n"
                "    with open(path, 'w') as f:\n"
                "        json.dump(results, f)\n\n"
                "def load_results(path: str) -> list:\n"
                "    try:\n"
                "        with open(path) as f:\n"
                "            return json.load(f)\n"
                "    except FileNotFoundError:\n"
                "        return []\n\n"
                "def test_round_trip(tmp_path):\n"
                "    path = str(tmp_path / 'results.json')\n"
                "    data = [{'name': 'test_a', 'passed': True}, {'name': 'test_b', 'passed': False}]\n"
                "    save_results(path, data)\n"
                "    loaded = load_results(path)\n"
                "    assert loaded == data\n\n"
                "def test_load_missing_file(tmp_path):\n"
                "    path = str(tmp_path / 'nonexistent.json')\n"
                "    assert load_results(path) == []"
            ),
            test_code=(
                "import json, tempfile, os\n\n"
                "def save_results(path, results):\n"
                "    with open(path, 'w') as f: json.dump(results, f)\n\n"
                "def load_results(path):\n"
                "    try:\n"
                "        with open(path) as f: return json.load(f)\n"
                "    except FileNotFoundError: return []\n\n"
                "with tempfile.TemporaryDirectory() as d:\n"
                "    p = os.path.join(d, 'r.json')\n"
                "    data = [{'name': 'test_a', 'passed': True}]\n"
                "    save_results(p, data)\n"
                "    assert load_results(p) == data\n"
                "    assert load_results(os.path.join(d, 'missing.json')) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "tmp_path is a pathlib.Path — use `tmp_path / 'filename'` to create paths.",
                "Convert to str with `str(tmp_path / 'file')` if the function expects a string path.",
            ],
        ),
    ]

    return TopicSection(
        title="Basic Fixtures",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Fixtures are injected by name — the parameter name must match the fixture name.",
            "Use `yield` in a fixture for teardown: code after yield runs after the test.",
            "tmp_path gives you a unique temp directory per test — no manual cleanup.",
            "capsys captures print() output so you can assert on stdout/stderr.",
            "Each test gets a fresh fixture instance by default (scope='function').",
        ],
    )


# ---------------------------------------------------------------------------
# Mid-Level sections
# ---------------------------------------------------------------------------

def _mid_level_sections() -> list[TopicSection]:
    return [
        _parametrize(),
        _advanced_fixtures(),
        _mocking_with_monkeypatch(),
        _conftest_and_plugins(),
    ]


def _parametrize() -> TopicSection:
    explanation = (
        "### Parametrize — Data-Driven Tests\n\n"
        "`@pytest.mark.parametrize` runs one test function with many different "
        "inputs. It eliminates copy-paste tests and makes coverage gaps obvious.\n\n"
        "**Basic syntax:**\n"
        "```python\n"
        "@pytest.mark.parametrize('input, expected', [\n"
        "    (2,  4),\n"
        "    (3,  9),\n"
        "    (-1, 1),\n"
        "    (0,  0),\n"
        "])\n"
        "def test_square(input, expected):\n"
        "    assert input ** 2 == expected\n"
        "```\n\n"
        "**Multiple parameters:**\n"
        "```python\n"
        "@pytest.mark.parametrize('a, b, expected', [\n"
        "    (1, 2, 3),\n"
        "    (0, 0, 0),\n"
        "    (-1, 1, 0),\n"
        "])\n"
        "def test_add(a, b, expected):\n"
        "    assert a + b == expected\n"
        "```\n\n"
        "**Custom test IDs:**\n"
        "```python\n"
        "@pytest.mark.parametrize('value, valid', [\n"
        "    pytest.param(8080, True,  id='valid-port'),\n"
        "    pytest.param(99999, False, id='too-high'),\n"
        "])\n"
        "def test_port(value, valid): ...\n"
        "```\n\n"
        "**Stacking parametrize** (cartesian product):\n"
        "```python\n"
        "@pytest.mark.parametrize('x', [1, 2])\n"
        "@pytest.mark.parametrize('y', [10, 20])\n"
        "def test_product(x, y):  # runs 4 times: (1,10),(1,20),(2,10),(2,20)\n"
        "    assert x * y > 0\n"
        "```"
    )

    examples = [
        (
            "# --- Parametrize: replacing copy-paste tests ---\n"
            "import pytest\n\n"
            "def is_palindrome(s: str) -> bool:\n"
            "    cleaned = ''.join(c.lower() for c in s if c.isalnum())\n"
            "    return cleaned == cleaned[::-1]\n\n"
            "# Without parametrize — repetitive:\n"
            "# def test_racecar(): assert is_palindrome('racecar') == True\n"
            "# def test_hello():   assert is_palindrome('hello') == False\n"
            "# ...\n\n"
            "# With parametrize — clean and extensible:\n"
            "@pytest.mark.parametrize('text, expected', [\n"
            "    ('racecar',                    True),\n"
            "    ('hello',                      False),\n"
            "    ('A man a plan a canal Panama', True),\n"
            "    ('',                           True),   # empty is palindrome\n"
            "    ('Was it a car or a cat I saw', True),\n"
            "    ('not a palindrome',            False),\n"
            "])\n"
            "def test_is_palindrome(text, expected):\n"
            "    assert is_palindrome(text) == expected\n\n"
            "# pytest output:\n"
            "# test_palindrome.py::test_is_palindrome[racecar-True] PASSED\n"
            "# test_palindrome.py::test_is_palindrome[hello-False] PASSED\n"
            "# ..."
        ),
        (
            "# --- Parametrize with pytest.param for custom IDs and marks ---\n"
            "import pytest\n\n"
            "def divide(a, b):\n"
            "    if b == 0:\n"
            "        raise ZeroDivisionError\n"
            "    return a / b\n\n"
            "@pytest.mark.parametrize('a, b, expected', [\n"
            "    pytest.param(10, 2,  5.0,  id='basic-division'),\n"
            "    pytest.param(7,  2,  3.5,  id='non-integer-result'),\n"
            "    pytest.param(-6, 3, -2.0,  id='negative-dividend'),\n"
            "    pytest.param(0,  5,  0.0,  id='zero-numerator'),\n"
            "])\n"
            "def test_divide(a, b, expected):\n"
            "    assert divide(a, b) == pytest.approx(expected)\n\n"
            "# Test IDs appear in output:\n"
            "# test_divide[basic-division]       PASSED\n"
            "# test_divide[non-integer-result]   PASSED\n"
            "# test_divide[negative-dividend]    PASSED\n"
            "# test_divide[zero-numerator]       PASSED"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Parametrized Validation Tests",
            statement=(
                "Write a parametrized test for the `validate_email` function "
                "below. Include at least 6 cases: 2 valid emails, and 4 invalid "
                "ones (missing @, missing domain, empty string, spaces).\n\n"
                "```python\n"
                "import re\n\n"
                "def validate_email(email: str) -> bool:\n"
                "    pattern = r'^[\\w.+-]+@[\\w-]+\\.[\\w.]+$'\n"
                "    return bool(re.match(pattern, email))\n"
                "```"
            ),
            function_signature=(
                "@pytest.mark.parametrize('email, expected', [...])\n"
                "def test_validate_email(email, expected):"
            ),
            examples=[
                {"input": "'user@example.com'", "output": "True"},
                {"input": "'not-an-email'", "output": "False"},
                {"input": "''", "output": "False"},
            ],
            solution_code=(
                "import re\n"
                "import pytest\n\n"
                "def validate_email(email: str) -> bool:\n"
                "    pattern = r'^[\\w.+-]+@[\\w-]+\\.[\\w.]+$'\n"
                "    return bool(re.match(pattern, email))\n\n"
                "@pytest.mark.parametrize('email, expected', [\n"
                "    # Valid\n"
                "    ('user@example.com',       True),\n"
                "    ('first.last+tag@sub.domain.org', True),\n"
                "    # Invalid\n"
                "    ('missing-at-sign',        False),\n"
                "    ('missing@domain',         False),\n"
                "    ('',                       False),\n"
                "    ('has spaces@example.com', False),\n"
                "    ('@nodomain.com',           False),\n"
                "])\n"
                "def test_validate_email(email, expected):\n"
                "    assert validate_email(email) == expected"
            ),
            test_code=(
                "import re\n\n"
                "def validate_email(email):\n"
                "    return bool(re.match(r'^[\\w.+-]+@[\\w-]+\\.[\\w.]+$', email))\n\n"
                "cases = [\n"
                "    ('user@example.com', True),\n"
                "    ('first.last+tag@sub.domain.org', True),\n"
                "    ('missing-at-sign', False),\n"
                "    ('missing@domain', False),\n"
                "    ('', False),\n"
                "    ('has spaces@example.com', False),\n"
                "    ('@nodomain.com', False),\n"
                "]\n"
                "for email, expected in cases:\n"
                "    assert validate_email(email) == expected, f'Failed for {email!r}'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "List your cases as tuples: ('email@example.com', True).",
                "Include edge cases: empty string, no @, no domain extension.",
            ],
        ),
        PracticeProblem(
            title="nip GPU Health Parametrized Tests",
            statement=(
                "Write a parametrized test for `validate_gpu_record`. "
                "Include at least 5 cases covering: healthy GPU, over-temperature, "
                "memory overflow, invalid gpu_id (negative), and missing key.\n\n"
                "```python\n"
                "def validate_gpu_record(record: dict) -> tuple[bool, str]:\n"
                "    if not isinstance(record.get('gpu_id'), int) or record['gpu_id'] < 0:\n"
                "        return False, 'invalid gpu_id'\n"
                "    if record.get('temperature_c', 0) >= 85:\n"
                "        return False, f'over temp: {record[\"temperature_c\"]}C'\n"
                "    if record.get('mem_used_gb', 0) > record.get('mem_total_gb', 0):\n"
                "        return False, 'memory overflow'\n"
                "    return True, 'OK'\n"
                "```"
            ),
            function_signature=(
                "@pytest.mark.parametrize('record, ok, msg_contains', [...])\n"
                "def test_validate_gpu_record(record, ok, msg_contains):"
            ),
            examples=[
                {"input": "{'gpu_id': 0, 'temperature_c': 72, 'mem_used_gb': 40, 'mem_total_gb': 80}", "output": "(True, 'OK')"},
                {"input": "{'gpu_id': 1, 'temperature_c': 90, 'mem_used_gb': 40, 'mem_total_gb': 80}", "output": "(False, 'over temp')"},
            ],
            solution_code=(
                "import pytest\n\n"
                "def validate_gpu_record(record: dict) -> tuple[bool, str]:\n"
                "    if not isinstance(record.get('gpu_id'), int) or record['gpu_id'] < 0:\n"
                "        return False, 'invalid gpu_id'\n"
                "    if record.get('temperature_c', 0) >= 85:\n"
                "        return False, f'over temp: {record[\"temperature_c\"]}C'\n"
                "    if record.get('mem_used_gb', 0) > record.get('mem_total_gb', 0):\n"
                "        return False, 'memory overflow'\n"
                "    return True, 'OK'\n\n"
                "@pytest.mark.parametrize('record, ok, msg_contains', [\n"
                "    pytest.param(\n"
                "        {'gpu_id': 0, 'temperature_c': 72, 'mem_used_gb': 40, 'mem_total_gb': 80},\n"
                "        True, 'OK', id='healthy'),\n"
                "    pytest.param(\n"
                "        {'gpu_id': 1, 'temperature_c': 90, 'mem_used_gb': 40, 'mem_total_gb': 80},\n"
                "        False, 'over temp', id='over-temp'),\n"
                "    pytest.param(\n"
                "        {'gpu_id': 2, 'temperature_c': 70, 'mem_used_gb': 90, 'mem_total_gb': 80},\n"
                "        False, 'memory overflow', id='mem-overflow'),\n"
                "    pytest.param(\n"
                "        {'gpu_id': -1, 'temperature_c': 70, 'mem_used_gb': 10, 'mem_total_gb': 80},\n"
                "        False, 'invalid gpu_id', id='negative-id'),\n"
                "    pytest.param(\n"
                "        {'temperature_c': 70, 'mem_used_gb': 10, 'mem_total_gb': 80},\n"
                "        False, 'invalid gpu_id', id='missing-id'),\n"
                "])\n"
                "def test_validate_gpu_record(record, ok, msg_contains):\n"
                "    is_valid, msg = validate_gpu_record(record)\n"
                "    assert is_valid == ok\n"
                "    assert msg_contains in msg"
            ),
            test_code=(
                "def validate_gpu_record(record):\n"
                "    if not isinstance(record.get('gpu_id'), int) or record['gpu_id'] < 0:\n"
                "        return False, 'invalid gpu_id'\n"
                "    if record.get('temperature_c', 0) >= 85:\n"
                "        return False, f'over temp: {record[\"temperature_c\"]}C'\n"
                "    if record.get('mem_used_gb', 0) > record.get('mem_total_gb', 0):\n"
                "        return False, 'memory overflow'\n"
                "    return True, 'OK'\n\n"
                "cases = [\n"
                "    ({'gpu_id': 0, 'temperature_c': 72, 'mem_used_gb': 40, 'mem_total_gb': 80}, True, 'OK'),\n"
                "    ({'gpu_id': 1, 'temperature_c': 90, 'mem_used_gb': 40, 'mem_total_gb': 80}, False, 'over temp'),\n"
                "    ({'gpu_id': 2, 'temperature_c': 70, 'mem_used_gb': 90, 'mem_total_gb': 80}, False, 'memory overflow'),\n"
                "    ({'gpu_id': -1, 'temperature_c': 70, 'mem_used_gb': 10, 'mem_total_gb': 80}, False, 'invalid gpu_id'),\n"
                "    ({'temperature_c': 70, 'mem_used_gb': 10, 'mem_total_gb': 80}, False, 'invalid gpu_id'),\n"
                "]\n"
                "for record, ok, msg_contains in cases:\n"
                "    is_valid, msg = validate_gpu_record(record)\n"
                "    assert is_valid == ok and msg_contains in msg\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use pytest.param(..., id='name') to give each case a readable ID.",
                "Check both the boolean result and that the message contains the expected substring.",
            ],
        ),
    ]

    return TopicSection(
        title="Parametrize — Data-Driven Tests",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "@pytest.mark.parametrize eliminates copy-paste tests — one function, many inputs.",
            "Use pytest.param(..., id='name') for readable test IDs in output.",
            "Stack two @parametrize decorators to get the cartesian product of inputs.",
            "Parametrize is ideal for validation functions, parsers, and converters.",
            "Each parametrized case is a separate test — one failure doesn't block others.",
        ],
    )


def _advanced_fixtures() -> TopicSection:
    explanation = (
        "### Advanced Fixtures\n\n"
        "Fixtures can depend on other fixtures, be scoped for performance, "
        "and be shared across files via `conftest.py`.\n\n"
        "**Fixture composition:**\n"
        "```python\n"
        "@pytest.fixture\n"
        "def base_config():\n"
        "    return {'host': 'localhost', 'port': 5432}\n\n"
        "@pytest.fixture\n"
        "def db_connection(base_config):  # depends on base_config\n"
        "    conn = connect(**base_config)\n"
        "    yield conn\n"
        "    conn.close()\n"
        "```\n\n"
        "**Fixture scope — avoid repeated expensive setup:**\n"
        "```python\n"
        "@pytest.fixture(scope='session')  # runs once for the whole test run\n"
        "def compiled_model():\n"
        "    return load_model('weights.pt')  # expensive — do it once\n\n"
        "@pytest.fixture(scope='module')   # runs once per test file\n"
        "def db_schema():\n"
        "    return create_schema()\n"
        "```\n\n"
        "**Parametrized fixtures** — run all tests that use the fixture "
        "once per parameter value:\n"
        "```python\n"
        "@pytest.fixture(params=['sqlite', 'postgres'])\n"
        "def db_backend(request):\n"
        "    return create_db(request.param)\n\n"
        "def test_insert(db_backend):  # runs twice: once per backend\n"
        "    ...\n"
        "```\n\n"
        "**`request` fixture** — access test context inside a fixture:\n"
        "```python\n"
        "@pytest.fixture\n"
        "def config(request):\n"
        "    # request.param — value from params=[...]\n"
        "    # request.node.name — current test name\n"
        "    # request.addfinalizer(fn) — register teardown\n"
        "    ...\n"
        "```"
    )

    examples = [
        (
            "# --- Fixture composition and scope ---\n"
            "import pytest\n\n"
            "# Simulated expensive resource\n"
            "class ModelCache:\n"
            "    _load_count = 0\n\n"
            "    def __init__(self, name):\n"
            "        ModelCache._load_count += 1\n"
            "        self.name = name\n"
            "        self.ready = True\n\n"
            "@pytest.fixture(scope='module')  # loaded once per test file\n"
            "def model():\n"
            "    print(f'\\nLoading model (load #{ModelCache._load_count + 1})')\n"
            "    m = ModelCache('resnet50')\n"
            "    yield m\n"
            "    print(f'\\nUnloading model')\n\n"
            "@pytest.fixture  # fresh per test (default scope='function')\n"
            "def inference_input():\n"
            "    return {'batch_size': 4, 'input_shape': (3, 224, 224)}\n\n"
            "def test_model_is_ready(model):\n"
            "    assert model.ready == True\n\n"
            "def test_model_name(model):\n"
            "    assert model.name == 'resnet50'\n\n"
            "def test_inference_shape(model, inference_input):\n"
            "    # model is reused; inference_input is fresh\n"
            "    assert inference_input['batch_size'] == 4"
        ),
        (
            "# --- Parametrized fixture: test against multiple backends ---\n"
            "import pytest\n\n"
            "class InMemoryStore:\n"
            "    def __init__(self): self._data = {}\n"
            "    def set(self, k, v): self._data[k] = v\n"
            "    def get(self, k): return self._data.get(k)\n\n"
            "class DictStore:\n"
            "    \"\"\"Alternative implementation.\"\"\"\n"
            "    def __init__(self): self._store = dict()\n"
            "    def set(self, k, v): self._store[k] = v\n"
            "    def get(self, k): return self._store.get(k)\n\n"
            "@pytest.fixture(params=['memory', 'dict'])\n"
            "def store(request):\n"
            "    \"\"\"Parametrized fixture — tests run once per store type.\"\"\"\n"
            "    if request.param == 'memory':\n"
            "        return InMemoryStore()\n"
            "    return DictStore()\n\n"
            "# These tests run TWICE — once with InMemoryStore, once with DictStore\n"
            "def test_set_and_get(store):\n"
            "    store.set('key', 'value')\n"
            "    assert store.get('key') == 'value'\n\n"
            "def test_missing_key(store):\n"
            "    assert store.get('nonexistent') is None"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Scoped Fixture for a Connection Pool",
            statement=(
                "Write a `connection_pool` fixture with `scope='module'` that "
                "creates a `ConnectionPool` once per test file, and a `connection` "
                "fixture (default scope) that checks out one connection per test "
                "and returns it after.\n\n"
                "```python\n"
                "class ConnectionPool:\n"
                "    def __init__(self, size=5):\n"
                "        self._available = list(range(size))\n"
                "        self.checkout_count = 0\n"
                "    def checkout(self):\n"
                "        self.checkout_count += 1\n"
                "        return self._available.pop()\n"
                "    def checkin(self, conn):\n"
                "        self._available.append(conn)\n"
                "    def available(self): return len(self._available)\n"
                "```"
            ),
            function_signature=(
                "@pytest.fixture(scope='module')\n"
                "def connection_pool():\n\n"
                "@pytest.fixture\n"
                "def connection(connection_pool):\n\n"
                "def test_connection_is_valid(connection):\n"
                "def test_pool_returns_connection(connection, connection_pool):"
            ),
            examples=[
                {"input": "pool.checkout()", "output": "an integer connection id"},
                {"input": "pool.available() after checkin", "output": "back to original size"},
            ],
            solution_code=(
                "import pytest\n\n"
                "class ConnectionPool:\n"
                "    def __init__(self, size=5):\n"
                "        self._available = list(range(size))\n"
                "        self.checkout_count = 0\n"
                "    def checkout(self):\n"
                "        self.checkout_count += 1\n"
                "        return self._available.pop()\n"
                "    def checkin(self, conn):\n"
                "        self._available.append(conn)\n"
                "    def available(self): return len(self._available)\n\n"
                "@pytest.fixture(scope='module')\n"
                "def connection_pool():\n"
                "    return ConnectionPool(size=5)\n\n"
                "@pytest.fixture\n"
                "def connection(connection_pool):\n"
                "    conn = connection_pool.checkout()\n"
                "    yield conn\n"
                "    connection_pool.checkin(conn)  # always return the connection\n\n"
                "def test_connection_is_valid(connection):\n"
                "    assert connection is not None\n"
                "    assert isinstance(connection, int)\n\n"
                "def test_pool_returns_connection(connection, connection_pool):\n"
                "    # During the test, one connection is checked out\n"
                "    assert connection_pool.available() == 4"
            ),
            test_code=(
                "class ConnectionPool:\n"
                "    def __init__(self, size=5):\n"
                "        self._available = list(range(size))\n"
                "        self.checkout_count = 0\n"
                "    def checkout(self):\n"
                "        self.checkout_count += 1\n"
                "        return self._available.pop()\n"
                "    def checkin(self, conn): self._available.append(conn)\n"
                "    def available(self): return len(self._available)\n\n"
                "pool = ConnectionPool(5)\n"
                "conn = pool.checkout()\n"
                "assert conn is not None\n"
                "assert pool.available() == 4\n"
                "pool.checkin(conn)\n"
                "assert pool.available() == 5\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use `yield conn` in the connection fixture so checkin runs as teardown.",
                "scope='module' means the pool is created once and shared across all tests in the file.",
            ],
        ),
    ]

    return TopicSection(
        title="Advanced Fixtures",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Fixtures can depend on other fixtures — pytest resolves the dependency graph.",
            "scope='session' > 'module' > 'class' > 'function' — wider scope = less setup overhead.",
            "Parametrized fixtures run all dependent tests once per parameter value.",
            "Use `yield` for teardown — code after yield always runs, even if the test fails.",
            "The `request` fixture gives access to params, test name, and finalizer registration.",
        ],
    )


def _mocking_with_monkeypatch() -> TopicSection:
    explanation = (
        "### Mocking with monkeypatch\n\n"
        "`monkeypatch` is pytest's built-in fixture for temporarily replacing "
        "attributes, functions, environment variables, and dictionary entries "
        "during a test. Changes are automatically reverted after each test.\n\n"
        "**Common methods:**\n"
        "```python\n"
        "monkeypatch.setattr(obj, 'attr', value)   # replace an attribute\n"
        "monkeypatch.delattr(obj, 'attr')           # delete an attribute\n"
        "monkeypatch.setenv('VAR', 'value')         # set env variable\n"
        "monkeypatch.delenv('VAR', raising=False)   # delete env variable\n"
        "monkeypatch.setitem(d, 'key', value)       # set dict item\n"
        "monkeypatch.chdir(path)                    # change working directory\n"
        "```\n\n"
        "**When to use monkeypatch vs unittest.mock:**\n"
        "- `monkeypatch` — simple attribute/env replacement, no call tracking\n"
        "- `unittest.mock.patch` — when you need to assert call counts, "
        "arguments, or return values from mocked functions\n\n"
        "**unittest.mock basics:**\n"
        "```python\n"
        "from unittest.mock import patch, MagicMock\n\n"
        "with patch('module.function') as mock_fn:\n"
        "    mock_fn.return_value = 42\n"
        "    result = code_that_calls_function()\n"
        "    mock_fn.assert_called_once_with('expected_arg')\n"
        "```"
    )

    examples = [
        (
            "# --- monkeypatch: replace functions and env vars ---\n"
            "import os\n"
            "import pytest\n\n"
            "def get_api_url() -> str:\n"
            "    \"\"\"Read API URL from environment.\"\"\"\n"
            "    return os.environ.get('API_URL', 'https://api.production.com')\n\n"
            "def fetch_data(url: str) -> dict:\n"
            "    \"\"\"Simulate an HTTP call (would use requests in real code).\"\"\"\n"
            "    # In tests we'll replace this with a fake\n"
            "    raise NotImplementedError('Real HTTP call')\n\n"
            "def get_user_count() -> int:\n"
            "    url = get_api_url() + '/users/count'\n"
            "    data = fetch_data(url)\n"
            "    return data['count']\n\n"
            "def test_uses_env_url(monkeypatch):\n"
            "    monkeypatch.setenv('API_URL', 'https://api.staging.com')\n"
            "    assert get_api_url() == 'https://api.staging.com'\n\n"
            "def test_get_user_count(monkeypatch):\n"
            "    # Replace fetch_data with a fake that returns mock data\n"
            "    monkeypatch.setattr(\n"
            "        'builtins.__import__',  # simpler: patch the function directly\n"
            "        __import__\n"
            "    )\n"
            "    # More practical: patch the function in the module\n"
            "    def fake_fetch(url):\n"
            "        return {'count': 42}\n\n"
            "    monkeypatch.setattr('__main__.fetch_data', fake_fetch)\n"
            "    assert get_user_count() == 42"
        ),
        (
            "# --- unittest.mock.patch: track calls ---\n"
            "from unittest.mock import patch, MagicMock, call\n"
            "import pytest\n\n"
            "def send_alert(message: str, level: str = 'INFO') -> None:\n"
            "    \"\"\"Send an alert (would call an external service).\"\"\"\n"
            "    pass  # real implementation omitted\n\n"
            "def process_gpu_temps(temps: list[float], threshold: float = 85.0) -> int:\n"
            "    \"\"\"Send alerts for GPUs over threshold. Returns alert count.\"\"\"\n"
            "    count = 0\n"
            "    for i, temp in enumerate(temps):\n"
            "        if temp >= threshold:\n"
            "            send_alert(f'GPU {i} over temp: {temp}C', level='WARNING')\n"
            "            count += 1\n"
            "    return count\n\n"
            "def test_alerts_sent_for_hot_gpus():\n"
            "    with patch('__main__.send_alert') as mock_alert:\n"
            "        count = process_gpu_temps([72.0, 90.0, 68.0, 88.0])\n\n"
            "    assert count == 2\n"
            "    assert mock_alert.call_count == 2\n"
            "    # Check specific calls\n"
            "    mock_alert.assert_any_call('GPU 1 over temp: 90.0C', level='WARNING')\n"
            "    mock_alert.assert_any_call('GPU 3 over temp: 88.0C', level='WARNING')\n\n"
            "def test_no_alerts_when_cool():\n"
            "    with patch('__main__.send_alert') as mock_alert:\n"
            "        count = process_gpu_temps([70.0, 72.0, 68.0])\n\n"
            "    assert count == 0\n"
            "    mock_alert.assert_not_called()"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Mock an External API Call",
            statement=(
                "Write tests for `get_server_status` using `unittest.mock.patch` "
                "to avoid real HTTP calls. Test: successful response returns "
                "'online', a 503 response returns 'degraded', and a connection "
                "error returns 'offline'.\n\n"
                "```python\n"
                "import requests\n\n"
                "def get_server_status(url: str) -> str:\n"
                "    try:\n"
                "        r = requests.get(url, timeout=5)\n"
                "        if r.status_code == 200: return 'online'\n"
                "        return 'degraded'\n"
                "    except requests.ConnectionError:\n"
                "        return 'offline'\n"
                "```"
            ),
            function_signature=(
                "def test_server_online():\n"
                "def test_server_degraded():\n"
                "def test_server_offline():"
            ),
            examples=[
                {"input": "requests.get returns status 200", "output": "'online'"},
                {"input": "requests.get returns status 503", "output": "'degraded'"},
                {"input": "requests.get raises ConnectionError", "output": "'offline'"},
            ],
            solution_code=(
                "import requests\n"
                "from unittest.mock import patch, MagicMock\n\n"
                "def get_server_status(url: str) -> str:\n"
                "    try:\n"
                "        r = requests.get(url, timeout=5)\n"
                "        if r.status_code == 200: return 'online'\n"
                "        return 'degraded'\n"
                "    except requests.ConnectionError:\n"
                "        return 'offline'\n\n"
                "def test_server_online():\n"
                "    mock_resp = MagicMock()\n"
                "    mock_resp.status_code = 200\n"
                "    with patch('requests.get', return_value=mock_resp):\n"
                "        assert get_server_status('http://example.com') == 'online'\n\n"
                "def test_server_degraded():\n"
                "    mock_resp = MagicMock()\n"
                "    mock_resp.status_code = 503\n"
                "    with patch('requests.get', return_value=mock_resp):\n"
                "        assert get_server_status('http://example.com') == 'degraded'\n\n"
                "def test_server_offline():\n"
                "    with patch('requests.get', side_effect=requests.ConnectionError):\n"
                "        assert get_server_status('http://example.com') == 'offline'"
            ),
            test_code=(
                "from unittest.mock import patch, MagicMock\n"
                "import requests\n\n"
                "def get_server_status(url):\n"
                "    try:\n"
                "        r = requests.get(url, timeout=5)\n"
                "        return 'online' if r.status_code == 200 else 'degraded'\n"
                "    except requests.ConnectionError:\n"
                "        return 'offline'\n\n"
                "mock_200 = MagicMock(); mock_200.status_code = 200\n"
                "with patch('requests.get', return_value=mock_200):\n"
                "    assert get_server_status('http://x.com') == 'online'\n\n"
                "mock_503 = MagicMock(); mock_503.status_code = 503\n"
                "with patch('requests.get', return_value=mock_503):\n"
                "    assert get_server_status('http://x.com') == 'degraded'\n\n"
                "with patch('requests.get', side_effect=requests.ConnectionError):\n"
                "    assert get_server_status('http://x.com') == 'offline'\n\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use MagicMock() to create a fake response object and set .status_code on it.",
                "Use side_effect=SomeException to make the mock raise an exception.",
            ],
        ),
    ]

    return TopicSection(
        title="Mocking with monkeypatch and unittest.mock",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "monkeypatch replaces attributes/env vars for the duration of one test.",
            "unittest.mock.patch replaces objects and lets you assert on calls.",
            "MagicMock() creates a fake object — set .return_value or .side_effect.",
            "Use side_effect=ExceptionClass to make a mock raise an exception.",
            "Always patch at the point of use, not where the function is defined.",
        ],
    )


def _conftest_and_plugins() -> TopicSection:
    explanation = (
        "### conftest.py and Useful Plugins\n\n"
        "`conftest.py` is a special file pytest loads automatically. "
        "Fixtures defined there are available to all tests in the same "
        "directory and subdirectories — no import needed.\n\n"
        "**Typical conftest.py layout:**\n"
        "```\n"
        "project/\n"
        "├── conftest.py          ← session-wide fixtures\n"
        "├── tests/\n"
        "│   ├── conftest.py      ← test-suite fixtures\n"
        "│   ├── test_api.py\n"
        "│   └── test_utils.py\n"
        "```\n\n"
        "**conftest.py example:**\n"
        "```python\n"
        "# conftest.py\n"
        "import pytest\n\n"
        "@pytest.fixture(scope='session')\n"
        "def app_config():\n"
        "    return {'env': 'test', 'db': ':memory:'}\n\n"
        "def pytest_configure(config):\n"
        "    config.addinivalue_line('markers', 'slow: slow tests')\n"
        "```\n\n"
        "**Useful plugins (install with pip):**\n\n"
        "| Plugin | Purpose |\n"
        "|--------|---------|\n"
        "| `pytest-cov` | Code coverage reports |\n"
        "| `pytest-xdist` | Parallel test execution |\n"
        "| `pytest-mock` | Cleaner mock fixture (`mocker`) |\n"
        "| `pytest-timeout` | Fail tests that run too long |\n"
        "| `pytest-randomly` | Randomise test order |\n\n"
        "**Coverage:**\n"
        "```bash\n"
        "pip install pytest-cov\n"
        "pytest --cov=mypackage --cov-report=term-missing\n"
        "```\n\n"
        "**Parallel execution:**\n"
        "```bash\n"
        "pip install pytest-xdist\n"
        "pytest -n auto   # use all CPU cores\n"
        "pytest -n 4      # use 4 workers\n"
        "```"
    )

    examples = [
        (
            "# --- conftest.py: shared fixtures without imports ---\n\n"
            "# File structure:\n"
            "# project/\n"
            "# ├── conftest.py\n"
            "# └── tests/\n"
            "#     ├── test_auth.py\n"
            "#     └── test_data.py\n\n"
            "# conftest.py  (no imports needed in test files)\n"
            "import pytest\n\n"
            "@pytest.fixture(scope='session')\n"
            "def app_settings():\n"
            "    \"\"\"Shared settings for the entire test session.\"\"\"\n"
            "    return {\n"
            "        'debug': True,\n"
            "        'db_url': 'sqlite:///:memory:',\n"
            "        'secret_key': 'test-secret',\n"
            "    }\n\n"
            "@pytest.fixture\n"
            "def admin_user():\n"
            "    \"\"\"A standard admin user dict for tests.\"\"\"\n"
            "    return {'username': 'admin', 'role': 'admin', 'active': True}\n\n"
            "# tests/test_auth.py  — uses conftest fixtures directly\n"
            "def test_admin_is_active(admin_user):          # no import!\n"
            "    assert admin_user['active'] == True\n\n"
            "def test_settings_has_db(app_settings):        # no import!\n"
            "    assert 'db_url' in app_settings"
        ),
        (
            "# --- pytest-cov: measuring test coverage ---\n\n"
            "# Install: pip install pytest-cov\n\n"
            "# Run with coverage:\n"
            "# pytest --cov=mymodule --cov-report=term-missing\n\n"
            "# Example output:\n"
            "# Name              Stmts   Miss  Cover   Missing\n"
            "# -----------------------------------------------\n"
            "# mymodule/utils.py    45      3    93%   12, 45, 67\n"
            "# mymodule/api.py      82      0   100%\n"
            "# -----------------------------------------------\n"
            "# TOTAL               127      3    98%\n\n"
            "# Generate HTML report:\n"
            "# pytest --cov=mymodule --cov-report=html\n"
            "# open htmlcov/index.html\n\n"
            "# Fail if coverage drops below threshold:\n"
            "# pytest --cov=mymodule --cov-fail-under=90\n\n"
            "# --- pytest-timeout: catch hanging tests ---\n"
            "# pip install pytest-timeout\n\n"
            "import pytest\n\n"
            "@pytest.mark.timeout(5)  # fail if test takes > 5 seconds\n"
            "def test_fast_operation():\n"
            "    result = sum(range(1_000_000))\n"
            "    assert result > 0"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Design a conftest.py for a Hardware Test Suite",
            statement=(
                "Design a `conftest.py` for a nip hardware validation test suite. "
                "It should provide:\n"
                "1. A `session`-scoped `test_config` fixture returning a dict with "
                "'max_temp_c', 'min_memory_gb', and 'timeout_s'\n"
                "2. A `function`-scoped `gpu_record` fixture returning a healthy "
                "GPU dict\n"
                "3. A `function`-scoped `bad_gpu_record` fixture returning an "
                "over-temperature GPU dict\n\n"
                "Then write 2 tests that use these fixtures."
            ),
            function_signature=(
                "# conftest.py\n"
                "@pytest.fixture(scope='session')\n"
                "def test_config():\n\n"
                "@pytest.fixture\n"
                "def gpu_record():\n\n"
                "@pytest.fixture\n"
                "def bad_gpu_record():\n\n"
                "# test_hardware.py\n"
                "def test_healthy_gpu_passes(gpu_record, test_config):\n"
                "def test_hot_gpu_fails(bad_gpu_record, test_config):"
            ),
            examples=[
                {"input": "gpu_record fixture", "output": "{'gpu_id': 0, 'temperature_c': 72, 'mem_gb': 80}"},
                {"input": "bad_gpu_record fixture", "output": "{'gpu_id': 1, 'temperature_c': 92, 'mem_gb': 80}"},
            ],
            solution_code=(
                "import pytest\n\n"
                "# --- conftest.py ---\n\n"
                "@pytest.fixture(scope='session')\n"
                "def test_config():\n"
                "    return {'max_temp_c': 85, 'min_memory_gb': 16, 'timeout_s': 30}\n\n"
                "@pytest.fixture\n"
                "def gpu_record():\n"
                "    return {'gpu_id': 0, 'temperature_c': 72, 'mem_gb': 80, 'status': 'OK'}\n\n"
                "@pytest.fixture\n"
                "def bad_gpu_record():\n"
                "    return {'gpu_id': 1, 'temperature_c': 92, 'mem_gb': 80, 'status': 'WARN'}\n\n"
                "# --- test_hardware.py ---\n\n"
                "def test_healthy_gpu_passes(gpu_record, test_config):\n"
                "    assert gpu_record['temperature_c'] < test_config['max_temp_c']\n"
                "    assert gpu_record['mem_gb'] >= test_config['min_memory_gb']\n\n"
                "def test_hot_gpu_fails(bad_gpu_record, test_config):\n"
                "    assert bad_gpu_record['temperature_c'] >= test_config['max_temp_c']"
            ),
            test_code=(
                "# Simulating conftest + test file in one block\n"
                "test_config = {'max_temp_c': 85, 'min_memory_gb': 16, 'timeout_s': 30}\n"
                "gpu_record = {'gpu_id': 0, 'temperature_c': 72, 'mem_gb': 80, 'status': 'OK'}\n"
                "bad_gpu_record = {'gpu_id': 1, 'temperature_c': 92, 'mem_gb': 80, 'status': 'WARN'}\n\n"
                "assert gpu_record['temperature_c'] < test_config['max_temp_c']\n"
                "assert gpu_record['mem_gb'] >= test_config['min_memory_gb']\n"
                "assert bad_gpu_record['temperature_c'] >= test_config['max_temp_c']\n"
                "print('All tests passed!')"
            ),
            hints=[
                "scope='session' means test_config is created once and shared across all tests.",
                "Fixtures in conftest.py are available to all test files in the same directory.",
            ],
        ),
    ]

    return TopicSection(
        title="conftest.py and Useful Plugins",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "conftest.py fixtures are auto-discovered — no import needed in test files.",
            "Place conftest.py at the right level: project root for session fixtures, subdirs for local ones.",
            "pytest-cov measures coverage; use --cov-fail-under=N to enforce a minimum.",
            "pytest-xdist runs tests in parallel with -n auto — great for large suites.",
            "pytest-mock provides a `mocker` fixture as a cleaner alternative to patch().",
        ],
    )


# ---------------------------------------------------------------------------
# Mock test
# ---------------------------------------------------------------------------

def _mock_test() -> list[PracticeProblem]:
    return [
        PracticeProblem(
            title="Mock Test 1: Full Test Suite for a Cache Class",
            statement=(
                "**Target: ~10 minutes**\n\n"
                "Write a complete test suite for the `TTLCache` class below. "
                "Cover: set/get, expiry (use monkeypatch to control time), "
                "max size eviction, and missing key returns None.\n\n"
                "```python\n"
                "import time\n\n"
                "class TTLCache:\n"
                "    def __init__(self, max_size=100, ttl_seconds=60):\n"
                "        self._store = {}\n"
                "        self._max_size = max_size\n"
                "        self._ttl = ttl_seconds\n"
                "    def set(self, key, value):\n"
                "        if len(self._store) >= self._max_size:\n"
                "            oldest = next(iter(self._store))\n"
                "            del self._store[oldest]\n"
                "        self._store[key] = (value, time.time())\n"
                "    def get(self, key):\n"
                "        if key not in self._store: return None\n"
                "        value, ts = self._store[key]\n"
                "        if time.time() - ts > self._ttl:\n"
                "            del self._store[key]\n"
                "            return None\n"
                "        return value\n"
                "```"
            ),
            function_signature=(
                "def test_set_and_get():\n"
                "def test_missing_key():\n"
                "def test_expired_key(monkeypatch):\n"
                "def test_max_size_eviction():"
            ),
            examples=[
                {"input": "cache.set('k', 'v'); cache.get('k')", "output": "'v'"},
                {"input": "cache.get('missing')", "output": "None"},
                {"input": "after TTL expires: cache.get('k')", "output": "None"},
            ],
            solution_code=(
                "import time\n"
                "import pytest\n\n"
                "class TTLCache:\n"
                "    def __init__(self, max_size=100, ttl_seconds=60):\n"
                "        self._store = {}\n"
                "        self._max_size = max_size\n"
                "        self._ttl = ttl_seconds\n"
                "    def set(self, key, value):\n"
                "        if len(self._store) >= self._max_size:\n"
                "            oldest = next(iter(self._store))\n"
                "            del self._store[oldest]\n"
                "        self._store[key] = (value, time.time())\n"
                "    def get(self, key):\n"
                "        if key not in self._store: return None\n"
                "        value, ts = self._store[key]\n"
                "        if time.time() - ts > self._ttl:\n"
                "            del self._store[key]\n"
                "            return None\n"
                "        return value\n\n"
                "def test_set_and_get():\n"
                "    cache = TTLCache()\n"
                "    cache.set('name', 'Alice')\n"
                "    assert cache.get('name') == 'Alice'\n\n"
                "def test_missing_key():\n"
                "    cache = TTLCache()\n"
                "    assert cache.get('nonexistent') is None\n\n"
                "def test_expired_key(monkeypatch):\n"
                "    cache = TTLCache(ttl_seconds=10)\n"
                "    cache.set('key', 'value')\n"
                "    # Simulate time passing beyond TTL\n"
                "    monkeypatch.setattr(time, 'time', lambda: time.time() + 20)\n"
                "    assert cache.get('key') is None\n\n"
                "def test_max_size_eviction():\n"
                "    cache = TTLCache(max_size=2)\n"
                "    cache.set('a', 1)\n"
                "    cache.set('b', 2)\n"
                "    cache.set('c', 3)  # evicts 'a'\n"
                "    assert cache.get('a') is None\n"
                "    assert cache.get('b') == 2\n"
                "    assert cache.get('c') == 3"
            ),
            test_code=(
                "import time\n\n"
                "class TTLCache:\n"
                "    def __init__(self, max_size=100, ttl_seconds=60):\n"
                "        self._store = {}; self._max_size = max_size; self._ttl = ttl_seconds\n"
                "    def set(self, key, value):\n"
                "        if len(self._store) >= self._max_size:\n"
                "            del self._store[next(iter(self._store))]\n"
                "        self._store[key] = (value, time.time())\n"
                "    def get(self, key):\n"
                "        if key not in self._store: return None\n"
                "        value, ts = self._store[key]\n"
                "        if time.time() - ts > self._ttl:\n"
                "            del self._store[key]; return None\n"
                "        return value\n\n"
                "c = TTLCache()\n"
                "c.set('k', 'v'); assert c.get('k') == 'v'\n"
                "assert c.get('missing') is None\n"
                "c2 = TTLCache(max_size=2)\n"
                "c2.set('a', 1); c2.set('b', 2); c2.set('c', 3)\n"
                "assert c2.get('a') is None\n"
                "assert c2.get('c') == 3\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use monkeypatch.setattr(time, 'time', lambda: time.time() + 20) to fast-forward time.",
                "Test max_size by setting max_size=2 and inserting 3 items — the first should be evicted.",
            ],
        ),
        PracticeProblem(
            title="Mock Test 2: Parametrized + Fixture Combination",
            statement=(
                "**Target: ~10 minutes**\n\n"
                "Write a `log_parser` fixture that returns a `LogParser` instance "
                "pre-loaded with sample log lines. Then write a parametrized test "
                "that checks `count_by_level(level)` for ERROR, WARNING, and INFO.\n\n"
                "```python\n"
                "class LogParser:\n"
                "    def __init__(self, lines: list[str]):\n"
                "        self._lines = lines\n"
                "    def count_by_level(self, level: str) -> int:\n"
                "        return sum(1 for l in self._lines if l.startswith(level))\n"
                "    def errors(self) -> list[str]:\n"
                "        return [l for l in self._lines if l.startswith('ERROR')]\n"
                "```\n\n"
                "Sample lines: `['ERROR: disk full', 'INFO: started', 'WARNING: slow', "
                "'ERROR: timeout', 'INFO: done']`"
            ),
            function_signature=(
                "@pytest.fixture\n"
                "def log_parser():\n\n"
                "@pytest.mark.parametrize('level, expected_count', [...])\n"
                "def test_count_by_level(log_parser, level, expected_count):\n\n"
                "def test_errors_list(log_parser):"
            ),
            examples=[
                {"input": "count_by_level('ERROR')", "output": "2"},
                {"input": "count_by_level('INFO')", "output": "2"},
                {"input": "errors()", "output": "['ERROR: disk full', 'ERROR: timeout']"},
            ],
            solution_code=(
                "import pytest\n\n"
                "class LogParser:\n"
                "    def __init__(self, lines):\n"
                "        self._lines = lines\n"
                "    def count_by_level(self, level):\n"
                "        return sum(1 for l in self._lines if l.startswith(level))\n"
                "    def errors(self):\n"
                "        return [l for l in self._lines if l.startswith('ERROR')]\n\n"
                "SAMPLE_LINES = [\n"
                "    'ERROR: disk full',\n"
                "    'INFO: started',\n"
                "    'WARNING: slow',\n"
                "    'ERROR: timeout',\n"
                "    'INFO: done',\n"
                "]\n\n"
                "@pytest.fixture\n"
                "def log_parser():\n"
                "    return LogParser(SAMPLE_LINES)\n\n"
                "@pytest.mark.parametrize('level, expected_count', [\n"
                "    ('ERROR',   2),\n"
                "    ('WARNING', 1),\n"
                "    ('INFO',    2),\n"
                "])\n"
                "def test_count_by_level(log_parser, level, expected_count):\n"
                "    assert log_parser.count_by_level(level) == expected_count\n\n"
                "def test_errors_list(log_parser):\n"
                "    errors = log_parser.errors()\n"
                "    assert len(errors) == 2\n"
                "    assert all(e.startswith('ERROR') for e in errors)"
            ),
            test_code=(
                "class LogParser:\n"
                "    def __init__(self, lines): self._lines = lines\n"
                "    def count_by_level(self, level): return sum(1 for l in self._lines if l.startswith(level))\n"
                "    def errors(self): return [l for l in self._lines if l.startswith('ERROR')]\n\n"
                "lines = ['ERROR: disk full', 'INFO: started', 'WARNING: slow', 'ERROR: timeout', 'INFO: done']\n"
                "p = LogParser(lines)\n"
                "assert p.count_by_level('ERROR') == 2\n"
                "assert p.count_by_level('WARNING') == 1\n"
                "assert p.count_by_level('INFO') == 2\n"
                "assert len(p.errors()) == 2\n"
                "print('All tests passed!')"
            ),
            hints=[
                "A fixture can be used alongside parametrize — pytest injects both.",
                "The fixture provides the object; parametrize provides the test cases.",
            ],
        ),
    ]


# ---------------------------------------------------------------------------
# Cheat sheet
# ---------------------------------------------------------------------------

def _cheat_sheet() -> str:
    return (
        "## pytest Quick-Reference Cheat Sheet\n\n"
        "### Running Tests\n"
        "```bash\n"
        "pytest                          # run all tests\n"
        "pytest test_file.py             # run one file\n"
        "pytest test_file.py::test_name  # run one test\n"
        "pytest -v                       # verbose output\n"
        "pytest -x                       # stop on first failure\n"
        "pytest -k 'login or auth'       # run matching tests\n"
        "pytest -m slow                  # run by mark\n"
        "pytest -m 'not slow'            # exclude by mark\n"
        "pytest --tb=short               # shorter tracebacks\n"
        "pytest -s                       # show print() output\n"
        "pytest --cov=pkg --cov-report=term-missing  # coverage\n"
        "pytest -n auto                  # parallel (pytest-xdist)\n"
        "```\n\n"
        "### Assertions\n"
        "```python\n"
        "assert x == expected\n"
        "assert x == pytest.approx(3.14)          # float comparison\n"
        "assert x == pytest.approx(100, rel=0.01) # within 1%\n"
        "assert 'key' in my_dict\n"
        "assert result is None\n"
        "assert isinstance(result, list)\n"
        "assert len(result) == 3\n"
        "```\n\n"
        "### Exceptions\n"
        "```python\n"
        "with pytest.raises(ValueError):\n"
        "    risky_call()\n\n"
        "with pytest.raises(ValueError, match='must be positive'):\n"
        "    risky_call(-1)\n\n"
        "with pytest.raises(KeyError) as exc_info:\n"
        "    d['missing']\n"
        "assert 'missing' in str(exc_info.value)\n"
        "```\n\n"
        "### Fixtures\n"
        "```python\n"
        "@pytest.fixture                    # function scope (default)\n"
        "@pytest.fixture(scope='module')    # once per file\n"
        "@pytest.fixture(scope='session')   # once per run\n"
        "@pytest.fixture(params=[1, 2, 3])  # parametrized fixture\n\n"
        "@pytest.fixture\n"
        "def my_fixture():\n"
        "    obj = setup()\n"
        "    yield obj       # test runs here\n"
        "    teardown(obj)   # always runs after\n"
        "```\n\n"
        "### Built-in Fixtures\n"
        "| Fixture | Purpose |\n"
        "|---------|--------|\n"
        "| `tmp_path` | Temporary directory (pathlib.Path) |\n"
        "| `capsys` | Capture stdout/stderr |\n"
        "| `monkeypatch` | Replace attrs, env vars, dict items |\n"
        "| `request` | Access test context inside fixture |\n"
        "| `mocker` | Mock fixture (requires pytest-mock) |\n\n"
        "### Parametrize\n"
        "```python\n"
        "@pytest.mark.parametrize('x, expected', [\n"
        "    (2, 4),\n"
        "    (3, 9),\n"
        "    pytest.param(-1, 1, id='negative'),\n"
        "])\n"
        "def test_square(x, expected):\n"
        "    assert x ** 2 == expected\n"
        "```\n\n"
        "### Marks\n"
        "```python\n"
        "@pytest.mark.skip(reason='...')         # always skip\n"
        "@pytest.mark.skipif(condition, reason)  # conditional skip\n"
        "@pytest.mark.xfail(reason='...')        # expected failure\n"
        "@pytest.mark.slow                       # custom mark\n"
        "@pytest.mark.timeout(5)                 # requires pytest-timeout\n"
        "```\n\n"
        "### Mocking\n"
        "```python\n"
        "# monkeypatch (built-in)\n"
        "monkeypatch.setattr(module, 'func', fake_func)\n"
        "monkeypatch.setenv('API_KEY', 'test-key')\n\n"
        "# unittest.mock\n"
        "from unittest.mock import patch, MagicMock\n"
        "with patch('module.func') as mock:\n"
        "    mock.return_value = 42\n"
        "    mock.side_effect = ValueError  # raise on call\n"
        "    mock.assert_called_once_with('arg')\n"
        "    mock.assert_not_called()\n"
        "```\n\n"
        "### conftest.py\n"
        "```python\n"
        "# conftest.py — fixtures available to all tests, no import needed\n"
        "@pytest.fixture(scope='session')\n"
        "def app_config():\n"
        "    return {'env': 'test'}\n\n"
        "def pytest_configure(config):\n"
        "    config.addinivalue_line('markers', 'slow: slow tests')\n"
        "```"
    )
