## 2026-07-15 - Double-Click Task Status Toggle
**Learning:** Double-clicking items in a list view (`ttk.Treeview`) is a natural desktop UX pattern for quick status updates (toggling between Pending and Done). Checking `tree.identify_region(event.x, event.y)` ensures clicks on column headers or empty space do not trigger unwanted status toggles.
**Action:** When implementing list interactions in Tkinter desktop applications, bind `<Double-1>` and check `identify_region` before executing row action.
