# Palette Journal

## 2025-05-14 - Theme-Aware Status Overrides in ttk.Treeview
**Learning:** When using `ttk.Treeview.tag_configure` to visually de-emphasize items (e.g., "Done" tasks), the last tag in the `tags` tuple takes precedence for defined attributes. To maintain WCAG AA compliance during theme switches (Light/Dark mode), colors must be explicitly re-configured within the list refresh method to ensure they adapt to the current background.
**Action:** Always wrap tag configurations that depend on application state (like `self.dark_mode`) inside the UI refresh logic, and ensure the status-based tag is appended last to the item's tags list.
