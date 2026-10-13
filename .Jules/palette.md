## 2026-07-15 - Double-click Quick Toggling of Task Status in Tkinter Treeview

**Learning:** In desktop list applications, double-clicking rows is a standard, low-friction gesture for taking primary actions (like toggling completion status). However, binding directly to `<Double-1>` on `ttk.Treeview` without checking `tree.identify_region(event.x, event.y) == "cell"` can cause unintended actions when users double-click table headers or empty space below rows.
**Action:** Always check `tree.identify_region(event.x, event.y) == "cell"` in Tkinter Treeview double-click handlers before acting on the selection.
