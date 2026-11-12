# Palette's UX/Accessibility Journal

## 2026-11-12 - Treeview Completed Task Visual Hierarchy & Tag Precedence
**Learning:** In Tkinter's `ttk.Treeview`, when multiple tags configure overlapping attributes (such as background and foreground), the FIRST tag in an item's tag sequence takes precedence. Configuring Treeview tags (`tag_configure`) inside rapid refresh loops (like search `trace`) causes unnecessary re-configuration overhead; configuring them once during initialization and theme toggling provides smoother performance while supporting WCAG AA compliant contrast (#595959 on #e9ecef for light mode, #a9a9a9 on #2c3035 for dark mode).
**Action:** Place override tags like `'done'` first in item tag tuples (`('done', priority)`), and extract tag configuration into a dedicated theme-aware method called on startup and mode toggles.
