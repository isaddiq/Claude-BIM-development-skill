#!/usr/bin/env python3
"""Validate a BIM element-to-object mapping CSV file."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_COLUMNS = {"element_id", "object_name"}
OPTIONAL_COLUMNS = {"ifc_guid", "category", "source_file"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a BIM mapping CSV with element_id and object_name columns."
    )
    parser.add_argument("csv_path", help="Path to the BIM mapping CSV file.")
    return parser.parse_args()


def read_rows(csv_path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with csv_path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    return rows, fieldnames


def validate(csv_path: Path) -> tuple[dict[str, Any], bool]:
    if not csv_path.exists():
        report = {
            "csv_path": str(csv_path),
            "status": "fail",
            "errors": [f"CSV file does not exist: {csv_path}"],
            "warnings": [],
        }
        return report, False

    if not csv_path.is_file():
        report = {
            "csv_path": str(csv_path),
            "status": "fail",
            "errors": [f"Path is not a file: {csv_path}"],
            "warnings": [],
        }
        return report, False

    try:
        rows, fieldnames = read_rows(csv_path)
    except OSError as exc:
        report = {
            "csv_path": str(csv_path),
            "status": "fail",
            "errors": [f"Could not read CSV file: {exc}"],
            "warnings": [],
        }
        return report, False

    columns = set(fieldnames)
    missing_required_columns = sorted(REQUIRED_COLUMNS - columns)
    present_optional_columns = sorted(OPTIONAL_COLUMNS & columns)
    errors: list[str] = []
    warnings: list[str] = []

    if missing_required_columns:
        errors.append(
            "Missing required column(s): " + ", ".join(missing_required_columns)
        )

    element_ids = [row.get("element_id", "").strip() for row in rows]
    object_names = [row.get("object_name", "").strip() for row in rows]
    element_id_counts = Counter(element_id for element_id in element_ids if element_id)

    missing_element_id_rows = [
        index + 2 for index, element_id in enumerate(element_ids) if not element_id
    ]
    missing_object_name_rows = [
        index + 2 for index, object_name in enumerate(object_names) if not object_name
    ]
    duplicate_element_ids = sorted(
        element_id for element_id, count in element_id_counts.items() if count > 1
    )

    if missing_element_id_rows:
        errors.append(
            "Rows with missing element_id: "
            + ", ".join(str(row_number) for row_number in missing_element_id_rows)
        )

    if duplicate_element_ids:
        errors.append(
            "Duplicate element_id value(s): " + ", ".join(duplicate_element_ids)
        )

    if missing_object_name_rows:
        errors.append(
            "Rows with missing object_name: "
            + ", ".join(str(row_number) for row_number in missing_object_name_rows)
        )

    if "ifc_guid" not in columns:
        warnings.append("Optional column not present: ifc_guid")

    if "category" not in columns:
        warnings.append("Optional column not present: category")

    if "source_file" not in columns:
        warnings.append("Optional column not present: source_file")

    status = "fail" if errors else "pass"
    report: dict[str, Any] = {
        "csv_path": str(csv_path),
        "status": status,
        "row_count": len(rows),
        "column_count": len(fieldnames),
        "columns": fieldnames,
        "required_columns": sorted(REQUIRED_COLUMNS),
        "optional_columns_present": present_optional_columns,
        "missing_required_columns": missing_required_columns,
        "missing_element_id_count": len(missing_element_id_rows),
        "duplicate_element_id_count": len(duplicate_element_ids),
        "missing_object_name_count": len(missing_object_name_rows),
        "duplicate_element_ids": duplicate_element_ids,
        "errors": errors,
        "warnings": warnings,
    }

    return report, not errors


def write_report(csv_path: Path, report: dict[str, Any]) -> Path:
    report_path = csv_path.with_name("validation_report.json")
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report_path


def print_summary(report: dict[str, Any], report_path: Path | None) -> None:
    print("BIM mapping validation summary")
    print(f"Status: {report.get('status', 'unknown')}")
    print(f"CSV path: {report.get('csv_path', '')}")
    print(f"Rows: {report.get('row_count', 0)}")
    print(f"Columns: {report.get('column_count', 0)}")
    print(f"Missing element_id: {report.get('missing_element_id_count', 0)}")
    print(f"Duplicate element_id: {report.get('duplicate_element_id_count', 0)}")
    print(f"Missing object_name: {report.get('missing_object_name_count', 0)}")

    for warning in report.get("warnings", []):
        print(f"Warning: {warning}")

    for error in report.get("errors", []):
        print(f"Error: {error}")

    if report_path is not None:
        print(f"Validation report: {report_path}")


def main() -> int:
    args = parse_args()
    csv_path = Path(args.csv_path).resolve()
    report, passed = validate(csv_path)

    report_path: Path | None = None
    if csv_path.exists() and csv_path.is_file():
        report_path = write_report(csv_path, report)

    print_summary(report, report_path)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
