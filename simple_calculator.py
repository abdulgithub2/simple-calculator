from tkinter import *
import re


root = Tk()
root.title('Simple Calculator')

action = None
data = None


def chech_input():
    return re.search(r'^(\d*\.\d+|\d+\.\d*|\d+)$', entry.get())


def input_correction():
    while not chech_input():
        if entry.get() == '' or entry.get() == '.':
            break
        back()


def store_data():
    global data
    if chech_input():
        if data == None:
            data = float(entry.get())
            entry.delete(0, END)
    else:
        input_correction()


def all_clear():
    global data
    entry.delete(0, END)
    data = None


def back():
    back_data = entry.get()[:-1]
    entry.delete(0, END)
    entry.insert(0, back_data)


def clicked(button):
    entry.insert(END, button)
    input_correction()


def plus():
    global action
    action = '+'
    store_data()


def subtract():
    global action
    action = '-'
    store_data()


def multiply():
    global action
    action = '*'
    store_data()


def divide():
    global action
    action = '/'
    store_data()


def equal():
    global action, data

    if chech_input() and data:
        if action == '+':
            data = data+float(entry.get())

        elif action == '-':
            data = data-float(entry.get())

        elif action == '*':
            data = data*float(entry.get())

        elif action == '/':
            try:
                data = data/float(entry.get())
            except ZeroDivisionError:
                data = ''

        entry.delete(0, END)
        entry.insert(0, str(data))
        data = None

    else:
        input_correction()


entry = Entry(root, width=15, font=('Halvetica', 15))
entry.grid(row=0, column=0, columnspan=2, padx=7, pady=7)

frame = LabelFrame(root, padx=5, pady=5)
frame.grid(row=2, column=0, columnspan=2, padx=7, pady=7)

button_clear = Button(root, text='AC', font=(
    'Halvetica', 10, 'bold'), command=all_clear)
button_back = Button(
    root, text='<-', font=('Halvetica', 10, 'bold'), command=back)
button_0 = Button(frame, text='0', font=(
    'Halvetica', 15),  command=lambda: clicked(0))
button_1 = Button(frame, text='1', font=(
    'Halvetica', 15),  command=lambda: clicked(1))
button_2 = Button(frame, text='2', font=(
    'Halvetica', 15),  command=lambda: clicked(2))
button_3 = Button(frame, text='3', font=(
    'Halvetica', 15),  command=lambda: clicked(3))
button_4 = Button(frame, text='4', font=(
    'Halvetica', 15),  command=lambda: clicked(4))
button_5 = Button(frame, text='5', font=(
    'Halvetica', 15),  command=lambda: clicked(5))
button_6 = Button(frame, text='6', font=(
    'Halvetica', 15),  command=lambda: clicked(6))
button_7 = Button(frame, text='7', font=(
    'Halvetica', 15),  command=lambda: clicked(7))
button_8 = Button(frame, text='8', font=(
    'Halvetica', 15),   command=lambda: clicked(8))
button_9 = Button(frame, text='9', font=(
    'Halvetica', 15),  command=lambda: clicked(9))
button_point = Button(frame, text='.', font=(
    'Halvetica', 15, 'bold'), command=lambda: clicked('.'), padx=14)
button_plus = Button(
    frame, text='+', font=('Halvetica', 15, 'bold'),  command=plus, padx=9)
button_subtract = Button(
    frame, text='-', font=('Halvetica', 15, 'bold'), command=subtract, padx=14)
button_multiply = Button(
    frame, text='*', font=('Halvetica', 15, 'bold'),  command=multiply, padx=12)
button_divide = Button(
    frame, text='/', font=('Halvetica', 15, 'bold'),  command=divide, padx=14)
button_equal = Button(frame, text='=', font=(
    'Halvetica', 15, 'bold'),  command=equal, padx=9)

button_clear.grid(row=1, column=0)
button_back.grid(row=1, column=1)
button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_point.grid(row=4, column=1)
button_plus.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equal.grid(row=4, column=2)


root.mainloop()
