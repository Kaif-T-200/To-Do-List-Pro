## 2026-07-15 - Double-Click Region Checking in Tkinter Treeview
**Learning:** In Tkinter `ttk.Treeview`, binding `<Double-1>` events fires on the entire widget including header columns and empty background area. Checking `tree.identify_region(event.x, event.y) == "cell"` prevents accidental actions or warning dialogs when users double-click column headers or empty space.
**Action:** Always filter Treeview double-click events with `identify_region` to ensure actions are only triggered on actual data cells.
