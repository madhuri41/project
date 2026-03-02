import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        self.tasks = []

        # UI
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.frame, text="Add", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        text = self.task_entry.get().strip()
        if text:
            self.tasks.append({"text": text, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
            self.save_tasks()

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
            self.save_tasks()

    def mark_complete(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()
            self.save_tasks()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display = task["text"]
            if task["completed"]:
                display += " ✔"
            self.listbox.insert(tk.END, display)

    def save_tasks(self):
        try:
            with open(FILE_NAME, "w") as f:
                json.dump(self.tasks, f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks:\n{e}")

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, "r") as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                messagebox.showwarning("Warning", "Corrupted JSON file. Starting fresh.")
                self.tasks = []
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load tasks:\n{e}")
        self.update_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()