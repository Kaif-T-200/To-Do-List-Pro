# Palette Journal
## 2026-06-10 - Visual De-emphasis for Completed Tasks
**Learning:** In Tkinter's `ttk.Treeview`, the visual precedence for overlapping attributes (like foreground or background colors) is determined by the order of tags in the item's tags sequence; the LAST tag that defines a specific attribute takes precedence. To visually override priority-based background colors when a task is completed, the 'done' tag must be appended last and explicitly define both foreground and background.
**Action:** Always append state-based override tags (like 'done' or 'selected') after category/priority tags in `ttk.Treeview` to ensure they correctly represent the item's current state.
