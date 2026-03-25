## 2025-03-25 - Treeview Tag Precedence for Completed Tasks
**Learning:** In Tkinter's `ttk.Treeview`, the visual precedence of tags is determined by their order in the `tags` tuple, with the last tag taking precedence. For task lists with priority-based background colors, a "done" state must be the last tag to ensure it correctly overrides the priority colors and applies its own styling (like a gray foreground).
**Action:** Always append state-based tags (like "done", "active", "selected") after category-based tags (like "priority") to ensure correct visual hierarchy.
