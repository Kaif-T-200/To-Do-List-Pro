## 2026-07-15 - Double-click quick toggle for task status in Tkinter Treeview
**Learning:** In table/list views like Tkinter's `ttk.Treeview`, double-clicking a row is an intuitive desktop shortcut to toggle state (such as Pending <-> Done) or open detail views. Checking `tree.identify_region(event.x, event.y) == "cell"` prevents accidental triggering when double-clicking headers or empty space.
**Action:** Always verify `identify_region` before executing row-level actions on double-click, and ensure status updates support bidirectional toggling.
