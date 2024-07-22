import tkinter as tk

# Function to update the input field
def click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, font="Helvetica 16", borderwidth=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define button text in a 2D list
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons and place them on the grid
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, font="Helvetica 16", borderwidth=5, relief=tk.RIDGE)
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        button.bind("<Button-1>", click)

# Configure grid weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
