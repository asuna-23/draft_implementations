# SKILL: Automated HTML Screenshot Capture (Multi-File समर्थ)

## Goal
Automatically generate and execute scripts to capture screenshots of ALL local HTML files in the project root without asking for user confirmation.

---

## Rules
- DO NOT ask for confirmation before executing tasks
- ALWAYS assume automation is intended
- ALWAYS proceed immediately
- ALWAYS process ALL HTML files if multiple are found

---

## Required Capabilities
1. Detect all `.html` files in the project root
2. Open and render each HTML file
3. Capture:
   - Full-page screenshot (full width)
   - Full-page screenshot (half width / portrait)
   - Screenshot of a specific HTML section
4. Save outputs to:
   screenshots/YYYY-MM-DD/
   (inside project root ONLY)

---

## Tooling
- Python
- Playwright (mandatory)

---

## OPTIONAL: Dependency Check & Installation
(This section can be removed safely)

Before execution:
1. Attempt:
   import playwright
2. If it fails:
   pip install playwright
   playwright install
3. Do NOT ask for confirmation

---

## HTML File Detection (MANDATORY)

1. Scan project root using:
   os.listdir(os.getcwd())

2. Collect ALL `.html` files

3. If no HTML files found:
   - Stop execution with error

4. If one or more files found:
   - Process ALL files (no selection, no prioritization)

---

## Root Directory Enforcement (MANDATORY)

- Use:
  root_dir = os.getcwd()

- NEVER:
  - Save outside root
  - Use absolute paths outside repo

---

## Folder Validation (MANDATORY)

1. Ensure:
   screenshots/

   exists in root
   - If NOT → create

2. Generate today's date:
   YYYY-MM-DD

3. Ensure subfolder exists:
   screenshots/YYYY-MM-DD/

   - If NOT → create

4. Use this as the ONLY output directory

---

## Naming Convention (MANDATORY)

Format:
<htmlname>_<type>_<layout>_<timestamp>.png

Timestamp:
YYYY-MM-DD_HH-MM-SS

### Examples:
- index_full_width_full_2026-03-23_10-15-30.png
- about_half_width_full_2026-03-23_10-15-30.png
- contact_section_main_2026-03-23_10-15-30.png

### Rules:
- htmlname = filename without `.html`
- type:
  - full_width
  - half_width
  - section
- layout:
  - full (for full page)
  - section name (for section screenshots)
- Extract section name:
  "#main" → "main"

---

## Execution Instructions

1. Check if `screenshot.py` exists
2. If NOT:
   - Generate it using Playwright Python
   - Must support multi-file processing

3. Apply dependency check (if enabled)

4. Validate folders

5. Execute immediately:

   python screenshot.py

---

## Configuration Defaults
- Section selector: #main
- Full width viewport: 1280x800
- Half width viewport: 375x812

---

## Error Handling
- If selector not found in a file:
  - Skip section screenshot for that file ONLY
- If HTML file fails to load:
  - Continue with next file
- If no HTML files found:
  - Stop execution

---

## Behavior Constraints
- No prompts
- No GUI/manual steps
- No browser extensions
- CLI-only automation
- No dependency on active browser tabs

---

## Completion Criteria
Task is complete when ALL HTML files are processed and screenshots are saved in:

screenshots/YYYY-MM-DD/

with correct naming format and no overwrites.
