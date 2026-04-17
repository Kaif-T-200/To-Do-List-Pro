## 2024-05-16 - Visual de-emphasis for completed tasks

**Learning:** In Tkinter's `ttk.Treeview`, tag priority is determined by the order of tags in the `tags` tuple passed during item insertion; the first tag in the list has the highest priority for visual attributes like `foreground` and `background`. To ensure a 'done' status correctly overrides priority-based colors, it should be placed at the beginning of the tags tuple. Additionally, maintaining WCAG AA compliance (4.5:1 or 7:1 contrast ratio) is essential for de-emphasized text in both light and dark modes.

**Action:** Always place status-based tags (like 'done' or 'active') at the beginning of the `tags` tuple in `Treeview.insert` if they are meant to override other styles. Verify contrast ratios using specific hex codes (#595959 for light mode, #a9a9a9 for dark mode) against the background.
