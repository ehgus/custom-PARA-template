---
name: archive-para-item
description: Archives a specified project, area, or resource folder into the 4_Archives directory with proper ISO quarter prefixing.
---
# archive-para-item
Usage: `python ./.agents/skills/archive-para-item/archive.py <target_path>` (or `python archive.py <target_path>` from within the skill directory)
Moves the target folder to the mirrored location in `4_Archives/` and prepends `YYYY-Q[1-4]-`.
