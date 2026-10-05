#!/usr/bin/env python3
"""
Archives a specified project, area, or resource folder into the 4_Archives directory
with proper ISO quarter prefixing (YYYY-Q[1-4]-).
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Archive a PARA item to 4_Archives with ISO quarter prefix."
    )
    parser.add_argument("target_path", help="Path to the item to archive")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    workspace_root = script_dir.parents[2]

    target = Path(args.target_path)
    if not target.is_absolute():
        target = (Path.cwd() / target).resolve()
    else:
        target = target.resolve()

    if not target.exists():
        print(f"Error: Target path does not exist: {target}", file=sys.stderr)
        sys.exit(1)

    try:
        rel_path = target.relative_to(workspace_root)
    except ValueError:
        print(
            f"Error: Target must be inside the workspace root: {workspace_root}",
            file=sys.stderr,
        )
        sys.exit(1)

    parts = rel_path.parts
    if len(parts) != 2 or parts[0] not in {"1_Projects", "2_Areas", "3_Resources"}:
        print(
            f"Error: Target must be a direct child of 1_Projects, 2_Areas, or 3_Resources. Got: {rel_path.as_posix()}",
            file=sys.stderr,
        )
        sys.exit(1)

    category = parts[0]
    item_name = parts[1]

    now = datetime.now()
    quarter = (now.month - 1) // 3 + 1
    prefix = f"{now.year}-Q{quarter}-"
    new_item_name = prefix + item_name

    archive_dir = workspace_root / "4_Archives" / category
    archive_dir.mkdir(parents=True, exist_ok=True)

    new_path = archive_dir / new_item_name
    if new_path.exists():
        print(f"Error: Destination already exists: {new_path}", file=sys.stderr)
        sys.exit(1)

    try:
        shutil.move(str(target), str(new_path))
        print(f"Successfully archived '{item_name}' to '{new_path}'")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to move: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
