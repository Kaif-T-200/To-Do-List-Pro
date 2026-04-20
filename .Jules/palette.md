## 2025-05-15 - De-emphasize completed tasks
**Learning:** In Tkinter's `ttk.Treeview`, when multiple tags are applied to an item, the tag configured *last* using `tag_configure` takes visual precedence for overlapping attributes (like background/foreground). To correctly de-emphasize completed tasks while maintaining their priority background for pending ones, the 'done' tag must be configured after the priority tags.
**Action:** Always ensure state-based tags (like 'done') are configured after category or priority-based tags to ensure they correctly override the default visual state.
