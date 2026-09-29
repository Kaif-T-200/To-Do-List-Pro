## 2026-07-15 - Double-Click Quick Toggle for Tkinter Treeview
**Learning:** In Tkinter `ttk.Treeview`, double-clicking tasks without verifying the click region can trigger unintended actions on table headers or empty space. Using `tree.identify_region(event.x, event.y) == "cell"` ensures interaction only occurs when clicking valid row data.
**Action:** Always filter Treeview double-click events using `identify_region` before performing row-level updates or status toggles.
