## 2026-07-15 - De-emphasize Completed Tasks for Clearer Visual Hierarchy

**Learning:** Completed tasks retained high-contrast priority background colors (red/yellow/green), creating visual noise and cluttering the active task list. De-emphasizing completed tasks with neutral background and grayed-out foreground text improves visual hierarchy and allows users to focus on active tasks while maintaining visible accomplishments.
**Action:** When styling completed items in `ttk.Treeview`, prepend a `done` tag with neutral background (`#f8f9fa` in light mode, `#212529` in dark mode) and accessible gray foreground text (`#595959` in light mode, `#a9a9a9` in dark mode) to ensure WCAG AA compliance (> 4.5:1 contrast ratio).
