# Implementation Plan: NVIDIA Interview Prep Notebooks

## Overview

Programmatically generate four Jupyter notebooks (.ipynb) for NVIDIA SDET HackerRank assessment preparation. The implementation uses Python with nbformat to build structured notebooks from content data modules covering DSA, OS/Linux, Python coding, and REST API sections.

## Tasks

- [x] 1. Set up project structure and dependencies
  - Create `nvidia_interview_prep/` output directory
  - Create `generator/` package with `__init__.py`
  - Create `generator/content/` subpackage with `__init__.py`
  - Install/ensure `nbformat` dependency is available
  - _Requirements: 1.1, 1.2_

- [x] 2. Implement content data structures
  - [x] 2.1 Create dataclass definitions in `generator/models.py`
    - Implement `MCQ` dataclass with fields: question, options (dict A-D), correct, explanation, distractors, mcq_type
    - Implement `PracticeProblem` dataclass with fields: title, statement, function_signature, examples, solution_code, test_code, hints
    - Implement `TopicSection` dataclass with fields: title, difficulty, explanation, examples, practice, key_takeaways
    - Implement `NotebookSpec` dataclass with fields: title, filename, strategy_tips, sections, mock_test, cheat_sheet
    - Add validation in `__post_init__` for MCQ correct field (must be A-D) and options count (must be 4)
    - _Requirements: 8.1, 8.3_

- [x] 3. Implement the NotebookGenerator class
  - [x] 3.1 Create `generator/notebook_generator.py` with the `NotebookGenerator` class
    - Implement `generate(spec: NotebookSpec) -> NotebookNode` method that assembles the full notebook
    - Implement `_build_toc(spec)` to create table of contents markdown cell listing all topic sections
    - Implement `_build_strategy_tips(tips)` to create strategy tips markdown cell
    - Implement `_build_topic_section(section)` to convert a TopicSection into ordered cells: heading with difficulty label, explanation, worked examples with inline comments, practice content, key takeaways
    - Implement `_build_mcq_cell(mcq, number)` to create question cell + separate solution cell with "Solution" heading, correct answer, explanation, and distractor notes
    - Implement `_build_practice_problem(problem)` to create problem statement cell, starter code cell, solution cell, and test cell with assert statements
    - Implement `_build_mock_test(items, time_limit)` to create timed practice section with timer instructions
    - Implement `_build_cheat_sheet(content)` to create cheat sheet markdown cell
    - Implement `write(notebook, output_dir, filename)` to write .ipynb to disk using nbformat
    - Ensure difficulty ordering: sort sections so all Beginner sections appear before Mid-Level
    - Run `nbformat.validate()` on generated notebook before writing
    - _Requirements: 1.4, 1.5, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 3.4, 4.6, 5.6, 6.6, 7.6, 8.5, 9.1, 9.6, 10.1, 10.4_

- [x] 4. Checkpoint - Verify generator infrastructure
  - Ensure all tests pass, ask the user if questions arise.

- [x] 5. Create DSA content module
  - [x] 5.1 Create `generator/content/dsa.py` with a function that returns a `NotebookSpec` for the DSA notebook
    - Filename: `01_data_structures_algorithms.ipynb`
    - Beginner topics (at least 3): Arrays and Strings, Linked Lists, Stacks and Queues, Hash Tables, basic Sorting (Bubble, Selection, Insertion)
    - Mid-Level topics (at least 3): Binary Trees and BSTs, Graphs and BFS/DFS, advanced Sorting (Merge Sort, Quick Sort), Searching (Binary Search), Big-O complexity analysis
    - Each data structure topic must include a Python implementation with common operations
    - Each algorithm must include time and space complexity analysis
    - At least 5 MCQs per difficulty level with four options, correct answer, explanation, and distractor notes
    - Include varied MCQ types: conceptual, code_output, command, complexity
    - Strategy tips for MCQ sections: elimination techniques, time allocation, skip-and-return advice
    - Mock test section: 8-10 MCQs designed for 15-minute completion
    - Cheat sheet: key formulas, complexity table, common patterns
    - _Requirements: 1.3, 2.4, 4.1, 4.2, 4.3, 4.4, 4.5, 8.1, 8.2, 8.3, 8.4, 9.2, 10.2_

- [ ] 6. Create OS/Linux content module
  - [-] 6.1 Create `generator/content/os_linux.py` with a function that returns a `NotebookSpec` for the OS/Linux notebook
    - Filename: `02_os_linux.ipynb`
    - Beginner topics (at least 3): Linux file system hierarchy, basic shell commands (ls, cd, grep, find, chmod, chown), process management (ps, top, kill), file permissions and ownership, package management (apt, yum/dnf)
    - Mid-Level topics (at least 3): process scheduling and memory management, shell scripting (variables, loops, conditionals, functions), networking commands (netstat, ss, ip, curl, ping, traceroute), systemd service management, log analysis (journalctl, common log locations)
    - NVIDIA-relevant topics: Docker container basics, CI/CD pipeline concepts (Jenkins), basic Kubernetes concepts (pods, deployments, services), PXE boot overview
    - Each command topic must include example command invocations with sample output
    - At least 8 MCQs per difficulty level with four options, correct answer, explanation, and distractor notes
    - Strategy tips for MCQ sections: elimination techniques, time allocation, skip-and-return advice
    - Mock test section: 10-12 MCQs designed for 25-minute completion
    - Cheat sheet: key commands, common flags, file paths reference
    - _Requirements: 1.3, 2.4, 5.1, 5.2, 5.3, 5.4, 5.5, 8.1, 8.2, 8.3, 8.4, 9.3, 10.2_

- [ ] 7. Create Python coding content module
  - [~] 7.1 Create `generator/content/python_coding.py` with a function that returns a `NotebookSpec` for the Python notebook
    - Filename: `03_python_coding.ipynb`
    - Beginner topics (at least 3): string manipulation, list comprehensions and built-in functions, dictionary operations, file I/O basics, basic error handling (try/except)
    - Mid-Level topics (at least 3): OOP (classes, inheritance, decorators), generators and iterators, regular expressions, collections module (Counter, defaultdict, deque), common algorithms (two pointers, sliding window, recursion)
    - At least 4 practice problems per difficulty level with problem statement, function signature, examples, complete solution, and assert-based test cases
    - NVIDIA-relevant examples: basic test automation script pattern, simple log parser, data validation utility
    - Solutions placed in separate cells below problem statements
    - Include timing tips for 30-minute constraint
    - Strategy tips for coding sections: read problem fully, start brute force, test edge cases, time management
    - Mock test section: 2-3 coding problems designed for 30-minute completion
    - Cheat sheet: common Python patterns, built-in functions, complexity of operations
    - _Requirements: 1.3, 2.4, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 9.4, 10.3_

- [ ] 8. Create REST API content module
  - [~] 8.1 Create `generator/content/rest_api.py` with a function that returns a `NotebookSpec` for the REST API notebook
    - Filename: `04_rest_api_coding.ipynb`
    - Beginner topics (at least 3): HTTP methods (GET, POST, PUT, DELETE), status codes, making requests with `requests` library, parsing JSON responses, query parameters and headers
    - Mid-Level topics (at least 3): API authentication (API keys, Bearer tokens), pagination handling, error handling and retry logic, nested JSON data, building API test scripts
    - At least 4 practice problems per difficulty level with problem statement, function signature, mock API data or public APIs (JSONPlaceholder, httpbin.org), and complete solution
    - NVIDIA-relevant examples: Redfish API interaction pattern, CI/CD webhook handler pattern, test result reporting API client
    - Solutions placed in separate cells below problem statements
    - Reference section on common HackerRank REST API patterns (filtering paginated endpoints, aggregating across API calls)
    - Strategy tips for coding sections: read problem fully, start brute force, test edge cases, time management
    - Mock test section: 2-3 coding problems designed for 25-minute completion
    - Cheat sheet: HTTP status codes, common request patterns, JSON handling tips
    - _Requirements: 1.3, 2.4, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 9.5, 10.3_

- [ ] 9. Checkpoint - Verify all content modules
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 10. Create main entry point and generate notebooks
  - [~] 10.1 Create `generate_notebooks.py` as the main entry point
    - Import all four content module spec functions and NotebookGenerator
    - Instantiate NotebookGenerator
    - Loop through all four NotebookSpecs, generate each notebook, and write to `nvidia_interview_prep/`
    - Print summary of generated files
    - _Requirements: 1.1, 1.2, 1.3_

  - [~] 10.2 Run the generator to produce all four .ipynb files
    - Execute `generate_notebooks.py`
    - Verify all four files exist in `nvidia_interview_prep/` with correct filenames
    - _Requirements: 1.1, 1.2, 1.3_

- [ ] 11. Final checkpoint - Verify generated notebooks
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Content modules are the bulk of the work — each contains extensive educational material
- The generator enforces structural invariants (cell ordering, difficulty ordering, MCQ format) so content authors can focus on content quality
