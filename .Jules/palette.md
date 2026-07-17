## 2026-07-15 - Visual Hierarchy of Completed Tasks
**Learning:** Using a de-emphasized color (grayed out) for completed tasks improves the visual hierarchy of the task list, allowing users to focus on active tasks while maintaining visibility of accomplishments.
**Action:** Implement a 'done' tag in the treeview that overrides priority colors with a de-emphasized style. To maintain WCAG AA compliance, use foreground #595959 on background #f8f9fa in light mode (~6.6:1 contrast), and foreground #a9a9a9 on background #212529 in dark mode (~6.4:1 contrast).
