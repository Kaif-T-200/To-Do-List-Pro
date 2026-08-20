## 2026-07-15 - Visual Hierarchy for Completed Tasks in Tkinter Treeview

**Learning:** When using `ttk.Treeview` with row background highlighting (such as priority colors), completed tasks can visually overwhelm active tasks if priority colors remain bright. Overriding background and foreground with a de-emphasized status tag (`done`) listed *first* in the tag tuple ensures proper visual hierarchy while maintaining WCAG AA contrast compliance (~6.6:1 in light mode, ~6.4:1 in dark mode).

**Action:** Whenever implementing status overrides in `ttk.Treeview`, place the status tag first in the item's tag sequence, and explicitly set neutral background colors matching the app canvas to ensure text contrast ratios remain WCAG AA compliant.
