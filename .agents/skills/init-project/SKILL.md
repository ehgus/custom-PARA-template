---
name: init-project
description: Initialize a new structured research project folder inside 1_Projects/ following the BMOL 5-stage project template guidelines.
---

# Init Project Skill

This skill automates the creation of a new research project folder inside `1_Projects/` following the BMOL 5-stage project management specification.

## Project Naming Convention

Directory Name Format: `[Priority]-[Type]-[Project_Name]` (or `[Priority]-Collab-[Type]-[Lead_Person]-[Project_Name]`)

### Naming Rules
1. **Priority Index**:
   * `01-`: Important & Urgent
   * `02-`: Urgent & Not Important
   * `03-`: Important & Not Urgent
   * `04-`: Not Important & Not Urgent
2. **Shared Prefixes (`[Type]`)**:
   * `Paper-`, `Grant-`, `Collab-`, `Research-`, `Lab-`, `Admin-`, `Template-`, `Ref-`, `SOP-`, `Code-`
3. **Delimiter Policy**:
   * **Hyphens (`-`)**: Used exclusively for structural delimiters (priority, prefix, dates).
   * **Underscores (`_`)**: Used **exclusively** for separating words inside `[Project_Name]`.
4. **Examples**: `01-Paper-Bacteria_Review`, `03-Paper-Data_Compression`, `01-Collab-Paper-강융-Ptychographic_Tomography`

---

## Complete Project Directory Blueprint

```text
[Priority]-[Type]-[Project_Name]/
│
├── README.md                           ← Project overview & stage status
│
├── 00-log/                             ← Audit trail & lifecycle logs
│   ├── issues/                         ← Issue log files (OPEN-ISSUE-xxx / CLOSED-ISSUE-xxx)
│   └── decisions/                      ← Research Decision Records (OPEN-RDR-xxx / CLOSED-RDR-xxx)
│
├── 01-background/                      [Stage 0: Idea Exploration] Paper (Zotero), Presentation, Product catalogs
├── 02-discussion/                      [Stage 0: Idea Exploration] Discussion notes in Markdown (link RDR-xxx for decisions)
│
├── 11-blueprint/                       [Stage 1: Equipment / HW & SW Blueprint] Schematics, parts, quotes, SW spec
├── 12-implementation/                  [Stage 1: HW & Implementation] Build process logs & operation instructions
├── 13-code/                            [Stage 1: Software Code & Git] SW version control (git), commit hash links in RDR
│
├── 21-data/                            [Stage 2: Execution & Results]
│   ├── raw/                            ← Read-only raw data (isolated by YYYY-MM-DD/ subfolders)
│   ├── processed/                      ← Processed data & CSV/Plots for visualization
│   └── experimental/                   ← Protocol notes & experimental execution logs
│
├── 31-review/                          [Stage 3: Internal Review & Gate Check]
│   ├── analysis.md                     ← Result interpretation & findings
│   ├── narrative.md                    ← Storytelling direction & core claims
│   └── gate.md                         ← Go / Rollback decision record
│
├── 32-figure/                          [Stage 3: Figure Design]
│   ├── Outline: Claim & figure flow breakdown
│   ├── Subfigures: Individual figure components
│   └── Figure: Final assembled figure panels
│
├── 41-manuscript/                      [Stage 4: External Publication]
│   ├── Manuscript                      ← Main paper text
│   ├── Cover letter                    ← Editor cover letter
│   ├── Supplementary material          ← SI documents & data
│   └── Peer review and response        ← Rebuttal & reviewer response
│
├── 42-presentation/                    [Stage 4: Conference slides & talk materials]
└── 43-patent/                          [Stage 4: Patent applications & filings]
```

---

## 5-Stage Numbering Matrix

| Stage Index | Phase | Description |
|---|---|---|
| `00-` | **Audit Logs** | Issues log (`00-log/issues/`) & Research Decision Records (`00-log/decisions/`) |
| `01-`, `02-` | **Stage 0: Idea Exploration** | Literature background (`01-background/`), discussion notes (`02-discussion/`) |
| `11-`, `12-`, `13-` | **Stage 1: Implementation** | Blueprints (`11-blueprint/`), build logs (`12-implementation/`), code (`13-code/`) |
| `21-` | **Stage 2: Execution** | Raw data (`21-data/raw/YYYY-MM-DD/`), processed data, experimental protocols |
| `31-`, `32-` | **Stage 3: Internal Review** | Analysis (`31-review/`), figure outlines & panels (`32-figure/`), Go/Rollback gate |
| `41-`, `42-`, `43-` | **Stage 4: Publication** | Manuscripts (`41-manuscript/`), slides (`42-presentation/`), patents (`43-patent/`) |

---

## 00-log File Naming & Templates

### File Status Matrix
| Status | Issue Log | Research Decision Record (RDR) |
|---|---|---|
| In Progress | `OPEN-ISSUE-001-[Title].md` | `OPEN-RDR-001-[Title].md` |
| Resolved / Closed | `CLOSED-ISSUE-001-[Title].md` | `CLOSED-RDR-001-[Title].md` |

* When resolved, rename `OPEN-` to `CLOSED-` (keep file contents).
* Sequential numbers are incremented independently for Issues and RDRs.

### 1. Issue Template (`OPEN-ISSUE-001-[Title].md`)
```markdown
# ISSUE-001: [Title]

- **Status**: Open | In Progress | Resolved | WontFix
- **Priority**: High | Medium | Low
- **Date**: YYYY-MM-DD
- **Stage**: 11-blueprint | 12-implementation | 13-code | 21-data | ...

## Problem Description

## Reproduction Steps / Environment
- Script/Protocol:
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

### 2. Decision Template (`OPEN-RDR-001-[Title].md`)
```markdown
# RDR-001: [Title]

- **Status**: Proposed | Accepted | Superseded
- **Date**: YYYY-MM-DD
- **Related Stage**: 13-code | 11-blueprint | ...
- **Related Commit**: (Git commit hash, e.g. `abc1234`)

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

## Starter Files to Create on Init

### `README.md`
```markdown
# [Priority]-[Type]-[Project_Name]

- **Created Date**: YYYY-MM-DD
- **Current Stage**: Stage 0 (Idea Exploration)
- **Primary Goal**: [Short description of project goal]

## Quick Links & Index
- **Audit Logs**: [00-log/](00-log/)
- **Background**: [01-background/](01-background/)
- **Review & Gate**: [31-review/gate.md](31-review/gate.md)
```

### `31-review/analysis.md`
```markdown
# Analysis & Findings

- **Date**: YYYY-MM-DD
- **Key Findings**:
- **Data References**: `21-data/processed/`
```

### `31-review/narrative.md`
```markdown
# Narrative & Storytelling Direction

- **Target Audience / Journal**:
- **Main Takeaway (Core Claim)**:
- **Key Figures Flow**:
```

### `31-review/gate.md`
```markdown
# Stage 3 Gate Review (Go / Rollback Decision)

- **Status**: Pending
- **Decision Date**:
- **Verdict**: [ ] Go (Proceed to Stage 4) | [ ] Rollback (Return to Stage 0/1/2)
- **Linked RDR**:
```

---

## Project Workflows

### Issue & Solution Extraction Workflow
1. When a problem arises, create `OPEN-ISSUE-xxx` or `OPEN-RDR-xxx` in `00-log/`.
2. Resolve issue and rename `OPEN-` to `CLOSED-`.
3. **Extraction Check**: If the solution is reusable across future lab projects, extract it to `3_Resources/SOP-` or `3_Resources/Code-`.

### Go / Rollback Gate Workflow
1. Complete `31-review/analysis.md` (results) and `31-review/narrative.md` (storyline).
2. Evaluate `31-review/gate.md`:
   * **Go**: Advance to `32-figure/` and Stage 4 (`41-manuscript/`).
   * **Rollback**: Return to Stage 0 (`01-background/`), Stage 1 (`11-blueprint/`), or Stage 2 (`21-data/raw/YYYY-MM-DD/`). Log an RDR (`OPEN-RDR-xxx-Gate-[Reason].md`).
