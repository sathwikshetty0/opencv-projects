from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    python_files = sorted(p.name for p in ROOT.glob("*.py") if p.is_file())
    print(f"Found {len(python_files)} demo and utility Python files:\n")
    for path in python_files:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
