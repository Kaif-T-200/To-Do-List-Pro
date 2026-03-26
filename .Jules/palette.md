## 2025-05-15 - Treeview Tag Precedence for Accessibility
**Learning:** In Tkinter's `ttk.Treeview`, the last tag in the `tags` tuple takes visual precedence. This is crucial for accessibility when a "done" state needs to visually override priority-based background colors (red/yellow/green) to ensure high contrast and a clear "de-emphasized" state.
**Action:** Always append state-based tags (like 'done', 'selected', 'disabled') to the end of the tags tuple in `Treeview.insert` or `item` calls to ensure they override default row styling.
