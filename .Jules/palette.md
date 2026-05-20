# Palette Journal

## 2025-05-15 - Visual De-emphasis for Completed Tasks
**Learning:** In Tkinter Treeviews, visual precedence is determined by tag order. To visually de-emphasize items (e.g., "done" status) while maintaining priority colors, the "done" tag must explicitly override both foreground and background to ensure WCAG AA contrast (e.g., #595959 on #f8f9fa for light mode).
**Action:** Apply the "done" tag last in the tags tuple and re-configure it within the refresh loop to ensure it reacts to theme changes.
