# Palette Journal

## 2026-06-14 - Visual De-emphasis for Completed Tasks
**Learning:** Using a de-emphasized color (grayed out) for completed tasks improves the visual hierarchy of the task list, allowing users to focus on active tasks while maintaining visibility of accomplishments. In `ttk.Treeview`, the last tag in the sequence takes precedence for visual attributes, so the 'done' tag should be appended last to override priority-based background colors.
**Action:** When implementing status-based row styling, ensure the status tag is applied last in the tags tuple and explicitly sets both foreground and background to maintain WCAG AA contrast ratios in both light and dark modes.
