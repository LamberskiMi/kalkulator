import tkinter as tk
from tkinter import END
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '**' : operator.pow,
    '//' : operator.floordiv

}

import ttkbootstrap as tb

a = []
variant = []
ct = 0


def one():
    my_entry.insert(END, "1")


def two():
    my_entry.insert(END, "2")


def three():
    my_entry.insert(END, "3")


def four():
    my_entry.insert(END, "4")


def five():
    my_entry.insert(END, "5")


def six():
    my_entry.insert(END, "6")


def seven():
    my_entry.insert(END, "7")


def eight():
    my_entry.insert(END, "8")


def nine():
    my_entry.insert(END, "9")


def zero():
    my_entry.insert(END, "0")


def delete():
    my_entry.delete(0, END)


def get_sum():
    global a
    global variant
    global ct
    print(int(ct))
    a.append(my_entry.get())
    variant.append("+")
    my_entry.delete(0, END)
    #do dopracowania dodawanie wielu wartości
    leng = int(len(a))
    if ct<=0:
        ct+=1
    if ct>0:
        for i in range(leng-1):
            print("operacja:", ops[variant[i]](int(a[i]), int(a[i+1])))
            print("wartosci ", (int(a[i]), variant[i], int(a[i + 1])))
            my_entry.insert(END, ops[variant[i]](int(a[i]), int(a[i+1])))
        a.clear()
        variant.clear()


def get_sub():
    a.append(my_entry.get())
    variant.append("-")
    my_entry.delete(0, END)


def get_div():
    a.append(my_entry.get())
    variant.append("/")
    my_entry.delete(0, END)

def get_multi():
    a.append(my_entry.get())
    variant.append("*")
    my_entry.delete(0, END)

def get_expo():
    a.append(my_entry.get())
    variant.append("**")
    my_entry.delete(0, END)

def get_root_ext():
    a.append(my_entry.get())
    variant.append("//")
    my_entry.delete(0, END)


def equals():
    a.append(my_entry.get())
    my_entry.delete(0, END)
    result = 0
    leng = int(len(a))
    for i in range(leng-1):
        print("operacja:", ops[variant[i]](int(a[i]), int(a[i+1])))
        print("wartosci ", (int(a[i]), variant[i], int(a[i + 1])))
        my_entry.insert(END, ops[variant[i]](int(a[i]), int(a[i+1])))
    a.clear()
    variant.clear()


app = tb.Window(themename="darkly")
app.title("Calculator")
app.geometry('370x500')
app.resizable(width=False, height=False)


#Frame
my_frame = tk.Frame(app)
my_frame.pack()

events_frame = tk.Frame(app)
events_frame.pack()

button_frame = tk.Frame(app)
button_frame.pack()


#Style
numbers_Style = tb.Style()
numbers_Style.configure('dark.TButton', font=("Helvetica", 24), width=4)


#Entry Text
my_entry = tb.Entry(my_frame,
                    font=("", 24))
my_entry.pack(ipady=20)

#Numbers
b_one = tb.Button(button_frame, text="1",
                        style="dark.TButton",
                        command=one)
b_one.grid(row=1, column=0, ipadx=10, ipady=10, padx=1, pady=1)

b_two = tb.Button(button_frame, text="2",
                        style="dark.TButton",
                        command=two)
b_two.grid(row=1, column=1, ipadx=10, ipady=10, padx=1, pady=1)

b_three = tb.Button(button_frame, text="3",
                        style="dark.TButton",
                        command=three)
b_three.grid(row=1, column=2, ipadx=10, ipady=10, padx=1, pady=1)

b_four = tb.Button(button_frame, text="4",
                        style="dark.TButton",
                        command=four)
b_four.grid(row=2, column=0, ipadx=10, ipady=10, padx=1, pady=1)

b_five = tb.Button(button_frame, text="5",
                        style="dark.TButton",
                        command=five)
b_five.grid(row=2, column=1, ipadx=10, ipady=10, padx=1, pady=1)

b_six = tb.Button(button_frame, text="6",
                        style="dark.TButton",
                        command=six)
b_six.grid(row=2, column=2, ipadx=10, ipady=10, padx=1, pady=1)

b_seven = tb.Button(button_frame, text="7",
                        style="dark.TButton",
                        command=seven)
b_seven.grid(row=3, column=0, ipadx=10, ipady=10, padx=1, pady=1)

b_eight = tb.Button(button_frame, text="8",
                        style="dark.TButton",
                        command=eight)
b_eight.grid(row=3, column=1, ipadx=10, ipady=10, padx=1, pady=1)

b_nine = tb.Button(button_frame, text="9",
                        style="dark.TButton",
                        command=nine)
b_nine.grid(row=3, column=2, ipadx=10, ipady=10, padx=1, pady=1)

b_zero = tb.Button(button_frame, text="0",
                        style="dark.TButton",
                        command=zero)
b_zero.grid(row=4, column=1, ipadx=10, ipady=10, padx=1, pady=1)

b_del = tb.Button(button_frame, text="←",
                        style="dark.TButton",
                        command=delete)

b_del.grid(row=4, column=0, ipadx=10, ipady=10, padx=1, pady=1)

b_equal = tb.Button(button_frame, text="=",
                        style="dark.TButton",
                        command=equals)
b_equal.grid(row=4, column=2, ipadx=10, ipady=10, padx=1, pady=1)


#Events
b_sum = tb.Button(events_frame, text="+",
                        width=2,
                        bootstyle="dark",
                        command=get_sum)
b_sum.grid(row=0, column=1, padx=1, pady=1)

b_sub = tb.Button(events_frame, text="-",
                        width=2,
                        bootstyle="dark",
                        command=get_sub)
b_sub.grid(row=0, column=2, padx=1, pady=1)

b_mul = tb.Button(events_frame, text="x",
                        width=2,
                        bootstyle="dark",
                        command=get_multi)
b_mul.grid(row=0, column=3, padx=1, pady=1)

b_div = tb.Button(events_frame, text="÷",
                        width=2,
                        bootstyle="dark",
                        command=get_div)
b_div.grid(row=0, column=4, padx=1, pady=1)

b_root_ext = tb.Button(events_frame, text="√",
                        width=2,
                        bootstyle="dark",
                        command=get_root_ext)
b_root_ext.grid(row=0, column=5, padx=1, pady=1)

b_expo = tb.Button(events_frame, text="xⁿ",
                        width=2,
                        bootstyle="dark",
                        command=get_expo)
b_expo.grid(row=0, column=6, padx=1, pady=1)




app.mainloop()

