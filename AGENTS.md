# BMOL Workspace Customization & PARA Structure Guide

This workspace (`c:\Users\labdo\Desktop\BMOL`) is managed based on the **PARA Method** framework to efficiently organize research and academic activities for **BMOL (Biomedical Molecular Operations Lab / Bio-Molecular Lab)**.

---

## PARA Directory Structure

Maintain the following 4 core folder structures at the root directory level and adhere to the classification principles:

```text
BMOL/
├── AGENTS.md                   # Workspace guidelines for AI agents and user (this file)
├── 1_Projects/                # [P] Short-term research & tasks with clear goals and deadlines
├── 2_Areas/                   # [A] Long-term responsibilities & main research topics requiring ongoing management
├── 3_Resources/               # [R] Reusable knowledge, code snippets, references, and protocols
└── 4_Archives/                # [A] Completed or inactive items (mirroring Projects/Areas/Resources)
    ├── 1_Projects/            # Completed or submitted past projects (e.g., 2025-Q4-01-Paper-KCC/)
    ├── 2_Areas/               # Concluded lab roles or past semester TA duties
    └── 3_Resources/           # Deprecated code, protocols, or datasets
```

---

## Categorization & Naming Rules

### Shared Prefix Pool
The following prefixes can be used across **`1_Projects/`**, **`2_Areas/`**, and **`3_Resources/`** to maintain visual consistency:
* `Paper-`: Manuscripts, algorithm/code development, literature reviews, experiment manuscripts.
* `Grant-`: Funding proposals, grant applications, active managed funding projects.
* `Collab-`: Internal/external collaborations (e.g., `Collab-[Type]-[Lead_Person]-[Name]`).
* `Research-`: Core long-term research domain/topics (e.g., `Research-Molecular_Docking/`).
* `Lab-`: Laboratory equipment, reagents, server administration, operations.
* `Admin-`: Account credentials, official administration documents, lab procedures.
* `Template-`: Reusable document/PPT/LaTeX/script templates.
* `Ref-`: Funding references, literature notes, background research, AI prompts.
* `SOP-`: Standard operating procedures, protocols, and manuals.
* `Code-`: Software utilities, code snippets, execution scripts, launch configurations.

---

### Strict Delimiter Rules
* **Hyphens (`-`)**: Must be used for **all** structural component separators, including priority numbers (`01-`), prefixes (`Paper-`), collaboration tags (`Collab-`), and ISO Quarter archiving dates (`YYYY-Q[1-4]-`).
* **Underscores (`_`)**: Reserved **exclusively** for separating words (spaces) inside `[Project_Name]`, `[Area_Name]`, or `[Resource_Name]`. Underscores must never be used as structural tag/date delimiters.

---

### 1. `1_Projects/`
* **Definition**: Short-term research, tasks, and grants with a specific **Goal** and a clear **Deadline**.
* **Naming Convention**: `[Priority]-[Type]-[Project_Name]` or `[Priority]-Collab-[Type]-[Lead_Person]-[Project_Name]`
* **Priority Indexing Rules**:
  * `01-`: Important & Urgent
  * `02-`: Urgent & Not Important
  * `03-`: Important & Not Urgent
  * `04-`: Not Important & Not Urgent
* **Examples**:
  * `01-Paper-Bacteria_Review/`
  * `03-Paper-Data_Compression/`
  * `01-Grant-삼성과제.lnk`
  * `01-Collab-Paper-강융-Ptychographic_Tomography/`
* **Formatting Rules**:
  * Prefix and tag delimiters must use hyphens (`-`).
  * Words inside `[Project_Name]` must be separated by underscores (`_`).
  * Korean project and lead names are preserved in Korean (e.g., `01-Grant-삼성과제.lnk`).

### 2. `2_Areas/`
* **Definition**: Long-term research fields and responsibilities without fixed deadlines, requiring continuous quality and status management.
* **Naming Convention**: `[Type]-[Area_Name]` (Uses the Shared Prefix Pool)
* **Examples**:
  * `Research-Molecular_Docking/` (Main research domain: Molecular docking & simulation)
  * `Lab-Management/` (Lab equipment, reagents, and server administration)
  * `Admin-Coursework_TA/` (Courses enrolled and Teaching Assistant duties)
  * `Ref-Qualifying_Exam/` (Qualifying exam preparation & degree requirements)

### 3. `3_Resources/`
* **Definition**: Reusable reference materials, datasets, code snippets, and protocols for future projects or research.
* **Naming Convention**: `[Type]-[Resource_Name]` (Uses the Shared Prefix Pool)
* **Examples**:
  * `Admin-Account_Credentials/`
  * `Template-Documents/`
  * `Ref-Funding/`
  * `SOP-Procedures/`
  * `Code-SW_Xwindows/`

### 4. `4_Archives/`
* **Definition**: Completed, inactive, or historical items from Projects, Areas, and Resources.
* **ISO Quarter Date Notation**: All archived items must be prepended with `YYYY-Q[1-4]-` representing the completion or deprecation quarter, joined with a hyphen.
* **Structure (Mirroring)**: Mirrors top-level P/A/R structures.
  ```text
  4_Archives/
  ├── 1_Projects/   # Completed past projects (e.g., 2026-Q3-01-Paper-3D_Metamaterial_Inverse_Solver/)
  ├── 2_Areas/      # Concluded lab roles or past TA duties (e.g., 2026-Q2-Admin-Coursework_TA/)
  └── 3_Resources/  # Deprecated code, protocols, or datasets (e.g., 2026-Q3-Ref-Funding_2024_Old/)
  ```

---

## Rules for AI Agent (Antigravity)

1. **File Creation & Location**:
   * Always place newly generated code, notes, or files under the appropriate PARA directory (`1_Projects`, `2_Areas`, or `3_Resources`).
   * Enforce priority index with hyphens (`01-` ~ `04-`) and shared prefix conventions strictly.
   * Keep temporary scratchpads or short-term analysis data inside the corresponding project folder under `1_Projects/`.

2. **Temporary & Cache Files Policy**:
   * Do NOT track, clean, or manage temporary/cache files generated automatically during code execution (e.g., `__pycache__`, `.pyc`, `.log`, build artifacts, system caches). AI agents should strictly ignore unintended execution caches.

3. **Archiving Policy**:
   * AI agents must **ONLY** perform archiving operations (moving items to `4_Archives/`) upon **explicit request from the user**. Never automatically archive active projects or resources.

4. **Windows Shortcut (.lnk) Handling**:
   * When encountering Windows shortcut files (`.lnk`), transparently resolve and treat them as the actual target directory or file for reading, writing, and navigation.

5. **Literature & References**:
   * Manage bulk paper PDF files via reference management tools like Zotero.
   * By default, new references, materials, or literature notes created while working inside a project MUST be placed in that project's background folder (e.g., `1_Projects/[Project_Name]/02-background/`).
   * These materials should ONLY be moved to `3_Resources/` when the user explicitly requests to share them globally across the workspace.

6. **Formatting Policy**:
   * Do NOT use emojis in `AGENTS.md` or workspace documentation files. Keep formatting clean and plain markdown.

7. **Skill Naming Policy**:
   * When creating or defining new skills, always start the skill name with an action verb using lowercase kebab-case (e.g., `init-project` instead of `project-init`).

8. **README.md Policy**:
   * Do NOT modify, edit, or overwrite `README.md` files inside any folder. These files are managed by the user. Only read them for context unless explicitly requested to modify them.

9. **GitHub Issue Management Policy**:
   * All GitHub issues and pull requests created for this workspace MUST be written entirely in **English**.
   * When generating issues, follow the standard templates:
     * **BUG**: Describe the conflict or error with the current PARA rules, how to reproduce it, and the expected behavior. (Prefix title with `BUG: `)
     * **ENHANCEMENT**: Describe the new feature, folder prefix, or rule change, and the justification for why it improves the workspace. (Prefix title with `ENHANCEMENT: `)
