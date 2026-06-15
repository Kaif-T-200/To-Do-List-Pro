# Palette Journal

## 2025-05-14 - Visual De-emphasis for Completed Tasks
**Learning:** In 'ttk.Treeview', visual precedence for overlapping attributes (foreground/background) is determined by the order of tags; the LAST tag that defines a specific attribute takes precedence. To maintain WCAG AA contrast (at least 4.5:1) for de-emphasized tasks against the app's background, use #595959 on #f8f9fa (Light Mode) and #a9a9a9 on #212529 (Dark Mode).
**Action:** When applying status-based styling (like 'done') over priority-based background colors, ensure the status tag is appended last and explicitly defines both foreground and background to guarantee accessibility.
