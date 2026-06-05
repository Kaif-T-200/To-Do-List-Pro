# Palette Journal

## 2026-06-05 - Accessible Task De-emphasis
**Learning:** When de-emphasizing completed tasks in a multi-theme (Light/Dark) desktop application, using a static gray is insufficient. WCAG AA compliance requires theme-aware foreground colors (#595959 for light, #a9a9a9 for dark) to maintain a minimum 4.5:1 contrast ratio against the respective backgrounds.
**Action:** Always define status-based styles (like 'done') within the view refresh cycle or theme toggle logic to ensure colors are updated dynamically with the theme.
