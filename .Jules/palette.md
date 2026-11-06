# Palette's UX Journal

## 2026-11-06 - Visual Hierarchy and Completed Task State in Tkinter Treeview
**Learning:** In task lists with color-coded priority backgrounds (such as red for High priority), completed tasks remain visually urgent and loud if the priority color is maintained after completion. De-emphasizing completed tasks with a muted, neutral background and lower-contrast foreground (while strictly meeting WCAG AA contrast) restores clear visual hierarchy so users can focus on active work while still seeing their accomplishments. In Tkinter's `ttk.Treeview`, the first matching tag in an item's tag sequence takes precedence, so prepending `'done'` before the priority tag cleanly overrides the urgent priority background.
**Action:** When implementing status overrides over multi-tag items in `ttk.Treeview`, always place the status override tag first in the tag tuple, and provide theme-aware muted colors for both light and dark modes.
