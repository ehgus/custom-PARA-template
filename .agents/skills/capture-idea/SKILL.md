---
name: capture-idea
description: Capture fleeting thoughts, inspirations, notes, or ideas into the 3_Resources/Ref-Idea inbox with timestamps and context.
---

# Capture Idea Skill

This skill handles quick, frictionless recording of raw thoughts, concepts, literature notes, or algorithmic ideas into the workspace idea buffer.

---

## 1. Scope & Target Path

* **Target Destination**: `3_Resources/Ref-Idea/INBOX.md`
* **Applicability**: Invoked whenever the user provides an unstructured thought, asks to record an inspiration, or requests to save a discussion point into the idea inbox.

---

## 2. Ingestion Rules

1. **Zero Categorization Overhead**: The agent MUST NOT demand categorization, priority tagging, or deadline assignment at capture time.
2. **Standard Entry Format**: Every entry appended to `INBOX.md` MUST adhere to the following schema:

```markdown
## [YYYY-MM-DD] <Concise Title>
- Context / Trigger: <Where the thought originated, active project link, paper, or conversation context>
- Core Idea / Hypothesis: <Summary of the idea or insight>
- References / Keywords: <Related URLs, DOIs, tools, or domain keywords>
```

3. **Context Preservation**:
   - If the idea originated from an active project or file within the workspace, the entry SHOULD include a markdown link to that resource.
   - If the user provides only raw text or bullet points, the agent MUST distill a 3- to 6-word title and format the entry cleanly.

4. **Append Integrity**:
   - New entries MUST be appended to `INBOX.md` without overwriting or reordering existing entries.
   - The file header and operational guidelines in `INBOX.md` MUST remain intact.
