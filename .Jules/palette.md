# Palette Journal

## 2025-05-14 - Visual Precedence in ttk.Treeview Tags
**Learning:** In Tkinter's `ttk.Treeview`, when multiple tags are applied to an item, the last tag in the sequence that defines a specific attribute (like foreground or background) takes precedence. To visually de-emphasize completed tasks while they still have priority-based background colors, the 'done' tag must be appended last.
**Action:** Always append state-based tags (like 'done' or 'disabled') after category/priority tags, and ensure they explicitly define both foreground and background to maintain WCAG contrast ratios regardless of underlying styles.
