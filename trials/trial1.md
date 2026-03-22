# SKILL: Automated HTML Screenshot Capture

## Goal
Automatically generate and execute scripts to capture screenshots of local HTML files without asking for user confirmation.

---

## Rules
- DO NOT ask for confirmation before executing tasks
- ALWAYS assume automation is intended
- ALWAYS proceed with execution once task is requested

---

## Required Capabilities
1. Open and render a local HTML file
2. Capture full-page screenshot (full width)
3. Capture full-page screenshot (half width / portrait)
4. Capture screenshot of a specific HTML section
5. Save outputs to: screenshots/YYYY-MM-DD/ in project root

---

## Tooling
- Python
- Playwright (mandatory)

---

## OPTIONAL: Dependency Check & Installation
This section can be removed safely.

Before execution:
1. Try importing `playwright`
2. If not installed:
   pip install playwright
   playwright install
3. Do NOT ask for confirmation

---

## HTML File Detection (MANDATORY)

Instead of relying on browser tabs:

1. Scan project root for `.html` files
2. If only one file exists → use it
3. If multiple files exist:
   - Prefer `index.html`
   - Otherwise use the first detected file
4. If no HTML file is found:
   - Stop execution with error

---

## Root Directory Enforcement

- Use `os.getcwd()` as project root
- NEVER save outside this directory

---

## Folder Validation (MANDATORY)

1. Ensure `screenshots/` exists in root
2. Generate today's date: YYYY-MM-DD
3. Ensure subfolder exists:
   screenshots/YYYY-MM-DD/
4. Use this as output directory

---

## Naming Convention (MANDATORY)

Format:
<type>_<layout>_<timestamp>.png

Timestamp:
YYYY-MM-DD_HH-MM-SS

### Examples:
- full_width_full_2026-03-19_14-32-08.png
- half_width_full_2026-03-19_14-32-08.png
- section_main_2026-03-19_14-32-08.png

### Rules:
- full_width → desktop layout
- half_width → portrait/mobile layout
- section_<name> → selector-based
- Extract section name:
  "#main" → "main"

---

## Execution Instructions

1. Use existing `screenshot.py` if present
2. Otherwise generate it
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
- If selector not found → skip section screenshot
- If no HTML file found → stop execution
- Do NOT stop for minor issues

---

## Behavior Constraints
- No prompts
- No GUI/manual steps
- CLI-only automation

---

## Completion Criteria
Screenshots saved in:
screenshots/YYYY-MM-DD/
with correct naming format.
