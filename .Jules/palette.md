## 2026-07-15 - Double-Click Quick Toggle for Task Completion
**Learning:** Users naturally expect desktop list views to support direct interaction shortcuts like double-clicking a row to toggle completion state or open primary actions, rather than relying solely on action buttons.
**Action:** When working with desktop tree views or data grids, bind `<Double-1>` events with appropriate region checks (`tree.identify_region(event.x, event.y) == 'cell'`) to trigger standard primary actions cleanly without interfering with headers or scrollbars.
