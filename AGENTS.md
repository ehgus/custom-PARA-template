# Workspace Customization & PARA Structure Guide

This workspace is managed based on the **PARA Method** framework to efficiently organize tasks, projects, and general work activities.

---

## Quick Reference (Golden Rules)

| Focus Area | Requirement (RFC 2119) | Primary Action |
| :--- | :--- | :--- |
| **New Content** | MUST | Place newly generated code, notes, or files in the appropriate PARA directory (`1_Projects/`, `2_Areas/`, `3_Resources/`). |
| **Folder Naming** | MUST | Follow strict delimiters: hyphen (`-`) for structural tags, underscore (`_`) for word spaces. |
| **Current State** | MUST | Inspect filesystem directly (file reading, directory listing); MUST NOT run Git for current state. |
| **Structure Validation** | MUST ONLY | Execute `validate-para-structure` exclusively when creating, renaming, or moving top-level item directories. |
| **Archiving** | MUST | Archive items ONLY upon explicit user request using the `archive-para-item` skill. |
| **README Files** | MUST NOT | Treat `README.md` as user-maintained; read for context, do not edit without explicit request. |

---

## PARA Directory Structure

Maintain the following 4 core folder structures at the root directory level and adhere to the classification principles:

```text
Workspace/
├── AGENTS.md                   # Workspace guidelines for AI agents and user (this file)
├── 1_Projects/                # [P] Short-term projects & tasks with clear goals and deadlines
├── 2_Areas/                   # [A] Long-term responsibilities & core domains requiring ongoing management
├── 3_Resources/               # [R] Reusable knowledge, code snippets, references, and templates
└── 4_Archives/                # [A] Completed or inactive items (mirroring Projects/Areas/Resources)
    ├── 1_Projects/            # Completed past projects (e.g., 2025-Q4-Project-Website_Redesign/)
    ├── 2_Areas/               # Concluded roles or past duties
    └── 3_Resources/           # Deprecated code, materials, or datasets
```

---

## Categorization & Naming Rules

### Shared Prefix Pool
The following prefixes can be used across **`1_Projects/`**, **`2_Areas/`**, and **`3_Resources/`** to maintain visual consistency:
* `Paper-`: Manuscripts, algorithm/code development, literature reviews, experiment manuscripts.
* `Grant-`: Funding proposals, grant applications, active managed funding projects.
* `Collab-`: Internal/external collaborations (e.g., `Collab-[Type]-[Lead_Person]-[Name]`).
* `Domain-`: Core long-term business or work domains (e.g., `Domain-Marketing/`).
* `Ops-`: Operations, equipment, server administration, internal processes.
* `Admin-`: Account credentials, official administration documents, procedures.
* `Template-`: Reusable document/PPT/script templates.
* `Ref-`: References, background research, AI prompts, meeting minutes.
* `SOP-`: Standard operating procedures, protocols, and manuals.
* `Code-`: Software utilities, code snippets, execution scripts, launch configurations.

---

### Strict Delimiter Rules
* **Hyphens (`-`)**: Must be used for **all** structural component separators, including priority numbers (`01-`), prefixes (`Project-`), collaboration tags (`Collab-`), and ISO Quarter archiving dates (`YYYY-Q[1-4]-`). (Exception: Domain terms inherently containing hyphens preserve their hyphens).
* **Underscores (`_`)**: Reserved **exclusively** for separating words (spaces) inside `[Project_Name]`, `[Area_Name]`, `[Resource_Name]`, and `[Lead_Person]`. Underscores must never be used as structural tag/date delimiters.

### Naming Patterns & Validation Matrix

#### Regular Expression Specifications
* **`1_Projects/`**: `^(0[1-4])-(?:Collab-([A-Za-z]+)-([A-Za-z0-9_]+)-|([A-Za-z]+)-)([A-Za-z0-9_]+)$`
  * Standard format: `^(0[1-4])-([A-Za-z]+)-([A-Za-z0-9_]+)$`
* **`2_Areas/` & `3_Resources/`**: `^(?:Collab-([A-Za-z]+)-([A-Za-z0-9_]+)-|([A-Za-z]+)-)([A-Za-z0-9_]+)$`
  * Standard format: `^([A-Za-z]+)-([A-Za-z0-9_]+)$`
* **`4_Archives/`**: `^(\d{4}-Q[1-4])-(?:Collab-([A-Za-z]+)-([A-Za-z0-9_]+)-|([A-Za-z]+)-)([A-Za-z0-9_]+)$`

#### Delimiter & Naming Examples

| Target Directory | Valid Example | Invalid Example | Violation Reason |
| :--- | :--- | :--- | :--- |
| `1_Projects/` | `01-Paper-Cell_Migration` | `01_Paper_CellMigration` | Underscores used as structural tag separators |
| `1_Projects/` | `02-Grant-NRF_2026` | `2-Grant-NRF_2026` | Missing two-digit priority index (`01`-`04`) |
| `1_Projects/` | `03-Collab-Paper-John-Drug_Assay` | `03-Collab_Paper_John-Drug_Assay` | Underscores used instead of hyphens for collaboration tags |
| `2_Areas/` | `Domain-Marketing` | `Domain_Marketing` | Hyphen must separate prefix from area name |
| `3_Resources/` | `Code-Utilities` | `code-utilities` | Prefix must follow TitleCase conventions |
| `4_Archives/` | `2026-Q3-Paper-Cell_Migration` | `2026_Q3_Paper_Cell_Migration` | ISO Quarter tag must be delimited with hyphens |

---

### 1. `1_Projects/`
* **Definition**: Short-term tasks and projects with a specific **Goal** and a clear **Deadline**.
* **Delegation**: For detailed naming conventions, priority indexing (`01-` to `04-`), formatting rules, and folder initialization, you MUST refer to and use the `init-project` skill.
* **Logging & Auditing**: For audit trail and lifecycle log initialization (`00-log/` containing `issues/` and `decisions/`), refer to and use the `init-log` skill.

### 2. `2_Areas/`
* **Definition**: Long-term domains and responsibilities without fixed deadlines, requiring continuous quality and status management.
* **Naming Convention**: `[Type]-[Area_Name]` (Uses the Shared Prefix Pool)
* **Logging & Auditing**: You may use the `init-log` skill to initialize and manage audit logs (`00-log/`) within an area.
* **Examples**:
  * `Domain-Marketing/` (Main domain: Marketing & outreach)
  * `Ops-Management/` (Operations, equipment, and server administration)
  * `Admin-Finance/` (Financial tracking and duties)
  * `Ref-Certifications/` (Exam preparation & requirements)

### 3. `3_Resources/`
* **Definition**: Reusable reference materials, datasets, code snippets, and protocols for future projects or tasks.
* **Naming Convention**: `[Type]-[Resource_Name]` (Uses the Shared Prefix Pool)
* **Logging & Auditing**: You may use the `init-log` skill to initialize and manage audit logs (`00-log/`) within a resource.
* **Examples**:
  * `Admin-Account_Credentials/`
  * `Template-Documents/`
  * `Ref-Industry_Trends/`
  * `SOP-Procedures/`
  * `Code-Utilities/`

### 4. `4_Archives/`
* **Definition**: Completed, inactive, or historical items from Projects, Areas, and Resources.
* **Delegation**: All structural archiving logic (ISO quarter date prepending, priority prefix stripping, etc.) is handled by the `archive-para-item` skill.
* **Structure (Mirroring)**: Mirrors top-level P/A/R structures.
  ```text
  4_Archives/
  ├── 1_Projects/   # Completed past projects (e.g., 2026-Q3-Project-Product_Launch/)
  ├── 2_Areas/      # Concluded roles or past duties (e.g., 2026-Q2-Admin-Event_Planning/)
  └── 3_Resources/  # Deprecated code, protocols, or datasets (e.g., 2026-Q3-Ref-2024_Old/)
  ```

---

## Rules for AI Agent

1. **File Creation & Location**:
   * Newly generated code, notes, or files MUST be placed under the appropriate PARA directory (`1_Projects/`, `2_Areas/`, or `3_Resources/`).
   * Enforce shared prefix conventions strictly.
   * Temporary scratchpads or short-term analysis data MUST reside inside the corresponding project folder under `1_Projects/`.

2. **Archiving Policy**:
   * Archiving operations (moving items to `4_Archives/`) MUST be executed ONLY upon explicit request from the user. Active projects and resources MUST remain in their active locations by default.
   * When executing an archive request, agents MUST exclusively invoke the `archive-para-item` skill to handle proper ISO quarter date tagging and structure mirroring. Raw shell commands (e.g., `mv`, `Rename-Item`, `cp`) MUST NOT be used for archiving.

3. **Reference Management**:
   * Manage bulk reference files via appropriate management tools.
   * Newly collected references, materials, or notes created while working inside a project MUST be placed in that project's background folder (e.g., `1_Projects/[Priority]-[Type]-[Project_Name]/02-background/`).
   * Move materials to `3_Resources/` ONLY when the user explicitly requests to share them globally across the workspace.

4. **Formatting Policy**:
   * Markdown formatting MUST remain clean and plain. Do NOT use emojis in `AGENTS.md` or workspace documentation files.

5. **Skill Naming Policy**:
   * When defining new skills, the skill name MUST start with an action verb in lowercase kebab-case (e.g., `init-project` instead of `project-init`).

6. **README.md Policy**:
   * `README.md` files are user-maintained documentation. Agents MUST inspect them for context, but MUST NOT modify, edit, or overwrite them unless explicitly requested by the user.

7. **GitHub Issue Management Policy**:
   * All GitHub issues and pull requests created for this workspace MUST be written entirely in **English**.
   * When generating issues, follow the standard templates:
     * **BUG**: Describe the conflict or error with the current PARA rules, how to reproduce it, and the expected behavior. (Prefix title with `BUG: `)
     * **ENHANCEMENT**: Describe the new feature, folder prefix, or rule change, and the justification for why it improves the workspace. (Prefix title with `ENHANCEMENT: `)

8. **Mandatory Structure Validation**:
   * **Trigger Condition**: The `validate-para-structure` skill MUST be executed ONLY when creating, renaming, or moving **top-level item directories directly under** `1_Projects/`, `2_Areas/`, or `3_Resources/` (e.g., creating a new project folder).
   * **Exemption Scope**: For internal file modifications, file creations, code edits, or subdirectory changes within existing items, agents MUST bypass this validation.
   * **Action on Failure**: If the validation skill returns an error (exit code > 0) when validating a top-level directory change, the agent must immediately halt, revert the structural change, and report the syntax violation.

9. **Lifecycle & Audit Logging Policy**:
   * Audit trail folders (`00-log/`), issue tracking (`issues/`), decision records (`decisions/`), and their respective templates across `1_Projects/`, `2_Areas/`, and `3_Resources/` are governed by the `init-log` skill.

10. **Skill Specification & Authoring Policy**:
    * **Design Philosophy (What over How)**: Skill instructions MUST focus on declarative goals, structure, and desired outcomes (What) rather than micromanaging internal execution procedures.
    * **Tool Decoupling**: Do not bind skill instructions to internal agent tool names or platform-specific shell scripts unless the skill fundamentally wraps a dedicated external CLI tool. Allow the agent autonomy to determine the most direct execution method.
    * **Clean Deprecation**: When removing or deprecating a feature or convention, cleanly excise obsolete specifications from the documentation. Avoid cluttering skill files with defensive negative rules or prohibition clauses.

11. **Inspection & Version Control Policy**:
    * **Filesystem-First Principle**: To understand current project state, inspect file contents, or answer inquiries regarding workspace structure, agents MUST inspect files directly using standard file-reading and directory-listing capabilities. Git commands (e.g., `git log`, `git status`, `git diff`) MUST NOT be used to explore current state.
    * **Git Usage Verification**: Before running any Git command, verify whether version-control metadata (such as commit revisions or commit histories) is strictly indispensable. If current filesystem inspection suffices, abort the Git command.
    * **Directory Skeletons**: Treat empty directories as standard filesystem folders. Creation of placeholder dummy files (`.gitkeep`, `.keep`) is prohibited.


