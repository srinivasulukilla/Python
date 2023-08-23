import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack(pady=10)

        self.mark_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.view_tasks()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_entry.delete(0, tk.END)
            self.view_tasks()

    def mark_completed(self):
        selected_indices = self.task_listbox.curselection()
        for index in selected_indices:
            self.tasks[index] = "✓ " + self.tasks[index]
        self.view_tasks()

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
