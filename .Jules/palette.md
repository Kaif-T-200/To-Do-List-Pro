## 2025-05-14 - De-emphasize completed tasks
**Learning:** Completed tasks should be visually distinguished from active ones to reduce cognitive load. Using a muted gray color for finished tasks helps users focus on remaining work. When using overlapping tags in Tkinter's Treeview, tag configuration order determines visual precedence.
**Action:** Use a 'done' tag with accessible gray foreground (`#595959` for light, `#a9a9a9` for dark) and explicitly set the background to match the theme to ensure it overrides priority-based background colors.
