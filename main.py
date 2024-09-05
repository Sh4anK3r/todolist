import tkinter as tk
import json

ROOT_SIZE = "800x800"
tasks = []

try:
    with open("data.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass

# --------------------------- ADD TASK ---------------------------

def add_task():
    data = entry.get()
 
    if data:
        tasks.append(data)
        update_task_list(tasks)
        entry.delete(0, tk.END)
        with open("data.json", "w") as data_file:
            json.dump(tasks, data_file)

# --------------------------- UPDATE TASK LIST ---------------------------    

def update_task_list(tasks):
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        pass

    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)
        
# --------------------------- DELETE TASK LIST ---------------------------    

def delete_task_list():
    selected_task = task_list.curselection() # to focus on item which I click
    if selected_task:
        task_to_delete = task_list.get(selected_task)
        tasks.remove(task_to_delete)
        task_list.delete(selected_task)
        with open("data.json", "w") as data_file:
            json.dump(tasks, data_file)
    
        update_task_list(tasks)

# --------------------------- BUTTON COLOR CHANGE ---------------------------

def change_color_add(event):
    add_button['bg'] = 'peachpuff'

def change_color_add_back(event):
    add_button['bg'] = "sandybrown"
    
def change_color_delete(event):
    delete_button['bg'] = 'peachpuff'

def change_color_delete_back(event):
    delete_button['bg'] = "sandybrown"
    
# --------------------------- UI SETUP ---------------------------
root = tk.Tk()
root.title("TO DO LIST")
root.geometry(ROOT_SIZE)
root.resizable(False, False)
root.config(background="SADDLEBROWN")

# --------------------------- LABEL ---------------------------

label = tk.Label(root)
label.config(text="TO DO LIST", font=("Times New Roman", 40, "bold"), bg="SADDLEBROWN", fg="bisque")
label.pack()

# --------------------------- LISTBOX ---------------------------

task_list = tk.Listbox(root)
task_list.config(width=50, height=20, bg="sandybrown", borderwidth=0)
task_list.pack(pady= 50)

# --------------------------- ENTRY ---------------------------

entry = tk.Entry(root)
entry.config(width=100, bg="sandybrown")
entry.pack(pady=20)

# --------------------------- BUTTONS ---------------------------

add_button = tk.Button(root)
add_button.config(text="ADD", width=50, height=3, bg="sandybrown", activebackground="burlywood", font=("Times New Roman", 10, "bold"), command=add_task)
add_button.bind("<Enter>", change_color_add)
add_button.bind("<Leave>", change_color_add_back)
add_button.pack(pady=30)

delete_button = tk.Button(root)
delete_button.config(text="DELETE", width=50, height=3, bg="sandybrown", activebackground="burlywood", font=("Times New Roman", 10, "bold"), command=delete_task_list)
delete_button.bind("<Enter>", change_color_delete)
delete_button.bind("<Leave>", change_color_delete_back)
delete_button.pack(pady=30)


root.mainloop()
