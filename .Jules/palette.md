# Palette Journal

## 2025-01-24 - Tkinter Treeview Tag Precedence
**Learning:** In `ttk.Treeview`, the order of tags in the item's tag list determines visual precedence. The last tag that defines a specific attribute (e.g., background) wins. This allows for effective "state layering" (e.g., a 'done' state overriding a 'priority' background).
**Action:** When implementing status-based styling that should override base categories, always append the status tag to the end of the tag sequence.
