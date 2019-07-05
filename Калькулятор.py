# imort dМодуль decimal
from decimal import Decimal
from math import sqrt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")
# Логіка калькулятора
def calc(key):
    global memory
    if key == "=":
# Недопускаємо введення букв
        str1 =".-+/*=0987654321sqrt"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Перший символ не число!")
            messagebox.showerror("Error, you enter not number!")
# Рахуємо
        try:
            result = round(eval(calc_entry.get()),4)
            calc_entry.insert(END,"="+str(result))
        except:
            calc_entry.insert(END, "Помилка!")
            messagebox.showerror("Помика!", "введіть правильні данні")
# Очистити поле
    elif key =="C":
        calc_entry.delete(0, END)
#  Корінь 
    elif key == "sqrt":
        calc_entry.sqrt[0]
#  +- зміна
    # elif key == "-/+":
    #     if "=" in calc_entry.get():
    #         calc_entry.delete(0,END)
    #     try:
    #         if calc_entry.get()[0] =="-":
    #             calc_entry.delete(0)
    #         else:
    #             calc_entry.insert(0,"-")
    #     except IndexError:
    #         pass
    # else:
    #     if "=" in calc_entry.get():
    #         calc_entry.delete(0, END)
    #     calc_entry.insert(END, key)

# Створюємо кнопки

bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "sqrt", "=",
    "0", ".", "C", 
]
r = 1
c = 0

for i in bttn_list:
    rel = ""
    command = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=command).grid(row=r,column=c)
    c += 1
    if c>4:
        c=0
        r += 1

calc_entry = Entry(root, width = 50)
calc_entry.grid(row=0, column=0, columnspan=5)
root.mainloop()