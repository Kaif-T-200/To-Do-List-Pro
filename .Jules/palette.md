# Palette Journal

## 2025-05-14 - Visual De-emphasis for Completed Tasks
**Learning:** In a `ttk.Treeview`, visual precedence for overlapping attributes (like background color) is determined by the order of tags in the item's tags sequence; the LAST tag that defines a specific attribute wins. To gray out completed tasks while maintaining their priority identity in the data, the 'done' tag must be appended last and explicitly define both foreground and background colors to ensure WCAG AA contrast.
**Action:** Always apply status-based override tags last in the tags tuple for Treeview items and provide theme-aware contrast values.
