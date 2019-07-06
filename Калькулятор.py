from math import sqrt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Назва вікна
root = Tk()
root.title("Калькулятор")

# def check_calc_entry():
#     """This function checks the correctness of the entered data"""
#     checklist = ['-','+','/','.','*','**','sqrt','0','9','8','7','6','5','4','3','2','1']
#     element = 0
#     for element in calc_entry.get() not in checklist:
#         element += 1
#         messagebox.showerror("Помилка!", "Введіть допустимі символи!\n '-+/**=0987654321'")
    
    
# Логіка калькулятора

def calc(key):
    global memory
    if key == "=":

# Недопускаємо введення букв
# ".*-+/**=0987654321"
        
        # if check_calc_entry():
            
            
        #     messagebox.showerror("Помилка!", "Введіть коректні данні!")
            

# Рахуємо

        try:
            result = round(eval(calc_entry.get()),16)
            calc_entry.insert(END," = {}".format(str(result)))
        except:
            messagebox.showerror("Помилка!", "Введіть допустимі символи!\n '-+/**=0987654321'")

# Очистити поле

    elif key == "C":
        calc_entry.delete(0, END)

# Корінь
    
    elif key == "sqrt":
        if calc_entry.get()[0] =="-":
            messagebox.showerror("Помика!", "Йой, Йой, мінус не канає!!!")
        else:
            calc_entry.insert(END," sqrt = {}".format(str(sqrt(float(calc_entry.get())))))
 
#  +- зміна

    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0,END) 
        try:
            if calc_entry.get()[0] =="-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0,"-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

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
    command = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=command).grid(row=r,column=c)
    c += 1
    if c>4:
        c=0
        r += 1

# Ширина рядка введеня

calc_entry = Entry(root, width = 63)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()