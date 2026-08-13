---
name: init-para-project
description: Initialize or verify the top-level PARA framework folder structure (1_Projects, 2_Areas, 3_Resources, 4_Archives) and workspace AGENTS.md guidelines.
---

# Init PARA Project Skill

This skill initializes or verifies the top-level **PARA Method** directory structure for the BMOL workspace according to [`AGENTS.md`](../../AGENTS.md).

## When to Use
- Setting up a new BMOL research workspace.
- Verifying that all core PARA folders (`1_Projects/`, `2_Areas/`, `3_Resources/`, `4_Archives/`) exist.

## Procedure

### 1. Verify Top-Level Directory Structure
Ensure the following directories exist at the workspace root (`c:\Users\labdo\Desktop\BMOL`):
- `1_Projects/`: Short-term research & tasks with clear goals and deadlines.
- `2_Areas/`: Long-term responsibilities & main research topics.
- `3_Resources/`: Reusable knowledge, code snippets, references, protocols, and templates.
- `4_Archives/`: Completed or inactive items.

### 2. Verify Archives Subdirectories
Ensure `4_Archives/` mirrors the top-level P/A/R structure:
- `4_Archives/1_Projects/`
- `4_Archives/2_Areas/`
- `4_Archives/3_Resources/`

### 3. Verify AGENTS.md Guidelines
Check that `AGENTS.md` is present at the workspace root. If missing, generate it with the BMOL PARA guidelines (priorities `01-`~`04-`, shared prefixes `Paper-`, `Grant-`, `Collab-`, hyphen/underscore naming rules, and ISO quarter date formatting `YYYY-Q[1-4]-` for archived items).
