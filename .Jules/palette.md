## 2025-05-15 - [Subdued Visual Feedback for Completed Tasks]
**Learning:** In list-based applications, the absence of visual distinction for completed tasks can lead to a cluttered and overwhelming interface. Providing a subdued visual state (e.g., grayed-out text and theme-aware backgrounds) immediately helps users distinguish between active and finished work. In Tkinter's `ttk.Treeview`, ensuring the "done" tag is last in the `tags` tuple allows it to correctly override priority-based styling.

**Action:** Always implement a de-emphasized visual state for completed or inactive items in list components. Ensure consistent contrast ratios for all states (e.g., #595959 for light mode, #a9a9a9 for dark mode) to maintain accessibility while signaling a "finished" status.
