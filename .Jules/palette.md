## 2026-04-06 - Implement standard desktop shortcuts
**Learning:** UX for list-based UI components like Treeview is significantly enhanced by implementing standard desktop shortcuts (Double-click to edit, Delete key to remove).
**Action:** When working with Treeview or similar widgets, always use `identify_region(event.x, event.y) == 'cell'` in double-click handlers to ensure the action only triggers on data rows. Update callback signatures to accept an optional `event=None` for compatibility with both buttons and bindings.
