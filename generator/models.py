"""Data models for notebook content generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Union


@dataclass
class MCQ:
    """Multiple-choice question with four options A-D."""

    question: str
    options: dict[str, str]
    correct: str
    explanation: str
    distractors: dict[str, str]
    mcq_type: str  # "conceptual" | "code_output" | "command" | "complexity"

    def __post_init__(self) -> None:
        if self.correct not in {"A", "B", "C", "D"}:
            raise ValueError(
                f"correct must be one of A, B, C, D — got {self.correct!r}"
            )
        if len(self.options) != 4:
            raise ValueError(
                f"options must have exactly 4 entries — got {len(self.options)}"
            )
        expected_keys = {"A", "B", "C", "D"}
        if set(self.options.keys()) != expected_keys:
            raise ValueError(
                f"options keys must be A, B, C, D — got {set(self.options.keys())}"
            )


@dataclass
class PracticeProblem:
    """Coding exercise with solution and tests."""

    title: str
    statement: str
    function_signature: str
    examples: list[dict]
    solution_code: str
    test_code: str
    hints: list[str] = field(default_factory=list)


@dataclass
class TopicSection:
    """A single topic within a notebook, covering one concept."""

    title: str
    difficulty: str  # "Beginner" | "Mid-Level"
    explanation: str
    examples: list[str]
    practice: list[Union[MCQ, PracticeProblem]]
    key_takeaways: list[str]


@dataclass
class NotebookSpec:
    """Full specification for generating one Jupyter notebook."""

    title: str
    filename: str
    strategy_tips: str
    sections: list[TopicSection]
    mock_test: list[Union[MCQ, PracticeProblem]]
    cheat_sheet: str
