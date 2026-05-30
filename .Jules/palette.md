# Palette Journal

## 2026-05-30 - Precision in Treeview Interactions
**Learning:** Binding events like <Double-1> to a ttk.Treeview triggers on the entire widget, including headers and empty space. Without a region check, this can lead to unexpected behavior (e.g., trying to edit a header).
**Action:** Always use self.tree.identify_region(event.x, event.y) == 'cell' within event handlers to restrict actions to data rows.
