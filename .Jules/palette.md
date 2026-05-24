# Palette Journal

## 2026-05-24 - Tkinter Treeview Tag Precedence for Accessibility
**Learning:** In `ttk.Treeview`, when an item has multiple tags, visual precedence for attributes (like foreground or background) is determined by the order of tags in the item's tags sequence; the FIRST tag that defines a specific attribute takes precedence. This is critical when overlapping attributes (e.g., status-based 'done' tag and priority-based background colors) are used.
**Action:** Always ensure that tags representing the most critical visual state (like 'done' for accessibility and hierarchy) are placed FIRST in the tags tuple when using `ttk.Treeview`.
