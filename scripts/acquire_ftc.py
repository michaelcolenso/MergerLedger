#!/usr/bin/env python3
"""Acquire and preserve the official FTC Merger Enforcement Actions sources.

Writes timestamped immutable source snapshots plus SHA-256 hashes. This script
intentionally performs no normalization; M0 begins by inspecting the real FTC
fields and dictionary before designing the normalized schema.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import urllib.request
from datetime import datetime, timezone

SOURCES = {
    "merger_actions": "https://search.ftc.gov/system/files/ftc_gov/data/FTC-Merger-Enforcement-Actions.csv",
    "dictionary": "https://search.ftc.gov/system/files/ftc_gov/data/FTC-Merger-Enforcement-Actions-dictionary.csv",
}

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "MergerLedger/0.1 research"})
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    snapshot = RAW / stamp
    snapshot.mkdir(parents=True, exist_ok=False)

    manifest = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sources": [],
    }

    for name, url in SOURCES.items():
        payload = fetch(url)
        filename = f"{name}.csv"
        path = snapshot / filename
        path.write_bytes(payload)
        manifest["sources"].append(
            {
                "name": name,
                "url": url,
                "path": str(path.relative_to(ROOT)),
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )

    (snapshot / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
