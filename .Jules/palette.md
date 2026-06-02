# Palette Journal

## 2025-05-15 - Treeview Tag Precedence
**Learning:** In `ttk.Treeview`, the order of tags in the `tags` tuple/list determines visual precedence for overlapping attributes (like foreground or background). The LAST tag in the sequence that defines a specific attribute takes precedence.
**Action:** To ensure a 'done' style (e.g., grayed out text and neutral background) overrides priority-based colors, append the 'done' tag to the end of the tags list and explicitly define both foreground and background for the 'done' tag to ensure proper contrast.
