from tkinter import *
import math  # importing math module for advanced function

# grid helps to create a row and column

root=Tk()

e=Entry(root,width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,pady=30,padx=34)

# Function to handle number button clicks
def click(num):
    current =e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))

# Function to store a new operation and start a new calculator
def set_operation(operator):
        global first_num, operation
        first_num = float(e.get())
        operation = operator
        e.delete(0, END)

# Function to clear the entry
def clear():
    e.delete(0, END)

# Function to perform the calculation based on the operator
def equal():
    second_num = float(e.get())
    e.delete(0, END)

    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    elif operation == '/':
        if second_num == 0:
            result = "Error"
        else:
            result = first_num / second_num
    elif operation == '^':  # For power (exponentiation)
        result = first_num ** second_num

    e.insert(0, str(result))

# Function for single-input operations (sin, cos, tan, log, etc.)
def single_operation(operation):
    num= float(e.get())
    e.delete(0,END)

    if operation == 'Sin':
        result = math.sin(math.radians(num))  # Convert to radians before applying sin
    elif operation == 'Cos':
        result = math.cos(math.radians(num))  # Convert to radians before applying cos
    elif operation == 'Tan':
         if math.cos(math.radians(num)) == 0:
             result = "Error"  # Prevent division by zero for tan(90), tan(270), etc.
         else:
            result = math.tan(math.radians(num))
    elif operation == 'exp':
        result  = math.exp(num)
    elif operation == 'log':  # Natural logarithm
        if num <= 0:
            result = "Error"
        else:
            result = math.log(num)

    e.insert(0, str(result))

# Buttons for numbers
button_1 = Button(root, text='1', padx=50, pady=25, command=lambda: click(1))
button_2 = Button(root, text='2', padx=50, pady=25, command=lambda: click(2))
button_3 = Button(root, text='3', padx=50, pady=25, command=lambda: click(3))
button_4 = Button(root, text='4', padx=50, pady=25, command=lambda: click(4))
button_5 = Button(root, text='5', padx=50, pady=25, command=lambda: click(5))
button_6 = Button(root, text='6', padx=50, pady=25, command=lambda: click(6))
button_7 = Button(root, text='7', padx=50, pady=25, command=lambda: click(7))
button_8 = Button(root, text='8', padx=50, pady=25, command=lambda: click(8))
button_9 = Button(root, text='9', padx=50, pady=25, command=lambda: click(9))
button_0 = Button(root, text='0', padx=50, pady=25, command=lambda: click(0))

button_equal=Button(root,text="=",padx=50,pady=25,command=equal)
button_Ac=Button(root,text='Ac',padx=55,pady=25,command=clear)

button_add=Button(root,text='+',padx=60,pady=25,command=lambda :set_operation('+'))
button_subract=Button(root,text='-',padx=60,pady=25,command=lambda :set_operation('-'))
button_multipy=Button(root,text='*',padx=60,pady=25,command=lambda :set_operation('*'))
button_divide=Button(root,text='/',padx=60,pady=25,command=lambda :set_operation('/'))

button_Sin=Button(root,text='Sin',padx=50,pady=25,command=lambda :single_operation('Sin'))
button_Cos=Button(root,text='Cos',padx=50,pady=25,command=lambda :single_operation('Cos'))
button_Tan=Button(root,text='Tan',padx=50,pady=25,command=lambda :single_operation('Tan'))
button_exp=Button(root,text='exp',padx=50,pady=25,command=lambda :single_operation('exp'))
button_log=Button(root,text='log',padx=50,pady=25,command=lambda :single_operation('log'))

# PLACE THE BUTTONS IN THE GRID
button_9.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=0)
button_6.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=0)
button_3.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=0)
button_0.grid(row=4,column=1)

button_equal.grid(row=5,column=1)
button_Ac.grid(row=1,column=3)

button_add.grid(row=4,column=3)
button_subract.grid(row=4,column=2)
button_multipy.grid(row=3,column=3)
button_divide.grid(row=2,column=3)

button_Sin.grid(row=1,column=4)
button_Cos.grid(row=2,column=4)
button_Tan.grid(row=3,column=4)
button_exp.grid(row=4,column=4)
button_log.grid(row=4,column=0)

first_num=0
operation=None

# Run The tkinter event loop
root.mainloop()