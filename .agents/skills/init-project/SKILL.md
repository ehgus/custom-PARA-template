---
name: init-project
description: Initialize a new structured project folder inside 1_Projects/ following the general 5-stage project template guidelines.
---

# Init Project Skill

Automates the creation of a 5-stage project folder inside `1_Projects/` following the general project management specification.

## 1. Usage

Agents MUST execute `init_project.py` to initialize project folders:

```bash
python ./.agents/skills/init-project/init_project.py <project_name> [--goal "<goal>"] [--dry-run]
```

### Examples
- Standard Project:
  ```bash
  python ./.agents/skills/init-project/init_project.py 01-Paper-Cell_Migration
  ```
- Collaboration Project with Goal:
  ```bash
  python ./.agents/skills/init-project/init_project.py 02-Collab-Grant-John-NRF_2026 --goal "Joint grant proposal for NRF 2026"
  ```
- Simulation / Dry Run:
  ```bash
  python ./.agents/skills/init-project/init_project.py 01-Paper-Cell_Migration --dry-run
  ```

### Script Execution Guarantees
1. **Naming Validation**: Enforces priority prefix (`01-` to `04-`), hyphen/underscore separation rules, and forbids whitespace before creation.
2. **Directory Tree**: Creates the full 17-directory structure across 5 stages without placeholder files (`.gitkeep`).
3. **Starter Files**: Generates `README.md`, `01-planning/objective.md`, `01-planning/strategy.md`, `31-review/analysis.md`, and `31-review/gate.md` populated with current timestamps and metadata.
4. **Collision Prevention**: Halts immediately if the target project directory already exists.

---

## 2. Project Naming Convention

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
   * **Underscores (`_`)**: Used **exclusively** for separating words inside `[Project_Name]`. Whitespace is strictly forbidden.
4. **Examples**: `01-Paper-Cell_Migration`, `03-Grant-Q3_Report`, `02-Collab-Grant-John-NRF_2026`

---

## 3. Complete Project Directory Blueprint

```text
[Priority]-[Type]-[Project_Name]/
│
├── README.md                           ← Project overview & stage status
│
├── 00-log/                             ← Audit trail & lifecycle logs (Managed by init-log skill)
│   ├── issues/                         ← Issue log files (OPEN-ISSUE-xxx / CLOSED-ISSUE-xxx)
│   └── decisions/                      ← Decision Records (OPEN-DR-xxx / CLOSED-DR-xxx)
│
├── 01-planning/                        [Stage 0: Project Planning & Proposal] objective.md, strategy.md
├── 02-resource/                        [Stage 0: Idea Exploration] References, notes, resources
├── 03-discussion/                      [Stage 0: Idea Exploration] Discussion notes in Markdown
│
├── 11-blueprint/                       [Stage 1: Design & Blueprint] Specifications, designs, architecture
├── 12-implementation/                  [Stage 1: Development] Execution logs & operation instructions
├── 13-code/                            [Stage 1: Software Code & Scripts] Source code, notebooks, execution scripts
│
├── 21-data/                            [Stage 2: Execution & Results]
│   ├── raw/                            ← Read-only raw data or inputs
│   ├── processed/                      ← Processed outputs & visualizations
│   └── execution/                      ← Execution logs and workflow notes
│
├── 31-review/                          [Stage 3: Internal Review & Gate Check] analysis.md, gate.md
├── 32-deliverables/                    [Stage 3: Deliverables Design] Drafts/, Final/
│
├── 41-finalization/                    [Stage 4: Delivery & Finalization] Report/, Handoff/
└── 42-presentation/                    [Stage 4: Presentation & slide materials]
```

---

## 4. Workflows & Gate Review

### Audit Trail & Lifecycle Logging (Delegated to `init-log`)
- Managed automatically by `init_project.py` on initialization.
- Issue and decision tracking across the project lifecycle MUST follow the [`init-log`](../init-log/SKILL.md) skill rules.
- Reusable solutions and protocols SHOULD be extracted to `3_Resources/SOP-` or `3_Resources/Code-`.

### Go / Rollback Gate Review
1. Complete `31-review/analysis.md` (results) and define delivery direction in `31-review/gate.md`.
2. Evaluate `31-review/gate.md` for final Go / Rollback decision:
   * **Go**: Advance to `32-deliverables/` and Stage 4 (`41-finalization/`).
   * **Rollback**: Return to Stage 0 (`01-planning/`), Stage 1 (`11-blueprint/`), or Stage 2 (`21-data/raw/`). Log a Decision Record (`OPEN-DR-xxx-Gate-[Reason].md`).
