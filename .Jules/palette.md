# Palette Journal

## 2025-05-14 - Visual Precedence in Tkinter Treeview Tags
**Learning:** In `ttk.Treeview`, when an item has multiple tags, visual precedence for overlapping attributes (foreground/background) is determined by the order of tags in the item's tags sequence; the FIRST tag that defines a specific attribute takes precedence.
**Action:** To ensure a status-based style (like 'done') overrides priority-based colors, prepend the status tag to the tags tuple.
