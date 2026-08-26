## 2026-07-15 - Dark Mode Container Styling and Text Cursor Visibility
**Learning:** In Tkinter desktop applications, toggling dark mode on the root window does not automatically update child container frames or Entry text cursors, creating bright light-mode patches and invisible cursors in dark mode.
**Action:** Always save child frames/entries as instance attributes and explicitly update background, text foreground, and `insertbackground='white'` on dark mode toggle.
