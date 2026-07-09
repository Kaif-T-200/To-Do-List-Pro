import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack()

tree.tag_configure("red", background="red")
tree.tag_configure("blue", background="blue")

tree.insert("", "end", text="Red then Blue", tags=("red", "blue"))
tree.insert("", "end", text="Blue then Red", tags=("blue", "red"))

def print_tags():
    print("Tags for item 1:", tree.item(tree.get_children()[0], "tags"))
    print("Tags for item 2:", tree.item(tree.get_children()[1], "tags"))

root.after(100, print_tags)
root.after(500, root.destroy)
root.mainloop()
