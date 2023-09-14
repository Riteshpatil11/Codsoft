import tkinter as tk

class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List")

        self.listbox = tk.Listbox(self.window)
        self.listbox.grid(row=0, column=0, sticky="nsew")

        add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        add_button.grid(row=1, column=0)

        mark_completed_button = tk.Button(self.window, text="Mark Completed", command=self.mark_completed)
        mark_completed_button.grid(row=2, column=0)

        delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=3, column=0)

        self.window.after(3000, self.update)  # Call the update function every 3 seconds

    def add_task(self):
        task_text = input("Enter a task: ")
        self.listbox.insert("end", task_text)

    def mark_completed(self):
        selected_task = self.listbox.get("active")
        self.listbox.delete("active")
        self.listbox.insert("end", selected_task + " ✔")

    def delete_task(self):
        self.listbox.delete("active")

    def update(self):
        # Do something here...
        self.window.after(3000, self.update)  # Call this function again in 3 seconds

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
