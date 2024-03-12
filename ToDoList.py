from tkinter import *
from tkinter import messagebox

def new_content():
    task = your_entry.get()
    if task != "":
        lb.insert(END, task)
        your_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def delete_content():
    lb.delete(ANCHOR)
    
root = Tk()
root.geometry('500x450+500+200')
root.title('TO DO LIST')
root.config(bg='#F5F5F5')  # Light gray background
root.resizable(width=True, height=True)

frame = Frame(root, bg='#F5F5F5')  # Light gray background
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#000000',
    highlightthickness=0,
    selectbackground='#ADD8E6',
    activestyle="none",
    bg='#F0F0F0',  # Lighter gray background
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Go for swimming',
    'Drink water',
    'Go for walking',
    'Write assignment',
    'Write documentation',
    'Take a nap',
    'Learn something',
    'Paint canvas'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame, bg='#F0F0F0', troughcolor='#C0C0C0')  # Lighter gray and gray colors for the scrollbar
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

your_entry = Entry(
    root,
    font=('times', 24),
    bg='#F0F0F0',  # Lighter gray background
    bd=0,
    fg='#000000',
    insertbackground='#000000'  # Black cursor
)

your_entry.pack(pady=20)

Button_F = Frame(root, bg='#F5F5F5')  # Light gray background
Button_F.pack(pady=20)

addTask_btn = Button(
    Button_F,
    text='Add Task',
    font=('Times 14 bold'),
    bg='#008CBA',  # Blue color for add button
    fg='#FFFFFF',  # White text color
    padx=10,
    pady=5,
    command=new_content
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

del_content = Button(
    Button_F,
    text='Delete Task',
    font=('Times 14 bold'),
    bg='#FF6347',  # Red color for delete button
    fg='#FFFFFF',  # White text color
    padx=10,
    pady=5,
    command=delete_content
)
del_content.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
from tkinter import *
from tkinter import messagebox

def new_content():
    task = your_entry.get()
    if task != "":
        lb.insert(END, task)
        your_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def delete_content():
    lb.delete(ANCHOR)
    
root = Tk()
root.geometry('500x450+500+200')
root.title('TO DO LIST')
root.config(bg='#F5F5F5')  # Light gray background
root.resizable(width=True, height=True)

frame = Frame(root, bg='#F5F5F5')  # Light gray background
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#000000',
    highlightthickness=0,
    selectbackground='#ADD8E6',
    activestyle="none",
    bg='#F0F0F0',  # Lighter gray background
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Go for swimming',
    'Drink water',
    'Go for walking',
    'Write assignment',
    'Write documentation',
    'Take a nap',
    'Learn something',
    'Paint canvas'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame, bg='#F0F0F0', troughcolor='#C0C0C0')  # Lighter gray and gray colors for the scrollbar
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

your_entry = Entry(
    root,
    font=('times', 24),
    bg='#F0F0F0',  # Lighter gray background
    bd=0,
    fg='#000000',
    insertbackground='#000000'  # Black cursor
)

your_entry.pack(pady=20)

Button_F = Frame(root, bg='#F5F5F5')  # Light gray background
Button_F.pack(pady=20)

addTask_btn = Button(
    Button_F,
    text='Add Task',
    font=('Times 14 bold'),
    bg='#008CBA',  # Blue color for add button
    fg='#FFFFFF',  # White text color
    padx=10,
    pady=5,
    command=new_content
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

del_content = Button(
    Button_F,
    text='Delete Task',
    font=('Times 14 bold'),
    bg='#FF6347',  # Red color for delete button
    fg='#FFFFFF',  # White text color
    padx=10,
    pady=5,
    command=delete_content
)
del_content.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
