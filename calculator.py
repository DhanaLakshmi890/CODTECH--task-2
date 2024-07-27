import tkinter as tk

# Function to update the expression in the display
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='black')

# Create a StringVar to hold the entry value
entry_var = tk.StringVar()

# Create an entry widget for the display
entry = tk.Entry(root, textvar=entry_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.configure(bg='black', fg='white', insertbackground='white')

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons in the grid
row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font="lucida 15 bold", padx=20, pady=20, bg='black', fg='white')
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
