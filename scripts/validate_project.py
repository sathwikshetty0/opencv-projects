from __future__ import annotations

import ast
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

KNOWN_PACKAGES = {
    "cv2",
    "cvzone",
    "mediapipe",
    "numpy",
    "pyautogui",
    "pynput",
    "requests",
    "scipy",
    "ultralytics",
}


def main() -> int:
    python_files = sorted(p for p in ROOT.glob("*.py") if p.is_file())
    errors = []
    for path in python_files:
        try:
            source = path.read_text(encoding="utf-8", errors="ignore")
            ast.parse(source, filename=str(path))
        except SyntaxError as exc:
            errors.append((path, exc))

    bad_filenames = [path for path in python_files if " " in path.name]

    print(f"Checked {len(python_files)} Python files.")
    if bad_filenames:
        print("\nFiles with spaces in the filename:")
        for path in bad_filenames:
            print(f"  - {path.name}")
    if errors:
        print("\nSyntax errors detected:")
        for path, exc in errors:
            print(f"  - {path.name}: {exc}")

    if not errors and not bad_filenames:
        print("\nValidation complete: no syntax issues or unsafe file names found.")
        return 0

    print("\nPlease fix the issues above before committing.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
