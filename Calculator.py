from math import sqrt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Назва вікна
root = Tk()
root.title("Калькулятор")
    
# Логіка калькулятора
def calculator(key):
    """This function defines the logic of the calculator"""
    if key == "=":

# Рахуємо
        try:
            result = round(eval(calculator_entry.get()),16)
            calculator_entry.insert(END," = {}".format(str(result)))
        except:
            messagebox.showerror("Помилка!", "Введені некоректні данні!\n\n     Допустимі символи:\n\n     '.-+*/**=0987654321'")
            

# Очистити поле
    elif key == "C":
        calculator_entry.delete(0, END)

# Корінь квадратний
    elif key == "sqrt":
        if calculator_entry.get()[0] =="-":
            messagebox.showerror("Помика!", "Йой, Йой, мінус не канає!!!")
        else:
            calculator_entry.insert(END," sqrt = {}".format(str(sqrt(float(calculator_entry.get())))))
 
#  +- зміна
    elif key == "-/+":
        if "=" in calculator_entry.get():
            calculator_entry.delete(0,END) 
        try:
            if calculator_entry.get()[0] =="-":
                calculator_entry.delete(0)
            else:
                calculator_entry.insert(0,"-")
        except IndexError:
            pass
    else:
        if "=" in calculator_entry.get():
            calculator_entry.delete(0, END)
        calculator_entry.insert(END, key)

# Створюємо кнопки
bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "sqrt", "**",
    "0", ".", "C", "-/+",'='
]
r = 1
c = 0

for i in bttn_list:
    rel = ""
    command = lambda x=i: calculator(x)
    ttk.Button(root, text=i, command=command).grid(row=r,column=c)
    c += 1
    if c>4:
        c=0
        r += 1

# Ширина рядка введеня
calculator_entry = Entry(root, width = 63)
calculator_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()