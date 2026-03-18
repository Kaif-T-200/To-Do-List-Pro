## 2024-05-24 - Overriding priority colors for completed tasks
**Learning:** In Tkinter `ttk.Treeview`, the visual precedence of tags is determined by their order in the `tags` tuple passed to `insert()`. The last tag's attributes override previous ones for the same property (e.g., background color).
**Action:** Always ensure the 'done' tag is the final element in the tags list to correctly de-emphasize completed items regardless of their priority level.
