import tkinter as tk
from tkinter import messagebox
import csv
import random
import time

def spin_wheel():
    names_list = []
    try:
        with open('names.csv', 'r') as file:
            reader = csv.reader(file)
            names_list = [name[0] for name in reader]
            if not names_list:
                messagebox.showwarning("Warning", "The CSV file is empty.")
                return
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")

    if not names_list:
        return

    spin_duration = 1.5  # seconds
    start_time = time.time()
    while time.time() - start_time < spin_duration:
        selected_name = random.choice(names_list)
        name_label.config(text=selected_name)
        root.update()
        time.sleep(0.05)

    messagebox.showinfo("Tossed Name", f"The selected name is: {selected_name}")

root = tk.Tk()
root.title("Name Toss")
root.geometry("400x200")  # Adjust the size of the window

label = tk.Label(root, text="Click the button to toss a name!", font=("Arial", 50))  # Increase font size
label.pack(pady=10)

name_label = tk.Label(root, text="", font=("Arial", 50))  # Increase font size
name_label.pack()

spin_button = tk.Button(root, text="Spin Wheel", command=spin_wheel, font=("Arial", 14))  # Increase font size
spin_button.pack()

root.mainloop()

