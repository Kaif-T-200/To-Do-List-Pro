# Palette Journal

## 2025-05-14 - Accessible De-emphasis in Tkinter Treeview
**Learning:** In ttk.Treeview, the last tag in the sequence takes visual precedence for attributes like foreground/background. To ensure WCAG AA compliance when de-emphasizing tasks (e.g., "Done" status) that might overlap with priority-based background colors (Red/Yellow/Green), the "done" tag must explicitly set both foreground and background to neutral theme-appropriate colors.
**Action:** Always append status-based styling tags last and define both FG and BG to override any previous tag styles while maintaining accessible contrast ratios.
