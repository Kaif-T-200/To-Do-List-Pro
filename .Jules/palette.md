## 2025-05-14 - Visual Precedence in ttk.Treeview
**Learning:** In Tkinter's `ttk.Treeview`, when an item has multiple tags, the attribute definitions (like `foreground` or `background`) of the LAST tag in the sequence take precedence over earlier ones.
**Action:** Always place status-based tags (like 'done' or 'active') after priority or category tags if you want the status styling to override the category/priority colors, especially to maintain accessible color contrast.
