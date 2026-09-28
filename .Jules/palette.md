## 2026-07-15 - Double-Click Quick Toggle for Task Completion Status
**Learning:** In desktop list views (like Tkinter `ttk.Treeview`), users expect direct double-click interactions on table rows to toggle primary state (e.g., Pending vs. Done). Restricting event handlers with `identify_region` checks prevents unintended state changes when users click column headers or empty whitespace.
**Action:** Always check `identify_region` on click/double-click events in Tkinter Treeviews before triggering row-level actions, and ensure state toggles support reversible workflow (e.g. Done <-> Pending).
