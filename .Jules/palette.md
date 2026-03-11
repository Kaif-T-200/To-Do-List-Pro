## 2025-05-14 - [Contrast in Overlapping Tags]
**Learning:** When using multiple tags in a Tkinter `ttk.Treeview` to indicate different states (e.g., priority and completion), tags applied later override previous ones. However, changing only the foreground color for a "done" state while keeping a high-contrast background (like red for high priority) can lead to accessibility (WCAG) violations.
**Action:** Always ensure both foreground and background are set on high-priority override tags (like 'done') to guarantee legible contrast, or use other visual cues like strikethroughs if supported.
