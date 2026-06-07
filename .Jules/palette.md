# Palette Journal

## 2025-05-14 - Overriding priority styles for completed tasks in ttk.Treeview
**Learning:** In a `ttk.Treeview`, the visual precedence of tags is determined by their order in the item's tags sequence; the LAST tag that defines a specific attribute (like background) takes precedence. Additionally, theme-dependent styles must be configured within the list refresh method to ensure they correctly adapt when the user toggles between Light and Dark modes.
**Action:** Always append status override tags (e.g., 'done') last in the tags tuple and explicitly define both foreground and background colors to maintain WCAG AA accessibility when overlapping with other styled rows.
