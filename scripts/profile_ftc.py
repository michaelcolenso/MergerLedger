#!/usr/bin/env python3
"""Profile an acquired FTC snapshot without assuming a schema."""

from __future__ import annotations

import csv
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]


def inspect_csv(path: pathlib.Path) -> dict:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        rows = list(reader)

    profile = {
        "path": str(path.relative_to(ROOT)),
        "row_count": len(rows),
        "columns": fields,
        "column_count": len(fields),
        "null_counts": {},
        "distinct_counts": {},
        "examples": {},
    }
    for field in fields:
        values = [(row.get(field) or "").strip() for row in rows]
        nonempty = [v for v in values if v]
        profile["null_counts"][field] = len(values) - len(nonempty)
        profile["distinct_counts"][field] = len(set(nonempty))
        profile["examples"][field] = [v for v, _ in Counter(nonempty).most_common(5)]
    return profile


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python scripts/profile_ftc.py data/raw/<timestamp>")
    snapshot = ROOT / sys.argv[1]
    output = {
        "merger_actions": inspect_csv(snapshot / "merger_actions.csv"),
        "dictionary": inspect_csv(snapshot / "dictionary.csv"),
    }
    out_path = snapshot / "profile.json"
    out_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
