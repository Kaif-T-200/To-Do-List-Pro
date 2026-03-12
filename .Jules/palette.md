## 2025-05-15 - De-emphasizing Completed Tasks
**Learning:** In a list-based UI where items are color-coded by priority, marking an item as "done" needs to visually override the priority color to clearly communicate its changed status. Using a de-emphasized foreground color and a neutral background color helps focus the user's attention on remaining tasks.
**Action:** When working with tagged list components (like Tkinter's Treeview), ensure that the "completed" state tag is applied last so it takes visual precedence, and explicitly reset background colors if they were used for other states.
