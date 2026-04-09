# Palette's UX/Accessibility Journal

## 2024-05-24 - [Task De-emphasis & Contrast]
**Learning:** Visually de-emphasizing completed tasks reduces cognitive load. However, maintaining WCAG AA contrast (4.5:1 or higher) is critical when using gray text. In this app, #595959 against #f8f9fa provides a 7:1 ratio.
**Action:** Use 'done' tags with #595959 foreground and ensure they override priority colors by being last in the tag tuple.

## 2024-05-24 - [Treeview Tag Precedence]
**Learning:** In Tkinter's `ttk.Treeview`, the last tag in the `tags` tuple takes visual precedence for shared attributes.
**Action:** Always place the 'done' tag last in the `tags` tuple to ensure it overrides priority-based background colors.

## 2024-05-24 - [Treeview Interaction Precision]
**Learning:** Double-click events on Treeview can trigger on headers or empty space if not restricted.
**Action:** Use `self.tree.identify_region(event.x, event.y) == 'cell'` to ensure interactions only trigger on data rows.
