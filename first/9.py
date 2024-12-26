import tkinter as tk
from tkinter import messagebox
import os
import json

def read_db():
    if not os.path.exists("users_main.json"):
        return []

    with open("users_main.json", "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def write_db(data):
    with open("users_main.json", "w") as file:
        json.dump(data, file, indent=4)

def add_user():
    name = name_entry.get()
    email = email_entry.get()
 
    if name and email:
        users = read_db()
        new_user = {'name': name, 'email': email}
        users.append(new_user)
        write_db(users)
        name_entry.delete(0,tk.END)
        email_entry.delete(0,tk.END)
        refresh_listbox()
        messagebox.showinfo("User added", f"User {name} added successfully")


def refresh_listbox():
    listbox.delete(0,tk.END)
    users=read_db()
    for user in users:
        listbox.insert(tk.END,f" {user['name']} - {user['email']} ")

def delete_user():
    try:
        selected = listbox.curselection()[0]
        users=read_db()
        users.pop(selected)
        write_db(users)
        refresh_listbox()
        messagebox.showinfo("User deleted", f"User {users[selected]['name']} deleted successfully")
    except IndexError:
        messagebox.showerror("No user selected", "Please select a user to delete")

    

#Label
root = tk.Tk()
root.title("User Management")

name_label = tk.Label(root, text='Name: ')
name_label.grid(row=0, column=1)
email_label = tk.Label(root, text='Email: ')
email_label.grid(row=2, column=1)

#Entry widget
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10 , pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, padx=10 , pady=10)

add_button = tk.Button(root, text="Add user", command=add_user)
add_button.grid(row=4, column=1, sticky=tk.W+tk.E, padx=10)
delete_button = tk.Button(root, text="Delete user", command=delete_user)
delete_button.grid(row=5, column=1, sticky=tk.W+tk.E, padx=10)

listbox = tk.Listbox(root)
listbox.grid(row=6, column=1, columnspan=2, sticky=tk.W+tk.E, padx=10, pady=10)




root.mainloop()
