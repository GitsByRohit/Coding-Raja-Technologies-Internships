


import tkinter as tk

# Define the main window
window = tk.Tk()
window.title("To-Do List")

# Define list to store tasks
tasks = []

# Function to add a new task
def add_task():
  task_text = entry.get()
  if task_text:
    tasks.append(task_text)
    listbox.insert(tk.END, task_text)
    entry.delete(0, tk.END)

# Function to delete a selected task
def delete_task():
  index = listbox.curselection()
  if index:
    task_text = listbox.get(index)
    tasks.remove(task_text)
    listbox.delete(index)

# Create entry field for new tasks
entry = tk.Entry(window, width=50)
entry.grid(row=0, column=0, pady=5)

# Create add task button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, pady=5)

# Create listbox to display tasks
listbox = tk.Listbox(window, width=50, height=10)
listbox.grid(row=1, column=0, columnspan=2, pady=5)

# Create delete task button
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=1, pady=5)

# Start the main loop
window.mainloop()


