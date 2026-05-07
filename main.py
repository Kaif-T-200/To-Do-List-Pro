# MADE BY KAIF TARASAGAR
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import json
import os# MADE BY KAIF TARASAGAR

DATA_FILE = "tasks.json"
# MADE BY KAIF TARASAGAR
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Pro")# MADE BY KAIF TARASAGAR
        self.root.geometry("750x550")
        self.root.config(bg="#f8f9fa")
# MADE BY KAIF TARASAGAR
        self.tasks = []
        self.dark_mode = False  
        self.load_tasks()

        self.title_label = tk.Label(
            root,
            text="📝 To-Do List Pro",
            font=("Arial", 22, "bold"),
            bg="#f8f9fa",
            fg="#212529"
        )# MADE BY KAIF TARASAGAR
        self.title_label.pack(pady=10)

        search_frame = tk.Frame(root, bg="#f8f9fa")# MADE BY KAIF TARASAGAR
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="🔍 Search:", font=("Arial", 12), bg="#f8f9fa").pack(side=tk.LEFT, padx=5)

        self.search_var = tk.StringVar()# MADE BY KAIF TARASAGAR
        self.search_var.trace("w", lambda *args: self.refresh_list())

        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=40, font=("Arial", 12))
        search_entry.pack(side=tk.LEFT, padx=5)
# MADE BY KAIF TARASAGAR
        self.tree = ttk.Treeview(root, columns=("Task", "Category", "Priority", "Status"), show="headings", height=12)
        self.tree.heading("Task", text="Task") ; self.tree.column("Task", width=260)
        self.tree.heading("Category", text="Category") ; self.tree.column("Category", width=120)
        self.tree.heading("Priority", text="Priority") ;  self.tree.column("Priority", width=100)
        self.tree.heading("Status", text="Status") ; self.tree.column("Status", width=100)# MADE BY KAIF TARASAGAR
        self.tree.pack(pady=10)
        btn_frame = tk.Frame(root, bg="#f8f9fa")
        btn_frame.pack(pady=10)
# MADE BY KAIF TARASAGAR
        tk.Button(btn_frame, text="➕ Add", width=14, command=self.add_task, bg="#0d6efd", fg="white").grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="✏️ Update", width=14, command=self.update_task, bg="#ffc107", fg="black").grid(row=0, column=1, padx=6)
        tk.Button(btn_frame, text="✅ Mark Done", width=14, command=self.mark_done, bg="#198754", fg="white").grid(row=0, column=2, padx=6)
        tk.Button(btn_frame, text="🗑️ Delete", width=14, command=self.delete_task, bg="#dc3545", fg="white").grid(row=0, column=3, padx=6)
        tk.Button(btn_frame, text="💾 Save ", width=14, command=self.save_as_txt, bg="#6f42c1", fg="white").grid(row=0, column=4, padx=6)
        tk.Button(btn_frame, text="🌙 Toggle Dark Mode", width=18, command=self.toggle_dark_mode, bg="#343a40", fg="white").grid(row=0, column=5, padx=6)
# MADE BY KAIF TARASAGAR
        self.status_var = tk.StringVar()
        self.status_label = tk.Label(root, textvariable=self.status_var, font=("Arial", 11), bg="#f8f9fa", fg="#495057")
        self.status_label.pack(side=tk.BOTTOM, pady=5)
# MADE BY KAIF TARASAGAR
        self.refresh_list()
    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter your new task:")
        if not task_name:
            return
# MADE BY KAIF TARASAGAR
        category_window = tk.Toplevel(self.root)
        category_window.title("Task Details")
        category_window.geometry("320x220")
        category_window.grab_set()
# MADE BY KAIF TARASAGAR
        tk.Label(category_window, text="Choose Category:", font=("Arial", 12)).pack(pady=5)
        category_var = tk.StringVar(value="General")
        categories = ["Work", "Study", "Personal", "Shopping", "General", "Other"]
        ttk.Combobox(category_window, textvariable=category_var, values=categories, state="readonly").pack(pady=5)# MADE BY KAIF TARASAGAR

        tk.Label(category_window, text="Select Priority:", font=("Arial", 12)).pack(pady=5)
        priority_var = tk.StringVar(value="Low")
        priorities = ["High", "Medium", "Low"]
        ttk.Combobox(category_window, textvariable=priority_var, values=priorities, state="readonly").pack(pady=5)
# MADE BY KAIF TARASAGAR
        def save_task():
            chosen_category = category_var.get()
            chosen_priority = priority_var.get()
            self.tasks.append({
                "task": task_name,# MADE BY KAIF TARASAGAR
                "category": chosen_category,
                "priority": chosen_priority,
                "status": "Pending"
            })# MADE BY KAIF TARASAGAR
            self.save_tasks()
            self.refresh_list()
            category_window.destroy()
# MADE BY KAIF TARASAGAR
        tk.Button(category_window, text="Save Task", command=save_task, bg="#0d6efd", fg="white").pack(pady=10)

    def update_task(self):
        selected = self.get_selected()
        if selected:
            new_task = simpledialog.askstring("Update Task", f"Edit task:\n{selected['task']}", initialvalue=selected["task"])
            if new_task:
                selected["task"] = new_task# MADE BY KAIF TARASAGAR
                self.save_tasks()
                self.refresh_list()

    def mark_done(self):
        selected = self.get_selected()
        if selected:
            selected["status"] = "Done"# MADE BY KAIF TARASAGAR
            self.save_tasks()
            self.refresh_list()
# MADE BY KAIF TARASAGAR
    def delete_task(self):
        selected = self.get_selected()
        if selected:
            confirm = messagebox.askyesno("Delete Task", f"Delete:\n{selected['task']}?")
            if confirm:
                self.tasks.remove(selected)
                self.save_tasks()
                self.refresh_list()# MADE BY KAIF TARASAGAR

    def get_selected(self):
        try:# MADE BY KAIF TARASAGAR
            item_id = self.tree.selection()[0]
            values = self.tree.item(item_id, "values")
            for task in self.tasks:
                if (task["task"], task["category"], task["priority"], task["status"]) == values:
                    return task
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")
            return None

    def refresh_list(self):# MADE BY KAIF TARASAGAR
        self.tree.delete(*self.tree.get_children())
        search_text = self.search_var.get().lower()

        for task in self.tasks:
            if search_text in task["task"].lower() or search_text in task["category"].lower():
                tags = [task["priority"].lower()]
                if task["status"] == "Done":
                    tags.append("done")
                self.tree.insert("", tk.END, values=(task["task"], task["category"], task["priority"], task["status"]), tags=tags)
# MADE BY KAIF TARASAGAR
        self.tree.tag_configure("high", background="#e45252")  
        self.tree.tag_configure("medium", background="#ebc139") 
        self.tree.tag_configure("low", background="#23e24f")    

        # De-emphasize completed tasks with WCAG AA compliant colors
        if self.dark_mode:
            self.tree.tag_configure("done", foreground="#a9a9a9", background="#212529")
        else:
            self.tree.tag_configure("done", foreground="#595959", background="#f8f9fa")

        self.update_status()

    def update_status(self):# MADE BY KAIF TARASAGAR
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["status"] == "Done")
        self.status_var.set(f"Total Tasks: {total} | Completed: {done}")
# MADE BY KAIF TARASAGAR
    def save_tasks(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def load_tasks(self):# MADE BY KAIF TARASAGAR
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)

    def save_as_txt(self):# MADE BY KAIF TARASAGAR
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save To-Do List As TXT"
        )
        if file_path:# MADE BY KAIF TARASAGAR
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("📝 To-Do List\n")
                    f.write("="*40 + "\n\n")
                    for i, task in enumerate(self.tasks, start=1):
                        f.write(f"{i}. {task['task']}  |  Category: {task['category']}  |  Priority: {task['priority']}  |  Status: {task['status']}\n")
                messagebox.showinfo("Success", f"Tasks saved successfully:\n{file_path}")
            except Exception as e:# MADE BY KAIF TARASAGAR
                messagebox.showerror("Error", f"Could not save file:\n{e}")

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.root.config(bg="#212529")# MADE BY KAIF TARASAGAR
            self.title_label.config(bg="#212529", fg="white")
            self.status_label.config(bg="#212529", fg="white")
        else:
            self.root.config(bg="#f8f9fa")# MADE BY KAIF TARASAGAR
            self.title_label.config(bg="#f8f9fa", fg="#212529")
            self.status_label.config(bg="#f8f9fa", fg="#495057")
        self.refresh_list()

root = tk.Tk()
app = TodoApp(root)# MADE BY KAIF TARASAGAR
root.mainloop()


                                        #-- MADE BY KAIF TARASAGAR 
                                               
                                         # https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                         # https://x.com/Kaif_T_200