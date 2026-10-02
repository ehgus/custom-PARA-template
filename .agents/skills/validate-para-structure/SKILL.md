---
name: validate-para-structure
description: Validates that top-level directories directly under 1_Projects, 2_Areas, and 3_Resources adhere strictly to PARA naming rules. Supports workspace-wide or target-specific directory validation.
---
# validate-para-structure

## 1. Usage

- **Workspace-wide Scan**:
  ```bash
  python ./.agents/skills/validate-para-structure/validate.py
  ```
  Scans all top-level directories directly under `1_Projects/`, `2_Areas/`, and `3_Resources/`. System hidden directories (starting with `.`) are ignored automatically. Exits with code > 0 if any structural violations exist.

- **Targeted Directory Validation**:
  ```bash
  python ./.agents/skills/validate-para-structure/validate.py <path-to-target-directory>
  ```
  Example:
  ```bash
  python ./.agents/skills/validate-para-structure/validate.py 3_Resources/SOP-Spec_Driven_Coding
  ```
  Validates only the specified top-level directory against its respective category rule.

## 2. Operational Rules

1. **Targeted Validation Priority**: When creating, renaming, or moving a specific top-level directory under `1_Projects/`, `2_Areas/`, or `3_Resources/`, agents SHOULD pass the target directory path as an argument to validate only that item without being blocked by unrelated or legacy folders.
2. **Internal Files Exemption**: Agents MUST NOT execute this skill for internal project files, subdirectories, or modifications within existing items.
