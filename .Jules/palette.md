## 2025-05-14 - Visual De-emphasis for Completed Tasks
**Learning:** In Tkinter `ttk.Treeview`, the tag appearing last in the `tags` tuple takes visual precedence for overlapping attributes. This is crucial for implementing state-based styling (like "Done") that should override category or priority-based background colors.
**Action:** Always place state-override tags (like "done", "selected", "disabled") at the end of the tags list in Tkinter Treeview widgets.
