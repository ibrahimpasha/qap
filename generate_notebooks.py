#!/usr/bin/env python3
"""Main entry point — generate all four nip interview prep notebooks."""

from __future__ import annotations

import os

from generator.content.dsa import get_dsa_spec
from generator.content.os_linux import get_os_linux_spec
from generator.content.python_coding import get_python_coding_spec
from generator.content.rest_api import get_rest_api_spec
from generator.content.pytest_testing import get_pytest_spec
from generator.notebook_generator import NotebookGenerator


OUTPUT_DIR = "nip_interview_prep"


def main() -> None:
    """Generate all four interview prep notebooks."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generator = NotebookGenerator()
    specs = [
        get_dsa_spec(),
        get_os_linux_spec(),
        get_python_coding_spec(),
        get_rest_api_spec(),
        get_pytest_spec(),
    ]

    print(f"Generating notebooks in '{OUTPUT_DIR}/'...")
    for spec in specs:
        path = generator.write(generator.generate(spec), OUTPUT_DIR, spec.filename)
        print(f"  ✓ {spec.filename}  ({path})")

    print(f"\nDone. {len(specs)} notebooks written to '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    main()
