---
name: validate-para-structure
description: Validates that top-level directories directly under 1_Projects, 2_Areas, and 3_Resources adhere strictly to PARA naming rules. Do NOT invoke for internal project files or subdirectories.
---
# validate-para-structure
Usage: `.\validate.ps1`
Scans the top-level PARA directories directly under `1_Projects/`, `2_Areas/`, and `3_Resources/`. Exits with > 0 if any structural delimiter rules or priority index rules are violated.
Note: Do NOT execute this skill for internal project files or internal subdirectories.
