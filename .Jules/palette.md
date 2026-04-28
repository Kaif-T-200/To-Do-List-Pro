## 2025-05-14 - Standard Desktop Interactions
**Learning:** Implementing standard desktop shortcuts (Double-click to edit, Delete key to remove) significantly improves user efficiency. For Treeview widgets, it's critical to use `identify_region` to ensure these actions only trigger on data cells, preventing unintended behavior when clicking headers or empty areas.
**Action:** Always implement standard keyboard and mouse shortcuts for list-based UI components and use precise region detection for event handlers.
