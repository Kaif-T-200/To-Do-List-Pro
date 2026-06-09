# Palette Journal
## 2026-06-09 - Tkinter Treeview Tag Precedence for Status Overlays
**Learning:** In `ttk.Treeview`, when multiple tags are applied to an item, the LAST tag in the sequence that defines a specific attribute (like `background` or `foreground`) takes visual precedence. To visually de-emphasize a completed task that already has a priority-based background color, the 'done' tag must be appended last and must explicitly define its own background (matching the theme) to ensure WCAG AA contrast for the grayed-out text.
**Action:** Always append status-based override tags (e.g., 'done', 'disabled') to the end of the tags tuple and define both foreground and background colors to guarantee accessibility regardless of underlying row styles.
