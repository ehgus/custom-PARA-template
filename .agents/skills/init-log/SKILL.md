---
name: init-log
description: Initialize and manage the 00-log audit trail and lifecycle log directory (issues and decision records) inside any PARA project, area, or resource item.
---

# Init Log Skill

This skill initializes and manages the `00-log/` audit trail and lifecycle log structure across all PARA folders (`1_Projects/`, `2_Areas/`, and `3_Resources/`).

## When to Use
- Initializing the audit log structure (`00-log/`) when creating or updating any Project, Area, or Resource item.
- Logging and tracking problems, bugs, or operational hurdles using Issue documents (`issues/`).
- Documenting architectural, operational, or design choices using Decision Records (`decisions/`).
- Managing issue and decision lifecycles across projects and ongoing responsibilities.

---

## Directory Blueprint

Inside any project, area, or resource root directory:

```text
[Target_Folder]/
└── 00-log/
    ├── issues/                         ← Issue tracking files (OPEN-ISSUE-xxx / CLOSED-ISSUE-xxx)
    └── decisions/                      ← Decision Records (OPEN-DR-xxx / CLOSED-DR-xxx)
```

---

## Log File Naming & Status Conventions

### File Status Matrix
| Status | Issue Log | Decision Record (DR) |
|---|---|---|
| In Progress / Open | `OPEN-ISSUE-001-[Title].md` | `OPEN-DR-001-[Title].md` |
| Resolved / Closed | `CLOSED-ISSUE-001-[Title].md` | `CLOSED-DR-001-[Title].md` |

- **Sequential Numbering**: Sequential 3-digit numbers (`001`, `002`, ...) incremented independently for Issues and DRs.
- **Status Transition**: When an issue or decision is resolved or accepted, rename the prefix from `OPEN-` to `CLOSED-` (keep file contents and history intact).
- **Delimiters**: Use hyphens (`-`) for structural tag separators and underscores (`_`) for multi-word titles.

---

## Templates

### 1. Issue Template (`OPEN-ISSUE-001-[Title].md`)

```markdown
# ISSUE-001: [Title]

- **Status**: Open | In Progress | Resolved | WontFix
- **Priority**: High | Medium | Low
- **Date**: YYYY-MM-DD
- **Target/Scope**: [Stage / Area Domain / Resource Name]

## Problem Description

## Reproduction Steps / Environment
- Component/Context:
- Parameters/Inputs:
- Error Log:

## Investigation Steps
- [ ] Hypothesis 1:
- [ ] Hypothesis 2:

## Solution & Resolution (Fill upon completion)
- Root Cause:
- Fix:
- Extracted Resource: → `3_Resources/...` (if reusable)
```

### 2. Decision Template (`OPEN-DR-001-[Title].md`)

```markdown
# DR-001: [Title]

- **Status**: Proposed | Accepted | Superseded
- **Date**: YYYY-MM-DD
- **Related Scope**: [Project Stage / Area Responsibility / Resource]

## Context & Problem Statement

## Decision

## Options Considered

| Option | Pros | Cons |
|---|---|---|
| Option A | | |
| Option B | | |

## Consequences & Trade-offs
```

---

## Contextual Usage Across PARA

### 1. `1_Projects/`
- Track technical blockers, experiment hurdles, and bug reproductions across stages (`01-planning`, `11-blueprint`, `12-implementation`, `13-code`, `21-data`, etc.).
- Record architecture, algorithm choices, or stage gate decisions.

### 2. `2_Areas/`
- Track long-term operational issues, server maintenance, equipment failures, lab chores, and account administration blockers.
- Document recurring policy changes, vendor choices, or infrastructure upgrades.

### 3. `3_Resources/`
- Track documentation revisions, template updates, library dependency breaks, or snippet enhancements.
- Document reasons for modifying shared reference standards or deprecating code modules.

---

## Lifecycle Workflows

### Issue Tracking & Resource Extraction
1. **Open**: When a problem, anomaly, or blocker arises, create `OPEN-ISSUE-xxx-[Title].md` inside `00-log/issues/`.
2. **Investigate & Resolve**: Fill out investigation hypotheses and findings. Implement the fix and record root cause.
3. **Close**: Rename `OPEN-ISSUE-xxx` to `CLOSED-ISSUE-xxx`.
4. **Cross-PARA Extraction**: If the solution, protocol, or code fix is reusable across future projects or areas, extract it into the appropriate folder under `3_Resources/` (e.g., `3_Resources/SOP-` or `3_Resources/Code-`).

### Decision Recording
1. **Propose**: When deciding between multiple architectural or operational alternatives, create `OPEN-DR-xxx-[Title].md` inside `00-log/decisions/`.
2. **Review & Conclude**: Document options considered with trade-offs. Record the final consensus decision.
3. **Close / Adopt**: Rename `OPEN-DR-xxx` to `CLOSED-DR-xxx`.

## Target Validation Laws

Before initializing `00-log/` in a target directory, the agent must verify the following constraints:

1. **Existence**: The target directory must exist.
2. **Workspace Confinement**: The target must be located within the current workspace root (`c:\Users\labdo\Desktop\BMOL`).
3. **PARA Placement**: The target must be a direct root item inside one of the three active PARA categories:
   - `1_Projects/[Item_Name]/`
   - `2_Areas/[Item_Name]/`
   - `3_Resources/[Item_Name]/`
   *(Targeting the workspace root itself or nested subdirectories outside the item root is forbidden).*
4. **Shortcut Resolution**: If the target is a `.lnk` Windows shortcut, resolve the actual target path before proceeding.

---

## Agent Initialization Procedure

1. **Inspect Target**: Verify its existence and check whether `00-log/issues/` or `00-log/decisions/` already exist.
2. **Create Directories**: If `00-log/issues/` or `00-log/decisions/` do not exist, create each directory.

---
