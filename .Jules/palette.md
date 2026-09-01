## 2026-07-15 - Synchronize Container Backgrounds & Entry Cursors in Tkinter Dark Mode

**Learning:** When toggling dark mode in a Tkinter desktop application, changing only the main window (`root`) background creates visible light borders/gaps around sub-containers (e.g. `Frame`, `Label`, `Entry`). Furthermore, dark `Entry` backgrounds hide the default black text insertion cursor unless `insertbackground='white'` is explicitly configured.

**Action:** Always bind inner sub-containers (`Frame`, `Label`, `Entry`) to instance variables so that theme switching methods explicitly update their background/foreground colors and set `insertbackground` appropriately on text inputs.
