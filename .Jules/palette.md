## 2025-05-15 - Visually de-emphasizing completed tasks
**Learning:** In list-based task managers, completed items can create visual noise if they maintain the same high-contrast styles as active tasks. De-emphasizing them helps users focus on remaining work.
**Learning:** In Tkinter `ttk.Treeview`, when multiple tags define overlapping attributes (like background), the *last* tag in the list takes precedence. To override priority colors, the "done" tag must be appended at the end.
**Action:** Use a "done" tag in Tkinter Treeview (appended to the end of the tags list) to override background/foreground colors with neutral tones for completed items, ensuring WCAG AA compliance for the de-emphasized state.
