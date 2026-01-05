import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def clear_screen():
    entry.delete(0, tk.END)

def calculate():
    try:
        
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "არასწორი გამოსახულება")

root = tk.Tk()
root.title("მარტივი კალკულატორი")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear_screen)
    else:
        
        btn = tk.Button(root, text=text, width=5, height=2, 
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

root.mainloop()