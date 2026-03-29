## 2025-05-15 - Treeview Task De-emphasis
**Learning:** In Tkinter `ttk.Treeview`, the tag appearing last in the `tags` tuple takes visual precedence for overlapping attributes (like background/foreground). This allows creating 'override' states like 'done' without needing to manually combine colors for every priority level.
**Action:** Always append state-based tags (e.g., 'done', 'selected', 'disabled') to the end of the tags list to ensure they correctly override default styling.
