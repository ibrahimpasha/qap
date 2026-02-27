"""DSA content module — Data Structures & Algorithms interview prep."""

from __future__ import annotations

from generator.models import MCQ, NotebookSpec, TopicSection


def get_dsa_spec() -> NotebookSpec:
    """Return a complete NotebookSpec for the DSA notebook."""
    return NotebookSpec(
        title="Data Structures & Algorithms — Interview Prep",
        filename="01_data_structures_algorithms.ipynb",
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
        "## Strategy Tips for the DSA MCQ Section (15 minutes)\n\n"
        "**Time Allocation:** You have roughly 1.5 minutes per question "
        "(assuming 8-10 questions). Don't spend more than 2 minutes on any "
        "single question.\n\n"
        "**Elimination Technique:** Read all four options first. Cross out "
        "answers that are obviously wrong — even eliminating one option "
        "increases your odds from 25% to 33%.\n\n"
        "**Skip and Return:** If a question looks complex, mark it mentally "
        "and move on. Answer the easy ones first to bank points, then come "
        "back to the harder ones with remaining time.\n\n"
        "**Code Output Questions:** Trace through the code on paper/mentally "
        "step by step. Watch for off-by-one errors and edge cases.\n\n"
        "**Complexity Questions:** Memorize the Big-O table for common data "
        "structures and sorting algorithms. Most complexity questions test "
        "recognition, not derivation.\n\n"
        "**Common Traps:** Watch for subtle differences between similar "
        "options (e.g., O(n) vs O(n log n)). Read the question stem carefully "
        "— it may ask for *worst-case* vs *average-case*."
    )


# ---------------------------------------------------------------------------
# Beginner sections
# ---------------------------------------------------------------------------

def _beginner_sections() -> list[TopicSection]:
    return [
        _arrays_and_strings(),
        _linked_lists(),
        _stacks_and_queues(),
        _hash_tables(),
        _basic_sorting(),
    ]


def _arrays_and_strings() -> TopicSection:
    explanation = (
        "### Arrays and Strings\n\n"
        "Arrays (Python `list`) and strings (`str`) are the most fundamental "
        "data structures. They store elements in contiguous memory, allowing "
        "O(1) random access by index.\n\n"
        "**Key operations:**\n"
        "- Indexing: `arr[i]` — O(1)\n"
        "- Slicing: `arr[i:j]` — O(j - i)\n"
        "- Append: `arr.append(x)` — amortized O(1)\n"
        "- Insert at index: `arr.insert(i, x)` — O(n)\n"
        "- Search (unsorted): `x in arr` — O(n)\n\n"
        "**Common patterns:**\n"
        "- Two-pointer technique\n"
        "- Sliding window\n"
        "- Frequency counting with dictionaries\n"
        "- Reversing in-place"
    )

    examples = [
        (
            "# --- Arrays: basic operations ---\n"
            "arr = [10, 20, 30, 40, 50]\n\n"
            "# Indexing — O(1)\n"
            "print(arr[2])          # 30\n\n"
            "# Slicing — O(k) where k = slice length\n"
            "print(arr[1:4])        # [20, 30, 40]\n\n"
            "# Append — amortized O(1)\n"
            "arr.append(60)\n"
            "print(arr)             # [10, 20, 30, 40, 50, 60]\n\n"
            "# Insert at index — O(n) due to shifting\n"
            "arr.insert(0, 5)\n"
            "print(arr)             # [5, 10, 20, 30, 40, 50, 60]\n\n"
            "# Reverse in-place — O(n)\n"
            "arr.reverse()\n"
            "print(arr)             # [60, 50, 40, 30, 20, 10, 5]"
        ),
        (
            "# --- Strings: common operations ---\n"
            "s = 'hello world'\n\n"
            "# Strings are immutable — slicing creates a new string\n"
            "print(s[0:5])          # 'hello'\n"
            "print(s[::-1])         # 'dlrow olleh'  (reverse)\n\n"
            "# Frequency count using a dict\n"
            "freq = {}\n"
            "for ch in s:\n"
            "    freq[ch] = freq.get(ch, 0) + 1\n"
            "print(freq)            # {'h': 1, 'e': 1, 'l': 3, ...}\n\n"
            "# Two-pointer: check if a string is a palindrome\n"
            "def is_palindrome(text: str) -> bool:\n"
            "    left, right = 0, len(text) - 1\n"
            "    while left < right:\n"
            "        if text[left] != text[right]:\n"
            "            return False\n"
            "        left += 1\n"
            "        right -= 1\n"
            "    return True\n\n"
            "print(is_palindrome('racecar'))  # True\n"
            "print(is_palindrome('hello'))    # False"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the time complexity of inserting an element at the "
                "beginning of a Python list of size n?"
            ),
            options={
                "A": "O(1)",
                "B": "O(log n)",
                "C": "O(n)",
                "D": "O(n²)",
            },
            correct="C",
            explanation=(
                "Inserting at index 0 requires shifting all n existing "
                "elements one position to the right, which takes O(n) time."
            ),
            distractors={
                "A": "O(1) applies to append at the end, not insert at the beginning.",
                "B": "O(log n) is not involved — there is no divide-and-conquer here.",
                "D": "O(n²) would require a nested loop; a single shift pass is O(n).",
            },
            mcq_type="complexity",
        ),
        MCQ(
            question=(
                "What does the following code print?\n\n"
                "```python\n"
                "s = 'abcdef'\n"
                "print(s[1:5:2])\n"
                "```"
            ),
            options={
                "A": "'bd'",
                "B": "'bce'",
                "C": "'bdf'",
                "D": "'ace'",
            },
            correct="A",
            explanation=(
                "s[1:5:2] starts at index 1 ('b'), steps by 2: index 1 → 'b', "
                "index 3 → 'd'. Index 5 is excluded. Result: 'bd'."
            ),
            distractors={
                "B": "'bce' would require step 1 from index 1 to 4, not step 2.",
                "C": "'bdf' would require starting at index 1 with step 2 up to index 6.",
                "D": "'ace' would result from s[0:5:2], starting at index 0.",
            },
            mcq_type="code_output",
        ),
    ]

    return TopicSection(
        title="Arrays and Strings",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Python lists provide O(1) indexing but O(n) insertion at arbitrary positions.",
            "Strings are immutable — every modification creates a new string object.",
            "Two-pointer and sliding-window are the most common array/string interview patterns.",
            "Use `collections.Counter` or a dict for frequency counting.",
        ],
    )


def _linked_lists() -> TopicSection:
    explanation = (
        "### Linked Lists\n\n"
        "A linked list is a linear data structure where each element (node) "
        "contains a value and a reference (pointer) to the next node. Unlike "
        "arrays, linked lists do not store elements contiguously in memory.\n\n"
        "**Key operations:**\n"
        "- Insert at head: O(1)\n"
        "- Insert at tail (with tail pointer): O(1)\n"
        "- Search: O(n)\n"
        "- Delete by value: O(n)\n"
        "- Traverse: O(n)\n\n"
        "**Advantages over arrays:**\n"
        "- O(1) insertion/deletion at the head\n"
        "- Dynamic size — no need to pre-allocate\n\n"
        "**Disadvantages:**\n"
        "- No random access (must traverse from head)\n"
        "- Extra memory for pointers"
    )

    examples = [
        (
            "# --- Singly Linked List implementation ---\n"
            "class Node:\n"
            "    \"\"\"A single node in the linked list.\"\"\"\n"
            "    def __init__(self, data):\n"
            "        self.data = data\n"
            "        self.next = None  # pointer to next node\n\n"
            "class SinglyLinkedList:\n"
            "    \"\"\"Singly linked list with insert, delete, search, traverse.\"\"\"\n"
            "    def __init__(self):\n"
            "        self.head = None\n\n"
            "    def insert_at_head(self, data):\n"
            "        \"\"\"Insert a new node at the beginning — O(1).\"\"\"\n"
            "        new_node = Node(data)\n"
            "        new_node.next = self.head\n"
            "        self.head = new_node\n\n"
            "    def insert_at_tail(self, data):\n"
            "        \"\"\"Insert a new node at the end — O(n).\"\"\"\n"
            "        new_node = Node(data)\n"
            "        if not self.head:\n"
            "            self.head = new_node\n"
            "            return\n"
            "        current = self.head\n"
            "        while current.next:\n"
            "            current = current.next\n"
            "        current.next = new_node\n\n"
            "    def search(self, target):\n"
            "        \"\"\"Search for a value — O(n).\"\"\"\n"
            "        current = self.head\n"
            "        while current:\n"
            "            if current.data == target:\n"
            "                return True\n"
            "            current = current.next\n"
            "        return False\n\n"
            "    def delete(self, target):\n"
            "        \"\"\"Delete first occurrence of target — O(n).\"\"\"\n"
            "        if not self.head:\n"
            "            return\n"
            "        if self.head.data == target:\n"
            "            self.head = self.head.next\n"
            "            return\n"
            "        current = self.head\n"
            "        while current.next:\n"
            "            if current.next.data == target:\n"
            "                current.next = current.next.next\n"
            "                return\n"
            "            current = current.next\n\n"
            "    def traverse(self):\n"
            "        \"\"\"Print all elements — O(n).\"\"\"\n"
            "        elements = []\n"
            "        current = self.head\n"
            "        while current:\n"
            "            elements.append(current.data)\n"
            "            current = current.next\n"
            "        return elements\n\n"
            "# Usage\n"
            "ll = SinglyLinkedList()\n"
            "ll.insert_at_head(3)\n"
            "ll.insert_at_head(2)\n"
            "ll.insert_at_head(1)\n"
            "ll.insert_at_tail(4)\n"
            "print(ll.traverse())    # [1, 2, 3, 4]\n"
            "print(ll.search(3))     # True\n"
            "ll.delete(2)\n"
            "print(ll.traverse())    # [1, 3, 4]"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the time complexity of searching for an element "
                "in a singly linked list of n nodes?"
            ),
            options={
                "A": "O(1)",
                "B": "O(log n)",
                "C": "O(n)",
                "D": "O(n log n)",
            },
            correct="C",
            explanation=(
                "In a singly linked list, you must traverse from the head "
                "node by node. In the worst case, the element is at the end "
                "or not present, requiring O(n) comparisons."
            ),
            distractors={
                "A": "O(1) would require direct index access, which linked lists don't support.",
                "B": "O(log n) would require a sorted structure with binary search capability.",
                "D": "O(n log n) is typical for efficient sorting, not linear search.",
            },
            mcq_type="complexity",
        ),
    ]

    return TopicSection(
        title="Linked Lists",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Linked lists excel at O(1) head insertion but lack random access.",
            "Always handle edge cases: empty list, single node, deleting the head.",
            "The Node class pattern (data + next pointer) is a building block for trees and graphs.",
            "Use a dummy head node to simplify insertion/deletion logic in interviews.",
        ],
    )


def _stacks_and_queues() -> TopicSection:
    explanation = (
        "### Stacks and Queues\n\n"
        "**Stack (LIFO — Last In, First Out):** Think of a stack of plates. "
        "The last plate placed on top is the first one removed.\n\n"
        "**Queue (FIFO — First In, First Out):** Think of a line at a store. "
        "The first person in line is the first one served.\n\n"
        "**Stack operations:**\n"
        "- `push(x)` — add to top: O(1)\n"
        "- `pop()` — remove from top: O(1)\n"
        "- `peek()` — view top element: O(1)\n\n"
        "**Queue operations:**\n"
        "- `enqueue(x)` — add to rear: O(1)\n"
        "- `dequeue()` — remove from front: O(1)\n"
        "- `peek()` — view front element: O(1)\n\n"
        "In Python, use a `list` for stacks and `collections.deque` for queues "
        "(deque provides O(1) popleft, whereas list.pop(0) is O(n))."
    )

    examples = [
        (
            "# --- Stack using a Python list ---\n"
            "stack = []\n\n"
            "# Push — O(1) amortized\n"
            "stack.append(10)\n"
            "stack.append(20)\n"
            "stack.append(30)\n"
            "print(stack)           # [10, 20, 30]\n\n"
            "# Peek — O(1)\n"
            "print(stack[-1])       # 30  (top of stack)\n\n"
            "# Pop — O(1) amortized\n"
            "top = stack.pop()\n"
            "print(top)             # 30\n"
            "print(stack)           # [10, 20]\n\n"
            "# Check if empty\n"
            "print(len(stack) == 0) # False"
        ),
        (
            "# --- Queue using collections.deque ---\n"
            "from collections import deque\n\n"
            "queue = deque()\n\n"
            "# Enqueue — O(1)\n"
            "queue.append(10)\n"
            "queue.append(20)\n"
            "queue.append(30)\n"
            "print(queue)           # deque([10, 20, 30])\n\n"
            "# Peek front — O(1)\n"
            "print(queue[0])        # 10\n\n"
            "# Dequeue — O(1)\n"
            "front = queue.popleft()\n"
            "print(front)           # 10\n"
            "print(queue)           # deque([20, 30])\n\n"
            "# Common use: BFS traversal uses a queue\n"
            "# Common use: DFS / backtracking uses a stack"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "Which data structure would you use to implement an undo "
                "feature in a text editor?"
            ),
            options={
                "A": "Queue",
                "B": "Stack",
                "C": "Hash Table",
                "D": "Linked List",
            },
            correct="B",
            explanation=(
                "An undo feature needs LIFO behavior — the most recent action "
                "should be undone first. A stack naturally supports this with "
                "push (record action) and pop (undo last action)."
            ),
            distractors={
                "A": "A queue is FIFO — it would undo the oldest action first, not the most recent.",
                "C": "A hash table stores key-value pairs but doesn't maintain insertion order for LIFO.",
                "D": "A linked list could work but doesn't inherently enforce LIFO semantics like a stack.",
            },
            mcq_type="conceptual",
        ),
    ]

    return TopicSection(
        title="Stacks and Queues",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Stack = LIFO (use `list.append()` / `list.pop()`).",
            "Queue = FIFO (use `collections.deque` for O(1) operations on both ends).",
            "Never use `list.pop(0)` for a queue — it's O(n). Use `deque.popleft()`.",
            "Stacks are used in DFS, expression evaluation, and undo systems.",
            "Queues are used in BFS, task scheduling, and buffering.",
        ],
    )


def _hash_tables() -> TopicSection:
    explanation = (
        "### Hash Tables\n\n"
        "A hash table (Python `dict`) maps keys to values using a hash "
        "function. The hash function converts a key into an index in an "
        "internal array, enabling average-case O(1) lookups.\n\n"
        "**Key operations (average case):**\n"
        "- Insert: O(1)\n"
        "- Lookup: O(1)\n"
        "- Delete: O(1)\n\n"
        "**Worst case:** O(n) when many keys hash to the same bucket "
        "(hash collision).\n\n"
        "**Collision handling strategies:**\n"
        "- **Chaining:** Each bucket stores a linked list of entries.\n"
        "- **Open addressing:** On collision, probe the next available slot "
        "(linear probing, quadratic probing, double hashing).\n\n"
        "**Python dict internals:**\n"
        "- Uses open addressing with a compact hash table.\n"
        "- Keys must be hashable (immutable types: `int`, `str`, `tuple`).\n"
        "- Maintains insertion order (Python 3.7+)."
    )

    examples = [
        (
            "# --- Hash Table (dict) operations ---\n"
            "# Creating a dict\n"
            "phonebook = {'Alice': '555-0100', 'Bob': '555-0200'}\n\n"
            "# Insert / Update — O(1) average\n"
            "phonebook['Charlie'] = '555-0300'\n"
            "print(phonebook)\n"
            "# {'Alice': '555-0100', 'Bob': '555-0200', 'Charlie': '555-0300'}\n\n"
            "# Lookup — O(1) average\n"
            "print(phonebook['Alice'])   # '555-0100'\n"
            "print(phonebook.get('Dave', 'Not found'))  # 'Not found'\n\n"
            "# Delete — O(1) average\n"
            "del phonebook['Bob']\n"
            "print(phonebook)  # {'Alice': '555-0100', 'Charlie': '555-0300'}\n\n"
            "# Check membership — O(1) average\n"
            "print('Alice' in phonebook)  # True"
        ),
        (
            "# --- Common pattern: frequency counting ---\n"
            "def most_frequent(nums: list[int]) -> int:\n"
            "    \"\"\"Return the most frequent element. O(n) time, O(n) space.\"\"\"\n"
            "    freq = {}  # hash table for counting\n"
            "    for num in nums:\n"
            "        freq[num] = freq.get(num, 0) + 1\n"
            "    # Find key with max value\n"
            "    return max(freq, key=freq.get)\n\n"
            "print(most_frequent([1, 3, 2, 3, 3, 1]))  # 3\n\n"
            "# --- Two-sum using a hash table ---\n"
            "def two_sum(nums: list[int], target: int) -> list[int]:\n"
            "    \"\"\"Return indices of two numbers that add up to target. O(n).\"\"\"\n"
            "    seen = {}  # value -> index\n"
            "    for i, num in enumerate(nums):\n"
            "        complement = target - num\n"
            "        if complement in seen:\n"
            "            return [seen[complement], i]\n"
            "        seen[num] = i\n"
            "    return []\n\n"
            "print(two_sum([2, 7, 11, 15], 9))  # [0, 1]"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the average-case time complexity of looking up a "
                "key in a Python dictionary?"
            ),
            options={
                "A": "O(1)",
                "B": "O(log n)",
                "C": "O(n)",
                "D": "O(n log n)",
            },
            correct="A",
            explanation=(
                "Python dictionaries use a hash table internally. The hash "
                "function maps the key to a bucket in O(1) average time. "
                "Worst case is O(n) due to collisions, but this is rare."
            ),
            distractors={
                "B": "O(log n) applies to balanced BST lookups, not hash tables.",
                "C": "O(n) is the worst case for hash tables with many collisions, not the average.",
                "D": "O(n log n) is typical for sorting algorithms, not dictionary lookups.",
            },
            mcq_type="complexity",
        ),
    ]

    return TopicSection(
        title="Hash Tables",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Python `dict` provides O(1) average-case insert, lookup, and delete.",
            "Keys must be hashable (immutable). Lists cannot be dict keys; tuples can.",
            "Hash tables are the go-to for frequency counting and two-sum style problems.",
            "Collision handling: chaining (linked lists) or open addressing (probing).",
            "Use `collections.defaultdict` or `dict.setdefault()` to simplify counting patterns.",
        ],
    )


def _basic_sorting() -> TopicSection:
    explanation = (
        "### Basic Sorting Algorithms\n\n"
        "Sorting is a fundamental operation. Understanding basic O(n²) sorts "
        "helps build intuition before tackling efficient O(n log n) algorithms.\n\n"
        "| Algorithm | Best | Average | Worst | Space | Stable? |\n"
        "|-----------|------|---------|-------|-------|---------|\n"
        "| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |\n"
        "| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |\n"
        "| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |\n\n"
        "**Bubble Sort:** Repeatedly swap adjacent elements if they're in the "
        "wrong order. Best case O(n) when already sorted (with early-exit "
        "optimization).\n\n"
        "**Selection Sort:** Find the minimum element in the unsorted portion "
        "and swap it to the front. Always O(n²) comparisons.\n\n"
        "**Insertion Sort:** Build the sorted array one element at a time by "
        "inserting each element into its correct position. Efficient for "
        "nearly-sorted data."
    )

    examples = [
        (
            "# --- Bubble Sort ---\n"
            "# Time: O(n²) average/worst, O(n) best (already sorted)\n"
            "# Space: O(1) — in-place\n"
            "def bubble_sort(arr: list) -> list:\n"
            "    \"\"\"Sort array using bubble sort with early-exit optimization.\"\"\"\n"
            "    n = len(arr)\n"
            "    for i in range(n):\n"
            "        swapped = False\n"
            "        for j in range(0, n - i - 1):\n"
            "            if arr[j] > arr[j + 1]:\n"
            "                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap\n"
            "                swapped = True\n"
            "        if not swapped:\n"
            "            break  # already sorted — early exit\n"
            "    return arr\n\n"
            "print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))\n"
            "# [11, 12, 22, 25, 34, 64, 90]"
        ),
        (
            "# --- Selection Sort ---\n"
            "# Time: O(n²) always\n"
            "# Space: O(1) — in-place\n"
            "def selection_sort(arr: list) -> list:\n"
            "    \"\"\"Sort array by repeatedly selecting the minimum.\"\"\"\n"
            "    n = len(arr)\n"
            "    for i in range(n):\n"
            "        min_idx = i\n"
            "        for j in range(i + 1, n):\n"
            "            if arr[j] < arr[min_idx]:\n"
            "                min_idx = j\n"
            "        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # swap minimum to front\n"
            "    return arr\n\n"
            "print(selection_sort([64, 25, 12, 22, 11]))\n"
            "# [11, 12, 22, 25, 64]"
        ),
        (
            "# --- Insertion Sort ---\n"
            "# Time: O(n²) average/worst, O(n) best (nearly sorted)\n"
            "# Space: O(1) — in-place\n"
            "def insertion_sort(arr: list) -> list:\n"
            "    \"\"\"Sort array by inserting each element into its correct position.\"\"\"\n"
            "    for i in range(1, len(arr)):\n"
            "        key = arr[i]  # element to insert\n"
            "        j = i - 1\n"
            "        # Shift elements greater than key to the right\n"
            "        while j >= 0 and arr[j] > key:\n"
            "            arr[j + 1] = arr[j]\n"
            "            j -= 1\n"
            "        arr[j + 1] = key  # place key in correct position\n"
            "    return arr\n\n"
            "print(insertion_sort([12, 11, 13, 5, 6]))\n"
            "# [5, 6, 11, 12, 13]"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "Which of the following sorting algorithms has the best "
                "performance on an already-sorted array?"
            ),
            options={
                "A": "Selection Sort — O(n)",
                "B": "Bubble Sort (with early exit) — O(n)",
                "C": "Selection Sort — O(n²)",
                "D": "Bubble Sort (with early exit) — O(n²)",
            },
            correct="B",
            explanation=(
                "Bubble Sort with the early-exit optimization detects that no "
                "swaps occurred in the first pass and terminates in O(n). "
                "Selection Sort always performs O(n²) comparisons regardless "
                "of input order."
            ),
            distractors={
                "A": "Selection Sort always does O(n²) comparisons — it has no early-exit mechanism.",
                "C": "While O(n²) is correct for Selection Sort, the question asks for the *best* performance.",
                "D": "Bubble Sort with early exit achieves O(n) on sorted input, not O(n²).",
            },
            mcq_type="conceptual",
        ),
    ]

    return TopicSection(
        title="Basic Sorting",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "All three basic sorts are O(n²) average/worst case and O(1) space.",
            "Insertion Sort is the best choice for small or nearly-sorted arrays.",
            "Bubble Sort with early exit achieves O(n) on already-sorted input.",
            "Selection Sort always does O(n²) comparisons — no best-case optimization.",
            "These sorts are rarely used in production but are essential interview knowledge.",
        ],
    )


# ---------------------------------------------------------------------------
# Mid-Level sections
# ---------------------------------------------------------------------------

def _mid_level_sections() -> list[TopicSection]:
    return [
        _binary_trees_bst(),
        _graphs_bfs_dfs(),
        _advanced_sorting(),
        _searching_algorithms(),
        _big_o_analysis(),
    ]


def _binary_trees_bst() -> TopicSection:
    explanation = (
        "### Binary Trees and Binary Search Trees (BSTs)\n\n"
        "A **binary tree** is a tree where each node has at most two children "
        "(left and right). A **Binary Search Tree (BST)** adds an ordering "
        "property: for every node, all values in the left subtree are smaller "
        "and all values in the right subtree are larger.\n\n"
        "**BST operations (average case — balanced tree):**\n"
        "- Search: O(log n)\n"
        "- Insert: O(log n)\n"
        "- Delete: O(log n)\n\n"
        "**Worst case (degenerate/skewed tree):** O(n) for all operations.\n\n"
        "**Tree traversals:**\n"
        "- **In-order (Left, Root, Right):** Produces sorted output for BSTs.\n"
        "- **Pre-order (Root, Left, Right):** Useful for copying/serializing trees.\n"
        "- **Post-order (Left, Right, Root):** Useful for deleting trees."
    )

    examples = [
        (
            "# --- Binary Search Tree implementation ---\n"
            "class TreeNode:\n"
            "    \"\"\"A node in the binary search tree.\"\"\"\n"
            "    def __init__(self, val):\n"
            "        self.val = val\n"
            "        self.left = None\n"
            "        self.right = None\n\n"
            "class BST:\n"
            "    \"\"\"Binary Search Tree with insert, search, and traversals.\"\"\"\n"
            "    def __init__(self):\n"
            "        self.root = None\n\n"
            "    def insert(self, val):\n"
            "        \"\"\"Insert a value into the BST — O(log n) average.\"\"\"\n"
            "        self.root = self._insert(self.root, val)\n\n"
            "    def _insert(self, node, val):\n"
            "        if node is None:\n"
            "            return TreeNode(val)\n"
            "        if val < node.val:\n"
            "            node.left = self._insert(node.left, val)\n"
            "        elif val > node.val:\n"
            "            node.right = self._insert(node.right, val)\n"
            "        return node  # duplicates ignored\n\n"
            "    def search(self, val) -> bool:\n"
            "        \"\"\"Search for a value — O(log n) average.\"\"\"\n"
            "        return self._search(self.root, val)\n\n"
            "    def _search(self, node, val) -> bool:\n"
            "        if node is None:\n"
            "            return False\n"
            "        if val == node.val:\n"
            "            return True\n"
            "        elif val < node.val:\n"
            "            return self._search(node.left, val)\n"
            "        else:\n"
            "            return self._search(node.right, val)\n\n"
            "    def inorder(self) -> list:\n"
            "        \"\"\"In-order traversal — returns sorted values.\"\"\"\n"
            "        result = []\n"
            "        self._inorder(self.root, result)\n"
            "        return result\n\n"
            "    def _inorder(self, node, result):\n"
            "        if node:\n"
            "            self._inorder(node.left, result)\n"
            "            result.append(node.val)\n"
            "            self._inorder(node.right, result)\n\n"
            "    def preorder(self) -> list:\n"
            "        \"\"\"Pre-order traversal (Root, Left, Right).\"\"\"\n"
            "        result = []\n"
            "        self._preorder(self.root, result)\n"
            "        return result\n\n"
            "    def _preorder(self, node, result):\n"
            "        if node:\n"
            "            result.append(node.val)\n"
            "            self._preorder(node.left, result)\n"
            "            self._preorder(node.right, result)\n\n"
            "# Usage\n"
            "bst = BST()\n"
            "for val in [5, 3, 7, 1, 4, 6, 8]:\n"
            "    bst.insert(val)\n\n"
            "print(bst.inorder())    # [1, 3, 4, 5, 6, 7, 8]  (sorted!)\n"
            "print(bst.preorder())   # [5, 3, 1, 4, 7, 6, 8]\n"
            "print(bst.search(4))    # True\n"
            "print(bst.search(9))    # False"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the output of an in-order traversal of a BST "
                "containing the values [5, 3, 7, 1, 4]?"
            ),
            options={
                "A": "[5, 3, 7, 1, 4]",
                "B": "[1, 3, 4, 5, 7]",
                "C": "[5, 3, 1, 4, 7]",
                "D": "[1, 4, 3, 7, 5]",
            },
            correct="B",
            explanation=(
                "In-order traversal of a BST visits nodes in Left-Root-Right "
                "order, which produces values in ascending sorted order. "
                "The sorted sequence is [1, 3, 4, 5, 7]."
            ),
            distractors={
                "A": "[5, 3, 7, 1, 4] is the insertion order, not a traversal order.",
                "C": "[5, 3, 1, 4, 7] is the pre-order traversal (Root, Left, Right).",
                "D": "[1, 4, 3, 7, 5] is the post-order traversal (Left, Right, Root).",
            },
            mcq_type="code_output",
        ),
        MCQ(
            question=(
                "What is the worst-case time complexity of searching in a "
                "Binary Search Tree?"
            ),
            options={
                "A": "O(1)",
                "B": "O(log n)",
                "C": "O(n)",
                "D": "O(n²)",
            },
            correct="C",
            explanation=(
                "In the worst case, a BST can degenerate into a linked list "
                "(e.g., inserting sorted values 1, 2, 3, 4, ...). In this "
                "case, search must traverse all n nodes, giving O(n)."
            ),
            distractors={
                "A": "O(1) is not possible — BST search always traverses at least one path.",
                "B": "O(log n) is the average case for a balanced BST, not the worst case.",
                "D": "O(n²) would require nested traversals; BST search follows a single path.",
            },
            mcq_type="complexity",
        ),
    ]

    return TopicSection(
        title="Binary Trees and BSTs",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "In-order traversal of a BST produces sorted output.",
            "BST operations are O(log n) average but O(n) worst case (skewed tree).",
            "Self-balancing trees (AVL, Red-Black) guarantee O(log n) worst case.",
            "Tree traversals: in-order (sorted), pre-order (copy), post-order (delete).",
        ],
    )
