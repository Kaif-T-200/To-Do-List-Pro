## 2026-07-15 - Double-Click Region Checking for Treeview Actions
**Learning:** In Tkinter `ttk.Treeview`, double-click (`<Double-1>`) events fire on any region of the widget, including table headings and empty whitespace. Checking `self.tree.identify_region(event.x, event.y) == "cell"` before executing row actions prevents erroneous triggers when users double-click column headers or empty table area.
**Action:** Always filter `<Double-1>` events using `identify_region` when binding row-level actions on Treeview widgets.
