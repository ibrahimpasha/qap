# Requirements Document

## Introduction

This feature delivers a comprehensive interview preparation course as a set of Jupyter notebooks (.ipynb files) targeting the nip Senior Software SDET Test Development Engineer HackerRank assessment. The assessment consists of four timed sections: Data Structures & Algorithms (15 min, multiple choice), OS/Linux (25 min, multiple choice), Python coding (30 min), and REST API coding (25 min). The notebooks cover beginner to mid-level content with explanations, examples, practice problems, solutions, and multiple-choice questions. Content is tailored to the nip SDET role, incorporating relevant technologies such as CI/CD, containers, AI frameworks, and systems-level tooling.

## Glossary

- **Notebook_System**: The collection of Jupyter notebook files (.ipynb) that comprise the interview preparation course material
- **DSA_Notebook**: The Jupyter notebook covering Data Structures and Algorithms topics with multiple-choice questions
- **OS_Linux_Notebook**: The Jupyter notebook covering Operating Systems and Linux topics with multiple-choice questions
- **Python_Notebook**: The Jupyter notebook covering Python coding problems with executable solutions
- **REST_API_Notebook**: The Jupyter notebook covering REST API coding problems with executable solutions
- **Topic_Section**: A markdown and code cell grouping within a notebook that covers a single concept, including explanation, examples, and practice content
- **Practice_Problem**: A coding exercise or multiple-choice question with a provided solution or answer explanation
- **MCQ**: Multiple-Choice Question with four answer options (A, B, C, D) and an explanation of the correct answer
- **Difficulty_Level**: Classification of content as Beginner or Mid-Level to indicate progressive complexity
- **HackerRank_Assessment**: The timed online coding and multiple-choice test used by nip for candidate evaluation

## Requirements

### Requirement 1: Notebook File Structure

**User Story:** As a candidate, I want each test section covered in its own dedicated Jupyter notebook, so that I can study each topic area independently and in a focused manner.

#### Acceptance Criteria

1. THE Notebook_System SHALL produce exactly four Jupyter notebook files in .ipynb format: one DSA_Notebook, one OS_Linux_Notebook, one Python_Notebook, and one REST_API_Notebook
2. THE Notebook_System SHALL place all notebook files in the `nip_interview_prep/` directory
3. THE Notebook_System SHALL name the notebooks using descriptive snake_case filenames: `01_data_structures_algorithms.ipynb`, `02_os_linux.ipynb`, `03_python_coding.ipynb`, `04_rest_api_coding.ipynb`
4. WHEN a notebook is opened in Jupyter, THE Notebook_System SHALL render all markdown cells with proper formatting including headings, bold text, code blocks, and bullet lists
5. THE Notebook_System SHALL include a table of contents markdown cell at the top of each notebook listing all Topic_Sections within that notebook

### Requirement 2: Progressive Difficulty Structure

**User Story:** As a candidate, I want content organized from beginner to mid-level difficulty, so that I can build foundational knowledge before tackling harder material.

#### Acceptance Criteria

1. THE Notebook_System SHALL organize each notebook into two clearly labeled sections: "Beginner" and "Mid-Level"
2. THE Notebook_System SHALL present Beginner Topic_Sections before Mid-Level Topic_Sections within each notebook
3. WHEN a Topic_Section is presented, THE Notebook_System SHALL label the Difficulty_Level in the section heading
4. THE Notebook_System SHALL include at minimum 3 Beginner Topic_Sections and 3 Mid-Level Topic_Sections per notebook

### Requirement 3: Topic Section Format

**User Story:** As a candidate, I want each topic to include a clear explanation, worked examples, and practice content, so that I can learn the concept and immediately test my understanding.

#### Acceptance Criteria

1. THE Notebook_System SHALL structure each Topic_Section with three parts: a concept explanation in markdown, one or more worked examples in code cells, and at least one Practice_Problem
2. WHEN presenting a concept explanation, THE Notebook_System SHALL use markdown cells with clear prose, relevant diagrams described in text, and key terminology highlighted
3. WHEN presenting a worked example, THE Notebook_System SHALL provide executable Python code cells with inline comments explaining each step
4. THE Notebook_System SHALL include a "Key Takeaways" markdown cell at the end of each Topic_Section summarizing the main points

### Requirement 4: Data Structures and Algorithms Notebook Content

**User Story:** As a candidate, I want to study core data structures and algorithms with multiple-choice questions matching the 15-minute HackerRank format, so that I can prepare for the timed MCQ section.

#### Acceptance Criteria

1. THE DSA_Notebook SHALL cover the following Beginner topics: Arrays and Strings, Linked Lists, Stacks and Queues, Hash Tables, and basic Sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort)
2. THE DSA_Notebook SHALL cover the following Mid-Level topics: Binary Trees and BSTs, Graphs and BFS/DFS traversal, advanced Sorting (Merge Sort, Quick Sort), Searching algorithms (Binary Search and variants), and Big-O complexity analysis
3. WHEN presenting a data structure topic, THE DSA_Notebook SHALL include a Python implementation of the data structure with methods for common operations
4. THE DSA_Notebook SHALL include at least 5 MCQs per Difficulty_Level, each with four answer options and an explanation of the correct answer
5. THE DSA_Notebook SHALL include time and space complexity analysis for each algorithm presented
6. WHEN presenting an MCQ, THE DSA_Notebook SHALL hide the answer and explanation in a separate cell marked with a "Click to reveal" or "Solution" heading so the candidate can attempt the question first

### Requirement 5: OS and Linux Notebook Content

**User Story:** As a candidate, I want to study operating systems concepts and Linux administration with multiple-choice questions matching the 25-minute HackerRank format, so that I can prepare for the timed MCQ section.

#### Acceptance Criteria

1. THE OS_Linux_Notebook SHALL cover the following Beginner topics: Linux file system hierarchy, basic shell commands (ls, cd, grep, find, chmod, chown), process management (ps, top, kill), file permissions and ownership, and package management (apt, yum/dnf)
2. THE OS_Linux_Notebook SHALL cover the following Mid-Level topics: process scheduling and memory management concepts, shell scripting fundamentals (variables, loops, conditionals, functions), networking commands (netstat, ss, ip, curl, ping, traceroute), systemd service management, and log analysis with journalctl and common log locations
3. THE OS_Linux_Notebook SHALL include nip-role-relevant topics: Docker container basics, CI/CD pipeline concepts (Jenkins), basic Kubernetes concepts (pods, deployments, services), and PXE boot overview
4. THE OS_Linux_Notebook SHALL include at least 8 MCQs per Difficulty_Level, each with four answer options and an explanation of the correct answer
5. WHEN presenting a Linux command topic, THE OS_Linux_Notebook SHALL include example command invocations with sample output shown in markdown or code cells
6. WHEN presenting an MCQ, THE OS_Linux_Notebook SHALL hide the answer and explanation in a separate cell marked with a "Solution" heading

### Requirement 6: Python Coding Notebook Content

**User Story:** As a candidate, I want to practice Python coding problems matching the 30-minute HackerRank coding format, so that I can prepare for the timed coding section.

#### Acceptance Criteria

1. THE Python_Notebook SHALL cover the following Beginner topics: string manipulation, list comprehensions and built-in functions, dictionary operations, file I/O basics, and basic error handling with try/except
2. THE Python_Notebook SHALL cover the following Mid-Level topics: object-oriented programming (classes, inheritance, decorators), generators and iterators, regular expressions, collections module (Counter, defaultdict, deque), and common algorithm implementations (two pointers, sliding window, recursion)
3. THE Python_Notebook SHALL include at least 4 Practice_Problems per Difficulty_Level, each with a problem statement, function signature, example inputs/outputs, and a complete solution in an executable code cell
4. WHEN presenting a Practice_Problem, THE Python_Notebook SHALL include test cases that validate the solution using assert statements
5. THE Python_Notebook SHALL include nip-role-relevant examples: a basic test automation script pattern, a simple log parser, and a data validation utility
6. WHEN presenting a solution, THE Python_Notebook SHALL place the solution in a separate cell below the problem statement so the candidate can attempt the problem first
7. THE Python_Notebook SHALL include timing considerations and tips for solving problems within the 30-minute constraint

### Requirement 7: REST API Coding Notebook Content

**User Story:** As a candidate, I want to practice REST API coding problems matching the 25-minute HackerRank coding format, so that I can prepare for the timed coding section.

#### Acceptance Criteria

1. THE REST_API_Notebook SHALL cover the following Beginner topics: HTTP methods (GET, POST, PUT, DELETE), status codes and their meanings, making API requests with the `requests` library, parsing JSON responses, and query parameters and headers
2. THE REST_API_Notebook SHALL cover the following Mid-Level topics: API authentication (API keys, Bearer tokens), pagination handling, error handling and retry logic, working with nested JSON data, and building API test scripts
3. THE REST_API_Notebook SHALL include at least 4 Practice_Problems per Difficulty_Level, each with a problem statement, expected function signature, example API responses as mock data, and a complete solution
4. WHEN presenting API Practice_Problems, THE REST_API_Notebook SHALL use mock data or public free APIs (such as JSONPlaceholder, httpbin.org) so that code cells can be executed without proprietary API access
5. THE REST_API_Notebook SHALL include nip-role-relevant examples: a Redfish API interaction pattern, a basic CI/CD webhook handler pattern, and a test result reporting API client
6. WHEN presenting a solution, THE REST_API_Notebook SHALL place the solution in a separate cell below the problem statement so the candidate can attempt the problem first
7. THE REST_API_Notebook SHALL include a reference section on common HackerRank REST API problem patterns (filtering data from paginated endpoints, aggregating results across API calls)

### Requirement 8: Multiple-Choice Question Quality

**User Story:** As a candidate, I want high-quality multiple-choice questions that reflect real HackerRank assessment patterns, so that my practice closely mirrors the actual test experience.

#### Acceptance Criteria

1. THE Notebook_System SHALL format each MCQ with a numbered question, four labeled options (A, B, C, D), and exactly one correct answer
2. WHEN an MCQ is presented, THE Notebook_System SHALL include at least one plausible distractor option that tests a common misconception
3. THE Notebook_System SHALL provide a detailed explanation for the correct answer and a brief note on why each incorrect option is wrong
4. THE Notebook_System SHALL vary MCQ types to include: conceptual understanding, code output prediction, "which command achieves X" scenarios, and time/space complexity identification
5. WHEN presenting code-based MCQs, THE Notebook_System SHALL include a code snippet in the question cell that the candidate must analyze

### Requirement 9: Timed Practice Simulation

**User Story:** As a candidate, I want guidance on simulating timed test conditions, so that I can practice under realistic time pressure.

#### Acceptance Criteria

1. THE Notebook_System SHALL include a "Timed Practice" section at the end of each notebook containing a mini mock test
2. THE DSA_Notebook SHALL include a mock test with 8-10 MCQs designed to be completed in 15 minutes
3. THE OS_Linux_Notebook SHALL include a mock test with 10-12 MCQs designed to be completed in 25 minutes
4. THE Python_Notebook SHALL include a mock test with 2-3 coding problems designed to be completed in 30 minutes
5. THE REST_API_Notebook SHALL include a mock test with 2-3 coding problems designed to be completed in 25 minutes
6. WHEN presenting a mock test section, THE Notebook_System SHALL include instructions to set a timer and attempt all questions before checking solutions

### Requirement 10: Study Tips and Strategy Content

**User Story:** As a candidate, I want test-taking strategies and study tips specific to each section, so that I can maximize my score within the time constraints.

#### Acceptance Criteria

1. THE Notebook_System SHALL include a "Strategy Tips" markdown section at the beginning of each notebook, after the table of contents
2. WHEN presenting strategy tips for MCQ sections (DSA and OS/Linux), THE Notebook_System SHALL include advice on elimination techniques, time allocation per question, and when to skip and return
3. WHEN presenting strategy tips for coding sections (Python and REST API), THE Notebook_System SHALL include advice on reading the problem fully, starting with brute force, testing edge cases, and managing time across problems
4. THE Notebook_System SHALL include a quick-reference cheat sheet markdown cell at the end of each notebook summarizing key formulas, commands, or patterns for that section
