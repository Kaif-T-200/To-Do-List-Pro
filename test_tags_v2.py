import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack()

# Configure tags in this order
tree.tag_configure("red", background="red")
tree.tag_configure("blue", background="blue")

# Item 1: red then blue
item1 = tree.insert("", "end", text="Red then Blue", tags=("red", "blue"))
# Item 2: blue then red
item2 = tree.insert("", "end", text="Blue then Red", tags=("blue", "red"))

def check():
    # Unfortunately we can't easily query the actual displayed color via API
    # but we can check if it runs without error.
    # From my experience with Tkinter, the LAST tag in the tuple wins for Treeview.
    print("Item 1 tags:", tree.item(item1, "tags"))
    print("Item 2 tags:", tree.item(item2, "tags"))
    root.destroy()

root.after(100, check)
root.mainloop()
