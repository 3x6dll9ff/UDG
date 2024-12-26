import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import csv
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager

        # Фрейм для основных полей ввода
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.grid(row=0, column=0, sticky="nsew")

        # Метки и поля ввода для задачи
        tk.Label(input_frame, text="Naziv:", anchor="w").grid(row=0, column=0, sticky="w")
        tk.Label(input_frame, text="Iznos:", anchor="w").grid(row=1, column=0, sticky="w")
        tk.Label(input_frame, text="Tip troška:", anchor="w").grid(row=2, column=0, sticky="w")
        tk.Label(input_frame, text="Namjena:", anchor="w").grid(row=3, column=0, sticky="w")
        tk.Label(input_frame, text="Lokacija troška:", anchor="w").grid(row=4, column=0, sticky="w")

        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.radio_var = tk.StringVar()

        radio_frame = tk.Frame(input_frame)
        radio_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.radio1 = tk.Radiobutton(radio_frame, text="fiksni", variable=self.radio_var, value="fiksni")
        self.radio1.grid(row=0, column=0, padx=10, sticky="w")
        self.radio2 = tk.Radiobutton(radio_frame, text="rekreacija", variable=self.radio_var, value="rekreacija")
        self.radio2.grid(row=0, column=1, padx=10, sticky="w")
        self.radio3 = tk.Radiobutton(radio_frame, text="drugo", variable=self.radio_var, value="drugo")
        self.radio3.grid(row=0, column=2, padx=10, sticky="w")

        self.purpose_var = tk.StringVar()
        self.purpose_dropdown = ttk.Combobox(input_frame, textvariable=self.purpose_var,
                                             values=["kirija", "hrana", "odjeca", "kafa", "obuca", "trening", "drugo"])
        self.purpose_dropdown.grid(row=3, column=1, padx=10, pady=10)

        self.location_entry = tk.Entry(input_frame)
        self.location_entry.grid(row=4, column=1, padx=10, pady=10)

        # Список задач
        listbox_frame = tk.Frame(self.root)
        listbox_frame.grid(row=1, column=0, sticky="nsew")
        self.listbox = tk.Listbox(listbox_frame)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.refresh_listbox()

        # Кнопки управления
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, pady=(0, 10))

        self.add_button = tk.Button(button_frame, text="Dodaj trošak", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=10)

        edit_button = tk.Button(button_frame, text="Izmeni trošak", command=self.edit_task)
        edit_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Obriši trošak", command=self.delete_task)
        delete_button.grid(row=0, column=2, padx=10)

        filter_button = tk.Button(button_frame, text="Izvoji po tipu i nameni", command=self.open_filter_window)
        filter_button.grid(row=1, column=0, padx=10, pady=5)

        top5_button = tk.Button(button_frame, text="Top 5 lokacija", command=self.top_5_locations)
        top5_button.grid(row=1, column=1, padx=10, pady=5)

        frequent_button = tk.Button(button_frame, text="Lokacije >4 puta", command=self.frequent_locations)
        frequent_button.grid(row=1, column=2, padx=10, pady=5)

        # Настройка растягивания столбцов и строк
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

    def read_db(self):
        if not os.path.exists('tasks.csv'):
            return []
        with open('tasks.csv', newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def write_db(self, data):
        with open('tasks.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def add_task(self):
        self.save_task()

    def save_task(self, index=None):
        name = self.name_entry.get()
        if not (5 <= len(name) <= 50):
            messagebox.showerror("Error", "Naziv must be between 5 and 50 characters")
            return
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Iznos must be a number")
            return
        type_expense = self.radio_var.get()
        purpose = self.purpose_var.get()
        location = self.location_entry.get()
        if len(location.split()) < 2:
            messagebox.showerror("Error", "Lokacija must be in format 'Country City ...'")
            return
        if name and amount and type_expense and purpose and location:
            tasks = self.read_db()
            new_task = [name, amount, type_expense, purpose, location]
            if index is None:
                tasks.append(new_task)
            else:
                tasks[index] = new_task
            self.write_db(tasks)
            self.name_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.purpose_var.set("")
            self.location_entry.delete(0, tk.END)
            self.radio_var.set("")
            self.refresh_listbox()
            messagebox.showinfo("Info", "Task saved successfully")
            self.set_add_mode()
        else:
            messagebox.showerror("Error", "All fields must be filled")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            task_name = self.listbox.get(selected_index).split()[0]  

            confirm = messagebox.askokcancel("Delete Task", f"Are you sure you want to delete task '{task_name}'?")
            if confirm:
                tasks = self.read_db()
                tasks.pop(selected_index)
                self.write_db(tasks)
                self.refresh_listbox()
                messagebox.showinfo("Info", "Task deleted successfully")
        except IndexError:
            messagebox.showerror("Error", "No task selected")


    def edit_task(self):
        try:
            selected = self.listbox.curselection()[0]
            tasks = self.read_db()
            task = tasks[selected]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, task[0])
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, task[1])
            self.radio_var.set(task[2])
            self.purpose_var.set(task[3])
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, task[4])
            self.set_save_mode(selected)
        except IndexError:
            messagebox.showerror("Error", "No task selected")

    def set_add_mode(self):
        self.add_button.config(text='Dodaj trošak', command=self.add_task)

    def set_save_mode(self, index):
        self.add_button.config(text='Sačuvaj izmene', command=lambda: self.save_task(index))

    def filter_tasks(self):
        type_expense = simpledialog.askstring("Input", "Enter type of expense:")
        purpose = simpledialog.askstring("Input", "Enter purpose:")
        if type_expense and purpose:
            tasks = self.read_db()
            filtered_tasks = [task for task in tasks if task[2] == type_expense and task[3] == purpose]
            self.listbox.delete(0, tk.END)
            for task in filtered_tasks:
                self.listbox.insert(tk.END, f"{task[0]} - Amount: {task[1]}, Type: {task[2]}, Purpose: {task[3]}, Location: {task[4]}")

    def top_5_locations(self):
        tasks = self.read_db()
        location_counts = {}
        for task in tasks:
            location = task[4]
            if location in location_counts:
                location_counts[location] += 1
            else:
                location_counts[location] = 1
        sorted_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, "Top 5 Locations:")
        for loc, count in sorted_locations:
            self.listbox.insert(tk.END, f"{loc}: {count} times")

    def frequent_locations(self):
        tasks = self.read_db()
        location_counts = {}
        for task in tasks:
            location = task[4]
            if location in location_counts:
                location_counts[location] += 1
            else:
                location_counts[location] = 1
        frequent_locs = [loc for loc, count in location_counts.items() if count > 4][:3]
        
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, "Top 3 Locations >4 times:")
        for loc in frequent_locs:
            self.listbox.insert(tk.END, loc)

    def open_filter_window(self):
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Izvoji po tipu i nameni")

        # Frame for type of expense
        type_frame = tk.LabelFrame(filter_window, text="Tip troška")
        type_frame.pack(padx=10, pady=10, anchor="w")

        tk.Radiobutton(type_frame, text="fiksni", variable=self.radio_var, value="fiksni").pack(anchor="w", padx=10, pady=5)
        tk.Radiobutton(type_frame, text="rekreacija", variable=self.radio_var, value="rekreacija").pack(anchor="w", padx=10, pady=5)
        tk.Radiobutton(type_frame, text="drugo", variable=self.radio_var, value="drugo").pack(anchor="w", padx=10, pady=5)

        # Frame for purpose
        purpose_frame = tk.LabelFrame(filter_window, text="Namjena")
        purpose_frame.pack(padx=10, pady=10, anchor="w")

        self.purpose_var.set("")  # Clear previous selection
        purpose_options = ["kirija", "hrana", "odjeca", "kafa", "obuca", "trening", "drugo"]
        purpose_dropdown = ttk.Combobox(purpose_frame, textvariable=self.purpose_var, values=purpose_options)
        purpose_dropdown.pack(padx=10, pady=5)

        # Apply button
        apply_button = tk.Button(filter_window, text="Primjeni", command=lambda: self.apply_filters(filter_window))
        apply_button.pack(padx=10, pady=10)

    def apply_filters(self, filter_window):
        type_expense = self.radio_var.get()
        purpose = self.purpose_var.get()

        if type_expense and purpose:
            tasks = self.read_db()
            filtered_tasks = [task for task in tasks if task[2] == type_expense and task[3] == purpose]
            self.listbox.delete(0, tk.END)
            for task in filtered_tasks:
                self.listbox.insert(tk.END, f"{task[0]} - Amount: {task[1]}, Type: {task[2]}, Purpose: {task[3]}, Location: {task[4]}")
            filter_window.destroy()
        else:
            messagebox.showerror("Error", "Both type of expense and purpose must be selected")


    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.read_db():
            self.listbox.insert(tk.END, f"{task[0]} - Amount: {task[1]}, Type: {task[2]}, Purpose: {task[3]}, Location: {task[4]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
