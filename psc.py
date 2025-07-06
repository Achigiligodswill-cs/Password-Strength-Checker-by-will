import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password= entry.get()

    if len(password) <8:
        messagebox.showwarning ("password must be atleast 8 characters long")
    elif not re.search("[A-Z]", password):
        messagebox.showwarning("password must contain an UPPERCASE letter")
    elif not re.search("[a-z]",password):
       messagebox.showwarning("password must contain a lowercase letter")
    elif not re.search("[0-9]", password):
        messagebox.showwarning("password must contain atleast one number")
    elif not re.search("[@#$*_]", password):
        messagebox.showwarning("password must contain a special character")
    else: 
        messagebox.showinfo("Good Job! thats a strong password!😃")
        
root = tk.Tk()
root.title("Password Checker")
root.bind('<Return>', lambda event:
    check_password())
show_password_var=tk.BooleanVar()
def toggle_password_visibility():
        if show_password_var.get():
            entry.config(show="")
        else:
            entry.config(show="*")
        



tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()
show_password_var= tk.BooleanVar()
tk.Checkbutton(
    root,
    text="show password",
    variable=show_password_var,
    command=toggle_password_visibility
).pack()
tk.Button(root, text="Check Password", command=check_password).pack(pady=10)

root.mainloop()