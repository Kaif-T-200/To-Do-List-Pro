## 2026-07-15 - Visual Hierarchy for Completed Tasks
**Learning:** Using a de-emphasized color (grayed out) for completed tasks improves the visual hierarchy of the task list, allowing users to focus on active tasks while maintaining visibility of accomplishments. To maintain WCAG AA compliance, the contrast ratio must remain above 4.5:1.
**Action:** Implement a 'done' tag in ttk.Treeview with foreground #595959 on background #f8f9fa in light mode (~6.6:1) and foreground #a9a9a9 on background #212529 in dark mode (~6.4:1).
