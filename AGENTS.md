# Workspace Customization & PARA Structure Guide

This workspace is managed based on the **PARA Method** framework. All activities MUST adhere to the following directory roles and agent rules.

---

## 1. PARA Directory Structure & Naming

```text
Workspace/
├── AGENTS.md       # Workspace guidelines for AI agents and user (this file)
├── 1_Projects/     # [Priority]-[Type]-[Name] (Short-term, clear goal & deadline. Priority: 01- to 04-)
├── 2_Areas/        # [Type]-[Name] (Long-term responsibilities & ongoing management)
├── 3_Resources/    # [Type]-[Name] (Reusable reference materials, code snippets, templates, SOPs)
└── 4_Archives/     # [YYYY-Q1~4]-[Original_Name] (Completed/inactive items, mirroring Projects/Areas/Resources)
```

### Shared Prefix Pool (`[Type]`)
* `Paper-`: Manuscripts, algorithm/code development, literature reviews, experiment manuscripts.
* `Grant-`: Funding proposals, grant applications, active managed funding projects.
* `Collab-`: Collaborations (format: `Collab-[Type]-[Lead_Person]-[Name]`).
* `Domain-`: Core long-term business or work domains.
* `Ops-`: Operations, equipment, server administration, internal processes.
* `Admin-`: Account credentials, official administration documents, procedures.
* `Template-`: Reusable document/PPT/script templates.
* `Ref-`: References, background research, AI prompts, meeting minutes.
* `SOP-`: Standard operating procedures, protocols, and manuals.
* `Code-`: Software utilities, code snippets, execution scripts, launch configurations.

### Delimiter & Format Rules
* **Hyphens (`-`)**: MUST be used as structural separators (priority `01-` to `04-`, prefix tags, collaboration tags, and ISO Quarter dates `YYYY-Q[1-4]-`).
* **Underscores (`_`)**: MUST be reserved for spaces within multi-word names (`[Project_Name]`, `[Area_Name]`, `[Lead_Person]`).
* **Standard Patterns**:
  * `1_Projects/`: `^(0[1-4])-(?:Collab-([A-Za-z]+)-([A-Za-z0-9_]+)-|([A-Za-z]+)-)([A-Za-z0-9_]+)$` (e.g., `01-Paper-Cell_Migration`, `02-Collab-Grant-John-NRF_2026`)
  * `2_Areas/` & `3_Resources/`: `^(?:Collab-([A-Za-z]+)-([A-Za-z0-9_]+)-|([A-Za-z]+)-)([A-Za-z0-9_]+)$` (e.g., `Domain-Marketing`, `Code-Utilities`)
  * `4_Archives/`: `^(\d{4}-Q[1-4])-(?:Collab-([A-Za-z]+)-([A-Za-z0-9_]+)-|([A-Za-z]+)-)([A-Za-z0-9_]+)$` (e.g., `2026-Q3-Paper-Cell_Migration`)

---

## 2. Rules for AI Agent

### Inspection & Filesystem Safety
1. **Filesystem MCP Inspection & Reading Priority**:
   * **MCP Inspection & Read Standard**: Agents MUST prioritize Filesystem MCP tools as the primary mechanism for inspecting workspace status, directory structures, and reading file contents.
   * **Provider Fallback**: Provider-specific native inspection tools MAY be used ONLY if the Filesystem MCP server is unavailable or unsupported in the runtime environment.
2. **Directory Skeletons**: Empty directories MUST be treated as standard filesystem folders. Agents MUST NOT create placeholder dummy files (`.gitkeep`, `.keep`).
3. **README.md Policy**: `README.md` files are user-maintained documentation. Agents MUST inspect them for context, but MUST NOT modify, edit, or overwrite them unless explicitly requested by the user.

### File Creation & Placement
4. **PARA Placement**: Newly generated code, notes, or files MUST reside under the appropriate PARA directory (`1_Projects/`, `2_Areas/`, or `3_Resources/`).
5. **Project Scopes & References**: Short-term analysis data or newly collected references MUST remain in that project's background folder (`1_Projects/.../02-background/`). Agents MUST NOT move materials to `3_Resources/` unless explicitly requested by the user.

### Skill Delegations
6. **Project Initialization**: New project folders inside `1_Projects/` MUST be initialized using the `init-project` skill.
7. **Lifecycle & Audit Logging**: Audit trail folders (`00-log/`), issue tracking (`issues/`), and decision records (`decisions/`) across all items MUST be governed by the `init-log` skill.
8. **Archiving Policy**: Items MUST be moved to `4_Archives/` ONLY upon explicit user request, exclusively invoking the `archive-para-item` skill. Raw shell commands (`mv`, `cp`, `Rename-Item`) MUST NOT be used for archiving.
9. **Mandatory Structure Validation**:
   * **Trigger**: Agents MUST execute the `validate-para-structure` skill ONLY when creating, renaming, or moving top-level item directories directly under `1_Projects/`, `2_Areas/`, or `3_Resources/`.
   * **Exemption**: Agents MUST bypass validation for internal file modifications, creations, or subdirectory changes within existing items.
   * **Action on Failure**: If validation fails (exit code > 0), agents MUST halt immediately, revert the structural change, and report the violation.

### General Conventions
10. **Documentation Formatting**: Markdown formatting MUST remain clean and plain. Emojis MUST NOT be used in `AGENTS.md` or workspace documentation files.
11. **Internal Documentation & RFC 2119 Standards**:
    * **Scope**: Technical specifications, checklists, skill definitions, logs, and prompt guidelines intended for internal use by the user and AI.
    * **Lean Authoring**: MUST avoid tautology, repetitive explanations, and low-utility structures (e.g., redundant example tables, tutorial prose). Keep content token-efficient, concise, structured, and actionable.
    * **RFC 2119 Compliance**: Requirements and constraints MUST strictly adhere to RFC 2119 terms (in uppercase):
      * `MUST` / `REQUIRED` / `SHALL`: Absolute requirement.
      * `MUST NOT` / `SHALL NOT`: Absolute prohibition.
      * `SHOULD` / `RECOMMENDED`: Strong recommendation (valid exceptions may exist, but full impact must be weighed).
      * `SHOULD NOT` / `NOT RECOMMENDED`: Strong discouragement.
      * `MAY` / `OPTIONAL`: Discretionary permission.
12. **GitHub Management**: All GitHub issues and pull requests MUST be in English, prefixed with `BUG: ` (reproduction & expected behavior) or `ENHANCEMENT: ` (rationale & changes).
13. **Skill Authoring**: Skill names MUST start with an action verb in lowercase kebab-case (e.g., `init-project`). Skill instructions MUST focus on declarative goals (What over How) and MUST remain decoupled from internal tool names.
