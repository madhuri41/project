import tkinter as tk
from todo_logic import TodoManager

manager = TodoManager()

root = tk.Tk()
root.title("To-Do App")

task_entry = tk.Entry(root, width=40)
task_entry.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

def refresh_list():
    listbox.delete(0, tk.END)
    for task in manager.tasks:
        status = "✔ " if task["completed"] else ""
        listbox.insert(tk.END, status + task["task"])

def add_task():
    task = task_entry.get()
    manager.add_task(task)
    manager.save_tasks()
    refresh_list()
    task_entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        manager.delete_task(selected[0])
        manager.save_tasks()
        refresh_list()

def mark_complete():
    selected = listbox.curselection()
    if selected:
        manager.toggle_complete(selected[0])
        manager.save_tasks()
        refresh_list()

tk.Button(root, text="Add", command=add_task).pack()
tk.Button(root, text="Delete", command=delete_task).pack()
tk.Button(root, text="Mark Complete", command=mark_complete).pack()

refresh_list()
root.mainloop()