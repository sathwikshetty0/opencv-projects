from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS = ROOT / "requirements.txt"


def load_requirements(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def main() -> int:
    if not REQUIREMENTS.exists():
        print(f"Missing requirements file: {REQUIREMENTS}")
        return 1

    packages = load_requirements(REQUIREMENTS)
    missing = []
    for package in packages:
        package_name = package.split("==")[0].split(">=")[0].split("<=")[0].strip()
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            missing.append(package)

    if missing:
        print("Missing installed packages:")
        for package in missing:
            print(f"  - {package}")
        print("\nInstall dependencies with: pip install -r requirements.txt")
        return 1

    print("All required packages are installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
