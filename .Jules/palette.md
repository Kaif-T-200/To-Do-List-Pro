## 2025-05-14 - Visual de-emphasis for completed tasks
**Learning:** In Tkinter's `ttk.Treeview`, the order of tags matters for visual precedence. When multiple tags apply (e.g., priority and 'done'), the tag appearing last in the `tags` tuple overrides conflicting styles of previous tags.
**Action:** Always append state-specific tags (like 'done' or 'selected') after category/priority tags to ensure they take visual precedence.

## 2025-05-14 - Adaptive Colors for Custom Tags
**Learning:** Custom tags in `ttk.Treeview` do not automatically update when the application's theme or mode changes. They must be re-configured manually within the refresh or toggle logic.
**Action:** Include `tag_configure` calls for custom tags within the main UI refresh loop or theme toggle function to maintain WCAG compliance across all modes.
