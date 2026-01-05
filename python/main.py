import tkinter as tk

window = tk.Tk()
window.title("ჩემი პირველი პროგრამა")
window.geometry("300x100")

def hello_action():
    print("ღილაკს დააჭირეს!")

button = tk.Button(window, text="დამაჭირე!", command=hello_action)

button.pack(pady=20)

window.mainloop()