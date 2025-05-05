import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

expression = ""

def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def calculate():
    global expression
    try:
        result = eval(expression, {__builtins__": None}, math.__dict__)
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

def scientific_func(func):
    global expression
    try:
        value = eval(expression)
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "exp":
            result = math.exp(value)
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

# Entry Field
equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=15, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
    ('C',5,0), ('⌫',5,1), ('(',5,2), (')',5,3),
    ('sin',6,0), ('cos',6,1), ('tan',6,2), ('sqrt',6,3),
    ('log',7,0), ('ln',7,1), ('exp',7,2), ('pow',7,3),
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear
    elif text == '⌫':
        cmd = backspace
    elif text in ['sin','cos','tan','log','ln','sqrt','exp']:
        cmd = lambda x=text: scientific_func(x)
    elif text == 'pow':
        cmd = lambda: press("**")
    else:
        cmd = lambda x=text: press(x)

    tk.Button(root, text=text, padx=20, pady=20, bd=4, font=('Arial', 12), command=cmd).grid(row=row, column=col)

root.mainloop()

