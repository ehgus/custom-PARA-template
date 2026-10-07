#!/usr/bin/env python3
"""
Initializes a new structured project folder inside 1_Projects/
following the general 5-stage project template guidelines.
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

PROJECT_NAME_PATTERN = re.compile(r"^0[1-4]-([\w]+-)*[\w]+$")

DIRECTORIES = [
    "00-log/issues",
    "00-log/decisions",
    "01-planning",
    "02-resource",
    "03-discussion",
    "11-blueprint",
    "12-implementation",
    "13-code",
    "21-data/raw",
    "21-data/processed",
    "21-data/execution",
    "31-review",
    "32-deliverables/Drafts",
    "32-deliverables/Final",
    "41-finalization/Report",
    "41-finalization/Handoff",
    "42-presentation",
]


def generate_readme(project_name: str, today_dot: str, goal: str = "") -> str:
    goal_text = goal if goal else "[Short description of project goal]"
    return f"""# {project_name}

# 1. Summary

- Goal: {goal_text}
- Key result so far: 
- Next milestone: 

# 2. Objective

## 2.1 What

## 2.2 Why
- scientific gap:
- practical impact:
- why now:
- why us:
- personal stake:
## 2.3 How
- strategy
- key technical risk
- Kill / Pivot criteria
# 3. Resource

- 

# 4. Execution Log

[{today_dot}]
- 

# 5. Discussion Log

[{today_dot}]
- 

# 6. Current Results

- 

# 7. Future work

- 

# 8. Quick Links & Index
- **Planning & Objective**: [01-planning/objective.md](01-planning/objective.md)
- **Audit Logs**: [00-log/](00-log/)
- **Code/Implementation**: [13-code/](13-code/)
- **Data/Inputs**: [21-data/](21-data/)
- **Review & Gate**: [31-review/gate.md](31-review/gate.md)
"""


def generate_objective() -> str:
    return """# Project Objective & Rationale (WHY)

## 1. North Star (Core Objective)
- **One-Sentence Claim**: [Single sentence defining the ultimate objective]

## 2. WHAT
- **Core Goal**: [Clear description of what will be established]

## 3. WHY - Rationale & Value
- **Business/Task Gap**: [Unresolved gap or problem]
- **Practical Impact**: [Who can do what differently if successful?]
- **Why Now**: [Why is this possible/necessary now?]
- **Why Us/Me**: [Why are we uniquely equipped to solve this?]
"""


def generate_strategy() -> str:
    return """# Execution Strategy & Risk Mitigation (HOW)

## 1. Strategy
- 1. [Phase 1 strategy & key approach]
- 2. [Phase 2 execution]
- 3. [Phase 3 validation & finalization]

## 2. Risks & Mitigation Plan
| Risk Description | Severity | Mitigation / Plan B |
|---|---|---|
| Risk 1: [Description] | High | Plan B: [Alternative] |
| Risk 2: [Description] | Medium | Plan B: [Alternative] |

## 3. Kill / Pivot Criteria
- **Criterion 1**: [Specific metric/event where project should be killed or pivoted]
- **Criterion 2**: [Time limit if no progress seen within X timeframe]
"""


def generate_analysis(today_iso: str) -> str:
    return f"""# Analysis & Findings

- **Date**: {today_iso}
- **Key Findings**:
- **Data/Assets References**: `21-data/processed/`
"""


def generate_gate(today_iso: str) -> str:
    return f"""# Stage 3 Gate Review (Go / Rollback Decision)

- **Status**: Pending
- **Decision Date**: {today_iso}
- **Verdict**: [ ] Go (Proceed to Stage 4) | [ ] Rollback (Return to Stage 0/1/2)
- **Linked DR**:

## 1. Delivery Direction
- **Target Audience / Stakeholder**:
- **Main Takeaway**:
- **Key Deliverables Flow**:

## 2. Gate Decision & Justification
- **Key Findings Summary**: (Refer to `31-review/analysis.md`)
- **Action Plan**:
  - If Go: Advance to `32-deliverables/` and Stage 4 (`41-finalization/`).
  - If Rollback: Target Stage (`01-planning/`, `11-blueprint/`, `21-data/`) and reason.
"""


def validate_project_name(name: str) -> None:
    if " " in name:
        raise ValueError(f"Project name '{name}' contains spaces. Spaces are forbidden; use underscores (_).")
    if not PROJECT_NAME_PATTERN.match(name):
        raise ValueError(
            f"Project name '{name}' violates PARA naming rules. "
            "Must start with priority '01-', '02-', '03-', or '04-', followed by prefix and name "
            "(e.g., '01-Paper-Sample_Project', '02-Collab-Grant-John-NRF_2026')."
        )


def init_project(project_name_or_path: str, goal: str = "", dry_run: bool = False) -> Path:
    script_dir = Path(__file__).resolve().parent
    workspace_root = script_dir.parents[2]
    projects_dir = workspace_root / "1_Projects"

    input_path = Path(project_name_or_path)

    # Determine project name and destination path
    if input_path.is_absolute():
        target_path = input_path.resolve()
        try:
            rel = target_path.relative_to(projects_dir)
            if len(rel.parts) != 1:
                raise ValueError(f"Target path must be a direct child of 1_Projects: {target_path}")
            project_name = rel.name
        except ValueError:
            raise ValueError(f"Absolute path must be directly inside {projects_dir}: {target_path}")
    else:
        # Check if user passed "1_Projects/name" or just "name"
        parts = input_path.parts
        if len(parts) == 2 and parts[0] == "1_Projects":
            project_name = parts[1]
        elif len(parts) == 1:
            project_name = parts[0]
        else:
            raise ValueError(
                f"Invalid project path '{project_name_or_path}'. Expected project name or '1_Projects/<name>'."
            )
        target_path = projects_dir / project_name

    validate_project_name(project_name)

    if target_path.exists():
        raise FileExistsError(f"Target project directory already exists: {target_path}")

    now = datetime.now()
    today_dot = now.strftime("%Y.%m.%d")
    today_iso = now.strftime("%Y-%m-%d")

    starter_files = {
        "README.md": generate_readme(project_name, today_dot, goal),
        "01-planning/objective.md": generate_objective(),
        "01-planning/strategy.md": generate_strategy(),
        "31-review/analysis.md": generate_analysis(today_iso),
        "31-review/gate.md": generate_gate(today_iso),
    }

    if dry_run:
        print(f"[DRY-RUN] Target directory: {target_path}")
        print(f"[DRY-RUN] Would create {len(DIRECTORIES)} directories:")
        for rel_dir in DIRECTORIES:
            print(f"  + {target_path / rel_dir}")
        print(f"[DRY-RUN] Would create {len(starter_files)} starter files:")
        for rel_file in starter_files:
            print(f"  * {target_path / rel_file}")
        return target_path

    # Create root and subdirectories
    target_path.mkdir(parents=True, exist_ok=False)
    for rel_dir in DIRECTORIES:
        (target_path / rel_dir).mkdir(parents=True, exist_ok=True)

    # Create starter files
    for rel_file, content in starter_files.items():
        file_path = target_path / rel_file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

    return target_path


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a structured 5-stage PARA project inside 1_Projects/."
    )
    parser.add_argument(
        "project_name",
        help="Project folder name (e.g. 01-Paper-Cell_Migration) or relative path (1_Projects/01-Paper-Cell_Migration)",
    )
    parser.add_argument(
        "--goal",
        default="",
        help="Optional short description of the project goal to populate in README.md",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate initialization without creating files or directories",
    )

    args = parser.parse_args()

    try:
        target_path = init_project(args.project_name, goal=args.goal, dry_run=args.dry_run)
        if args.dry_run:
            print(f"\nDry-run completed successfully for '{target_path.name}'.")
        else:
            print(f"Successfully initialized project at '{target_path}'.")
            print("Created directories:")
            for d in DIRECTORIES:
                print(f"  + {d}")
            print("Created starter files:")
            print("  * README.md")
            print("  * 01-planning/objective.md")
            print("  * 01-planning/strategy.md")
            print("  * 31-review/analysis.md")
            print("  * 31-review/gate.md")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
