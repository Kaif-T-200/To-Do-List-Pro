# Palette Journal

## 2025-01-24 - Visual De-emphasis of Completed Tasks
**Learning:** In Tkinter's `ttk.Treeview`, visual precedence for overlapping attributes is determined by the order of tags; the last tag wins. To visually de-emphasize completed tasks that already have priority-based background colors, the 'done' tag must be applied last and explicitly define both foreground and background colors to ensure WCAG AA compliance (contrast ratio >= 4.5:1).
**Action:** Always append status override tags last in the Treeview and explicitly set both foreground and background colors to maintain accessibility across different priority levels and UI themes.
