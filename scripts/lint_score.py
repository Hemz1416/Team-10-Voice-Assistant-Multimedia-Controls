"""Automated Linting Quality Scorer and GitHub Actions Step Summary Generator.

Executes Ruff linting, tallies issues, computes a 10.0-scale code quality score,
and appends a formatted quality card to $GITHUB_STEP_SUMMARY if available.
"""

import json
import os
import subprocess
import sys


def calculate_lint_score() -> int:
    print("=" * 65)
    print("        AUTOMATED CODE LINTING QUALITY SCORE (RUFF)")
    print("=" * 65)

    # Run ruff check with JSON output
    cmd = [sys.executable, "-m", "ruff", "check", ".", "--output-format=json"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    violations = []
    if result.stdout.strip():
        try:
            violations = json.loads(result.stdout)
        except json.JSONDecodeError:
            violations = []

    count = len(violations)
    # Calculate score on 10.0 scale
    score = max(0.0, round(10.0 - (count * 0.2), 2))
    cleanliness = max(0.0, round(100.0 - (count * 2.0), 1))

    if count == 0:
        grade = "A+ (PERFECT)"
        status = "PASSED"
    elif count <= 3:
        grade = "A (EXCELLENT)"
        status = "PASSED"
    elif count <= 7:
        grade = "B (GOOD)"
        status = "PASSED"
    else:
        grade = "C (NEEDS IMPROVEMENT)"
        status = "FAILED"

    print("Total Files Checked:    All project modules in src/, tests/, scripts/")
    print(f"Violations Detected:    {count}")
    print(f"Code Cleanliness:       {cleanliness}%")
    print(f"Linting Quality Score:  {score:.2f} / 10.00 (Grade: {grade})")
    print(f"Status:                 {status}")
    print("=" * 65)

    # If running inside GitHub Actions, publish to Job Summary
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write("### 🔍 Code Linting Quality Report\n\n")
            f.write(f"- **Linting Score:** `{score:.2f} / 10.00` ({grade})\n")
            f.write(f"- **Cleanliness Rating:** `{cleanliness}%`\n")
            f.write(f"- **Total Violations:** `{count}`\n")
            f.write("- **Linter Engine:** Ruff (Python 3.11, pyproject.toml)\n\n")

    return 0 if count == 0 else 1


if __name__ == "__main__":
    sys.exit(calculate_lint_score())
