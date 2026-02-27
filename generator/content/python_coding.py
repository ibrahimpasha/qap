"""Python coding content module — Python interview prep for nip SDET."""

from __future__ import annotations

from generator.models import MCQ, NotebookSpec, PracticeProblem, TopicSection


def get_python_coding_spec() -> NotebookSpec:
    """Return a complete NotebookSpec for the Python coding notebook."""
    return NotebookSpec(
        title="Python Coding — Interview Prep",
        filename="03_python_coding.ipynb",
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
        "## Strategy Tips for the Python Coding Section (30 minutes)\n\n"
        "**Read the Problem Fully:** Spend the first 1-2 minutes reading the "
        "entire problem statement, including constraints and examples. "
        "Misreading the problem is the #1 cause of wasted time.\n\n"
        "**Start with Brute Force:** Get a working solution first, even if "
        "it's O(n²). A correct brute-force answer scores more than an "
        "incomplete optimized one.\n\n"
        "**Test Edge Cases:** Before submitting, mentally run through: empty "
        "input, single element, duplicates, negative numbers, and very large "
        "input. Add a quick check if time allows.\n\n"
        "**Time Management (2-3 problems in 30 minutes):**\n"
        "- Problem 1 (easy): ~8 minutes\n"
        "- Problem 2 (medium): ~12 minutes\n"
        "- Problem 3 (harder): ~10 minutes\n"
        "- If stuck on one problem for more than 5 minutes, move on and "
        "come back.\n\n"
        "**Use Python's Strengths:** Leverage built-in functions (`sorted`, "
        "`zip`, `enumerate`, `collections`), list comprehensions, and string "
        "methods. They save time and reduce bugs.\n\n"
        "**Common Pitfalls:**\n"
        "- Forgetting to return (printing instead of returning)\n"
        "- Off-by-one errors in slicing and ranges\n"
        "- Mutating a list while iterating over it\n"
        "- Using `==` vs `is` for comparisons"
    )


# ---------------------------------------------------------------------------
# Beginner sections
# ---------------------------------------------------------------------------

def _beginner_sections() -> list[TopicSection]:
    return [
        _string_manipulation(),
        _list_comprehensions(),
        _dictionary_operations(),
        _file_io_basics(),
        _basic_error_handling(),
    ]



def _string_manipulation() -> TopicSection:
    """Beginner: String manipulation with nip data-validation example."""
    explanation = (
        "### String Manipulation\n\n"
        "Strings in Python are immutable sequences of characters. Mastering "
        "string methods is essential — they appear in nearly every coding "
        "interview.\n\n"
        "**Common methods:**\n"
        "- `split(sep)` / `join(iterable)` — split into list / join list into string\n"
        "- `strip()` / `lstrip()` / `rstrip()` — remove whitespace\n"
        "- `replace(old, new)` — substitute substrings\n"
        "- `find(sub)` / `index(sub)` — locate substrings (-1 vs exception)\n"
        "- `startswith()` / `endswith()` — prefix/suffix checks\n"
        "- `upper()` / `lower()` / `title()` — case conversion\n\n"
        "**f-strings (Python 3.6+):**\n"
        "```python\n"
        "name = 'nip'\n"
        "print(f'Company: {name}, Length: {len(name)}')\n"
        "```\n\n"
        "**String slicing:** `s[start:stop:step]` — works like list slicing.\n\n"
        "**nip context:** String manipulation is critical for parsing test "
        "output, validating configuration data, and processing log files."
    )

    examples = [
        (
            "# --- Common string methods ---\n"
            "text = '  Hello, World!  '\n\n"
            "# strip — remove leading/trailing whitespace\n"
            "print(text.strip())        # 'Hello, World!'\n\n"
            "# split — break into a list\n"
            "csv_line = 'gpu_0,Tesla V100,passed,98.5'\n"
            "fields = csv_line.split(',')\n"
            "print(fields)              # ['gpu_0', 'Tesla V100', 'passed', '98.5']\n\n"
            "# join — combine a list into a string\n"
            "print(' | '.join(fields))  # 'gpu_0 | Tesla V100 | passed | 98.5'\n\n"
            "# replace\n"
            "path = '/var/log/nip/test.log'\n"
            "print(path.replace('/var/log', '/tmp'))  # '/tmp/nip/test.log'\n\n"
            "# find vs index\n"
            "print(path.find('nip'))    # 9\n"
            "print(path.find('amd'))       # -1  (not found, no exception)\n\n"
            "# f-strings with expressions\n"
            "gpu_count = 8\n"
            "print(f'Cluster has {gpu_count} GPUs ({gpu_count * 16}GB total VRAM)')"
        ),
        (
            "# --- String slicing ---\n"
            "s = 'nip_SDET_2024'\n\n"
            "print(s[0:6])       # 'nip'\n"
            "print(s[7:11])      # 'SDET'\n"
            "print(s[-4:])       # '2024'\n"
            "print(s[::-1])      # '4202_TEDS_AIDIVN'  (reversed)\n\n"
            "# Check prefix/suffix\n"
            "print(s.startswith('nip'))  # True\n"
            "print(s.endswith('2024'))      # True\n\n"
            "# Count occurrences\n"
            "log = 'ERROR: disk full. ERROR: timeout. WARNING: slow.'\n"
            "print(log.count('ERROR'))  # 2"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Data Validation Utility",
            statement=(
                "Write a function that validates a device serial number. "
                "A valid serial has the format `XXX-YYYY-ZZ` where X is an "
                "uppercase letter, Y is a digit, and Z is an alphanumeric "
                "character. Return `True` if valid, `False` otherwise."
            ),
            function_signature="def validate_serial(serial: str) -> bool:",
            examples=[
                {"input": "'ABC-1234-X9'", "output": "True"},
                {"input": "'abc-1234-X9'", "output": "False"},
                {"input": "'AB-1234-X9'", "output": "False"},
                {"input": "'ABC-12-X9'", "output": "False"},
            ],
            solution_code=(
                "def validate_serial(serial: str) -> bool:\n"
                "    \"\"\"Validate device serial number format XXX-YYYY-ZZ.\"\"\"\n"
                "    parts = serial.split('-')\n"
                "    if len(parts) != 3:\n"
                "        return False\n"
                "    prefix, middle, suffix = parts\n"
                "    if len(prefix) != 3 or not prefix.isalpha() or not prefix.isupper():\n"
                "        return False\n"
                "    if len(middle) != 4 or not middle.isdigit():\n"
                "        return False\n"
                "    if len(suffix) != 2 or not suffix.isalnum():\n"
                "        return False\n"
                "    return True"
            ),
            test_code=(
                "assert validate_serial('ABC-1234-X9') == True\n"
                "assert validate_serial('abc-1234-X9') == False\n"
                "assert validate_serial('AB-1234-X9') == False\n"
                "assert validate_serial('ABC-12-X9') == False\n"
                "assert validate_serial('ABC-1234-X') == False\n"
                "assert validate_serial('') == False\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Split the string on '-' and check each part separately.",
                "Use str.isalpha(), str.isdigit(), str.isalnum(), str.isupper().",
            ],
        ),
        PracticeProblem(
            title="Reverse Words in a String",
            statement=(
                "Given a string of words separated by spaces, return the "
                "string with the words in reverse order. Multiple spaces "
                "between words should be collapsed to a single space, and "
                "leading/trailing spaces should be removed."
            ),
            function_signature="def reverse_words(s: str) -> str:",
            examples=[
                {"input": "'  hello world  '", "output": "'world hello'"},
                {"input": "'the sky is blue'", "output": "'blue is sky the'"},
                {"input": "'a good   example'", "output": "'example good a'"},
            ],
            solution_code=(
                "def reverse_words(s: str) -> str:\n"
                "    \"\"\"Reverse words in a string, collapsing extra spaces.\"\"\"\n"
                "    return ' '.join(s.split()[::-1])"
            ),
            test_code=(
                "assert reverse_words('  hello world  ') == 'world hello'\n"
                "assert reverse_words('the sky is blue') == 'blue is sky the'\n"
                "assert reverse_words('a good   example') == 'example good a'\n"
                "assert reverse_words('  ') == ''\n"
                "assert reverse_words('single') == 'single'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "s.split() with no argument splits on any whitespace and removes empty strings.",
                "Reverse the resulting list with [::-1], then join with a single space.",
            ],
        ),
        PracticeProblem(
            title="Count Character Frequency",
            statement=(
                "Write a function that returns a dictionary mapping each "
                "character to its frequency in the input string. Ignore "
                "spaces and treat uppercase and lowercase as the same character."
            ),
            function_signature="def char_frequency(s: str) -> dict[str, int]:",
            examples=[
                {"input": "'Hello World'", "output": "{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}"},
                {"input": "''", "output": "{}"},
            ],
            solution_code=(
                "def char_frequency(s: str) -> dict[str, int]:\n"
                "    \"\"\"Count frequency of each character (case-insensitive, no spaces).\"\"\"\n"
                "    freq = {}\n"
                "    for ch in s.lower():\n"
                "        if ch != ' ':\n"
                "            freq[ch] = freq.get(ch, 0) + 1\n"
                "    return freq"
            ),
            test_code=(
                "assert char_frequency('Hello World') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}\n"
                "assert char_frequency('') == {}\n"
                "assert char_frequency('   ') == {}\n"
                "assert char_frequency('aA') == {'a': 2}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Convert to lowercase first with s.lower().",
                "Use dict.get(key, 0) to safely increment counts.",
            ],
        ),
        PracticeProblem(
            title="Is Palindrome",
            statement=(
                "Write a function that checks if a string is a palindrome. "
                "Consider only alphanumeric characters and ignore case. "
                "Return True if it is a palindrome, False otherwise."
            ),
            function_signature="def is_palindrome(s: str) -> bool:",
            examples=[
                {"input": "'A man, a plan, a canal: Panama'", "output": "True"},
                {"input": "'race a car'", "output": "False"},
                {"input": "' '", "output": "True"},
            ],
            solution_code=(
                "def is_palindrome(s: str) -> bool:\n"
                "    \"\"\"Check if string is a palindrome (alphanumeric only, case-insensitive).\"\"\"\n"
                "    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())\n"
                "    return cleaned == cleaned[::-1]"
            ),
            test_code=(
                "assert is_palindrome('A man, a plan, a canal: Panama') == True\n"
                "assert is_palindrome('race a car') == False\n"
                "assert is_palindrome(' ') == True\n"
                "assert is_palindrome('') == True\n"
                "assert is_palindrome('Was it a car or a cat I saw?') == True\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Filter to alphanumeric characters with ch.isalnum(), then lowercase.",
                "Compare the cleaned string to its reverse with [::-1].",
            ],
        ),
    ]

    return TopicSection(
        title="String Manipulation",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Strings are immutable — every operation returns a new string.",
            "Use split/join for parsing and assembling delimited data.",
            "f-strings are the cleanest way to format output (Python 3.6+).",
            "find() returns -1 on failure; index() raises ValueError.",
            "String slicing s[start:stop:step] is a powerful tool for extraction and reversal.",
        ],
    )


def _list_comprehensions() -> TopicSection:
    """Beginner: List comprehensions and built-in functions."""
    explanation = (
        "### List Comprehensions and Built-in Functions\n\n"
        "List comprehensions provide a concise way to create lists. Combined "
        "with Python's powerful built-in functions, they let you write "
        "expressive one-liners that replace verbose loops.\n\n"
        "**List comprehension syntax:**\n"
        "```python\n"
        "[expression for item in iterable if condition]\n"
        "```\n\n"
        "**Key built-in functions:**\n"
        "- `map(func, iterable)` — apply function to every element\n"
        "- `filter(func, iterable)` — keep elements where func returns True\n"
        "- `zip(*iterables)` — pair up elements from multiple iterables\n"
        "- `enumerate(iterable)` — get (index, value) pairs\n"
        "- `sorted(iterable, key=, reverse=)` — return sorted list\n"
        "- `any(iterable)` / `all(iterable)` — logical OR / AND across elements"
    )

    examples = [
        (
            "# --- List comprehensions ---\n"
            "# Basic: squares of 0-9\n"
            "squares = [x ** 2 for x in range(10)]\n"
            "print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n\n"
            "# With condition: even squares only\n"
            "even_sq = [x ** 2 for x in range(10) if x % 2 == 0]\n"
            "print(even_sq)  # [0, 4, 16, 36, 64]\n\n"
            "# Nested: flatten a 2D list\n"
            "matrix = [[1, 2], [3, 4], [5, 6]]\n"
            "flat = [val for row in matrix for val in row]\n"
            "print(flat)     # [1, 2, 3, 4, 5, 6]\n\n"
            "# Dict comprehension\n"
            "word = 'banana'\n"
            "freq = {ch: word.count(ch) for ch in set(word)}\n"
            "print(freq)     # {'b': 1, 'a': 3, 'n': 2}"
        ),
        (
            "# --- Built-in functions ---\n"
            "nums = [3, 1, 4, 1, 5, 9, 2, 6]\n\n"
            "# enumerate — get index and value\n"
            "for i, val in enumerate(nums):\n"
            "    if val == 5:\n"
            "        print(f'Found 5 at index {i}')  # Found 5 at index 4\n\n"
            "# zip — pair up two lists\n"
            "names = ['GPU-0', 'GPU-1', 'GPU-2']\n"
            "temps = [72, 68, 75]\n"
            "for name, temp in zip(names, temps):\n"
            "    print(f'{name}: {temp}°C')\n\n"
            "# sorted with key\n"
            "words = ['banana', 'apple', 'cherry']\n"
            "print(sorted(words, key=len))  # ['apple', 'banana', 'cherry']\n\n"
            "# any / all\n"
            "test_results = [True, True, False, True]\n"
            "print(any(test_results))  # True  (at least one passed)\n"
            "print(all(test_results))  # False (not all passed)"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Filter and Transform Test Results",
            statement=(
                "Given a list of test result dictionaries with keys 'name', "
                "'status' ('pass'/'fail'), and 'duration' (float seconds), "
                "return a list of names of failed tests sorted by duration "
                "(longest first)."
            ),
            function_signature=(
                "def failed_tests_by_duration(results: list[dict]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'name': 'test_a', 'status': 'fail', 'duration': 1.2}, "
                        "{'name': 'test_b', 'status': 'pass', 'duration': 0.5}, "
                        "{'name': 'test_c', 'status': 'fail', 'duration': 3.1}]"
                    ),
                    "output": "['test_c', 'test_a']",
                },
            ],
            solution_code=(
                "def failed_tests_by_duration(results: list[dict]) -> list[str]:\n"
                "    \"\"\"Return names of failed tests sorted by duration descending.\"\"\"\n"
                "    failed = [r for r in results if r['status'] == 'fail']\n"
                "    failed.sort(key=lambda r: r['duration'], reverse=True)\n"
                "    return [r['name'] for r in failed]"
            ),
            test_code=(
                "results = [\n"
                "    {'name': 'test_a', 'status': 'fail', 'duration': 1.2},\n"
                "    {'name': 'test_b', 'status': 'pass', 'duration': 0.5},\n"
                "    {'name': 'test_c', 'status': 'fail', 'duration': 3.1},\n"
                "    {'name': 'test_d', 'status': 'pass', 'duration': 0.1},\n"
                "]\n"
                "assert failed_tests_by_duration(results) == ['test_c', 'test_a']\n"
                "assert failed_tests_by_duration([]) == []\n"
                "assert failed_tests_by_duration([{'name': 'x', 'status': 'pass', 'duration': 1.0}]) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a list comprehension to filter, then sort with a key function.",
                "Extract names after sorting with another comprehension.",
            ],
        ),
        PracticeProblem(
            title="Flatten and Deduplicate",
            statement=(
                "Given a list of lists of integers, return a sorted list of "
                "unique integers from all the sublists combined."
            ),
            function_signature="def flatten_unique(lists: list[list[int]]) -> list[int]:",
            examples=[
                {"input": "[[3, 1, 2], [2, 4, 1], [5]]", "output": "[1, 2, 3, 4, 5]"},
                {"input": "[[1, 1, 1]]", "output": "[1]"},
                {"input": "[]", "output": "[]"},
            ],
            solution_code=(
                "def flatten_unique(lists: list[list[int]]) -> list[int]:\n"
                "    \"\"\"Flatten nested lists and return sorted unique values.\"\"\"\n"
                "    return sorted({val for sublist in lists for val in sublist})"
            ),
            test_code=(
                "assert flatten_unique([[3, 1, 2], [2, 4, 1], [5]]) == [1, 2, 3, 4, 5]\n"
                "assert flatten_unique([[1, 1, 1]]) == [1]\n"
                "assert flatten_unique([]) == []\n"
                "assert flatten_unique([[], [1], [2, 3]]) == [1, 2, 3]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a nested comprehension: `val for sublist in lists for val in sublist`.",
                "Wrap in set() to deduplicate, then sorted() to sort.",
            ],
        ),
        PracticeProblem(
            title="Transpose a Matrix",
            statement=(
                "Given a 2D matrix (list of lists), return its transpose. "
                "The transpose swaps rows and columns: element at [i][j] "
                "moves to [j][i]."
            ),
            function_signature="def transpose(matrix: list[list[int]]) -> list[list[int]]:",
            examples=[
                {"input": "[[1, 2, 3], [4, 5, 6]]", "output": "[[1, 4], [2, 5], [3, 6]]"},
                {"input": "[[1, 2], [3, 4], [5, 6]]", "output": "[[1, 3, 5], [2, 4, 6]]"},
            ],
            solution_code=(
                "def transpose(matrix: list[list[int]]) -> list[list[int]]:\n"
                "    \"\"\"Return the transpose of a 2D matrix using zip.\"\"\"\n"
                "    if not matrix:\n"
                "        return []\n"
                "    return [list(row) for row in zip(*matrix)]"
            ),
            test_code=(
                "assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]\n"
                "assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]\n"
                "assert transpose([]) == []\n"
                "assert transpose([[1]]) == [[1]]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "zip(*matrix) unpacks the matrix rows and zips corresponding columns.",
                "Wrap each zip result in list() to get a list of lists.",
            ],
        ),
        PracticeProblem(
            title="Word Length Dictionary",
            statement=(
                "Given a list of words, return a dictionary mapping each "
                "word length to the list of words with that length. "
                "Words should appear in the order they were encountered."
            ),
            function_signature="def group_by_length(words: list[str]) -> dict[int, list[str]]:",
            examples=[
                {
                    "input": "['cat', 'dog', 'elephant', 'ant', 'ox']",
                    "output": "{3: ['cat', 'dog', 'ant'], 8: ['elephant'], 2: ['ox']}",
                },
            ],
            solution_code=(
                "def group_by_length(words: list[str]) -> dict[int, list[str]]:\n"
                "    \"\"\"Group words by their length.\"\"\"\n"
                "    result = {}\n"
                "    for word in words:\n"
                "        length = len(word)\n"
                "        result.setdefault(length, []).append(word)\n"
                "    return result"
            ),
            test_code=(
                "result = group_by_length(['cat', 'dog', 'elephant', 'ant', 'ox'])\n"
                "assert result[3] == ['cat', 'dog', 'ant']\n"
                "assert result[8] == ['elephant']\n"
                "assert result[2] == ['ox']\n"
                "assert group_by_length([]) == {}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use dict.setdefault(key, []) to initialize missing keys.",
                "Or use defaultdict(list) from collections.",
            ],
        ),
    ]

    return TopicSection(
        title="List Comprehensions and Built-in Functions",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "List comprehensions are faster and more Pythonic than equivalent for-loops.",
            "Use enumerate() instead of manual index tracking.",
            "zip() pairs elements; use zip(*matrix) to transpose a 2D list.",
            "sorted() returns a new list; list.sort() sorts in-place.",
            "any() and all() short-circuit — useful for validation checks.",
        ],
    )


def _dictionary_operations() -> TopicSection:
    """Beginner: Dictionary operations."""
    explanation = (
        "### Dictionary Operations\n\n"
        "Dictionaries (`dict`) are Python's hash table implementation — "
        "the most versatile data structure for key-value storage.\n\n"
        "**Creating dicts:**\n"
        "```python\n"
        "d = {'key': 'value'}          # literal\n"
        "d = dict(a=1, b=2)            # constructor\n"
        "d = {x: x**2 for x in range(5)}  # comprehension\n"
        "```\n\n"
        "**Key operations (all O(1) average):**\n"
        "- `d[key]` — access (raises KeyError if missing)\n"
        "- `d.get(key, default)` — safe access\n"
        "- `d[key] = value` — insert/update\n"
        "- `del d[key]` — delete\n"
        "- `key in d` — membership test\n\n"
        "**Iteration:**\n"
        "- `d.keys()`, `d.values()`, `d.items()` — views for looping\n\n"
        "**Merging (Python 3.9+):** `merged = d1 | d2`\n\n"
        "**defaultdict:** Auto-initializes missing keys with a factory function."
    )

    examples = [
        (
            "# --- Dictionary basics ---\n"
            "gpu_info = {\n"
            "    'model': 'A100',\n"
            "    'memory_gb': 80,\n"
            "    'cuda_cores': 6912,\n"
            "}\n\n"
            "# Access\n"
            "print(gpu_info['model'])              # 'A100'\n"
            "print(gpu_info.get('tdp', 'unknown')) # 'unknown'\n\n"
            "# Update and add\n"
            "gpu_info['tdp_watts'] = 300\n"
            "gpu_info['memory_gb'] = 80\n\n"
            "# Iterate\n"
            "for key, val in gpu_info.items():\n"
            "    print(f'{key}: {val}')\n\n"
            "# Dict comprehension — filter keys\n"
            "numeric = {k: v for k, v in gpu_info.items() if isinstance(v, int)}\n"
            "print(numeric)  # {'memory_gb': 80, 'cuda_cores': 6912, 'tdp_watts': 300}"
        ),
        (
            "# --- defaultdict and merging ---\n"
            "from collections import defaultdict\n\n"
            "# defaultdict — auto-initialize missing keys\n"
            "word_count = defaultdict(int)\n"
            "for word in 'the cat sat on the mat'.split():\n"
            "    word_count[word] += 1  # no KeyError for new keys\n"
            "print(dict(word_count))  # {'the': 2, 'cat': 1, 'sat': 1, ...}\n\n"
            "# Group items with defaultdict(list)\n"
            "test_by_status = defaultdict(list)\n"
            "results = [('test_a', 'pass'), ('test_b', 'fail'), ('test_c', 'pass')]\n"
            "for name, status in results:\n"
            "    test_by_status[status].append(name)\n"
            "print(dict(test_by_status))\n"
            "# {'pass': ['test_a', 'test_c'], 'fail': ['test_b']}\n\n"
            "# Merging dicts (Python 3.9+)\n"
            "defaults = {'timeout': 30, 'retries': 3}\n"
            "overrides = {'timeout': 60, 'verbose': True}\n"
            "config = defaults | overrides\n"
            "print(config)  # {'timeout': 60, 'retries': 3, 'verbose': True}"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Group Anagrams",
            statement=(
                "Given a list of strings, group the anagrams together. "
                "Two strings are anagrams if they contain the same characters "
                "in any order. Return a list of groups (each group is a list "
                "of strings). Order of groups and within groups does not matter."
            ),
            function_signature="def group_anagrams(words: list[str]) -> list[list[str]]:",
            examples=[
                {
                    "input": "['eat', 'tea', 'tan', 'ate', 'nat', 'bat']",
                    "output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]",
                },
            ],
            solution_code=(
                "from collections import defaultdict\n\n"
                "def group_anagrams(words: list[str]) -> list[list[str]]:\n"
                "    \"\"\"Group anagrams using sorted-string keys.\"\"\"\n"
                "    groups = defaultdict(list)\n"
                "    for word in words:\n"
                "        key = ''.join(sorted(word))  # anagrams share the same sorted form\n"
                "        groups[key].append(word)\n"
                "    return list(groups.values())"
            ),
            test_code=(
                "result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])\n"
                "# Sort inner lists and outer list for comparison\n"
                "result_sorted = sorted([sorted(g) for g in result])\n"
                "expected = sorted([sorted(g) for g in [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]])\n"
                "assert result_sorted == expected\n"
                "assert group_anagrams([]) == []\n"
                "assert group_anagrams(['a']) == [['a']]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a dictionary where the key is the sorted version of each word.",
                "defaultdict(list) makes grouping easy.",
            ],
        ),
        PracticeProblem(
            title="Two Sum",
            statement=(
                "Given a list of integers and a target sum, return the indices "
                "of the two numbers that add up to the target. Each input has "
                "exactly one solution, and you may not use the same element twice."
            ),
            function_signature="def two_sum(nums: list[int], target: int) -> list[int]:",
            examples=[
                {"input": "[2, 7, 11, 15], 9", "output": "[0, 1]"},
                {"input": "[3, 2, 4], 6", "output": "[1, 2]"},
            ],
            solution_code=(
                "def two_sum(nums: list[int], target: int) -> list[int]:\n"
                "    \"\"\"Find two indices that sum to target using a hash map. O(n).\"\"\"\n"
                "    seen = {}  # value -> index\n"
                "    for i, num in enumerate(nums):\n"
                "        complement = target - num\n"
                "        if complement in seen:\n"
                "            return [seen[complement], i]\n"
                "        seen[num] = i\n"
                "    return []"
            ),
            test_code=(
                "assert two_sum([2, 7, 11, 15], 9) == [0, 1]\n"
                "assert two_sum([3, 2, 4], 6) == [1, 2]\n"
                "assert two_sum([3, 3], 6) == [0, 1]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "For each number, check if its complement (target - num) is already in a dict.",
                "Store each number's index in the dict as you iterate.",
            ],
        ),
        PracticeProblem(
            title="Word Frequency Counter",
            statement=(
                "Write a function that counts the frequency of each word in "
                "a sentence. Words are case-insensitive and punctuation should "
                "be stripped. Return a dict mapping word to count, sorted by "
                "frequency (highest first)."
            ),
            function_signature="def word_frequency(sentence: str) -> dict[str, int]:",
            examples=[
                {
                    "input": "'The cat sat on the mat. The cat!'",
                    "output": "{'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}",
                },
            ],
            solution_code=(
                "import re\n\n"
                "def word_frequency(sentence: str) -> dict[str, int]:\n"
                "    \"\"\"Count word frequencies, case-insensitive, punctuation stripped.\"\"\"\n"
                "    words = re.findall(r'[a-z]+', sentence.lower())\n"
                "    freq = {}\n"
                "    for word in words:\n"
                "        freq[word] = freq.get(word, 0) + 1\n"
                "    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))"
            ),
            test_code=(
                "import re\n"
                "result = word_frequency('The cat sat on the mat. The cat!')\n"
                "assert result['the'] == 3\n"
                "assert result['cat'] == 2\n"
                "assert result['sat'] == 1\n"
                "# Verify sorted by frequency\n"
                "counts = list(result.values())\n"
                "assert counts == sorted(counts, reverse=True)\n"
                "assert word_frequency('') == {}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use re.findall(r'[a-z]+', sentence.lower()) to extract words.",
                "Sort the dict items by value (count) in descending order.",
            ],
        ),
        PracticeProblem(
            title="Merge Dictionaries with Conflict Resolution",
            statement=(
                "Write a function that merges a list of dictionaries. If the "
                "same key appears in multiple dicts, sum the values (assuming "
                "all values are integers). Return the merged dictionary."
            ),
            function_signature="def merge_dicts(dicts: list[dict]) -> dict:",
            examples=[
                {
                    "input": "[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]",
                    "output": "{'a': 6, 'b': 5, 'c': 4}",
                },
            ],
            solution_code=(
                "def merge_dicts(dicts: list[dict]) -> dict:\n"
                "    \"\"\"Merge dicts, summing values for duplicate keys.\"\"\"\n"
                "    result = {}\n"
                "    for d in dicts:\n"
                "        for key, value in d.items():\n"
                "            result[key] = result.get(key, 0) + value\n"
                "    return result"
            ),
            test_code=(
                "assert merge_dicts([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]) == {'a': 6, 'b': 5, 'c': 4}\n"
                "assert merge_dicts([]) == {}\n"
                "assert merge_dicts([{'x': 10}]) == {'x': 10}\n"
                "assert merge_dicts([{'a': 1}, {'a': 2}, {'a': 3}]) == {'a': 6}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Iterate over each dict and each key-value pair.",
                "Use result.get(key, 0) to safely accumulate values.",
            ],
        ),
    ]

    return TopicSection(
        title="Dictionary Operations",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "dict provides O(1) average-case access, insert, and delete.",
            "Use .get(key, default) to avoid KeyError on missing keys.",
            "defaultdict auto-initializes missing keys — great for counting and grouping.",
            "Dict comprehensions are concise for filtering and transforming dicts.",
            "Python 3.9+ supports dict merging with the | operator.",
        ],
    )


def _file_io_basics() -> TopicSection:
    """Beginner: File I/O basics with nip log-parser example."""
    explanation = (
        "### File I/O Basics\n\n"
        "Reading and writing files is a core skill for any SDET — from "
        "parsing test logs to generating reports.\n\n"
        "**Context managers (`with` statement):**\n"
        "```python\n"
        "with open('file.txt', 'r') as f:\n"
        "    content = f.read()\n"
        "# File is automatically closed when the block exits\n"
        "```\n\n"
        "**File modes:**\n"
        "- `'r'` — read (default)\n"
        "- `'w'` — write (overwrites)\n"
        "- `'a'` — append\n"
        "- `'x'` — exclusive create (fails if file exists)\n\n"
        "**Reading methods:**\n"
        "- `f.read()` — entire file as string\n"
        "- `f.readline()` — one line at a time\n"
        "- `f.readlines()` — list of all lines\n"
        "- Iterate: `for line in f:` — memory-efficient line-by-line\n\n"
        "**CSV handling:**\n"
        "```python\n"
        "import csv\n"
        "with open('data.csv') as f:\n"
        "    reader = csv.DictReader(f)\n"
        "    for row in reader:\n"
        "        print(row['column_name'])\n"
        "```"
    )

    examples = [
        (
            "# --- Reading and writing files ---\n"
            "# Write a file\n"
            "with open('/tmp/test_results.txt', 'w') as f:\n"
            "    f.write('test_login: PASS\\n')\n"
            "    f.write('test_logout: FAIL\\n')\n"
            "    f.write('test_signup: PASS\\n')\n\n"
            "# Read entire file\n"
            "with open('/tmp/test_results.txt', 'r') as f:\n"
            "    content = f.read()\n"
            "print(content)\n\n"
            "# Read line by line (memory-efficient for large files)\n"
            "with open('/tmp/test_results.txt', 'r') as f:\n"
            "    for line in f:\n"
            "        name, status = line.strip().split(': ')\n"
            "        print(f'{name} -> {status}')"
        ),
        (
            "# --- CSV handling ---\n"
            "import csv\n"
            "import io\n\n"
            "# Simulate a CSV file with io.StringIO\n"
            "csv_data = 'gpu_id,temperature,utilization\\n0,72,95\\n1,68,88\\n2,75,92\\n'\n"
            "reader = csv.DictReader(io.StringIO(csv_data))\n"
            "for row in reader:\n"
            "    print(f\"GPU {row['gpu_id']}: {row['temperature']}°C, {row['utilization']}% util\")\n\n"
            "# Writing CSV\n"
            "rows = [{'name': 'test_a', 'result': 'pass'}, {'name': 'test_b', 'result': 'fail'}]\n"
            "output = io.StringIO()\n"
            "writer = csv.DictWriter(output, fieldnames=['name', 'result'])\n"
            "writer.writeheader()\n"
            "writer.writerows(rows)\n"
            "print(output.getvalue())"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Simple Log Parser",
            statement=(
                "Write a function that parses a multi-line log string and "
                "returns a summary dictionary. Each log line has the format: "
                "`LEVEL: message` where LEVEL is one of ERROR, WARNING, INFO. "
                "Return a dict with keys 'error_count', 'warning_count', "
                "'info_count', and 'errors' (a list of error messages)."
            ),
            function_signature="def parse_log(log_text: str) -> dict:",
            examples=[
                {
                    "input": (
                        "'INFO: Server started\\n"
                        "ERROR: Disk full\\n"
                        "WARNING: High memory\\n"
                        "ERROR: Connection timeout'"
                    ),
                    "output": (
                        "{'error_count': 2, 'warning_count': 1, 'info_count': 1, "
                        "'errors': ['Disk full', 'Connection timeout']}"
                    ),
                },
            ],
            solution_code=(
                "def parse_log(log_text: str) -> dict:\n"
                "    \"\"\"Parse log text and return a summary dict.\"\"\"\n"
                "    result = {'error_count': 0, 'warning_count': 0,\n"
                "              'info_count': 0, 'errors': []}\n"
                "    if not log_text.strip():\n"
                "        return result\n"
                "    for line in log_text.strip().split('\\n'):\n"
                "        if not line.strip():\n"
                "            continue\n"
                "        level, _, message = line.partition(': ')\n"
                "        level = level.strip().upper()\n"
                "        if level == 'ERROR':\n"
                "            result['error_count'] += 1\n"
                "            result['errors'].append(message)\n"
                "        elif level == 'WARNING':\n"
                "            result['warning_count'] += 1\n"
                "        elif level == 'INFO':\n"
                "            result['info_count'] += 1\n"
                "    return result"
            ),
            test_code=(
                "log = 'INFO: Server started\\nERROR: Disk full\\nWARNING: High memory\\nERROR: Connection timeout'\n"
                "result = parse_log(log)\n"
                "assert result['error_count'] == 2\n"
                "assert result['warning_count'] == 1\n"
                "assert result['info_count'] == 1\n"
                "assert result['errors'] == ['Disk full', 'Connection timeout']\n"
                "assert parse_log('')['error_count'] == 0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Split the log text on newlines, then split each line on ': '.",
                "Use str.partition(': ') to safely split into level and message.",
            ],
        ),
        PracticeProblem(
            title="Parse nvidia-smi CSV Output",
            statement=(
                "Write a function that parses the CSV output of:\n"
                "`nvidia-smi --query-gpu=index,name,temperature.gpu,utilization.gpu,"
                "memory.used,memory.total --format=csv,noheader,nounits`\n\n"
                "Each line has 6 comma-separated fields. Return a list of dicts "
                "with keys: 'index' (int), 'name' (str), 'temp_c' (int), "
                "'util_pct' (int), 'mem_used_mb' (int), 'mem_total_mb' (int).\n\n"
                "Also write a `find_hot_gpus(gpus, threshold=85)` function that "
                "returns a list of GPU indices where temperature exceeds the threshold."
            ),
            function_signature=(
                "def parse_nvidia_smi(output: str) -> list[dict]:\n\n"
                "def find_hot_gpus(gpus: list[dict], threshold: int = 85) -> list[int]:"
            ),
            examples=[
                {
                    "input": "'0, A100-SXM4, 38, 5, 2048, 81920\\n1, A100-SXM4, 91, 98, 81920, 81920'",
                    "output": "[{'index': 0, 'temp_c': 38, ...}, {'index': 1, 'temp_c': 91, ...}]",
                },
                {"input": "find_hot_gpus(gpus, threshold=85)", "output": "[1]"},
            ],
            solution_code=(
                "def parse_nvidia_smi(output: str) -> list[dict]:\n"
                "    \"\"\"Parse nvidia-smi CSV output into a list of GPU stat dicts.\"\"\"\n"
                "    gpus = []\n"
                "    for line in output.strip().split('\\n'):\n"
                "        if not line.strip():\n"
                "            continue\n"
                "        parts = [p.strip() for p in line.split(',')]\n"
                "        gpus.append({\n"
                "            'index':        int(parts[0]),\n"
                "            'name':         parts[1],\n"
                "            'temp_c':       int(parts[2]),\n"
                "            'util_pct':     int(parts[3]),\n"
                "            'mem_used_mb':  int(parts[4]),\n"
                "            'mem_total_mb': int(parts[5]),\n"
                "        })\n"
                "    return gpus\n\n"
                "def find_hot_gpus(gpus: list[dict], threshold: int = 85) -> list[int]:\n"
                "    \"\"\"Return indices of GPUs exceeding the temperature threshold.\"\"\"\n"
                "    return [g['index'] for g in gpus if g['temp_c'] > threshold]"
            ),
            test_code=(
                "smi_output = '0, A100-SXM4-80GB, 38, 5, 2048, 81920\\n1, A100-SXM4-80GB, 91, 98, 81920, 81920'\n"
                "gpus = parse_nvidia_smi(smi_output)\n"
                "assert len(gpus) == 2\n"
                "assert gpus[0]['index'] == 0\n"
                "assert gpus[0]['temp_c'] == 38\n"
                "assert gpus[1]['util_pct'] == 98\n"
                "assert gpus[1]['mem_used_mb'] == 81920\n"
                "assert find_hot_gpus(gpus, threshold=85) == [1]\n"
                "assert find_hot_gpus(gpus, threshold=95) == []\n"
                "assert parse_nvidia_smi('') == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Split each line on ',' and strip whitespace from each field.",
                "Cast fields to int where needed: index, temp_c, util_pct, mem_used_mb, mem_total_mb.",
            ],
        ),
    ]

    return TopicSection(
        title="File I/O Basics",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Always use `with open(...)` — it guarantees the file is closed properly.",
            "Iterate over file objects line-by-line for memory efficiency on large files.",
            "csv.DictReader gives you rows as dictionaries keyed by header names.",
            "Use io.StringIO to simulate file objects in tests without touching disk.",
            "str.partition() is safer than split() when the delimiter might be missing.",
        ],
    )


def _basic_error_handling() -> TopicSection:
    """Beginner: Error handling with try/except/else/finally."""
    explanation = (
        "### Basic Error Handling\n\n"
        "Robust error handling is essential for test automation — tests must "
        "handle unexpected conditions gracefully.\n\n"
        "**try/except/else/finally:**\n"
        "```python\n"
        "try:\n"
        "    result = risky_operation()\n"
        "except SpecificError as e:\n"
        "    handle_error(e)\n"
        "else:\n"
        "    # Runs only if no exception was raised\n"
        "    process(result)\n"
        "finally:\n"
        "    # Always runs — cleanup code\n"
        "    cleanup()\n"
        "```\n\n"
        "**Common built-in exceptions:**\n"
        "- `ValueError` — wrong value (e.g., `int('abc')`)\n"
        "- `TypeError` — wrong type (e.g., `'a' + 1`)\n"
        "- `KeyError` — missing dict key\n"
        "- `IndexError` — list index out of range\n"
        "- `FileNotFoundError` — file doesn't exist\n"
        "- `ZeroDivisionError` — division by zero\n\n"
        "**Raising exceptions:**\n"
        "```python\n"
        "if value < 0:\n"
        "    raise ValueError(f'Expected non-negative, got {value}')\n"
        "```\n\n"
        "**Custom exceptions:**\n"
        "```python\n"
        "class TestFailedError(Exception):\n"
        "    \"\"\"Raised when a test case fails validation.\"\"\"\n"
        "    pass\n"
        "```"
    )

    examples = [
        (
            "# --- try/except/else/finally ---\n"
            "def safe_divide(a, b):\n"
            "    \"\"\"Divide a by b with error handling.\"\"\"\n"
            "    try:\n"
            "        result = a / b\n"
            "    except ZeroDivisionError:\n"
            "        print('Cannot divide by zero!')\n"
            "        return None\n"
            "    except TypeError as e:\n"
            "        print(f'Type error: {e}')\n"
            "        return None\n"
            "    else:\n"
            "        # Only runs if no exception\n"
            "        print(f'{a} / {b} = {result}')\n"
            "        return result\n"
            "    finally:\n"
            "        # Always runs\n"
            "        print('Division operation complete.')\n\n"
            "safe_divide(10, 3)   # 10 / 3 = 3.333...\n"
            "safe_divide(10, 0)   # Cannot divide by zero!\n"
            "safe_divide('a', 2)  # Type error: unsupported operand type(s)"
        ),
        (
            "# --- Custom exceptions for test automation ---\n"
            "class TestTimeoutError(Exception):\n"
            "    \"\"\"Raised when a test exceeds its time limit.\"\"\"\n"
            "    def __init__(self, test_name: str, limit_seconds: float):\n"
            "        self.test_name = test_name\n"
            "        self.limit_seconds = limit_seconds\n"
            "        super().__init__(\n"
            "            f'Test \"{test_name}\" exceeded {limit_seconds}s limit'\n"
            "        )\n\n"
            "def run_test(name: str, duration: float, limit: float):\n"
            "    \"\"\"Simulate running a test with a time limit.\"\"\"\n"
            "    if duration > limit:\n"
            "        raise TestTimeoutError(name, limit)\n"
            "    return f'{name}: PASSED in {duration}s'\n\n"
            "# Usage\n"
            "try:\n"
            "    print(run_test('test_login', 2.5, 5.0))   # PASSED\n"
            "    print(run_test('test_upload', 8.0, 5.0))   # raises!\n"
            "except TestTimeoutError as e:\n"
            "    print(f'TIMEOUT: {e}')\n"
            "    print(f'Test: {e.test_name}, Limit: {e.limit_seconds}s')"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Robust Config Parser",
            statement=(
                "Write a function that parses a configuration string into a "
                "dictionary. Each line has the format `key=value`. The function "
                "should skip blank lines and lines starting with '#' (comments). "
                "If a line doesn't contain '=', raise a ValueError with a "
                "message including the line number. Return the parsed dict."
            ),
            function_signature="def parse_config(config_text: str) -> dict:",
            examples=[
                {
                    "input": "'host=localhost\\nport=8080\\n# comment\\n\\ntimeout=30'",
                    "output": "{'host': 'localhost', 'port': '8080', 'timeout': '30'}",
                },
            ],
            solution_code=(
                "def parse_config(config_text: str) -> dict:\n"
                "    \"\"\"Parse key=value config text into a dict.\"\"\"\n"
                "    result = {}\n"
                "    for lineno, line in enumerate(config_text.split('\\n'), start=1):\n"
                "        line = line.strip()\n"
                "        if not line or line.startswith('#'):\n"
                "            continue\n"
                "        if '=' not in line:\n"
                "            raise ValueError(f'Invalid config at line {lineno}: {line!r}')\n"
                "        key, _, value = line.partition('=')\n"
                "        result[key.strip()] = value.strip()\n"
                "    return result"
            ),
            test_code=(
                "cfg = parse_config('host=localhost\\nport=8080\\n# comment\\n\\ntimeout=30')\n"
                "assert cfg == {'host': 'localhost', 'port': '8080', 'timeout': '30'}\n"
                "assert parse_config('') == {}\n"
                "assert parse_config('# only comments') == {}\n"
                "try:\n"
                "    parse_config('valid=ok\\nbad line')\n"
                "    assert False, 'Should have raised ValueError'\n"
                "except ValueError as e:\n"
                "    assert 'line 2' in str(e)\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use enumerate() to track line numbers.",
                "str.partition('=') splits on the first '=' only.",
            ],
        ),
    ]

    return TopicSection(
        title="Basic Error Handling",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Always catch specific exceptions, not bare `except:`.",
            "Use `else` for code that should run only when no exception occurs.",
            "Use `finally` for cleanup that must happen regardless of exceptions.",
            "Custom exceptions make error handling more expressive and testable.",
            "Raise exceptions early with descriptive messages — fail fast, fail clearly.",
        ],
    )


# ---------------------------------------------------------------------------
# Mid-Level sections
# ---------------------------------------------------------------------------

def _mid_level_sections() -> list[TopicSection]:
    return [
        _oop_section(),
        _generators_iterators(),
        _regular_expressions(),
        _collections_module(),
        _common_algorithms(),
    ]


def _oop_section() -> TopicSection:
    """Mid-Level: OOP with nip test-automation-script pattern."""
    explanation = (
        "### Object-Oriented Programming\n\n"
        "OOP is the backbone of test frameworks and automation scripts. "
        "Understanding classes, inheritance, and decorators is essential.\n\n"
        "**Core concepts:**\n"
        "- `__init__` — constructor, initializes instance attributes\n"
        "- **Inheritance** — child class extends parent class\n"
        "- **Polymorphism** — same interface, different behavior\n"
        "- `@property` — getter/setter as attribute access\n"
        "- `@staticmethod` — no access to instance or class\n"
        "- `@classmethod` — receives class as first argument\n\n"
        "**Decorators:**\n"
        "A decorator wraps a function to add behavior:\n"
        "```python\n"
        "def timer(func):\n"
        "    def wrapper(*args, **kwargs):\n"
        "        start = time.time()\n"
        "        result = func(*args, **kwargs)\n"
        "        print(f'{func.__name__} took {time.time() - start:.2f}s')\n"
        "        return result\n"
        "    return wrapper\n"
        "```\n\n"
        "**nip context:** Test automation frameworks use OOP heavily — "
        "base test classes, page objects, fixture managers."
    )

    examples = [
        (
            "# --- Classes, inheritance, and decorators ---\n"
            "import time\n"
            "from functools import wraps\n\n"
            "# Decorator: retry on failure\n"
            "def retry(max_attempts=3):\n"
            "    \"\"\"Decorator that retries a function on exception.\"\"\"\n"
            "    def decorator(func):\n"
            "        @wraps(func)\n"
            "        def wrapper(*args, **kwargs):\n"
            "            for attempt in range(1, max_attempts + 1):\n"
            "                try:\n"
            "                    return func(*args, **kwargs)\n"
            "                except Exception as e:\n"
            "                    if attempt == max_attempts:\n"
            "                        raise\n"
            "                    print(f'Attempt {attempt} failed: {e}. Retrying...')\n"
            "        return wrapper\n"
            "    return decorator\n\n"
            "# Base test class\n"
            "class BaseTest:\n"
            "    \"\"\"Base class for all test cases.\"\"\"\n"
            "    def __init__(self, name: str):\n"
            "        self._name = name\n"
            "        self._status = 'not_run'\n\n"
            "    @property\n"
            "    def name(self) -> str:\n"
            "        return self._name\n\n"
            "    @property\n"
            "    def status(self) -> str:\n"
            "        return self._status\n\n"
            "    def run(self):\n"
            "        \"\"\"Override in subclasses.\"\"\"\n"
            "        raise NotImplementedError\n\n"
            "    @classmethod\n"
            "    def from_config(cls, config: dict):\n"
            "        \"\"\"Create test from a config dict.\"\"\"\n"
            "        return cls(name=config['name'])\n\n"
            "# Child class\n"
            "class GPUTest(BaseTest):\n"
            "    \"\"\"Test that validates GPU functionality.\"\"\"\n"
            "    def __init__(self, name: str, gpu_id: int):\n"
            "        super().__init__(name)\n"
            "        self.gpu_id = gpu_id\n\n"
            "    @retry(max_attempts=2)\n"
            "    def run(self):\n"
            "        print(f'Running {self.name} on GPU {self.gpu_id}')\n"
            "        self._status = 'passed'\n"
            "        return self._status\n\n"
            "# Usage\n"
            "test = GPUTest('test_cuda_init', gpu_id=0)\n"
            "test.run()\n"
            "print(f'{test.name}: {test.status}')  # test_cuda_init: passed"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Test Automation Script Pattern",
            statement=(
                "Implement a `TestSuite` class that manages a collection of "
                "test cases. Each test case is a callable that returns True "
                "(pass) or False (fail). The suite should:\n"
                "1. Accept test cases via `add_test(name, func)`\n"
                "2. Run all tests via `run_all()` and return a results dict\n"
                "3. Provide a `summary()` method returning pass/fail counts"
            ),
            function_signature=(
                "class TestSuite:\n"
                "    def __init__(self):\n"
                "    def add_test(self, name: str, func) -> None:\n"
                "    def run_all(self) -> dict[str, bool]:\n"
                "    def summary(self) -> dict[str, int]:"
            ),
            examples=[
                {
                    "input": "suite.add_test('test_1', lambda: True); suite.add_test('test_2', lambda: False); suite.run_all()",
                    "output": "{'test_1': True, 'test_2': False}",
                },
            ],
            solution_code=(
                "class TestSuite:\n"
                "    \"\"\"Simple test suite that runs callable test cases.\"\"\"\n\n"
                "    def __init__(self):\n"
                "        self._tests = {}  # name -> callable\n"
                "        self._results = {}  # name -> bool\n\n"
                "    def add_test(self, name: str, func) -> None:\n"
                "        \"\"\"Register a test case.\"\"\"\n"
                "        self._tests[name] = func\n\n"
                "    def run_all(self) -> dict[str, bool]:\n"
                "        \"\"\"Run all tests and return results.\"\"\"\n"
                "        self._results = {}\n"
                "        for name, func in self._tests.items():\n"
                "            try:\n"
                "                self._results[name] = bool(func())\n"
                "            except Exception:\n"
                "                self._results[name] = False\n"
                "        return dict(self._results)\n\n"
                "    def summary(self) -> dict[str, int]:\n"
                "        \"\"\"Return pass/fail counts.\"\"\"\n"
                "        passed = sum(1 for v in self._results.values() if v)\n"
                "        failed = sum(1 for v in self._results.values() if not v)\n"
                "        return {'passed': passed, 'failed': failed}"
            ),
            test_code=(
                "suite = TestSuite()\n"
                "suite.add_test('test_pass', lambda: True)\n"
                "suite.add_test('test_fail', lambda: False)\n"
                "suite.add_test('test_error', lambda: 1 / 0)  # exception = fail\n"
                "results = suite.run_all()\n"
                "assert results == {'test_pass': True, 'test_fail': False, 'test_error': False}\n"
                "s = suite.summary()\n"
                "assert s == {'passed': 1, 'failed': 2}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Store tests in a dict mapping name to callable.",
                "Wrap func() in try/except to handle exceptions as failures.",
            ],
        ),
        PracticeProblem(
            title="Shape Hierarchy with Polymorphism",
            statement=(
                "Implement a `Shape` base class with an abstract `area()` method. "
                "Then implement `Circle` and `Rectangle` subclasses. Each should "
                "override `area()` and provide a `__repr__` method. Also add a "
                "`total_area(shapes)` function that returns the sum of all areas."
            ),
            function_signature=(
                "class Shape:\n"
                "    def area(self) -> float:\n\n"
                "class Circle(Shape):\n"
                "    def __init__(self, radius: float):\n\n"
                "class Rectangle(Shape):\n"
                "    def __init__(self, width: float, height: float):\n\n"
                "def total_area(shapes: list[Shape]) -> float:"
            ),
            examples=[
                {"input": "Circle(5).area()", "output": "78.53981633974483"},
                {"input": "Rectangle(3, 4).area()", "output": "12.0"},
                {"input": "total_area([Circle(1), Rectangle(2, 3)])", "output": "9.141592653589793"},
            ],
            solution_code=(
                "import math\n\n"
                "class Shape:\n"
                "    \"\"\"Abstract base shape.\"\"\"\n"
                "    def area(self) -> float:\n"
                "        raise NotImplementedError('Subclasses must implement area()')\n\n"
                "class Circle(Shape):\n"
                "    def __init__(self, radius: float):\n"
                "        self.radius = radius\n\n"
                "    def area(self) -> float:\n"
                "        return math.pi * self.radius ** 2\n\n"
                "    def __repr__(self) -> str:\n"
                "        return f'Circle(radius={self.radius})'\n\n"
                "class Rectangle(Shape):\n"
                "    def __init__(self, width: float, height: float):\n"
                "        self.width = width\n"
                "        self.height = height\n\n"
                "    def area(self) -> float:\n"
                "        return self.width * self.height\n\n"
                "    def __repr__(self) -> str:\n"
                "        return f'Rectangle(width={self.width}, height={self.height})'\n\n"
                "def total_area(shapes: list) -> float:\n"
                "    \"\"\"Sum the areas of all shapes.\"\"\"\n"
                "    return sum(s.area() for s in shapes)"
            ),
            test_code=(
                "import math\n"
                "assert abs(Circle(5).area() - math.pi * 25) < 1e-9\n"
                "assert Rectangle(3, 4).area() == 12.0\n"
                "assert abs(total_area([Circle(1), Rectangle(2, 3)]) - (math.pi + 6)) < 1e-9\n"
                "assert total_area([]) == 0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use math.pi for the circle area formula.",
                "total_area can use sum() with a generator expression.",
            ],
        ),
        PracticeProblem(
            title="Singleton Pattern",
            statement=(
                "Implement a `Config` class using the Singleton pattern — "
                "only one instance should ever exist. The class should store "
                "key-value settings via `set(key, value)` and retrieve them "
                "via `get(key, default=None)`. Calling `Config()` multiple "
                "times should return the same instance."
            ),
            function_signature=(
                "class Config:\n"
                "    def __new__(cls):\n"
                "    def set(self, key: str, value) -> None:\n"
                "    def get(self, key: str, default=None):"
            ),
            examples=[
                {
                    "input": "c1 = Config(); c2 = Config(); c1 is c2",
                    "output": "True",
                },
            ],
            solution_code=(
                "class Config:\n"
                "    \"\"\"Singleton configuration store.\"\"\"\n"
                "    _instance = None\n\n"
                "    def __new__(cls):\n"
                "        if cls._instance is None:\n"
                "            cls._instance = super().__new__(cls)\n"
                "            cls._instance._data = {}\n"
                "        return cls._instance\n\n"
                "    def set(self, key: str, value) -> None:\n"
                "        self._data[key] = value\n\n"
                "    def get(self, key: str, default=None):\n"
                "        return self._data.get(key, default)"
            ),
            test_code=(
                "# Reset singleton for testing\n"
                "Config._instance = None\n"
                "c1 = Config()\n"
                "c2 = Config()\n"
                "assert c1 is c2, 'Should be the same instance'\n"
                "c1.set('host', 'localhost')\n"
                "assert c2.get('host') == 'localhost'  # shared state\n"
                "assert c1.get('missing', 'default') == 'default'\n"
                "Config._instance = None  # cleanup\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Override __new__ to control instance creation.",
                "Store the single instance in a class variable _instance.",
            ],
        ),
        PracticeProblem(
            title="Mixin for Logging",
            statement=(
                "Implement a `LogMixin` class that adds logging capability "
                "to any class via multiple inheritance. It should provide a "
                "`log(message)` method that stores messages in a list and a "
                "`get_logs()` method that returns all logged messages. "
                "Demonstrate with a `Service` class that uses the mixin."
            ),
            function_signature=(
                "class LogMixin:\n"
                "    def log(self, message: str) -> None:\n"
                "    def get_logs(self) -> list[str]:\n\n"
                "class Service(LogMixin):\n"
                "    def __init__(self, name: str):\n"
                "    def start(self) -> None:"
            ),
            examples=[
                {
                    "input": "svc = Service('api'); svc.start(); svc.get_logs()",
                    "output": "['Service api starting...']",
                },
            ],
            solution_code=(
                "class LogMixin:\n"
                "    \"\"\"Mixin that adds logging capability.\"\"\"\n"
                "    def __init__(self):\n"
                "        self._logs = []\n\n"
                "    def log(self, message: str) -> None:\n"
                "        self._logs.append(message)\n\n"
                "    def get_logs(self) -> list:\n"
                "        return list(self._logs)\n\n"
                "class Service(LogMixin):\n"
                "    def __init__(self, name: str):\n"
                "        super().__init__()\n"
                "        self.name = name\n\n"
                "    def start(self) -> None:\n"
                "        self.log(f'Service {self.name} starting...')"
            ),
            test_code=(
                "svc = Service('api')\n"
                "svc.start()\n"
                "assert svc.get_logs() == ['Service api starting...']\n"
                "svc.log('Custom message')\n"
                "assert len(svc.get_logs()) == 2\n"
                "# Each instance has its own logs\n"
                "svc2 = Service('db')\n"
                "svc2.start()\n"
                "assert len(svc2.get_logs()) == 1\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Initialize _logs in LogMixin.__init__ and call super().__init__() in Service.",
                "Return a copy of _logs in get_logs() to prevent external mutation.",
            ],
        ),
    ]

    return TopicSection(
        title="Object-Oriented Programming",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Use @property for controlled attribute access (getters/setters).",
            "@classmethod receives the class; @staticmethod receives nothing extra.",
            "Decorators wrap functions to add behavior (logging, retry, timing).",
            "Inheritance + polymorphism enable extensible test frameworks.",
            "Always call super().__init__() in child class constructors.",
        ],
    )


def _generators_iterators() -> TopicSection:
    """Mid-Level: Generators and iterators."""
    explanation = (
        "### Generators and Iterators\n\n"
        "Generators produce values lazily — one at a time — instead of "
        "building an entire list in memory. This is critical for processing "
        "large datasets or infinite sequences.\n\n"
        "**Iterator protocol:**\n"
        "- `__iter__()` — return the iterator object\n"
        "- `__next__()` — return the next value or raise `StopIteration`\n\n"
        "**Generator functions** use `yield` instead of `return`:\n"
        "```python\n"
        "def count_up(n):\n"
        "    i = 0\n"
        "    while i < n:\n"
        "        yield i\n"
        "        i += 1\n"
        "```\n\n"
        "**Generator expressions** — like list comprehensions but lazy:\n"
        "```python\n"
        "squares = (x**2 for x in range(1000000))  # no memory spike\n"
        "```\n\n"
        "**itertools basics:**\n"
        "- `chain(*iterables)` — concatenate iterables\n"
        "- `islice(iterable, stop)` — slice an iterator\n"
        "- `groupby(iterable, key)` — group consecutive elements"
    )

    examples = [
        (
            "# --- Generator function ---\n"
            "def fibonacci(limit):\n"
            "    \"\"\"Generate Fibonacci numbers up to limit.\"\"\"\n"
            "    a, b = 0, 1\n"
            "    while a < limit:\n"
            "        yield a       # pause here, return value\n"
            "        a, b = b, a + b  # resume on next call\n\n"
            "# Usage — lazy evaluation\n"
            "for num in fibonacci(50):\n"
            "    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34\n"
            "print()\n\n"
            "# Convert to list if needed\n"
            "fib_list = list(fibonacci(100))\n"
            "print(fib_list)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]"
        ),
        (
            "# --- Generator expressions and itertools ---\n"
            "import itertools\n\n"
            "# Generator expression — memory efficient\n"
            "total = sum(x ** 2 for x in range(1000))  # no intermediate list\n"
            "print(f'Sum of squares: {total}')\n\n"
            "# itertools.chain — combine multiple iterables\n"
            "beginner = ['arrays', 'strings']\n"
            "advanced = ['trees', 'graphs']\n"
            "all_topics = list(itertools.chain(beginner, advanced))\n"
            "print(all_topics)  # ['arrays', 'strings', 'trees', 'graphs']\n\n"
            "# itertools.islice — slice an iterator\n"
            "first_5_fibs = list(itertools.islice(fibonacci(1000), 5))\n"
            "print(first_5_fibs)  # [0, 1, 1, 2, 3]\n\n"
            "# itertools.groupby — group consecutive elements\n"
            "data = [('pass', 'a'), ('pass', 'b'), ('fail', 'c'), ('fail', 'd')]\n"
            "for status, group in itertools.groupby(data, key=lambda x: x[0]):\n"
            "    items = [item[1] for item in group]\n"
            "    print(f'{status}: {items}')  # pass: ['a', 'b'], fail: ['c', 'd']"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Chunked Iterator",
            statement=(
                "Write a generator function that yields successive chunks "
                "of a given size from a list. The last chunk may be smaller "
                "than the chunk size."
            ),
            function_signature="def chunked(lst: list, size: int):",
            examples=[
                {
                    "input": "[1, 2, 3, 4, 5], 2",
                    "output": "[[1, 2], [3, 4], [5]]",
                },
                {
                    "input": "[1, 2, 3, 4], 4",
                    "output": "[[1, 2, 3, 4]]",
                },
            ],
            solution_code=(
                "def chunked(lst: list, size: int):\n"
                "    \"\"\"Yield successive chunks of `size` from `lst`.\"\"\"\n"
                "    for i in range(0, len(lst), size):\n"
                "        yield lst[i:i + size]"
            ),
            test_code=(
                "assert list(chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]\n"
                "assert list(chunked([1, 2, 3, 4], 4)) == [[1, 2, 3, 4]]\n"
                "assert list(chunked([], 3)) == []\n"
                "assert list(chunked([1], 5)) == [[1]]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use range(0, len(lst), size) to get chunk start indices.",
                "Slice lst[i:i+size] — Python handles the last short chunk automatically.",
            ],
        ),
        PracticeProblem(
            title="Infinite Counter Generator",
            statement=(
                "Write a generator function `counter(start=0, step=1)` that "
                "yields an infinite sequence of numbers starting at `start` "
                "and incrementing by `step`. Then write a function "
                "`take(gen, n)` that returns the first n values from any generator."
            ),
            function_signature=(
                "def counter(start: int = 0, step: int = 1):\n\n"
                "def take(gen, n: int) -> list:"
            ),
            examples=[
                {"input": "take(counter(0, 2), 5)", "output": "[0, 2, 4, 6, 8]"},
                {"input": "take(counter(10, -3), 4)", "output": "[10, 7, 4, 1]"},
            ],
            solution_code=(
                "def counter(start: int = 0, step: int = 1):\n"
                "    \"\"\"Infinite counter generator.\"\"\"\n"
                "    current = start\n"
                "    while True:\n"
                "        yield current\n"
                "        current += step\n\n"
                "def take(gen, n: int) -> list:\n"
                "    \"\"\"Take the first n values from a generator.\"\"\"\n"
                "    return [next(gen) for _ in range(n)]"
            ),
            test_code=(
                "assert take(counter(0, 2), 5) == [0, 2, 4, 6, 8]\n"
                "assert take(counter(10, -3), 4) == [10, 7, 4, 1]\n"
                "assert take(counter(), 3) == [0, 1, 2]\n"
                "assert take(counter(5), 0) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use `while True: yield current` for an infinite generator.",
                "take() can use a list comprehension with next(gen).",
            ],
        ),
        PracticeProblem(
            title="Pipeline with Generator Chaining",
            statement=(
                "Implement a data processing pipeline using generators. "
                "Write three generator functions:\n"
                "1. `read_lines(text)` — yields each non-empty line\n"
                "2. `parse_csv_line(lines)` — yields each line split by comma\n"
                "3. `filter_errors(rows)` — yields rows where the last field is 'ERROR'\n"
                "Chain them to process a multi-line CSV string."
            ),
            function_signature=(
                "def read_lines(text: str):\n"
                "def parse_csv_line(lines):\n"
                "def filter_errors(rows):"
            ),
            examples=[
                {
                    "input": "'ts1,login,INFO\\nts2,upload,ERROR\\nts3,logout,INFO\\nts4,crash,ERROR'",
                    "output": "[['ts2', 'upload', 'ERROR'], ['ts4', 'crash', 'ERROR']]",
                },
            ],
            solution_code=(
                "def read_lines(text: str):\n"
                "    \"\"\"Yield each non-empty line from text.\"\"\"\n"
                "    for line in text.split('\\n'):\n"
                "        if line.strip():\n"
                "            yield line.strip()\n\n"
                "def parse_csv_line(lines):\n"
                "    \"\"\"Yield each line split by comma.\"\"\"\n"
                "    for line in lines:\n"
                "        yield line.split(',')\n\n"
                "def filter_errors(rows):\n"
                "    \"\"\"Yield rows where the last field is 'ERROR'.\"\"\"\n"
                "    for row in rows:\n"
                "        if row and row[-1] == 'ERROR':\n"
                "            yield row"
            ),
            test_code=(
                "data = 'ts1,login,INFO\\nts2,upload,ERROR\\nts3,logout,INFO\\nts4,crash,ERROR'\n"
                "pipeline = filter_errors(parse_csv_line(read_lines(data)))\n"
                "result = list(pipeline)\n"
                "assert result == [['ts2', 'upload', 'ERROR'], ['ts4', 'crash', 'ERROR']]\n"
                "assert list(filter_errors(parse_csv_line(read_lines('')))) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Each generator takes another generator as input — chain them together.",
                "The pipeline is lazy: no data is processed until you iterate.",
            ],
        ),
        PracticeProblem(
            title="Running Average Generator",
            statement=(
                "Write a generator function `running_average(numbers)` that "
                "takes an iterable of numbers and yields the running average "
                "after each new number is consumed."
            ),
            function_signature="def running_average(numbers):",
            examples=[
                {"input": "[1, 2, 3, 4, 5]", "output": "[1.0, 1.5, 2.0, 2.5, 3.0]"},
                {"input": "[10, 20]", "output": "[10.0, 15.0]"},
            ],
            solution_code=(
                "def running_average(numbers):\n"
                "    \"\"\"Yield the running average after each new number.\"\"\"\n"
                "    total = 0\n"
                "    count = 0\n"
                "    for num in numbers:\n"
                "        total += num\n"
                "        count += 1\n"
                "        yield total / count"
            ),
            test_code=(
                "assert list(running_average([1, 2, 3, 4, 5])) == [1.0, 1.5, 2.0, 2.5, 3.0]\n"
                "assert list(running_average([10, 20])) == [10.0, 15.0]\n"
                "assert list(running_average([])) == []\n"
                "assert list(running_average([5])) == [5.0]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Keep a running total and count, yield total/count after each update.",
                "The generator naturally handles empty input — the for loop just doesn't execute.",
            ],
        ),
    ]

    return TopicSection(
        title="Generators and Iterators",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Generators use yield and produce values lazily — great for large data.",
            "Generator expressions (x for x in ...) use less memory than list comprehensions.",
            "itertools provides powerful tools: chain, islice, groupby, product, permutations.",
            "A generator can only be iterated once — convert to list if you need multiple passes.",
            "Use generators when you don't need all values at once.",
        ],
    )


def _regular_expressions() -> TopicSection:
    """Mid-Level: Regular expressions with nip log-parser example."""
    explanation = (
        "### Regular Expressions\n\n"
        "The `re` module provides pattern matching for strings — essential "
        "for parsing logs, validating input, and extracting data.\n\n"
        "**Common functions:**\n"
        "- `re.search(pattern, string)` — find first match anywhere\n"
        "- `re.match(pattern, string)` — match at start of string\n"
        "- `re.findall(pattern, string)` — list of all matches\n"
        "- `re.sub(pattern, repl, string)` — replace matches\n"
        "- `re.compile(pattern)` — pre-compile for reuse\n\n"
        "**Common patterns:**\n"
        "- `\\d` — digit, `\\w` — word char, `\\s` — whitespace\n"
        "- `.` — any char, `*` — 0+, `+` — 1+, `?` — 0 or 1\n"
        "- `^` — start, `$` — end\n"
        "- `(...)` — capture group, `(?:...)` — non-capturing group\n"
        "- `{n,m}` — between n and m repetitions\n\n"
        "**nip context:** Regex is used heavily for parsing test logs, "
        "extracting GPU metrics, and validating command output."
    )

    examples = [
        (
            "# --- Basic regex operations ---\n"
            "import re\n\n"
            "# search — find first match\n"
            "text = 'GPU 0: Tesla V100, Temp: 72C, Util: 95%'\n"
            "match = re.search(r'Temp: (\\d+)C', text)\n"
            "if match:\n"
            "    print(f'Temperature: {match.group(1)}')  # 72\n\n"
            "# findall — all matches\n"
            "log = 'Error at 10:23:45, Warning at 10:24:01, Error at 10:25:30'\n"
            "times = re.findall(r'\\d{2}:\\d{2}:\\d{2}', log)\n"
            "print(times)  # ['10:23:45', '10:24:01', '10:25:30']\n\n"
            "# sub — replace\n"
            "cleaned = re.sub(r'\\s+', ' ', '  too   many   spaces  ')\n"
            "print(cleaned.strip())  # 'too many spaces'\n\n"
            "# compile — reuse pattern\n"
            "ip_pattern = re.compile(r'\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\b')\n"
            "ips = ip_pattern.findall('Server 192.168.1.1 connected to 10.0.0.5')\n"
            "print(ips)  # ['192.168.1.1', '10.0.0.5']"
        ),
        (
            "# --- Groups and named groups ---\n"
            "import re\n\n"
            "# Parse a log line with named groups\n"
            "log_line = '2024-01-15 10:23:45 ERROR [gpu_driver] CUDA init failed'\n"
            "pattern = r'(?P<date>\\d{4}-\\d{2}-\\d{2}) (?P<time>\\d{2}:\\d{2}:\\d{2}) (?P<level>\\w+) \\[(?P<module>\\w+)\\] (?P<message>.+)'\n"
            "m = re.match(pattern, log_line)\n"
            "if m:\n"
            "    print(f\"Date: {m.group('date')}\")     # 2024-01-15\n"
            "    print(f\"Level: {m.group('level')}\")    # ERROR\n"
            "    print(f\"Module: {m.group('module')}\")  # gpu_driver\n"
            "    print(f\"Message: {m.group('message')}\")  # CUDA init failed\n\n"
            "# Validate email format\n"
            "email_re = re.compile(r'^[\\w.+-]+@[\\w-]+\\.[\\w.]+$')\n"
            "print(bool(email_re.match('user@nip.com')))  # True\n"
            "print(bool(email_re.match('invalid@')))          # False"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Log Timestamp Extractor",
            statement=(
                "Write a function that extracts all timestamps from a log "
                "string. Timestamps have the format `YYYY-MM-DD HH:MM:SS`. "
                "Return a list of timestamp strings."
            ),
            function_signature="def extract_timestamps(log: str) -> list[str]:",
            examples=[
                {
                    "input": "'Started at 2024-01-15 10:23:45. Ended at 2024-01-15 10:25:30.'",
                    "output": "['2024-01-15 10:23:45', '2024-01-15 10:25:30']",
                },
            ],
            solution_code=(
                "import re\n\n"
                "def extract_timestamps(log: str) -> list[str]:\n"
                "    \"\"\"Extract all YYYY-MM-DD HH:MM:SS timestamps from log text.\"\"\"\n"
                "    pattern = r'\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}'\n"
                "    return re.findall(pattern, log)"
            ),
            test_code=(
                "import re\n"
                "assert extract_timestamps('Started at 2024-01-15 10:23:45. Ended at 2024-01-15 10:25:30.') == [\n"
                "    '2024-01-15 10:23:45', '2024-01-15 10:25:30'\n"
                "]\n"
                "assert extract_timestamps('No timestamps here') == []\n"
                "assert extract_timestamps('One: 2023-12-31 23:59:59') == ['2023-12-31 23:59:59']\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use re.findall() with a pattern matching the timestamp format.",
                "\\d{4} matches exactly 4 digits.",
            ],
        ),
    ]

    return TopicSection(
        title="Regular Expressions",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Use raw strings (r'...') for regex patterns to avoid backslash issues.",
            "re.compile() is faster when reusing the same pattern many times.",
            "Named groups (?P<name>...) make complex patterns more readable.",
            "findall() returns strings; search()/match() return Match objects.",
            "Always test regex patterns with edge cases — they can be tricky.",
        ],
    )


def _collections_module() -> TopicSection:
    """Mid-Level: Collections module — Counter, defaultdict, deque, namedtuple."""
    explanation = (
        "### Collections Module\n\n"
        "The `collections` module provides specialized container types that "
        "extend Python's built-in dict, list, and tuple.\n\n"
        "**Counter** — count hashable objects:\n"
        "```python\n"
        "from collections import Counter\n"
        "c = Counter('abracadabra')  # Counter({'a': 5, 'b': 2, ...})\n"
        "c.most_common(2)            # [('a', 5), ('b', 2)]\n"
        "```\n\n"
        "**defaultdict** — dict with default factory for missing keys.\n\n"
        "**deque** — double-ended queue with O(1) append/pop on both ends.\n\n"
        "**namedtuple** — lightweight immutable class:\n"
        "```python\n"
        "from collections import namedtuple\n"
        "Point = namedtuple('Point', ['x', 'y'])\n"
        "p = Point(3, 4)\n"
        "print(p.x, p.y)  # 3 4\n"
        "```\n\n"
        "**OrderedDict** — dict that remembers insertion order (mostly "
        "redundant since Python 3.7+ dicts are ordered, but useful for "
        "`move_to_end()` and equality comparisons that consider order)."
    )

    examples = [
        (
            "# --- Counter ---\n"
            "from collections import Counter\n\n"
            "# Count word frequencies\n"
            "words = 'the cat sat on the mat the cat'.split()\n"
            "word_counts = Counter(words)\n"
            "print(word_counts)              # Counter({'the': 3, 'cat': 2, ...})\n"
            "print(word_counts.most_common(2))  # [('the', 3), ('cat', 2)]\n\n"
            "# Counter arithmetic\n"
            "a = Counter('aabbc')\n"
            "b = Counter('abcdd')\n"
            "print(a + b)  # Counter({'a': 3, 'b': 3, 'c': 2, 'd': 2})\n"
            "print(a - b)  # Counter({'a': 1, 'b': 1})  (only positive counts)\n\n"
            "# Check if one is subset of another\n"
            "print(not (Counter('abc') - Counter('aabbcc')))  # True (abc is subset)"
        ),
        (
            "# --- deque and namedtuple ---\n"
            "from collections import deque, namedtuple\n\n"
            "# deque — O(1) operations on both ends\n"
            "dq = deque([1, 2, 3])\n"
            "dq.appendleft(0)    # [0, 1, 2, 3]\n"
            "dq.append(4)        # [0, 1, 2, 3, 4]\n"
            "dq.popleft()        # 0 — O(1)\n"
            "print(dq)           # deque([1, 2, 3, 4])\n\n"
            "# deque as fixed-size sliding window\n"
            "window = deque(maxlen=3)\n"
            "for i in range(5):\n"
            "    window.append(i)\n"
            "    print(list(window))  # [0], [0,1], [0,1,2], [1,2,3], [2,3,4]\n\n"
            "# namedtuple — readable, immutable records\n"
            "TestResult = namedtuple('TestResult', ['name', 'status', 'duration'])\n"
            "r = TestResult('test_login', 'pass', 1.23)\n"
            "print(f'{r.name}: {r.status} ({r.duration}s)')  # test_login: pass (1.23s)"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Top K Frequent Elements",
            statement=(
                "Given a list of integers and an integer k, return the k "
                "most frequent elements. If there are ties, any order is "
                "acceptable."
            ),
            function_signature="def top_k_frequent(nums: list[int], k: int) -> list[int]:",
            examples=[
                {
                    "input": "[1, 1, 1, 2, 2, 3], 2",
                    "output": "[1, 2]",
                },
                {
                    "input": "[1], 1",
                    "output": "[1]",
                },
            ],
            solution_code=(
                "from collections import Counter\n\n"
                "def top_k_frequent(nums: list[int], k: int) -> list[int]:\n"
                "    \"\"\"Return the k most frequent elements.\"\"\"\n"
                "    counts = Counter(nums)\n"
                "    return [item for item, _ in counts.most_common(k)]"
            ),
            test_code=(
                "from collections import Counter\n"
                "result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)\n"
                "assert set(result) == {1, 2}\n"
                "assert len(result) == 2\n"
                "assert top_k_frequent([1], 1) == [1]\n"
                "assert set(top_k_frequent([4, 4, 5, 5, 6], 2)) == {4, 5}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Counter.most_common(k) returns the k most common elements.",
                "Extract just the elements (not counts) from the result.",
            ],
        ),
    ]

    return TopicSection(
        title="Collections Module",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Counter is the fastest way to count frequencies — use most_common(k) for top-k.",
            "defaultdict(list) and defaultdict(int) eliminate key-existence checks.",
            "deque provides O(1) append/pop on both ends — use for queues and sliding windows.",
            "namedtuple creates lightweight, immutable record types with named fields.",
            "OrderedDict.move_to_end() is useful for LRU cache implementations.",
        ],
    )


def _common_algorithms() -> TopicSection:
    """Mid-Level: Common algorithm implementations — two pointers, sliding window, memoization."""
    explanation = (
        "### Common Algorithm Implementations\n\n"
        "These patterns appear frequently in coding interviews. Recognizing "
        "the pattern is half the battle.\n\n"
        "**Two Pointers:**\n"
        "Use two indices moving toward each other (or in the same direction) "
        "to solve problems in O(n) instead of O(n²).\n"
        "- Classic: pair sum in sorted array, palindrome check, container with most water.\n\n"
        "**Sliding Window:**\n"
        "Maintain a window [left, right] over a sequence. Expand right to "
        "include elements, shrink left to maintain constraints.\n"
        "- Classic: max sum subarray of size k, longest substring without repeats.\n\n"
        "**Recursion with Memoization:**\n"
        "Cache results of expensive recursive calls to avoid recomputation. "
        "Turns exponential time into polynomial.\n"
        "- Classic: Fibonacci, coin change, climbing stairs.\n"
        "- Use `@functools.lru_cache` for automatic memoization."
    )

    examples = [
        (
            "# --- Two Pointers: pair sum in sorted array ---\n"
            "def two_sum_sorted(nums: list[int], target: int) -> list[int]:\n"
            "    \"\"\"Find two numbers in sorted array that sum to target. O(n).\"\"\"\n"
            "    left, right = 0, len(nums) - 1\n"
            "    while left < right:\n"
            "        current_sum = nums[left] + nums[right]\n"
            "        if current_sum == target:\n"
            "            return [nums[left], nums[right]]\n"
            "        elif current_sum < target:\n"
            "            left += 1   # need larger sum\n"
            "        else:\n"
            "            right -= 1  # need smaller sum\n"
            "    return []\n\n"
            "print(two_sum_sorted([1, 3, 5, 7, 9], 8))   # [1, 7] or [3, 5]\n"
            "print(two_sum_sorted([2, 4, 6, 8], 10))      # [2, 8] or [4, 6]"
        ),
        (
            "# --- Sliding Window: max sum subarray of size k ---\n"
            "def max_sum_subarray(nums: list[int], k: int) -> int:\n"
            "    \"\"\"Find maximum sum of any contiguous subarray of size k. O(n).\"\"\"\n"
            "    if len(nums) < k:\n"
            "        return 0\n"
            "    # Compute sum of first window\n"
            "    window_sum = sum(nums[:k])\n"
            "    max_sum = window_sum\n"
            "    # Slide the window: add right element, remove left element\n"
            "    for i in range(k, len(nums)):\n"
            "        window_sum += nums[i] - nums[i - k]\n"
            "        max_sum = max(max_sum, window_sum)\n"
            "    return max_sum\n\n"
            "print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9 (5+1+3)"
        ),
        (
            "# --- Recursion with Memoization ---\n"
            "from functools import lru_cache\n\n"
            "# Without memoization: O(2^n) — very slow\n"
            "# With memoization: O(n) — each subproblem solved once\n"
            "@lru_cache(maxsize=None)\n"
            "def climb_stairs(n: int) -> int:\n"
            "    \"\"\"Number of ways to climb n stairs (1 or 2 steps at a time).\"\"\"\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    return climb_stairs(n - 1) + climb_stairs(n - 2)\n\n"
            "print(climb_stairs(5))   # 8\n"
            "print(climb_stairs(10))  # 89\n"
            "print(climb_stairs(30))  # 1346269  (instant with memoization)"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Longest Substring Without Repeating Characters",
            statement=(
                "Given a string, find the length of the longest substring "
                "without repeating characters. Use the sliding window technique."
            ),
            function_signature="def length_of_longest_substring(s: str) -> int:",
            examples=[
                {"input": "'abcabcbb'", "output": "3"},
                {"input": "'bbbbb'", "output": "1"},
                {"input": "'pwwkew'", "output": "3"},
                {"input": "''", "output": "0"},
            ],
            solution_code=(
                "def length_of_longest_substring(s: str) -> int:\n"
                "    \"\"\"Sliding window approach — O(n) time, O(min(n, alphabet)) space.\"\"\"\n"
                "    char_index = {}  # char -> last seen index\n"
                "    max_len = 0\n"
                "    left = 0\n"
                "    for right, char in enumerate(s):\n"
                "        if char in char_index and char_index[char] >= left:\n"
                "            left = char_index[char] + 1  # shrink window past duplicate\n"
                "        char_index[char] = right\n"
                "        max_len = max(max_len, right - left + 1)\n"
                "    return max_len"
            ),
            test_code=(
                "assert length_of_longest_substring('abcabcbb') == 3\n"
                "assert length_of_longest_substring('bbbbb') == 1\n"
                "assert length_of_longest_substring('pwwkew') == 3\n"
                "assert length_of_longest_substring('') == 0\n"
                "assert length_of_longest_substring('abcdef') == 6\n"
                "assert length_of_longest_substring('a') == 1\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a dict to track the last index of each character.",
                "Move left pointer past the duplicate when one is found.",
            ],
        ),
        PracticeProblem(
            title="Container With Most Water (Two Pointers)",
            statement=(
                "Given a list of non-negative integers representing heights of "
                "vertical lines, find two lines that together with the x-axis "
                "form a container that holds the most water. Return the maximum "
                "amount of water. Use the two-pointer technique."
            ),
            function_signature="def max_water(heights: list[int]) -> int:",
            examples=[
                {"input": "[1, 8, 6, 2, 5, 4, 8, 3, 7]", "output": "49"},
                {"input": "[1, 1]", "output": "1"},
            ],
            solution_code=(
                "def max_water(heights: list[int]) -> int:\n"
                "    \"\"\"Two-pointer approach — O(n) time.\"\"\"\n"
                "    left, right = 0, len(heights) - 1\n"
                "    max_vol = 0\n"
                "    while left < right:\n"
                "        width = right - left\n"
                "        height = min(heights[left], heights[right])\n"
                "        max_vol = max(max_vol, width * height)\n"
                "        # Move the shorter side inward\n"
                "        if heights[left] < heights[right]:\n"
                "            left += 1\n"
                "        else:\n"
                "            right -= 1\n"
                "    return max_vol"
            ),
            test_code=(
                "assert max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49\n"
                "assert max_water([1, 1]) == 1\n"
                "assert max_water([4, 3, 2, 1, 4]) == 16\n"
                "assert max_water([1, 2, 1]) == 2\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Start with pointers at both ends. Volume = width * min(height_left, height_right).",
                "Always move the pointer with the shorter height inward.",
            ],
        ),
        PracticeProblem(
            title="Coin Change (Recursion + Memoization)",
            statement=(
                "Given a list of coin denominations and a target amount, "
                "return the minimum number of coins needed to make up the "
                "amount. If it's not possible, return -1. Use recursion with "
                "memoization."
            ),
            function_signature="def coin_change(coins: list[int], amount: int) -> int:",
            examples=[
                {"input": "[1, 5, 11], 15", "output": "3"},
                {"input": "[2], 3", "output": "-1"},
                {"input": "[1, 2, 5], 11", "output": "3"},
            ],
            solution_code=(
                "from functools import lru_cache\n\n"
                "def coin_change(coins: list[int], amount: int) -> int:\n"
                "    \"\"\"Minimum coins to make amount using memoized recursion.\"\"\"\n"
                "    @lru_cache(maxsize=None)\n"
                "    def dp(remaining: int) -> int:\n"
                "        if remaining == 0:\n"
                "            return 0\n"
                "        if remaining < 0:\n"
                "            return float('inf')\n"
                "        return min(dp(remaining - c) + 1 for c in coins)\n\n"
                "    result = dp(amount)\n"
                "    return result if result != float('inf') else -1"
            ),
            test_code=(
                "from functools import lru_cache\n"
                "assert coin_change([1, 5, 11], 15) == 3\n"
                "assert coin_change([2], 3) == -1\n"
                "assert coin_change([1, 2, 5], 11) == 3\n"
                "assert coin_change([1], 0) == 0\n"
                "assert coin_change([1, 2, 5], 0) == 0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Define a recursive helper dp(remaining) that returns min coins for that amount.",
                "Use @lru_cache to memoize — without it, this is exponential time.",
            ],
        ),
        PracticeProblem(
            title="Maximum Subarray Sum (Kadane's Algorithm)",
            statement=(
                "Given an integer array, find the contiguous subarray with "
                "the largest sum and return its sum. The array may contain "
                "negative numbers. (Kadane's algorithm — O(n))"
            ),
            function_signature="def max_subarray(nums: list[int]) -> int:",
            examples=[
                {"input": "[-2, 1, -3, 4, -1, 2, 1, -5, 4]", "output": "6"},
                {"input": "[1]", "output": "1"},
                {"input": "[-1, -2, -3]", "output": "-1"},
            ],
            solution_code=(
                "def max_subarray(nums: list[int]) -> int:\n"
                "    \"\"\"Kadane's algorithm — O(n) time, O(1) space.\"\"\"\n"
                "    max_sum = nums[0]\n"
                "    current_sum = nums[0]\n"
                "    for num in nums[1:]:\n"
                "        # Either extend the current subarray or start fresh\n"
                "        current_sum = max(num, current_sum + num)\n"
                "        max_sum = max(max_sum, current_sum)\n"
                "    return max_sum"
            ),
            test_code=(
                "assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6\n"
                "assert max_subarray([1]) == 1\n"
                "assert max_subarray([-1, -2, -3]) == -1\n"
                "assert max_subarray([5, 4, -1, 7, 8]) == 23\n"
                "assert max_subarray([-2, -1]) == -1\n"
                "print('All tests passed!')"
            ),
            hints=[
                "At each step, decide: extend the current subarray or start a new one from here.",
                "current_sum = max(num, current_sum + num) captures this decision.",
            ],
        ),
    ]

    return TopicSection(
        title="Common Algorithm Implementations",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Two pointers reduce O(n²) brute force to O(n) on sorted data.",
            "Sliding window maintains a running computation as the window moves.",
            "@lru_cache turns recursive solutions from exponential to polynomial time.",
            "Recognize the pattern first, then apply the template.",
            "Always consider edge cases: empty input, single element, all duplicates.",
        ],
    )


# ---------------------------------------------------------------------------
# Mock test — 3 coding problems for 30-minute simulation
# ---------------------------------------------------------------------------

def _mock_test() -> list[PracticeProblem]:
    """Return 3 practice problems for the timed mock test."""
    return [
        PracticeProblem(
            title="Mock Problem 1: Flatten Nested Dictionary",
            statement=(
                "**Time target: ~8 minutes**\n\n"
                "Write a function that flattens a nested dictionary. Keys "
                "should be joined with dots. For example, `{'a': {'b': 1}}` "
                "becomes `{'a.b': 1}`. Only dict values should be recursed "
                "into; all other values are leaf values."
            ),
            function_signature="def flatten_dict(d: dict, parent_key: str = '', sep: str = '.') -> dict:",
            examples=[
                {
                    "input": "{'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}",
                    "output": "{'a': 1, 'b.c': 2, 'b.d.e': 3}",
                },
                {
                    "input": "{'x': {'y': 10}}",
                    "output": "{'x.y': 10}",
                },
            ],
            solution_code=(
                "def flatten_dict(d: dict, parent_key: str = '', sep: str = '.') -> dict:\n"
                "    \"\"\"Flatten a nested dict with dot-separated keys.\"\"\"\n"
                "    items = {}\n"
                "    for key, value in d.items():\n"
                "        new_key = f'{parent_key}{sep}{key}' if parent_key else key\n"
                "        if isinstance(value, dict):\n"
                "            items.update(flatten_dict(value, new_key, sep))\n"
                "        else:\n"
                "            items[new_key] = value\n"
                "    return items"
            ),
            test_code=(
                "assert flatten_dict({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}) == {\n"
                "    'a': 1, 'b.c': 2, 'b.d.e': 3\n"
                "}\n"
                "assert flatten_dict({'x': {'y': 10}}) == {'x.y': 10}\n"
                "assert flatten_dict({}) == {}\n"
                "assert flatten_dict({'a': 1}) == {'a': 1}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use recursion — if a value is a dict, recurse with the updated parent key.",
                "Build the new key by joining parent_key and current key with the separator.",
            ],
        ),
        PracticeProblem(
            title="Mock Problem 2: Matrix Spiral Order",
            statement=(
                "**Time target: ~12 minutes**\n\n"
                "Given an m x n matrix, return all elements in spiral order "
                "(clockwise from the top-left corner). The matrix is "
                "represented as a list of lists."
            ),
            function_signature="def spiral_order(matrix: list[list[int]]) -> list[int]:",
            examples=[
                {
                    "input": "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
                    "output": "[1, 2, 3, 6, 9, 8, 7, 4, 5]",
                },
                {
                    "input": "[[1, 2], [3, 4], [5, 6]]",
                    "output": "[1, 2, 4, 6, 5, 3]",
                },
            ],
            solution_code=(
                "def spiral_order(matrix: list[list[int]]) -> list[int]:\n"
                "    \"\"\"Return elements in spiral (clockwise) order.\"\"\"\n"
                "    if not matrix or not matrix[0]:\n"
                "        return []\n"
                "    result = []\n"
                "    top, bottom = 0, len(matrix) - 1\n"
                "    left, right = 0, len(matrix[0]) - 1\n"
                "    while top <= bottom and left <= right:\n"
                "        # Traverse right\n"
                "        for col in range(left, right + 1):\n"
                "            result.append(matrix[top][col])\n"
                "        top += 1\n"
                "        # Traverse down\n"
                "        for row in range(top, bottom + 1):\n"
                "            result.append(matrix[row][right])\n"
                "        right -= 1\n"
                "        # Traverse left\n"
                "        if top <= bottom:\n"
                "            for col in range(right, left - 1, -1):\n"
                "                result.append(matrix[bottom][col])\n"
                "            bottom -= 1\n"
                "        # Traverse up\n"
                "        if left <= right:\n"
                "            for row in range(bottom, top - 1, -1):\n"
                "                result.append(matrix[row][left])\n"
                "            left += 1\n"
                "    return result"
            ),
            test_code=(
                "assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]\n"
                "assert spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]\n"
                "assert spiral_order([[1]]) == [1]\n"
                "assert spiral_order([]) == []\n"
                "assert spiral_order([[1, 2, 3]]) == [1, 2, 3]\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use four boundaries: top, bottom, left, right.",
                "Traverse right, down, left, up — then shrink boundaries.",
                "Check boundary conditions before traversing left and up.",
            ],
        ),
        PracticeProblem(
            title="Mock Problem 3: LRU Cache",
            statement=(
                "**Time target: ~10 minutes**\n\n"
                "Implement a Least Recently Used (LRU) cache with a fixed "
                "capacity. It should support `get(key)` and `put(key, value)` "
                "in O(1) time. When the cache exceeds capacity, evict the "
                "least recently used item."
            ),
            function_signature=(
                "class LRUCache:\n"
                "    def __init__(self, capacity: int):\n"
                "    def get(self, key: int) -> int:\n"
                "    def put(self, key: int, value: int) -> None:"
            ),
            examples=[
                {
                    "input": "cache = LRUCache(2); cache.put(1, 1); cache.put(2, 2); cache.get(1); cache.put(3, 3); cache.get(2)",
                    "output": "get(1) -> 1, get(2) -> -1 (evicted)",
                },
            ],
            solution_code=(
                "from collections import OrderedDict\n\n"
                "class LRUCache:\n"
                "    \"\"\"LRU Cache using OrderedDict for O(1) operations.\"\"\"\n\n"
                "    def __init__(self, capacity: int):\n"
                "        self.capacity = capacity\n"
                "        self.cache = OrderedDict()\n\n"
                "    def get(self, key: int) -> int:\n"
                "        \"\"\"Return value if key exists, else -1. Marks key as recently used.\"\"\"\n"
                "        if key not in self.cache:\n"
                "            return -1\n"
                "        self.cache.move_to_end(key)  # mark as recently used\n"
                "        return self.cache[key]\n\n"
                "    def put(self, key: int, value: int) -> None:\n"
                "        \"\"\"Insert or update key-value. Evict LRU if over capacity.\"\"\"\n"
                "        if key in self.cache:\n"
                "            self.cache.move_to_end(key)\n"
                "        self.cache[key] = value\n"
                "        if len(self.cache) > self.capacity:\n"
                "            self.cache.popitem(last=False)  # evict oldest"
            ),
            test_code=(
                "from collections import OrderedDict\n"
                "cache = LRUCache(2)\n"
                "cache.put(1, 1)\n"
                "cache.put(2, 2)\n"
                "assert cache.get(1) == 1       # returns 1, marks 1 as recent\n"
                "cache.put(3, 3)                 # evicts key 2 (least recent)\n"
                "assert cache.get(2) == -1       # 2 was evicted\n"
                "cache.put(4, 4)                 # evicts key 1\n"
                "assert cache.get(1) == -1       # 1 was evicted\n"
                "assert cache.get(3) == 3\n"
                "assert cache.get(4) == 4\n"
                "print('All tests passed!')"
            ),
            hints=[
                "OrderedDict.move_to_end(key) marks a key as most recently used.",
                "OrderedDict.popitem(last=False) removes the oldest (least recent) item.",
            ],
        ),
    ]


# ---------------------------------------------------------------------------
# Cheat sheet
# ---------------------------------------------------------------------------

def _cheat_sheet() -> str:
    """Return a markdown cheat sheet for quick reference."""
    return (
        "## Python Coding Cheat Sheet\n\n"
        "### Common Built-in Functions\n"
        "| Function | Description | Example |\n"
        "|----------|-------------|--------|\n"
        "| `len(x)` | Length of sequence | `len([1,2,3])` → 3 |\n"
        "| `sorted(x)` | Return sorted list | `sorted([3,1,2])` → [1,2,3] |\n"
        "| `reversed(x)` | Reverse iterator | `list(reversed([1,2,3]))` → [3,2,1] |\n"
        "| `enumerate(x)` | Index-value pairs | `list(enumerate('ab'))` → [(0,'a'),(1,'b')] |\n"
        "| `zip(a, b)` | Pair elements | `list(zip([1,2],[3,4]))` → [(1,3),(2,4)] |\n"
        "| `map(f, x)` | Apply function | `list(map(str, [1,2]))` → ['1','2'] |\n"
        "| `filter(f, x)` | Keep if True | `list(filter(bool, [0,1,2]))` → [1,2] |\n"
        "| `any(x)` / `all(x)` | Logical OR / AND | `any([0,1])` → True |\n"
        "| `min(x)` / `max(x)` | Extremes | `max([3,1,2])` → 3 |\n"
        "| `sum(x)` | Sum of elements | `sum([1,2,3])` → 6 |\n\n"
        "### String Methods Quick Reference\n"
        "| Method | Description |\n"
        "|--------|-------------|\n"
        "| `s.split(sep)` | Split into list |\n"
        "| `sep.join(lst)` | Join list into string |\n"
        "| `s.strip()` | Remove whitespace |\n"
        "| `s.replace(a, b)` | Replace substring |\n"
        "| `s.find(sub)` | Find index (-1 if missing) |\n"
        "| `s.startswith(p)` | Prefix check |\n"
        "| `s.isdigit()` | All digits? |\n"
        "| `s.isalpha()` | All letters? |\n\n"
        "### Complexity of Common Operations\n"
        "| Operation | list | dict | set | deque |\n"
        "|-----------|------|------|-----|-------|\n"
        "| Access by index | O(1) | — | — | O(n) |\n"
        "| Search | O(n) | O(1) | O(1) | O(n) |\n"
        "| Insert at end | O(1)* | O(1) | O(1) | O(1) |\n"
        "| Insert at start | O(n) | — | — | O(1) |\n"
        "| Delete | O(n) | O(1) | O(1) | O(n) |\n"
        "| Sort | O(n log n) | — | — | — |\n"
        "\\* amortized\n\n"
        "### Common Patterns\n"
        "```python\n"
        "# Frequency counting\n"
        "from collections import Counter\n"
        "freq = Counter(items)\n\n"
        "# Two pointers (sorted array)\n"
        "left, right = 0, len(arr) - 1\n"
        "while left < right: ...\n\n"
        "# Sliding window\n"
        "for right in range(len(arr)):\n"
        "    # expand window\n"
        "    while constraint_violated:\n"
        "        left += 1  # shrink window\n\n"
        "# Memoization\n"
        "from functools import lru_cache\n"
        "@lru_cache(maxsize=None)\n"
        "def solve(state): ...\n\n"
        "# defaultdict for grouping\n"
        "from collections import defaultdict\n"
        "groups = defaultdict(list)\n"
        "for item in items:\n"
        "    groups[key(item)].append(item)\n"
        "```\n\n"
        "### Timing Tips (30-minute section)\n"
        "- **Problem 1 (easy):** 8 min — use built-ins, don't over-think\n"
        "- **Problem 2 (medium):** 12 min — identify the pattern, code it\n"
        "- **Problem 3 (harder):** 10 min — brute force first, optimize if time\n"
        "- If stuck > 5 min on one problem, move on\n"
        "- Save 2 min at the end to review edge cases"
    )
