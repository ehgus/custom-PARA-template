#!/usr/bin/env python3
"""
Validates that top-level directories directly under 1_Projects, 2_Areas, and 3_Resources
adhere strictly to PARA naming rules.
"""

import re
import sys
from pathlib import Path

# In Python \w matches alphanumeric characters and underscores across Unicode scripts (including Korean)
CATEGORIES = {
    "1_Projects": re.compile(r"^0[1-4]-([\w]+-)*[\w]+$"),
    "2_Areas": re.compile(r"^(?!0[1-4]-)([\w]+-)+[\w]+$"),
    "3_Resources": re.compile(r"^(?!0[1-4]-)([\w]+-)+[\w]+$"),
}


def main():
    script_dir = Path(__file__).resolve().parent
    workspace_root = script_dir.parents[2]

    validation_errors = []
    target_args = [Path(arg).resolve() for arg in sys.argv[1:]]

    for cat, pattern in CATEGORIES.items():
        cat_path = workspace_root / cat
        if not cat_path.is_dir():
            continue

        for item in sorted(cat_path.iterdir()):
            if not item.is_dir() or item.name.startswith("."):
                continue

            if target_args and item.resolve() not in target_args:
                continue

            name_to_check = item.name

            if " " in name_to_check:
                validation_errors.append(
                    f"[{cat}] '{name_to_check}' contains spaces. Spaces are forbidden; use underscores (_)."
                )
                continue

            if not pattern.match(name_to_check):
                validation_errors.append(
                    f"[{cat}] '{name_to_check}' violates naming structure rules. Check strict delimiter rules (hyphens for tags, underscores for spaces)."
                )

    if validation_errors:
        print("PARA Structure Validation Failed!", file=sys.stderr)
        for err in validation_errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    else:
        print("PARA Structure Validation Passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
