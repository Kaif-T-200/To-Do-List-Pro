## 2026-07-15 - Dark Mode Entry Cursor Visibility and Container Frame Consistency
**Learning:** In Tkinter, toggling dark mode on container frames (`tk.Frame`) and input widgets (`tk.Entry`) requires explicitly updating `bg`, `fg`, and `insertbackground`. Without updating `insertbackground="white"`, the text editing cursor remains black and becomes invisible against dark input backgrounds.
**Action:** Always store container frames and input widgets as instance attributes and update their background, foreground, and insertion cursor colors when toggling themes.
