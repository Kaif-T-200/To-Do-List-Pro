# Palette Journal

## 2024-05-23 - Visual precedence in Treeview tags
**Learning:** In Tkinter's ttk.Treeview, when multiple tags are applied to an item, the last tag in the sequence that defines a specific attribute (like foreground or background) takes precedence. This allows for layering styles, such as a base 'priority' color and a 'done' overlay.
**Action:** Always append status-based tags (like 'done' or 'selected') to the end of the tags list to ensure they visually override base styles.
