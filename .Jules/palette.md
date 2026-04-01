## 2025-05-15 - Treeview Event Identification
**Learning:** When binding double-click events to a `ttk.Treeview`, the event triggers even when clicking on column headers or empty space. This can lead to confusing behavior (like "select an item" warnings) if not filtered.
**Action:** Use `tree.identify_region(event.x, event.y) == 'cell'` in the event handler to ensure the action only applies when a data row is actually clicked.
