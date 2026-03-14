# PALETTE'S JOURNAL - CRITICAL LEARNINGS ONLY

## 2026-03-14 - Visual De-emphasis with Tag Precedence
**Learning:** In Tkinter's `ttk.Treeview`, when multiple tags are applied to an item, the configuration of the last tag in the sequence takes visual precedence for overlapping attributes. This is crucial for states like 'Done' that should override default priority-based styling. Additionally, maintaining WCAG AA contrast (e.g., #595959 on #f8f9fa) for de-emphasized text requires explicit background setting when using tags that otherwise only change the background.
**Action:** Always append state-based tags (like 'done') to the end of the tags tuple and explicitly define both foreground and background colors to ensure accessibility and proper visual layering.
