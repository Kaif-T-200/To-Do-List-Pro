## 2026-03-20 - Theme-Aware Visual States in Treeview
**Learning:** In Tkinter's `ttk.Treeview`, item styling via tags must be dynamically updated when toggling themes (like Dark Mode) because tag configurations are global to the widget and not automatically linked to parent widget background changes.
**Action:** When implementing theme toggles, ensure any custom tags (like 'done' or 'priority') are re-configured with theme-appropriate colors within the refresh or toggle logic.
