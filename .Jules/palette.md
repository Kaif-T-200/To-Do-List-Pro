## 2025-05-14 - Visual De-emphasis for Completed Tasks
**Learning:** In Tkinter `ttk.Treeview`, when multiple tags are assigned to an item, the tag configured *last* using `tag_configure` (or the one appearing last in the `tags` tuple for overlapping attributes) takes visual precedence. This allows status-based styling (e.g., "Done") to reliably override priority-based styling.
**Action:** Always ensure status-based tags are appended to the end of the `tags` tuple and their configurations are defined to properly handle both foreground and background for WCAG AA compliance.
