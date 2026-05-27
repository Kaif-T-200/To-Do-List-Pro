# Palette Journal

## 2025-05-14 - Visual De-emphasis for Completed Tasks
**Learning:** In Tkinter `ttk.Treeview`, the order of tags in the item's tags sequence determines visual precedence; the LAST tag that defines a specific attribute (like foreground or background) takes precedence. For accessibility (WCAG AA), completed tasks should be dimmed (e.g., #595959 on light, #a9a9a9 on dark) while maintaining a neutral background to ensure contrast.
**Action:** Always append the 'done' or 'disabled' state tags last in the Treeview tag list and ensure they explicitly set both foreground and background to maintain accessible contrast ratios regardless of underlying row colors.
