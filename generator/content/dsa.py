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


def _graphs_bfs_dfs() -> TopicSection:
    explanation = (
        "### Graphs and BFS/DFS\n\n"
        "A **graph** consists of vertices (nodes) and edges connecting them. "
        "Graphs can be directed or undirected, weighted or unweighted.\n\n"
        "**Representation — Adjacency List:**\n"
        "The most common representation uses a dictionary where each key is a "
        "vertex and the value is a list of its neighbors. Space: O(V + E).\n\n"
        "**Breadth-First Search (BFS):**\n"
        "- Explores level by level using a queue.\n"
        "- Time: O(V + E), Space: O(V)\n"
        "- Use cases: shortest path (unweighted), level-order traversal.\n\n"
        "**Depth-First Search (DFS):**\n"
        "- Explores as deep as possible before backtracking, using a stack "
        "(or recursion).\n"
        "- Time: O(V + E), Space: O(V)\n"
        "- Use cases: cycle detection, topological sort, connected components."
    )

    examples = [
        (
            "# --- Graph representation and BFS ---\n"
            "from collections import deque\n\n"
            "# Adjacency list representation\n"
            "graph = {\n"
            "    'A': ['B', 'C'],\n"
            "    'B': ['A', 'D', 'E'],\n"
            "    'C': ['A', 'F'],\n"
            "    'D': ['B'],\n"
            "    'E': ['B', 'F'],\n"
            "    'F': ['C', 'E'],\n"
            "}\n\n"
            "def bfs(graph: dict, start: str) -> list[str]:\n"
            "    \"\"\"Breadth-First Search — O(V + E) time, O(V) space.\"\"\"\n"
            "    visited = set()\n"
            "    queue = deque([start])\n"
            "    visited.add(start)\n"
            "    order = []\n\n"
            "    while queue:\n"
            "        vertex = queue.popleft()  # dequeue front\n"
            "        order.append(vertex)\n"
            "        for neighbor in graph[vertex]:\n"
            "            if neighbor not in visited:\n"
            "                visited.add(neighbor)\n"
            "                queue.append(neighbor)  # enqueue\n"
            "    return order\n\n"
            "print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']"
        ),
        (
            "# --- DFS (iterative with stack) ---\n"
            "def dfs_iterative(graph: dict, start: str) -> list[str]:\n"
            "    \"\"\"Depth-First Search using a stack — O(V + E) time.\"\"\"\n"
            "    visited = set()\n"
            "    stack = [start]\n"
            "    order = []\n\n"
            "    while stack:\n"
            "        vertex = stack.pop()  # pop from top (LIFO)\n"
            "        if vertex not in visited:\n"
            "            visited.add(vertex)\n"
            "            order.append(vertex)\n"
            "            # Add neighbors in reverse for consistent ordering\n"
            "            for neighbor in reversed(graph[vertex]):\n"
            "                if neighbor not in visited:\n"
            "                    stack.append(neighbor)\n"
            "    return order\n\n"
            "# --- DFS (recursive) ---\n"
            "def dfs_recursive(graph: dict, start: str, visited: set = None) -> list[str]:\n"
            "    \"\"\"Depth-First Search using recursion — O(V + E) time.\"\"\"\n"
            "    if visited is None:\n"
            "        visited = set()\n"
            "    visited.add(start)\n"
            "    order = [start]\n"
            "    for neighbor in graph[start]:\n"
            "        if neighbor not in visited:\n"
            "            order.extend(dfs_recursive(graph, neighbor, visited))\n"
            "    return order\n\n"
            "graph = {\n"
            "    'A': ['B', 'C'],\n"
            "    'B': ['A', 'D', 'E'],\n"
            "    'C': ['A', 'F'],\n"
            "    'D': ['B'],\n"
            "    'E': ['B', 'F'],\n"
            "    'F': ['C', 'E'],\n"
            "}\n"
            "print(dfs_iterative(graph, 'A'))  # ['A', 'B', 'D', 'E', 'F', 'C']\n"
            "print(dfs_recursive(graph, 'A'))  # ['A', 'B', 'D', 'E', 'F', 'C']"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "Which data structure does BFS use internally to track "
                "which vertices to visit next?"
            ),
            options={
                "A": "Stack",
                "B": "Queue",
                "C": "Priority Queue (Heap)",
                "D": "Hash Table",
            },
            correct="B",
            explanation=(
                "BFS uses a queue (FIFO) to process vertices level by level. "
                "The first vertex discovered at each level is the first to be "
                "explored, ensuring breadth-first ordering."
            ),
            distractors={
                "A": "A stack gives LIFO behavior, which produces DFS, not BFS.",
                "C": "A priority queue is used in Dijkstra's algorithm, not standard BFS.",
                "D": "A hash table is used for the visited set, not for traversal ordering.",
            },
            mcq_type="conceptual",
        ),
    ]

    return TopicSection(
        title="Graphs and BFS/DFS",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Adjacency list is the standard graph representation: O(V + E) space.",
            "BFS uses a queue → level-by-level exploration → shortest path (unweighted).",
            "DFS uses a stack (or recursion) → deep exploration → cycle detection, topological sort.",
            "Both BFS and DFS run in O(V + E) time.",
            "Always maintain a `visited` set to avoid infinite loops in graphs with cycles.",
        ],
    )


def _advanced_sorting() -> TopicSection:
    explanation = (
        "### Advanced Sorting — Merge Sort and Quick Sort\n\n"
        "These divide-and-conquer algorithms achieve O(n log n) average-case "
        "performance, making them practical for large datasets.\n\n"
        "| Algorithm | Best | Average | Worst | Space | Stable? |\n"
        "|-----------|------|---------|-------|-------|---------|\n"
        "| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |\n"
        "| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |\n\n"
        "**Merge Sort:** Divide the array in half, recursively sort each half, "
        "then merge the two sorted halves. Guaranteed O(n log n) but uses "
        "O(n) extra space.\n\n"
        "**Quick Sort:** Pick a pivot, partition elements into those less than "
        "and greater than the pivot, then recursively sort each partition. "
        "O(n log n) average but O(n²) worst case (poor pivot choice). "
        "In-place with O(log n) stack space.\n\n"
        "**Python's built-in `sorted()` and `list.sort()`** use Timsort, "
        "a hybrid of Merge Sort and Insertion Sort — O(n log n) worst case, "
        "stable, and highly optimized."
    )

    examples = [
        (
            "# --- Merge Sort ---\n"
            "# Time: O(n log n) always\n"
            "# Space: O(n) — needs auxiliary arrays\n"
            "def merge_sort(arr: list) -> list:\n"
            "    \"\"\"Sort array using merge sort (divide and conquer).\"\"\"\n"
            "    if len(arr) <= 1:\n"
            "        return arr\n\n"
            "    mid = len(arr) // 2\n"
            "    left = merge_sort(arr[:mid])    # sort left half\n"
            "    right = merge_sort(arr[mid:])   # sort right half\n"
            "    return merge(left, right)\n\n"
            "def merge(left: list, right: list) -> list:\n"
            "    \"\"\"Merge two sorted arrays into one sorted array.\"\"\"\n"
            "    result = []\n"
            "    i = j = 0\n"
            "    while i < len(left) and j < len(right):\n"
            "        if left[i] <= right[j]:  # <= for stability\n"
            "            result.append(left[i])\n"
            "            i += 1\n"
            "        else:\n"
            "            result.append(right[j])\n"
            "            j += 1\n"
            "    result.extend(left[i:])   # remaining elements\n"
            "    result.extend(right[j:])\n"
            "    return result\n\n"
            "print(merge_sort([38, 27, 43, 3, 9, 82, 10]))\n"
            "# [3, 9, 10, 27, 38, 43, 82]"
        ),
        (
            "# --- Quick Sort ---\n"
            "# Time: O(n log n) average, O(n²) worst case\n"
            "# Space: O(log n) stack space\n"
            "def quick_sort(arr: list) -> list:\n"
            "    \"\"\"Sort array using quick sort with last-element pivot.\"\"\"\n"
            "    if len(arr) <= 1:\n"
            "        return arr\n\n"
            "    pivot = arr[-1]  # choose last element as pivot\n"
            "    left = [x for x in arr[:-1] if x <= pivot]\n"
            "    right = [x for x in arr[:-1] if x > pivot]\n"
            "    return quick_sort(left) + [pivot] + quick_sort(right)\n\n"
            "print(quick_sort([10, 7, 8, 9, 1, 5]))\n"
            "# [1, 5, 7, 8, 9, 10]"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the worst-case time complexity of Quick Sort, and "
                "when does it occur?"
            ),
            options={
                "A": "O(n log n) — when the array is random",
                "B": "O(n²) — when the pivot is always the smallest or largest element",
                "C": "O(n) — when the array is already sorted",
                "D": "O(n²) — when all elements are equal and we use merge sort",
            },
            correct="B",
            explanation=(
                "Quick Sort degrades to O(n²) when the pivot consistently "
                "produces the most unbalanced partition (e.g., always picking "
                "the smallest or largest element). This happens with sorted "
                "input and a naive first/last-element pivot strategy."
            ),
            distractors={
                "A": "O(n log n) is the average case, not the worst case.",
                "C": "O(n) is not achievable by any comparison-based sort in the worst case.",
                "D": "This describes a different algorithm (merge sort), not quick sort.",
            },
            mcq_type="complexity",
        ),
    ]

    return TopicSection(
        title="Advanced Sorting",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Merge Sort: O(n log n) guaranteed, stable, but uses O(n) extra space.",
            "Quick Sort: O(n log n) average, O(n²) worst case, in-place (O(log n) stack).",
            "Python's built-in sort (Timsort) is O(n log n) worst case — use it in production.",
            "Randomized pivot selection avoids Quick Sort's worst case in practice.",
            "Merge Sort is preferred when stability is required; Quick Sort for in-place sorting.",
        ],
    )


def _searching_algorithms() -> TopicSection:
    explanation = (
        "### Searching Algorithms — Binary Search\n\n"
        "**Binary Search** works on sorted arrays by repeatedly dividing the "
        "search space in half. It's one of the most important algorithms to "
        "master for interviews.\n\n"
        "**Time complexity:** O(log n)\n"
        "**Space complexity:** O(1) iterative, O(log n) recursive\n\n"
        "**Variants:**\n"
        "- **Standard:** Find exact target.\n"
        "- **Lower bound (bisect_left):** Find the first position where "
        "target could be inserted to keep the array sorted.\n"
        "- **Upper bound (bisect_right):** Find the position after the last "
        "occurrence of target.\n\n"
        "**Key insight:** Binary search can be applied to any monotonic "
        "function, not just sorted arrays (e.g., 'find the minimum speed to "
        "finish within time T')."
    )

    examples = [
        (
            "# --- Standard Binary Search ---\n"
            "# Time: O(log n), Space: O(1)\n"
            "def binary_search(arr: list, target: int) -> int:\n"
            "    \"\"\"Return index of target, or -1 if not found.\"\"\"\n"
            "    left, right = 0, len(arr) - 1\n\n"
            "    while left <= right:\n"
            "        mid = (left + right) // 2  # avoid overflow in other languages\n"
            "        if arr[mid] == target:\n"
            "            return mid\n"
            "        elif arr[mid] < target:\n"
            "            left = mid + 1   # search right half\n"
            "        else:\n"
            "            right = mid - 1  # search left half\n"
            "    return -1  # not found\n\n"
            "arr = [1, 3, 5, 7, 9, 11, 13]\n"
            "print(binary_search(arr, 7))   # 3\n"
            "print(binary_search(arr, 4))   # -1"
        ),
        (
            "# --- Lower Bound and Upper Bound ---\n"
            "def lower_bound(arr: list, target: int) -> int:\n"
            "    \"\"\"Find first index where arr[i] >= target. O(log n).\"\"\"\n"
            "    left, right = 0, len(arr)\n"
            "    while left < right:\n"
            "        mid = (left + right) // 2\n"
            "        if arr[mid] < target:\n"
            "            left = mid + 1\n"
            "        else:\n"
            "            right = mid\n"
            "    return left\n\n"
            "def upper_bound(arr: list, target: int) -> int:\n"
            "    \"\"\"Find first index where arr[i] > target. O(log n).\"\"\"\n"
            "    left, right = 0, len(arr)\n"
            "    while left < right:\n"
            "        mid = (left + right) // 2\n"
            "        if arr[mid] <= target:\n"
            "            left = mid + 1\n"
            "        else:\n"
            "            right = mid\n"
            "    return left\n\n"
            "arr = [1, 3, 3, 3, 5, 7]\n"
            "print(lower_bound(arr, 3))  # 1  (first index of 3)\n"
            "print(upper_bound(arr, 3))  # 4  (first index after all 3s)\n"
            "# Count of 3s = upper_bound - lower_bound = 4 - 1 = 3"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the time complexity of binary search on a sorted "
                "array of n elements?"
            ),
            options={
                "A": "O(n)",
                "B": "O(n log n)",
                "C": "O(log n)",
                "D": "O(1)",
            },
            correct="C",
            explanation=(
                "Binary search halves the search space with each comparison. "
                "After k comparisons, the remaining space is n/2^k. The search "
                "ends when n/2^k = 1, so k = log₂(n), giving O(log n)."
            ),
            distractors={
                "A": "O(n) is linear search — binary search is much faster on sorted data.",
                "B": "O(n log n) is the complexity of sorting, not searching.",
                "D": "O(1) would mean finding the element without any comparisons.",
            },
            mcq_type="complexity",
        ),
    ]

    return TopicSection(
        title="Searching Algorithms",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Binary search requires a sorted array and runs in O(log n).",
            "Use `left <= right` for standard search, `left < right` for bound variants.",
            "Lower bound finds the first valid position; upper bound finds one past the last.",
            "Python's `bisect` module provides optimized `bisect_left` and `bisect_right`.",
            "Binary search applies to any monotonic condition, not just sorted arrays.",
        ],
    )


def _big_o_analysis() -> TopicSection:
    explanation = (
        "### Big-O Complexity Analysis\n\n"
        "Big-O notation describes the upper bound of an algorithm's growth "
        "rate as input size increases. It tells you how an algorithm **scales**, "
        "not its exact runtime.\n\n"
        "**Common complexities (fastest to slowest):**\n\n"
        "| Big-O | Name | Example |\n"
        "|-------|------|---------|\n"
        "| O(1) | Constant | Array index access, hash table lookup |\n"
        "| O(log n) | Logarithmic | Binary search |\n"
        "| O(n) | Linear | Single loop through array |\n"
        "| O(n log n) | Linearithmic | Merge sort, efficient sorting |\n"
        "| O(n²) | Quadratic | Nested loops, bubble sort |\n"
        "| O(2ⁿ) | Exponential | Recursive Fibonacci (naive) |\n"
        "| O(n!) | Factorial | Generating all permutations |\n\n"
        "**Rules for analyzing code:**\n"
        "1. **Drop constants:** O(2n) → O(n)\n"
        "2. **Drop lower-order terms:** O(n² + n) → O(n²)\n"
        "3. **Nested loops multiply:** Two nested loops over n → O(n²)\n"
        "4. **Sequential code adds:** Loop O(n) then loop O(m) → O(n + m)\n"
        "5. **Recursive calls:** Analyze the recurrence relation (e.g., "
        "T(n) = 2T(n/2) + O(n) → O(n log n) for merge sort)"
    )

    examples = [
        (
            "# --- Analyzing time complexity ---\n\n"
            "# O(1) — Constant time\n"
            "def get_first(arr):\n"
            "    return arr[0]  # single operation, independent of n\n\n"
            "# O(n) — Linear time\n"
            "def find_max(arr):\n"
            "    max_val = arr[0]\n"
            "    for x in arr:        # one loop through n elements\n"
            "        if x > max_val:\n"
            "            max_val = x\n"
            "    return max_val\n\n"
            "# O(n²) — Quadratic time\n"
            "def has_duplicate_pair(arr):\n"
            "    for i in range(len(arr)):       # outer loop: n\n"
            "        for j in range(i + 1, len(arr)):  # inner loop: ~n\n"
            "            if arr[i] == arr[j]:    # n * n = n²\n"
            "                return True\n"
            "    return False\n\n"
            "# O(log n) — Logarithmic time\n"
            "def count_halvings(n):\n"
            "    count = 0\n"
            "    while n > 1:\n"
            "        n //= 2   # halving each iteration → log₂(n) iterations\n"
            "        count += 1\n"
            "    return count\n\n"
            "print(count_halvings(16))  # 4  (16 → 8 → 4 → 2 → 1)"
        ),
        (
            "# --- Space complexity analysis ---\n\n"
            "# O(1) space — in-place\n"
            "def reverse_in_place(arr):\n"
            "    left, right = 0, len(arr) - 1\n"
            "    while left < right:\n"
            "        arr[left], arr[right] = arr[right], arr[left]\n"
            "        left += 1\n"
            "        right -= 1\n"
            "    # Only uses a constant number of variables\n\n"
            "# O(n) space — creates new data structure\n"
            "def get_squares(arr):\n"
            "    return [x ** 2 for x in arr]  # new list of size n\n\n"
            "# O(n) space — recursive call stack\n"
            "def factorial(n):\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    return n * factorial(n - 1)  # n frames on the call stack"
        ),
    ]

    mcqs = [
        MCQ(
            question=(
                "What is the time complexity of the following code?\n\n"
                "```python\n"
                "def mystery(n):\n"
                "    count = 0\n"
                "    i = 1\n"
                "    while i < n:\n"
                "        count += 1\n"
                "        i *= 2\n"
                "    return count\n"
                "```"
            ),
            options={
                "A": "O(n)",
                "B": "O(n²)",
                "C": "O(log n)",
                "D": "O(n log n)",
            },
            correct="C",
            explanation=(
                "The variable `i` doubles each iteration (1, 2, 4, 8, ...). "
                "It reaches n after log₂(n) steps, so the loop runs O(log n) "
                "times."
            ),
            distractors={
                "A": "O(n) would require i to increment by 1 each step, not double.",
                "B": "O(n²) would require nested loops, not a single doubling loop.",
                "D": "O(n log n) would require an O(n) operation inside the O(log n) loop.",
            },
            mcq_type="code_output",
        ),
    ]

    return TopicSection(
        title="Big-O Complexity Analysis",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=mcqs,
        key_takeaways=[
            "Big-O describes the upper bound of growth rate — drop constants and lower-order terms.",
            "Nested loops multiply: O(n) inside O(n) = O(n²).",
            "Sequential operations add: O(n) + O(m) = O(n + m).",
            "Halving patterns (binary search, divide-and-conquer) are O(log n).",
            "Space complexity counts extra memory used, including the recursive call stack.",
        ],
    )


# ---------------------------------------------------------------------------
# Mock test (8-10 MCQs for 15-minute timed practice)
# ---------------------------------------------------------------------------

def _mock_test() -> list[MCQ]:
    return [
        MCQ(
            question=(
                "What is the time complexity of accessing an element by "
                "index in a Python list?"
            ),
            options={
                "A": "O(1)",
                "B": "O(n)",
                "C": "O(log n)",
                "D": "O(n²)",
            },
            correct="A",
            explanation=(
                "Python lists are backed by dynamic arrays. Accessing an "
                "element by index is a direct memory offset calculation, "
                "which takes O(1) time."
            ),
            distractors={
                "B": "O(n) applies to searching for a value, not accessing by index.",
                "C": "O(log n) applies to binary search, not direct index access.",
                "D": "O(n²) involves nested operations — simple indexing is constant time.",
            },
            mcq_type="complexity",
        ),
        MCQ(
            question=(
                "What does the following code print?\n\n"
                "```python\n"
                "stack = []\n"
                "stack.append(1)\n"
                "stack.append(2)\n"
                "stack.append(3)\n"
                "stack.pop()\n"
                "stack.append(4)\n"
                "print(stack.pop())\n"
                "```"
            ),
            options={
                "A": "1",
                "B": "2",
                "C": "3",
                "D": "4",
            },
            correct="D",
            explanation=(
                "After appending 1, 2, 3: stack = [1, 2, 3]. Pop removes 3: "
                "stack = [1, 2]. Append 4: stack = [1, 2, 4]. Final pop "
                "removes and returns 4."
            ),
            distractors={
                "A": "1 is at the bottom of the stack and would be the last to be popped.",
                "B": "2 is the second element; the top element (4) is popped first.",
                "C": "3 was already popped in the first pop() call.",
            },
            mcq_type="code_output",
        ),
        MCQ(
            question=(
                "Which traversal of a Binary Search Tree produces elements "
                "in sorted order?"
            ),
            options={
                "A": "Pre-order (Root, Left, Right)",
                "B": "Post-order (Left, Right, Root)",
                "C": "In-order (Left, Root, Right)",
                "D": "Level-order (BFS)",
            },
            correct="C",
            explanation=(
                "In-order traversal visits the left subtree, then the root, "
                "then the right subtree. Due to the BST property (left < root "
                "< right), this produces values in ascending order."
            ),
            distractors={
                "A": "Pre-order visits the root first, which doesn't produce sorted output.",
                "B": "Post-order visits the root last, which doesn't produce sorted output.",
                "D": "Level-order visits by depth level, not by value order.",
            },
            mcq_type="conceptual",
        ),
        MCQ(
            question=(
                "What is the space complexity of Merge Sort when sorting "
                "an array of n elements?"
            ),
            options={
                "A": "O(1)",
                "B": "O(log n)",
                "C": "O(n)",
                "D": "O(n log n)",
            },
            correct="C",
            explanation=(
                "Merge Sort requires O(n) auxiliary space for the temporary "
                "arrays used during the merge step. The recursion stack adds "
                "O(log n), but O(n) dominates."
            ),
            distractors={
                "A": "O(1) would mean in-place sorting; Merge Sort needs auxiliary arrays.",
                "B": "O(log n) is the recursion depth, but the merge arrays use O(n).",
                "D": "O(n log n) is the time complexity, not the space complexity.",
            },
            mcq_type="complexity",
        ),
        MCQ(
            question=(
                "What does the following code output?\n\n"
                "```python\n"
                "d = {'a': 1, 'b': 2, 'c': 3}\n"
                "d['b'] = 20\n"
                "d['d'] = 4\n"
                "del d['a']\n"
                "print(list(d.keys()))\n"
                "```"
            ),
            options={
                "A": "['a', 'b', 'c', 'd']",
                "B": "['b', 'c', 'd']",
                "C": "['b', 'd', 'c']",
                "D": "['c', 'b', 'd']",
            },
            correct="B",
            explanation=(
                "Starting with keys ['a', 'b', 'c']. Update 'b' (no key "
                "change). Add 'd': keys = ['a', 'b', 'c', 'd']. Delete 'a': "
                "keys = ['b', 'c', 'd']. Python 3.7+ dicts maintain insertion "
                "order."
            ),
            distractors={
                "A": "'a' was deleted, so it should not appear in the keys.",
                "C": "Python dicts maintain insertion order — 'c' was inserted before 'd'.",
                "D": "The order follows insertion, not alphabetical or any other sorting.",
            },
            mcq_type="code_output",
        ),
        MCQ(
            question=(
                "Which algorithm would you choose to find the shortest path "
                "in an unweighted graph?"
            ),
            options={
                "A": "Depth-First Search (DFS)",
                "B": "Breadth-First Search (BFS)",
                "C": "Binary Search",
                "D": "Quick Sort",
            },
            correct="B",
            explanation=(
                "BFS explores vertices level by level, so the first time it "
                "reaches a vertex, it has found the shortest path (in terms "
                "of number of edges) from the source. DFS does not guarantee "
                "shortest paths."
            ),
            distractors={
                "A": "DFS explores deeply first and may find a longer path before the shortest.",
                "C": "Binary Search works on sorted arrays, not graphs.",
                "D": "Quick Sort is a sorting algorithm, not a graph traversal algorithm.",
            },
            mcq_type="conceptual",
        ),
        MCQ(
            question=(
                "What is the time complexity of the following function?\n\n"
                "```python\n"
                "def func(arr):\n"
                "    n = len(arr)\n"
                "    for i in range(n):\n"
                "        for j in range(n):\n"
                "            if arr[i] == arr[j]:\n"
                "                print(i, j)\n"
                "```"
            ),
            options={
                "A": "O(n)",
                "B": "O(n log n)",
                "C": "O(n²)",
                "D": "O(2ⁿ)",
            },
            correct="C",
            explanation=(
                "There are two nested loops, each iterating n times. The "
                "inner operation (comparison and print) is O(1). Total: "
                "n × n = O(n²)."
            ),
            distractors={
                "A": "O(n) would require a single loop, not nested loops.",
                "B": "O(n log n) would require the inner loop to halve each time.",
                "D": "O(2ⁿ) applies to exponential algorithms like naive recursion, not nested loops.",
            },
            mcq_type="code_output",
        ),
        MCQ(
            question=(
                "Which sorting algorithm is NOT stable?"
            ),
            options={
                "A": "Merge Sort",
                "B": "Insertion Sort",
                "C": "Bubble Sort",
                "D": "Selection Sort",
            },
            correct="D",
            explanation=(
                "Selection Sort is not stable because it swaps non-adjacent "
                "elements. For example, sorting [3a, 3b, 1] — Selection Sort "
                "swaps 3a with 1, changing the relative order of equal "
                "elements. Merge Sort, Insertion Sort, and Bubble Sort are "
                "all stable."
            ),
            distractors={
                "A": "Merge Sort is stable — it preserves order of equal elements during merge.",
                "B": "Insertion Sort is stable — it shifts elements without swapping non-adjacent ones.",
                "C": "Bubble Sort is stable — it only swaps adjacent elements when strictly out of order.",
            },
            mcq_type="conceptual",
        ),
        MCQ(
            question=(
                "What is the result of performing binary search for the "
                "value 6 in the array [1, 3, 5, 7, 9]?"
            ),
            options={
                "A": "Returns index 2",
                "B": "Returns index 3",
                "C": "Returns -1 (not found)",
                "D": "Returns index 5",
            },
            correct="C",
            explanation=(
                "The value 6 is not present in the array [1, 3, 5, 7, 9]. "
                "Binary search will narrow down between indices 2 (value 5) "
                "and 3 (value 7), find no match, and return -1."
            ),
            distractors={
                "A": "Index 2 holds value 5, not 6.",
                "B": "Index 3 holds value 7, not 6.",
                "D": "Index 5 is out of bounds for a 5-element array (indices 0-4).",
            },
            mcq_type="code_output",
        ),
        MCQ(
            question=(
                "Which command correctly sorts a Python list in descending "
                "order?"
            ),
            options={
                "A": "arr.sort(reverse=True)",
                "B": "arr.sort(descending=True)",
                "C": "sorted(arr, order='desc')",
                "D": "arr.reverse_sort()",
            },
            correct="A",
            explanation=(
                "`list.sort(reverse=True)` sorts the list in-place in "
                "descending order. The `reverse` parameter is the correct "
                "keyword argument for both `sort()` and `sorted()`."
            ),
            distractors={
                "B": "There is no `descending` parameter — the correct parameter is `reverse`.",
                "C": "There is no `order` parameter in `sorted()` — use `reverse=True`.",
                "D": "`reverse_sort()` is not a built-in list method.",
            },
            mcq_type="command",
        ),
    ]


# ---------------------------------------------------------------------------
# Cheat sheet
# ---------------------------------------------------------------------------

def _cheat_sheet() -> str:
    return (
        "## DSA Quick-Reference Cheat Sheet\n\n"
        "### Big-O Complexity Table — Data Structures\n\n"
        "| Data Structure | Access | Search | Insert | Delete | Space |\n"
        "|----------------|--------|--------|--------|--------|-------|\n"
        "| Array (list) | O(1) | O(n) | O(n)* | O(n) | O(n) |\n"
        "| Linked List | O(n) | O(n) | O(1)** | O(n) | O(n) |\n"
        "| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |\n"
        "| Queue (deque) | O(n) | O(n) | O(1) | O(1) | O(n) |\n"
        "| Hash Table (dict) | N/A | O(1)† | O(1)† | O(1)† | O(n) |\n"
        "| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |\n"
        "| BST (worst) | O(n) | O(n) | O(n) | O(n) | O(n) |\n\n"
        "\\* Array insert at end is amortized O(1); insert at arbitrary index is O(n).  \n"
        "\\*\\* Linked list insert at head is O(1); insert at arbitrary position is O(n).  \n"
        "† Hash table average case; worst case is O(n) due to collisions.\n\n"
        "### Big-O Complexity Table — Sorting Algorithms\n\n"
        "| Algorithm | Best | Average | Worst | Space | Stable |\n"
        "|-----------|------|---------|-------|-------|--------|\n"
        "| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |\n"
        "| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |\n"
        "| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |\n"
        "| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |\n"
        "| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |\n"
        "| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |\n\n"
        "### Common Patterns\n\n"
        "| Pattern | When to Use | Complexity |\n"
        "|---------|-------------|------------|\n"
        "| Two Pointers | Sorted array, pair finding | O(n) |\n"
        "| Sliding Window | Subarray/substring problems | O(n) |\n"
        "| Hash Map Counting | Frequency, duplicates, two-sum | O(n) |\n"
        "| Binary Search | Sorted data, monotonic condition | O(log n) |\n"
        "| BFS | Shortest path (unweighted), level-order | O(V + E) |\n"
        "| DFS | Cycle detection, connected components | O(V + E) |\n"
        "| Divide & Conquer | Merge sort, quick sort | O(n log n) |\n\n"
        "### Key Reminders\n\n"
        "- `list.pop(0)` is O(n) — use `collections.deque.popleft()` for O(1).\n"
        "- Python `dict` keys must be hashable (immutable).\n"
        "- In-order traversal of BST = sorted output.\n"
        "- Binary search requires sorted input.\n"
        "- Always check edge cases: empty input, single element, duplicates."
    )
