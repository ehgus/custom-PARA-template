---
name: review-paper
description: >-
  Use this skill to generate a paper review summary. Activate this when the user asks to summarize, review, or analyze an academic paper.
---

# Paper Review Summary Skill

When the user requests a summary or review of an academic paper, you MUST format your response using the following template. Analyze the paper thoroughly to fill out each section.

## Template

```markdown
# [Paper Title]

**Journal:** [Journal/Conference Name]

**Authors:** [Author Names and Affiliations]

## Summary (What, why, how)
[Summarize the core of the paper in at most two paragraphs:
- What is the research about?
- Why is it important (background/motivation)?
- How was the research conducted (methods/experiments)?
- What are the key findings?]

## Critical evaluation and suggestions for improvement
[Critically analyze the paper:
- What are the limitations or weaknesses?
- What claims lack sufficient verification or evidence?
- Suggest improvements or alternative approaches.]

## Can be exploited for my research
[Identify how the methods, tools, or findings can be applied to our lab's research:
- Provide concrete scenarios (e.g., Scenario 1: [Use case])
- Explain the expected value or correlation with our work.]

## Elegant expressions useful for my scientific writing
[Extract 2-3 well-crafted sentences or phrases from the paper that are useful for academic writing. State the purpose of each expression in English.]
- [Purpose]: "[Extracted sentence]"
```

## Output Language
- Write the entire review in **English**, including all section content, scenario descriptions, and the stated purpose of each extracted expression. This applies even when the user's request is written in another language.
- Quote extracted sentences verbatim from the paper without translation.

## Plain-Text Formatting Rules
These rules keep the review portable across editors, note apps, and reference managers.

- **No tables.** Never emit a markdown table, an ASCII-art table, or a pipe-delimited block. When you would reach for a table to hold numbers, write the numbers as a short narrative paragraph or a plain list instead.
- **No special characters.** Restrict the output to plain ASCII. Concretely:
  - Do not use em dashes, en dashes, arrows, bullets other than a leading hyphen, curly or typographic quotes, or ellipsis characters. Use a plain hyphen, the word "to" for ranges, and straight quotes.
  - Do not use Greek letters, superscripts, subscripts, or mathematical symbols. Spell units out or use ASCII abbreviations: write "um" for micrometre, "deg" for degree, "delta n" for refractive index change, "5.6 x 10^-5" for powers of ten, "1230 fs2" for squared units, and "percent" or "%" for proportions.
  - Do not use emoji or decorative glyphs anywhere in the review.
- **Headings and emphasis** follow the template exactly. Bold is permitted only for the field labels shown in the template and for the leading label of a bullet.

## Guidelines for Narrative Writing Style
- **Flow and Cohesion:** Write the summary and evaluation sections in a narrative (story-telling) style rather than merely listing disjointed facts or using excessive bullet points.
- **Logical Transitions:** Connect the "What", "Why", and "How" logically. For example, explain the background (Why) in a way that naturally leads to the problem they are solving (What), followed by their specific approach (How), and ending with the implications of their findings.
- **Readable Sentences:** Use complete, well-structured sentences that read naturally and engagingly.
- **Lead with the claim:** Open the Summary section with one sentence stating the paper's central result, then unfold the background, method, and evidence behind it.
- **Summary length limit:** The Summary section is capped at two paragraphs. A workable split is one paragraph for the central claim and the motivation behind it, and one for the method and the evidence that supports it. Never exceed two paragraphs there, and do not evade the cap by inserting sub-headings, lists, or a trailing paragraph of numbers. Key figures belong inside those two paragraphs, and details that do not fit are either dropped or moved to the critical evaluation where they carry an argument. The other sections have no such cap.

## Instructions
1. Read the provided paper carefully.
2. Fill out the template sections comprehensively based on the paper's content, applying the **Narrative Writing Style** guidelines.
3. Before returning the review, scan the draft for tables and for any non-ASCII character and rewrite those passages in plain prose or plain ASCII, and confirm the Summary section is at most two paragraphs.
4. Provide your final response formatted exactly as the markdown template above.
