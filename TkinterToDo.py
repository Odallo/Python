import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")

task_entry = tk.Entry(root)
task_entry.pack(pady=10)

def add_task():
    task = task_entry.get()
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def remove_task():
    task_list.delete(tk.ACTIVE)
    task_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

task_list = tk.Listbox(root)
task_list.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=10)

task_list.bind('<Delete>', remove_task)
task_list.bind('<Return>', add_task)    




root.mainloop()
