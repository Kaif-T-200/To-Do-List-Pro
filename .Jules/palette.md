# Palette's UX Journal

## 2025-05-14 - Visual De-emphasis of Completed Tasks
**Learning:** In a task management UI, visually de-emphasizing completed tasks (e.g., using grayed-out text) helps users focus on remaining work, but it must be done without sacrificing accessibility (maintaining WCAG AA contrast ratios). In Tkinter's `ttk.Treeview`, the order of tags determines visual precedence.
**Action:** When implementing 'Done' states, use `#595959` foreground for Light Mode and `#a9a9a9` for Dark Mode, and ensure the 'done' tag is applied last to override priority-based background colors if necessary, or configure it to handle both.
