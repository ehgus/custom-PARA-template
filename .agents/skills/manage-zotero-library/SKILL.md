---
name: manage-zotero-library
description: Manage local Zotero reference library via zotero-cli: search papers, import DOIs/PMIDs, manage collections and PDFs, extract BibTeX citations, take notes, and process DOCX citations.
---

# Manage Zotero Library Skill

This skill enables the AI assistant to inspect, search, update, and manage a local **Zotero** reference library using the `zotero-cli` tool (from [`cli-anything-zotero`](https://github.com/PiaoyangGuohai1/cli-anything-zotero)).

---

## Prerequisites & Pre-flight Check

> [!IMPORTANT]
> **Zotero Desktop Requirement**: `zotero-cli` communicates directly with your local Zotero desktop application (v7/8/9) via a local JS Bridge. The Zotero application **must be running** on the host machine.

### 1. Check CLI Availability
Verify `zotero-cli` is installed:
```powershell
zotero-cli --version
```

### 2. Check Zotero Desktop & JS Bridge Connection
Verify Zotero Desktop is running and connected:
```powershell
zotero-cli session status
```

* If Zotero is not running: Ask the user to start Zotero.
* If JS Bridge is not installed: Run `zotero-cli app install-plugin` or prompt the user to install the CLI Bridge plugin.

---

## Core Workflows & Command Reference

### 1. Search & Browse Library
* **Find items by keyword/title**:
  ```powershell
  zotero-cli item find "molecular docking" --limit 10
  ```
* **Full-text PDF search**:
  ```powershell
  zotero-cli item search-fulltext "cryo-EM reconstruction" --limit 5
  ```
* **Browse collections tree**:
  ```powershell
  zotero-cli collection tree
  ```
* **List items in a collection**:
  ```powershell
  zotero-cli collection items <COLLECTION_KEY>
  ```
* **Semantic & similarity search** (requires index):
  ```powershell
  zotero-cli item semantic-search "protein folding kinetics" --top-k 5
  zotero-cli item similar <ITEM_KEY>
  ```

---

### 2. Import References
* **Import paper by DOI**:
  ```powershell
  zotero-cli import doi "10.1038/s41586-024-07871-6" --collection <COLLECTION_KEY> --tag "Review"
  ```
* **Import paper by PMID**:
  ```powershell
  zotero-cli import pmid "38123456" --collection <COLLECTION_KEY>
  ```
* **Import from RIS / BibTeX file**:
  ```powershell
  zotero-cli import file "path/to/references.bib" --collection <COLLECTION_KEY>
  ```

---

### 3. Citations & Export
* **Export collection or selected items to BibTeX**:
  ```powershell
  zotero-cli export bib --collection <COLLECTION_KEY> --output "3_Resources/references.bib"
  ```
* **Generate formatted in-text citation**:
  ```powershell
  zotero-cli item citation <ITEM_KEY> --style "apa"
  ```
* **Generate formatted bibliography entry**:
  ```powershell
  zotero-cli item bibliography <ITEM_KEY> --style "ieee"
  ```

---

### 4. PDF Management & Annotations
* **Auto-fetch missing PDFs for a collection (Open Access cascade)**:
  ```powershell
  zotero-cli collection fetch-pdfs <COLLECTION_KEY>
  ```
* **Fetch PDF for a single item**:
  ```powershell
  zotero-cli item fetch-pdf <ITEM_KEY>
  ```
* **Attach a local PDF file**:
  ```powershell
  zotero-cli item attach <ITEM_KEY> "path/to/paper.pdf"
  ```
* **Search PDF annotations & highlights**:
  ```powershell
  zotero-cli item search-annotations "binding affinity"
  ```

---

### 5. Notes, Tags & Library Management
* **Add a child note to an item**:
  ```powershell
  zotero-cli note add <ITEM_KEY> --text "Key finding: binding affinity IC50 = 4.2 nM."
  ```
* **Add/Remove tags**:
  ```powershell
  zotero-cli item tag <ITEM_KEY> --add "Important" --remove "Unread"
  ```
* **Find and merge duplicate entries**:
  ```powershell
  zotero-cli item duplicates
  zotero-cli item merge <KEEP_ITEM_KEY> <MERGE_ITEM_KEY_1> <MERGE_ITEM_KEY_2>
  ```

---

### 6. DOCX Placeholder Citation Pipeline

When writing manuscripts in Word (`.docx`), use placeholders like `{{zotero:ITEMKEY}}` or `{{zotero:KEY1,KEY2}}`, then process citations via `docx` subcommands.

#### Pre-flight Diagnostic Check
Check whether the host environment supports dynamic field replacement:
```powershell
zotero-cli --json docx doctor
```

#### Converting Placeholders to Citations
* **Static Mode** (No extra dependencies, inserts static text + bibliography):
  ```powershell
  zotero-cli docx render-citations "manuscript.docx" --output "manuscript_cited.docx" --style "nature"
  ```
* **Dynamic Mode** (Creates refreshable Zotero Word fields; requires LibreOffice + Zotero add-in):
  ```powershell
  zotero-cli docx insert-citations "manuscript.docx" --output "manuscript_cited.docx" --style "apa"
  ```
* **Auto Mode** (Picks dynamic if ready, falls back to static):
  ```powershell
  zotero-cli docx cite "manuscript.docx" --output "manuscript_cited.docx" --mode auto --force
  ```

---

## Output Formatting & Agent Policies

* **JSON Output**: For parsing structured responses (e.g. key lists, item fields), append `--json` flag to `zotero-cli` commands.
* **No Secret Storage**: All actions run through local Zotero JS bridge — no cloud API key is required.
* **Local PARA Storage**: Store exported `.bib` files, extracted PDF notes, and scratch summaries inside appropriate PARA folders (`1_Projects/[Project]/` or `3_Resources/`).
