---
name: read-document-with-pandoc
description: Convert and extract plain text or markdown from non-text document files (.docx, .pptx, .epub, .odt, .rtf, .html, .tex) using Pandoc CLI to inspect their contents.
---

# Read Document with Pandoc Skill

This skill allows the agent to read and inspect non-plain-text binary or formatted document files (such as Word `.docx`, PowerPoint `.pptx`, OpenDocument `.odt`, Rich Text `.rtf`, `.epub`, `.html`, LaTeX `.tex`) by converting them to clean Markdown or plain text via **Pandoc CLI**.

## Supported Input Formats
- Microsoft Word (`.docx`)
- Microsoft PowerPoint (`.pptx`)
- OpenDocument Text (`.odt`)
- Rich Text Format (`.rtf`)
- Electronic Publication (`.epub`)
- HTML (`.html`, `.htm`)
- LaTeX (`.tex`)

---

## Strict Requirement: Pandoc Dependency Policy

> [!CRITICAL]
> **No Fallback Policy**: If `pandoc` is not installed or the `pandoc` command fails due to being missing on the user's system:
> 1. **DO NOT** attempt to use any alternative tools or python libraries (e.g., `python-docx`, `pypdf`, `catdoc`).
> 2. **STOP** reading and processing the requested non-text document immediately.
> 3. **Prompt the user** to install Pandoc before retrying.

---

## Execution Workflow

### 1. Direct Markdown Extraction (To Console)
Run `pandoc` via shell to convert the target document into Markdown:

```
pandoc -t markdown "path/to/document.docx"
```

### 2. Extract Content to a Scratch Markdown File (For Large Documents)
If the document is long, convert it into a temporary scratch file:

```
pandoc "path/to/large_document.docx" -o "3_Resources/scratch/extracted_doc.md"
```

### 3. Extracting Media or Images (Optional)
If the document contains embedded images that need to be preserved:

```
pandoc "path/to/document.docx" --extract-media="3_Resources/scratch/media" -t markdown
```

### Error Handling and User Feedback
- If the previous commands fail, run `pandoc --version` to check if Pandoc is installed.
- If the command fails, prompt the user to install Pandoc.
