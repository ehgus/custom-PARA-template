---
name: init-project
description: Initialize a new structured project folder inside 1_Projects/ following the general 5-stage project template guidelines.
---

# Init Project Skill

This skill automates the creation of a new project folder inside `1_Projects/` following the general 5-stage project management specification.

## Project Naming Convention

Directory Name Format: `[Priority]-[Type]-[Project_Name]` (or `[Priority]-Collab-[Type]-[Lead_Person]-[Project_Name]`)

### Naming Rules
1. **Priority Index**:
   * `01-`: Important & Urgent
   * `02-`: Urgent & Not Important
   * `03-`: Important & Not Urgent
   * `04-`: Not Important & Not Urgent
2. **Shared Prefixes (`[Type]`)**:
   * `Paper-`, `Grant-`, `Collab-`, `Domain-`, `Ops-`, `Admin-`, `Template-`, `Ref-`, `SOP-`, `Code-`
3. **Delimiter Policy**:
   * **Hyphens (`-`)**: Used exclusively for structural delimiters (priority, prefix, dates).
   * **Underscores (`_`)**: Used **exclusively** for separating words inside `[Project_Name]`.
4. **Examples**: `01-Project-Website_Redesign`, `03-Task-Q3_Report`, `01-Collab-Project-Alex-New_Campaign`

---

## Complete Project Directory Blueprint

```text
[Priority]-[Type]-[Project_Name]/
│
├── README.md                           ← Project overview & stage status
│
├── 00-log/                             ← Audit trail & lifecycle logs (Managed by init-log skill)
│   ├── issues/                         ← Issue log files (OPEN-ISSUE-xxx / CLOSED-ISSUE-xxx)
│   └── decisions/                      ← Decision Records (OPEN-DR-xxx / CLOSED-DR-xxx)
│
├── 01-planning/                        [Stage 0: Project Planning & Proposal]
│   ├── objective.md                    ← North Star, WHAT, WHY (Gap, Impact, Stake)
│   └── strategy.md                     ← HOW (Strategy, Risks & Plan B, Pivot Criteria)
│
├── 02-background/                      [Stage 0: Idea Exploration] References, notes, resources
├── 03-discussion/                      [Stage 0: Idea Exploration] Discussion notes in Markdown
│
├── 11-blueprint/                       [Stage 1: Design & Blueprint] Specifications, designs, architecture
├── 12-implementation/                  [Stage 1: Development] Execution logs & operation instructions
├── 13-code/                            [Stage 1: Software Code & Git] Version control (git)
│
├── 21-data/                            [Stage 2: Execution & Results]
│   ├── raw/                            ← Read-only raw data or inputs
│   ├── processed/                      ← Processed outputs & visualizations
│   └── execution/                      ← Execution logs and workflow notes
│
├── 31-review/                          [Stage 3: Internal Review & Gate Check]
│   ├── analysis.md                     ← Result interpretation & findings
│   └── gate.md                         ← Delivery direction & Go / Rollback gate decision record
│
├── 32-deliverables/                    [Stage 3: Deliverables Design]
│   ├── Drafts                          ← Draft components
│   └── Final                           ← Final assembled assets
│
├── 41-finalization/                    [Stage 4: Delivery & Finalization]
│   ├── Report                          ← Final reports and documentation
│   └── Handoff                         ← Client or team handoff materials
│
└── 42-presentation/                    [Stage 4: Presentation & slide materials]
```

---

## 5-Stage Numbering Matrix

| Stage Index | Phase | Description |
|---|---|---|
| `00-` | **Audit Logs** | Issues log (`00-log/issues/`) & Decision Records (`00-log/decisions/`) — Delegated to `init-log` skill |
| `01-`, `02-`, `03-` | **Stage 0: Planning** | Objectives (`01-planning/`), background (`02-background/`), discussion notes (`03-discussion/`) |
| `11-`, `12-`, `13-` | **Stage 1: Design** | Blueprints (`11-blueprint/`), development (`12-implementation/`), code (`13-code/`) |
| `21-` | **Stage 2: Execution** | Raw data/inputs (`21-data/raw/`), processed data, execution logs |
| `31-`, `32-` | **Stage 3: Review** | Analysis (`31-review/`), deliverables (`32-deliverables/`), Go/Rollback gate |
| `41-`, `42-` | **Stage 4: Delivery** | Finalization (`41-finalization/`), slides (`42-presentation/`) |

---

## 00-log Initialization & Templates (Delegated to `init-log`)

The `00-log/` audit trail directory (`issues/` and `decisions/`), file naming conventions, status matrices (`OPEN-` / `CLOSED-`), and templates (`OPEN-ISSUE-xxx`, `OPEN-DR-xxx`) are standardized and managed by the dedicated **`init-log`** skill.

- **Initialization**: Use the [`init-log`](../init-log/SKILL.md) skill to set up `00-log/issues/` and `00-log/decisions/` (along with `.gitkeep` files) within the project root via native file operations.
- **Templates & Rules**: Refer to the [`init-log`](../init-log/SKILL.md) skill documentation for:
  - Issue Template (`OPEN-ISSUE-001-[Title].md`)
  - Decision Record (DR) Template (`OPEN-DR-001-[Title].md`)
  - Status transitions (`OPEN-` to `CLOSED-`)
  - Cross-PARA resource extraction workflows


---

## Starter Files to Create on Init

### `README.md`
```markdown
# [Priority]-[Type]-[Project_Name]

# 1. Summary

- Goal: [Short description of project goal]
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
# 3. Background & Related Work

- 

# 4. Execution Log

[YYYY.MM.DD]
- 

# 5. Discussion Log

[YYYY.MM.DD]
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
```

### `01-planning/objective.md`
```markdown
# Project Objective & Rationale (WHY)

## 1. North Star (Core Objective)
- **One-Sentence Claim**: [Single sentence defining the ultimate objective]

## 2. WHAT
- **Core Goal**: [Clear description of what will be established]

## 3. WHY - Rationale & Value
- **Business/Task Gap**: [Unresolved gap or problem]
- **Practical Impact**: [Who can do what differently if successful?]
- **Why Now**: [Why is this possible/necessary now?]
- **Why Us/Me**: [Why are we uniquely equipped to solve this?]
```

### `01-planning/strategy.md`
```markdown
# Execution Strategy & Risk Mitigation (HOW)

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
```

### `31-review/analysis.md`
```markdown
# Analysis & Findings

- **Date**: YYYY-MM-DD
- **Key Findings**:
- **Data/Assets References**: `21-data/processed/`
```

### `31-review/gate.md`
```markdown
# Stage 3 Gate Review (Go / Rollback Decision)

- **Status**: Pending
- **Decision Date**: YYYY-MM-DD
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
```

---

## Project Workflows

### Issue & Solution Extraction Workflow
1. When a problem or decision arises, initialize/use `00-log/` via the [`init-log`](../init-log/SKILL.md) skill and create `OPEN-ISSUE-xxx` or `OPEN-DR-xxx`.
2. Resolve issue and rename `OPEN-` to `CLOSED-` according to `init-log` lifecycle rules.
3. **Extraction Check**: If the solution is reusable across future projects, extract it to `3_Resources/SOP-` or `3_Resources/Code-`.

### Go / Rollback Gate Workflow
1. Complete `31-review/analysis.md` (results) and define delivery direction in `31-review/gate.md`.
2. Evaluate `31-review/gate.md` for final Go / Rollback decision:
   * **Go**: Advance to `32-deliverables/` and Stage 4 (`41-finalization/`).
   * **Rollback**: Return to Stage 0 (`01-planning/`), Stage 1 (`11-blueprint/`), or Stage 2 (`21-data/raw/`). Log a Decision Record (`OPEN-DR-xxx-Gate-[Reason].md`).
