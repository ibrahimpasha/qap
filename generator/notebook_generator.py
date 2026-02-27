"""Notebook generator — assembles NotebookSpec data into valid .ipynb files."""

from __future__ import annotations

import os
from typing import Union

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

from generator.models import MCQ, NotebookSpec, PracticeProblem, TopicSection


class NotebookGenerator:
    """Builds Jupyter notebooks from *NotebookSpec* objects using nbformat v4."""

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def generate(self, spec: NotebookSpec) -> nbformat.NotebookNode:
        """Assemble a complete notebook from *spec*.

        Cell order:
        1. Title
        2. Table of contents
        3. Strategy tips
        4. Topic sections (Beginner first, then Mid-Level)
        5. Mock test (timed practice)
        6. Cheat sheet
        """
        nb = new_notebook()
        nb.metadata.update(
            {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3",
                },
                "language_info": {
                    "name": "python",
                    "version": "3.10.0",
                },
            }
        )

        cells: list[nbformat.NotebookNode] = []

        # 1. Title
        cells.append(new_markdown_cell(f"# {spec.title}"))

        # 2. Table of contents
        cells.append(self._build_toc(spec))

        # 3. Strategy tips
        cells.append(self._build_strategy_tips(spec.strategy_tips))

        # 4. Topic sections — beginner before mid-level
        sorted_sections = sorted(
            spec.sections,
            key=lambda s: 0 if s.difficulty == "Beginner" else 1,
        )
        for section in sorted_sections:
            cells.extend(self._build_topic_section(section))

        # 5. Mock test
        time_limit = self._infer_time_limit(spec.filename)
        cells.extend(self._build_mock_test(spec.mock_test, time_limit))

        # 6. Cheat sheet
        cells.append(self._build_cheat_sheet(spec.cheat_sheet))

        nb.cells = cells
        nbformat.validate(nb)
        return nb

    def write(
        self,
        notebook: nbformat.NotebookNode,
        output_dir: str,
        filename: str,
    ) -> str:
        """Write *notebook* to *output_dir/filename* and return the full path."""
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, filename)
        with open(path, "w", encoding="utf-8") as fh:
            nbformat.write(notebook, fh)
        return path

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _build_toc(self, spec: NotebookSpec) -> nbformat.NotebookNode:
        """Table of contents listing every topic section."""
        sorted_sections = sorted(
            spec.sections,
            key=lambda s: 0 if s.difficulty == "Beginner" else 1,
        )
        lines = ["## Table of Contents\n"]
        for idx, section in enumerate(sorted_sections, 1):
            anchor = section.title.lower().replace(" ", "-")
            lines.append(
                f"{idx}. [{section.title}](#{anchor}) "
                f"*({section.difficulty})*"
            )
        lines.append("")  # trailing newline
        return new_markdown_cell("\n".join(lines))

    def _build_strategy_tips(self, tips: str) -> nbformat.NotebookNode:
        """Strategy tips markdown cell."""
        return new_markdown_cell(f"## Strategy Tips\n\n{tips}")

    def _build_topic_section(
        self, section: TopicSection
    ) -> list[nbformat.NotebookNode]:
        """Convert a *TopicSection* into an ordered list of cells.

        Order: heading → explanation → worked examples → practice → takeaways.
        """
        cells: list[nbformat.NotebookNode] = []

        # Heading with difficulty label
        cells.append(
            new_markdown_cell(
                f"## {section.title} ({section.difficulty})"
            )
        )

        # Concept explanation
        cells.append(new_markdown_cell(section.explanation))

        # Worked examples (code cells with inline comments)
        for example in section.examples:
            cells.append(new_code_cell(example))

        # Practice content
        mcq_counter = 1
        for item in section.practice:
            if isinstance(item, MCQ):
                cells.extend(self._build_mcq_cell(item, mcq_counter))
                mcq_counter += 1
            elif isinstance(item, PracticeProblem):
                cells.extend(self._build_practice_problem(item))

        # Key takeaways
        takeaway_lines = ["### Key Takeaways\n"]
        for point in section.key_takeaways:
            takeaway_lines.append(f"- {point}")
        cells.append(new_markdown_cell("\n".join(takeaway_lines)))

        return cells

    def _build_mcq_cell(
        self, mcq: MCQ, number: int
    ) -> list[nbformat.NotebookNode]:
        """Question cell + separate solution cell for an MCQ."""
        # --- Question cell ---
        q_lines = [f"### Question {number}\n"]
        q_lines.append(mcq.question)
        q_lines.append("")
        for letter in ("A", "B", "C", "D"):
            q_lines.append(f"**{letter}.** {mcq.options[letter]}")
        question_cell = new_markdown_cell("\n".join(q_lines))

        # --- Solution cell ---
        s_lines = [f"### Solution — Question {number}\n"]
        s_lines.append(f"**Correct Answer: {mcq.correct}**\n")
        s_lines.append(f"{mcq.explanation}\n")
        s_lines.append("**Why the other options are incorrect:**\n")
        for letter in ("A", "B", "C", "D"):
            if letter != mcq.correct and letter in mcq.distractors:
                s_lines.append(f"- **{letter}.** {mcq.distractors[letter]}")
        solution_cell = new_markdown_cell("\n".join(s_lines))

        return [question_cell, solution_cell]

    def _build_practice_problem(
        self, problem: PracticeProblem
    ) -> list[nbformat.NotebookNode]:
        """Problem statement, starter code, solution, and test cells."""
        # --- Problem statement ---
        p_lines = [f"### Practice: {problem.title}\n"]
        p_lines.append(problem.statement)
        p_lines.append("")
        p_lines.append(f"**Function signature:** `{problem.function_signature}`\n")
        if problem.examples:
            p_lines.append("**Examples:**\n")
            for ex in problem.examples:
                p_lines.append(f"- Input: `{ex.get('input', '')}` → Output: `{ex.get('output', '')}`")
        if problem.hints:
            p_lines.append("\n**Hints:**\n")
            for hint in problem.hints:
                p_lines.append(f"- {hint}")
        problem_cell = new_markdown_cell("\n".join(p_lines))

        # --- Starter code cell ---
        starter_cell = new_code_cell(
            f"# TODO: Implement your solution\n{problem.function_signature}\n    pass"
        )

        # --- Solution cell ---
        solution_cell = new_code_cell(
            f"# Solution: {problem.title}\n{problem.solution_code}"
        )

        # --- Test cell ---
        test_cell = new_code_cell(
            f"# Tests for {problem.title}\n{problem.test_code}"
        )

        return [problem_cell, starter_cell, solution_cell, test_cell]

    def _build_mock_test(
        self,
        items: list[Union[MCQ, PracticeProblem]],
        time_limit: str,
    ) -> list[nbformat.NotebookNode]:
        """Timed practice section with timer instructions."""
        cells: list[nbformat.NotebookNode] = []

        header_lines = [
            "## Timed Practice — Mock Test\n",
            f"**Time limit: {time_limit}**\n",
            "**Instructions:**\n",
            "1. Set a timer before you begin.",
            "2. Attempt **all** questions before checking any solutions.",
            "3. Mark questions you are unsure about and revisit them if time permits.",
            "4. When the timer ends, stop and review your answers against the solutions below.",
        ]
        cells.append(new_markdown_cell("\n".join(header_lines)))

        mcq_counter = 1
        for item in items:
            if isinstance(item, MCQ):
                cells.extend(self._build_mcq_cell(item, mcq_counter))
                mcq_counter += 1
            elif isinstance(item, PracticeProblem):
                cells.extend(self._build_practice_problem(item))

        return cells

    def _build_cheat_sheet(self, content: str) -> nbformat.NotebookNode:
        """Cheat sheet markdown cell."""
        return new_markdown_cell(f"## Quick-Reference Cheat Sheet\n\n{content}")

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    @staticmethod
    def _infer_time_limit(filename: str) -> str:
        """Return a human-readable time limit based on the notebook filename."""
        mapping = {
            "01_data_structures_algorithms.ipynb": "15 minutes",
            "02_os_linux.ipynb": "25 minutes",
            "03_python_coding.ipynb": "30 minutes",
            "04_rest_api_coding.ipynb": "25 minutes",
        }
        return mapping.get(filename, "25 minutes")
