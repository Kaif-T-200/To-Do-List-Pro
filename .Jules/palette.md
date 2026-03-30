# Palette's UX/Accessibility Journal

## 2025-05-14 - Treeview Tag Precedence for Status States
**Learning:** In Tkinter's `ttk.Treeview`, when multiple tags are applied to an item, the tag that appears *last* in the `tags` tuple takes visual precedence for overlapping attributes (like background or foreground).
**Action:** Always place status-based tags (like 'done' or 'disabled') after priority or category tags in the `tags` tuple to ensure the final visual state correctly reflects the task's status.
