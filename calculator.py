import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field to display the calculator input/output
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Global variable to store expression
expression = ""

# Function to update the entry field
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the final expression
def equals():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)  # Display the result
        expression = result  # Store result for further calculations
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Function to clear the entry field
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Adding buttons to the calculator
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row_value = 1
col_value = 0
for text in button_texts:
    if text == 'C':
        button = tk.Button(root, text=text, height=2, width=5, font=("Arial", 18), command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, height=2, width=5, font=("Arial", 18), command=equals)
    else:
        button = tk.Button(root, text=text, height=2, width=5, font=("Arial", 18), command=lambda t=text: press(t))
    button.grid(row=row_value, column=col_value, padx=5, pady=5)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Run the main loop
root.mainloop()
