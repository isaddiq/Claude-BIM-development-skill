# Python IfcOpenShell Extraction

```python
import csv
import json
from pathlib import Path

import ifcopenshell
import ifcopenshell.util.element


def extract_ifc_metadata(ifc_path: str) -> list[dict]:
    model = ifcopenshell.open(ifc_path)
    rows: list[dict] = []

    for element in model.by_type("IfcElement"):
        property_sets = ifcopenshell.util.element.get_psets(element)
        rows.append(
            {
                "global_id": getattr(element, "GlobalId", ""),
                "name": getattr(element, "Name", ""),
                "type": element.is_a(),
                "property_sets": property_sets,
            }
        )

    return rows


def write_json(rows: list[dict], output_path: str) -> None:
    Path(output_path).write_text(json.dumps(rows, indent=2), encoding="utf-8")


def write_csv(rows: list[dict], output_path: str) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["global_id", "name", "type"])
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "global_id": row["global_id"],
                    "name": row["name"],
                    "type": row["type"],
                }
            )


if __name__ == "__main__":
    metadata = extract_ifc_metadata("model.ifc")
    write_json(metadata, "ifc_metadata.json")
    write_csv(metadata, "ifc_metadata.csv")

    # Geometry extraction should be validated separately from metadata extraction.
```
