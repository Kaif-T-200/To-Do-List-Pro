# Palette's Journal - Critical Learnings Only

## 2026-11-01 - Visual Hierarchy for Completed Items in Tkinter Treeview
**Learning:** In Tkinter `ttk.Treeview`, items retain strong background highlight colors when priority tags are applied. Completed tasks ("Done") compete visually with pending actionable tasks if they retain bright red/yellow/green fills. Prepending a dedicated `'done'` tag before priority tags allows muted background and foreground styling to override priority fills while preserving WCAG AA compliant contrast in both light (#595959 on #e9ecef, ~5.9:1) and dark mode (#a9a9a9 on #2c3035, ~5.6:1).
**Action:** When overriding multi-colored row styles in Tkinter `ttk.Treeview`, prepend status override tags before priority tags so that visual precedence takes effect cleanly without removing task metadata.
