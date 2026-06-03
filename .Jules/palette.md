# Palette Journal

## 2025-05-15 - Visual De-emphasis with Priority Backgrounds
**Learning:** In a `ttk.Treeview` where background colors indicate priority, simply changing the foreground color for completed tasks is insufficient because it may not provide enough contrast against all priority colors. Explicitly resetting the background to a neutral theme color and applying the 'done' tag last ensures both WCAG AA contrast and clear visual de-emphasis.
**Action:** When overriding multi-colored row styles (like priority levels), always apply the status override tag last in the tags tuple and explicitly define both foreground and background colors to ensure accessibility.
