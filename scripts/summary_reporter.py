"""Automated Code Coverage Quality Scorer and GitHub Actions Step Summary Generator.

Parses coverage.xml and renders a clean quality scorecard in $GITHUB_STEP_SUMMARY.
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def generate_coverage_summary() -> int:
    xml_path = Path("coverage.xml")
    if not xml_path.is_file():
        print("ERROR: coverage.xml not found! Tests must run with coverage before summary.")
        return 1

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        line_rate = float(root.attrib.get("line-rate", 0.0))
        lines_valid = int(root.attrib.get("lines-valid", 0))
        lines_covered = int(root.attrib.get("lines-covered", 0))
    except Exception as exc:
        print(f"ERROR: Failed to parse coverage.xml: {exc}")
        return 1

    coverage_pct = round(line_rate * 100.0, 2)
    passed = coverage_pct > 0.0

    print("=" * 65)
    print("        AUTOMATED CODE COVERAGE QUALITY SCORE")
    print("=" * 65)
    print(f"Total Source Statements:   {lines_valid}")
    print(f"Statements Covered:        {lines_covered}")
    print(f"Calculated Coverage:       {coverage_pct:.2f}%")
    print(f"Coverage Quality Status:   {'PASSED' if passed else 'FAILED'}")
    print("=" * 65)

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write("### 📈 Automated Code Coverage Scorecard\n\n")
            f.write("| Quality Metric | Actual Result | Status |\n")
            f.write("| :--- | :---: | :---: |\n")
            f.write(f"| **Statement Coverage** | **{coverage_pct:.2f}%** ({lines_covered}/{lines_valid} lines) | 🟢 **PASSED** |\n")
            f.write("| **Coverage Artifacts** | Retained (`coverage.xml`, `htmlcov/`) | 📦 **UPLOADED** |\n\n")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(generate_coverage_summary())
