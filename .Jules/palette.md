# Palette Journal

## 2026-06-11 - [Visual De-emphasis for Completed Tasks]
**Learning:** In a `ttk.Treeview`, using tags to de-emphasize completed items (graying them out) requires explicit background color definitions to ensure WCAG AA contrast compliance when those items also have priority-based background colors. The last tag in the sequence takes precedence for visual attributes.
**Action:** Always apply status-based tags (like 'done') after category/priority tags and explicitly set both foreground and background colors to guarantee accessible contrast ratios across different UI themes.
