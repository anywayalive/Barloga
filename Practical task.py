#Змінній   value_int надайте значення 10,
#                value_float - значення 8.4, 
#                 value_str - "No".
#1.	Змініть значення, збережене у змінній value_int, збільшивши його в 3.5 рази, 
# результат зв'яжіть зі змінною big_int.
#2.	Змініть значення, збережене у змінній value_float, зменшивши його на одиницю, 
# результат зв'яжіть з тією ж змінною.
#3.	Розділіть value_int на value_float, а потім big_int на value_float. Результат 
# даних виразів не прив'язуйте до жодних змінних.
#4.	Змініть значення змінної value_str на "NoNoYesYesYes". При формуванні нового 
# значення використовуйте операції конкатенації (+) і повторення рядка (*).


# value_int = int(10)
# value_float = float(8.4)
# value_str = str("No")
# big_int = (value_int*3.5)
# print ("big_int ", big_int)
# value_float = (value_float - 1)
# print ("value_float ", value_float)
# print (value_int/value_float)
# print (big_int/value_float)
# value_str = ((value_str*2)+(3*"Yes"))
# print (value_str)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # перевірити яке з двох чисел більше

# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# if a==b:
#     print ("First number: ",a,"Second number: ",b," Both numbers are equal!")
# elif a<b:
#     print ("First number: ",a,"Second number: ",b," The second number is more!")
# else:
#     print ("First number: ",a,"Second number: ",b," First number more!")

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 2.	Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне 
# # повідомлення.

# input_number = int(input("Input number: "))
# if input_number%2==0:
#     print ("The number: {} is paired!".format(input_number))
# else:
#     print ("The number: {} no paired!".format(input_number))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 3.	Написати скрипт, який обчислить факторіал введеного числа.

# input_number = int(input("Input natural number: "))
# i = 1
# fact = 1
# while i <= input_number: 
#     fact *= i
#     i += 1
# print("Factorial {}! ={}".format(input_number,fact))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 1.	Роздрукувати всі парні числа менші 100 
# # (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

# i = 0
# while i<100:
#     if i % 2 == 0:
#         print(i)
# #     i = i + 1
# #####################################
# # for i in range(100):
# #     if i % 2 == 0:
# #         print(i)
# ###################################
# for i in range(0,100,2):
#     print(i)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 2. Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: 
# # один використовуючи оператор continue, а інший без цього оператора).

# for item in range(100):
#     if item % 2 == 0:
#         continue
#     print(item)
# ################################
# for item in range(1,100,2):
#     print(item)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 3.	Перевірити чи список містить непарні числа.
# #           (Підказка: використати оператор break)

# list_number=[2,4,6,8,9,10]
# contain_odd=False
# for i in list_number:
#     if not i % 2 == 0: 
#         contain_odd=True
#         break
# if contain_odd:
#     print("There is odd number in the list")
# else: 
#     print("There is only even number in the list")

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 4.	Створити список, який містить елементи цілочисельного типу, потім 
# за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# # (Підказка: використати вбудовану функцію float ()).

# list_number = [2,3,4,5,6,7,8,8,9,12]
# element = []
# for i in list_number:
#     element.append(float(i))
# list_number = element
# print(list_number)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # # 5.	Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. 
# # # (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# n=int(input('enter some number from fibonacci list='))
# fibonacci_numbers = [0, 1]
# for i in range(2,n):
#     fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
#     if fibonacci_numbers[i]==n:
#         break
# print('there are some numbers from fibanacci till that you entered',n,'\n',fibonacci_numbers)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 6.	Створити список, що складається з чотирьох елементів типу string. Потім, 
# # за допомогою циклу for, вивести елементи по черзі на екран.

# List_elements = ['ta','po','ha','be']
# for i in List_elements:
#     print(i)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 7.	Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”. 
# #          (Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).

# List_elements = ['ta','po','ha','be']
# for i in List_elements:
#     for j in i:
#         print(j,end='#')

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # 8.	Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.

# input_namber = int(input("Your number: "))
# for i in range(2,input_namber):
#     if input_namber % i ==0:
#         print("Number is complex")
#         break
#     else:print("Number is simple")

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 9.	Знайти максимальну цифру дійсного числа. Дійсне число генеруємо випадковим чином за допомогою методу random() з модуля random
# (для цього підключаємо модуль random наступним чином  from random import random)

# import random
# random_list=[random.randrange(1,1000) for i in range(int(input("Input number of elements in list: ")))]
# print("Max number in a {} = {}".format(random_list,max(random_list)))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 10.	Визначити чи введене слово паліндром, тобто чи воно читається однаково зліва направо і навпаки.

# input_number = input("Enter your name: ")
# if input_number == input_number[::-1]:
#     print("You number palindrom")
# else:
#     print("Not palindrom")

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1.	Створити список цілих чисел, які вводяться з терміналу та визначити серед них 
# максимальне та мінімальне число.

# number_user = [int(input("input your number: ")) for i in range(int(input("Input number of elements in list: ")))]
# print("In list {}:\nMax = {}\nMin = {}".format(number_user,max(number_user),min(number_user)))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1.	Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

# def arithmetic_mean(*arg):
#     """this function counts the arithmetic mean"""
#     return print("arithmetic mean: ",sum(arg) / len(arg))
# arithmetic_mean(1,2,3,4)

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2.	Написати функцію, яка повертає абсолютне значення числа

# def modul(num):
#     """This function finds a number module"""
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(modul(-5))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3.	Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати
#  рядки документації DocStrings.

# def find_max(num1,num2):
#     """maximum number of two numbers"""
#     if num1>num2: return num1
#     elif num1==num2:
#         print("Numbers are equal")
#     else: return num2
# print("max number: ",find_max(5,3))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 4.	Написати програму, яка обчислює площу прямокутника, трикутника та кола 
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від 
# вибору користувача)


# choise_figure = str(input("choose a geometric figure:"'\n'"Triangle - 1"'\n'"Circle - 2"'\n'"Rectangle - 3"'\n'))
# def area_triangle(a,b,c):
# """This function finds area triangle"""
#     p=(a+b+c)/2
#     return (p*(p-a)*(p-b)*(p-c))**0.5
# def area_circle(r):
# """This function finds area circle"""
#     return 3.14*(r**2) 
# def area_rectangle(a,b):
# """This function finds area rectangle"""
#     return a*b
# if choise_figure == "1":
#     a = float(input("Enter the first side: "))
#     b = float(input("Enter the second side: "))
#     c = float(input("Enter the third side: "))
#     print("Area of triangle: ",area_triangle(a,b,c),'m2')
# elif choise_figure == "2":
#     r = float(input("Enter radius: "))
#     print("Area of circle: ",area_circle(r),"m2")
# elif  choise_figure == "3" :
#     a = float(input("Enter the first side: "))
#     b = float(input("Enter the second side: "))
#     print("Area of rectangele: ",area_rectangle(a,b),"m2")
# else:
#     print("You luse. Restart program!!!")

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 5.	Написати функцію, яка обчислює суму цифр введеного числа.

# def sum_number(num):
    #  """sum numbers"""
#     lol = 0
#     i=1
#     for i in range(1,num+1):
#         lol += i
#         i += 1
#     return lol
   
# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
# 7.	Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.

# def fib(n):             # write Fibonacci series up to n
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#     print()
# print(fib(500))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 8.	Написати програму, яка обчислює дискримінант квадратного рівняння

# def qvadro_vieto(a,b,c):
# """Discriminator"""
#     D = (b**2) - (4*a*c)
#     return print("The discriminator of the square equation: ",a,"x**2 +",b,"x +",c," = 0 is equal to:", D)
# print(qvadro_vieto(1,2,3))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1.	Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне,
# чи введені дані коректні.

# class Parne:
#     def __init__(self,number):
# try:
#     self.number = int(input("Enter yor number: "))
# except TypeError:
#     print("ooops something wrong!")
# if self.number %2 == 0:
#     print("You number is even!")
# if self.number %2 != 0:
#     print("Yor number is odd!")
# print(Parne(5))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2.	Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення
#  про те чи вік є парним чи непарним числом. Необхідно передбачити можливість введення від’ємного числа,
#   в цьому випадку згенерувати власну виняткову ситуацію. Головний код має викликати функцію, яка обробляє 
#   введену інформацію. 



# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3.	Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
# Використати блоки else та finaly.

# try:
#     num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
#     result = num1 / num2
#     print("Result is", result)
 
# except ZeroDivisionError:
#     print("Division by zero is error !!")
# except ValueError:
#     print("Value Error.") 
# except SyntaxError:
#     print("Comma is missing. Enter numbers numbers separated by comma like this 1, 2")
#  #65866hgjh75785
# except:
#     print("Wrong input")
 
# else:
#     print("No exceptions")

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 4.	Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

# d = {
#     1: 'Monday',
#     2: 'Tuesday',
#     3: 'Wednesday',
#     4: 'Thursday',
#     5: 'Friday',
#     6: 'Saturday',
#     7: 'Sunday'
# }
# while True:
#     try:
#         i = int(input('Enter the day of the week: '))
#     except ValueError:
#         print('You did not enter a number!')
#     else:
#         print(d.get(i, 'There is no such day of the week!'))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1.	Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами,
# використовуючи  більш надійний метод.

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names)

# swap = map(lambda x: hash(x),names)
# print(list(swap))

# swap = map(hash,names)
# print(list(swap))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2.Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список,
# всі числа якого мають тип даних integer:
# 1)	використовуючи метод  append
# 2)	використовуючи метод  map

# list_map = ['1','2','3','4','5','7']
# app = []
# for i in list_map:
#     app.append(int(i))
# print (app)

# app1 = map(int,list_map)
# print (list(app1))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#  	a) використовуючи функцію map
# 	b) використовуючи функцію map та lambda

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 5.  Знайти найбільший елемент в списку  використовуючи функцію reduce

from functools import reduce
list = [1, 2, 3, 4, 5, 7, 9, 5, 4, 3]
print(reduce(lambda a,i:for a  max(iin int(list)))

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 6. Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. Повертає колекцію тих елементів, для яких функція повертає True.
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
# height_total = 0 
# height_count = 0 
# for person in people: 
#     if 'height' in person: 
#         height_total += person['height'] 
#         height_count += 1 
# print(height_total)
# # => 240

# 7. Використовуючи декілька декораторів створіть сендвіч, який складається з листя салату, помідорів та мяса.
#  <\^^^^^^^/>
#   #tomatos#
#   --meat--
#   ~salad~
# <\______/>
# 8. Cтворити просту функцію-генератор, аналогічну роботі ітератора range.