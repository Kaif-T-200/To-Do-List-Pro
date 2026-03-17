## 2025-05-14 - Visual Precedence for Completed Tasks
**Learning:** In Tkinter's `ttk.Treeview`, the visual precedence for overlapping tag attributes (like background/foreground) is determined by the order in the `tags` tuple. The tag appearing last takes precedence.
**Action:** When implementing status-based overrides (e.g., 'done'), ensure they are appended to the end of the `tags` list to correctly override default state styling.
