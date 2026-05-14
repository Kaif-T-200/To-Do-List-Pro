## 2025-05-15 - Visual Precedence in Treeview Tags
**Learning:** In Tkinter `ttk.Treeview`, when multiple tags are applied to an item, the last tag in the sequence that defines a specific attribute (like background or foreground) takes precedence. This is crucial for layering "status" styles (like 'Done') over "category" or "priority" styles.
**Action:** Always append status-based tags (e.g., 'done') to the end of the `tags` tuple to ensure they correctly override priority or category colors for de-emphasis.
