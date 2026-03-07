# Palette's UX/Accessibility Journal

## 2025-05-14 - Initial UX Standards
**Learning:** Standard desktop shortcuts (Double-click to edit, Delete key to remove) for list-based UI components like Treeview significantly improve efficiency for power users.
**Action:** Always implement these shortcuts when using Treeview or similar list components.

**Learning:** Visually de-emphasizing completed tasks (e.g., using a 'done' tag with gray foreground) improves list scanability and helps users focus on remaining work.
**Action:** Use lower contrast or strike-through for completed/inactive items in a list.

**Learning:** Automatically focusing the primary input or search field on application launch reduces the number of clicks required to start interacting with the app.
**Action:** Ensure `focus_set()` is called on the main entry point during initialization.

**Learning:** Keyboard accessibility is crucial. Icon-only buttons need ARIA labels and all interactive elements must be reachable via keyboard.
**Action:** Use `aria-label` for web or descriptive tooltips/text for desktop, and verify tab order.
