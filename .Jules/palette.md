# Palette Journal

## 2024-05-23 - Visual hierarchy for task completion
**Learning:** Using only text (e.g., "Done") to indicate task completion fails to provide immediate visual feedback. De-emphasizing completed tasks via color (graying out) helps users quickly scan the list and focus on active items.
**Action:** Implement a 'done' tag in `ttk.Treeview` with appropriate foreground/background colors for both light and dark modes, ensuring it is applied last in the tags sequence to take visual precedence.
