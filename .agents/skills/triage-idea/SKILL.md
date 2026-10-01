---
name: triage-idea
description: Triage, review, and categorize unprocessed ideas in 3_Resources/Ref-Idea/INBOX.md, promoting actionable projects via init-project or extracting reusable resources.
---

# Triage Idea Skill

This skill executes periodic or on-demand curation of the idea buffer (`3_Resources/Ref-Idea/`), ensuring items transition to actionable projects, reusable resources, incubations, or clean discards.

---

## 1. Operating Targets

* **Inbox Source**: `3_Resources/Ref-Idea/INBOX.md`
* **Drafts Directory**: `3_Resources/Ref-Idea/drafts/`

---

## 2. Triage Procedure

### Step 1: Scan & Inventory
1. Read `INBOX.md` and identify all distinct uncurated entries.
2. Check `drafts/` for lingering idea drafts.
3. Present a concise numbered summary to the user outlining title, capture date, and preliminary assessment.

### Step 2: 4-Way Disposition
For each entry, evaluate and agree with the user on one of the four actions:

| Action | Criteria | Target Disposition |
|---|---|---|
| **Drop** | Obsolete, duplicate, unfeasible, or abandoned concept | Remove from `INBOX.md` without archival. |
| **Resource** | Reusable code utility, protocol, or general reference | Move to target `3_Resources/Code-*` or `3_Resources/Ref-*` folder. Remove from `INBOX.md`. |
| **Incubate** | Worth exploring further, but lacks immediate goal or deadline | Create dedicated note in `drafts/[YYYY-MM-DD]-[Idea_Name].md`. Remove from `INBOX.md`. |
| **Promote** | Has clear WHAT, WHY, and target completion milestone | Transition to `1_Projects/` (see Step 3). |

### Step 3: Project Promotion Workflow
When an entry is approved for promotion to `1_Projects/`:

1. **Verify Prerequisites**:
   - Determine `[Priority]` index (`01-` to `04-`).
   - Determine `[Type]` prefix (`Paper-`, `Grant-`, `Code-`, `Domain-`, etc.).
   - Confirm project name adhering to underscore delimiter rules (`[Project_Name]`).
2. **Execute Project Initialization**:
   - Delegate directory creation to the `init-project` skill.
   - Populate `01-planning/objective.md` with the captured WHAT and WHY rationales.
   - Populate `02-background/` with captured references, links, and notes.
3. **Validate Structure**:
   - Invoke the `validate-para-structure` skill to verify top-level directory compliance.
4. **Purge Buffer**:
   - Delete the source entry from `INBOX.md` or remove the draft from `drafts/`.
