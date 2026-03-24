import tkinter as tk
from tkinter import messagebox
from desktop_client.viewmodels.task_viewmodel import TaskViewModel


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("StudyBoard Distributed Client")
        self.root.geometry("700x500")

        self.vm = TaskViewModel()

        self.title_label = tk.Label(root, text="Task title")
        self.title_label.pack()

        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()

        self.desc_label = tk.Label(root, text="Task description")
        self.desc_label.pack()

        self.desc_entry = tk.Entry(root, width=50)
        self.desc_entry.pack()

        self.add_button = tk.Button(root, text="Add task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(root, width=90, height=15)
        self.listbox.pack(pady=10)

        self.progress_button = tk.Button(root, text="Move to IN_PROGRESS", command=self.set_in_progress)
        self.progress_button.pack(pady=3)

        self.done_button = tk.Button(root, text="Move to DONE", command=self.set_done)
        self.done_button.pack(pady=3)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.draw_tasks)
        self.refresh_button.pack(pady=5)

        self.draw_tasks()

    def draw_tasks(self):
        self.listbox.delete(0, tk.END)
        tasks = self.vm.refresh()
        for task in tasks:
            self.listbox.insert(
                tk.END,
                f"{task['id']}. {task['title']} | {task['description']} | {task['status']}"
            )

    def get_selected_task_id(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task first")
            return None
        line = self.listbox.get(selected[0])
        return int(line.split(".")[0])

    def add_task(self):
        try:
            self.vm.add_task(
                self.title_entry.get(),
                self.desc_entry.get()
            )
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.draw_tasks()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def set_in_progress(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            self.vm.move_to_in_progress(task_id)
            self.draw_tasks()

    def set_done(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            self.vm.move_to_done(task_id)
            self.draw_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
