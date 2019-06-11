# 2. Задано чотирицифрове натуральне число. 
#      Знайти добуток цифр цього числа.
#      Записати число в реверсному порядку.
#      Посортувати цифри, що входять в дане число


int_number = str(input("Please enter an integer four-digit number: "))
item = 1
for i in list(int_number):
     item *= int(i)
print("The product of numbers: ",item)
print("Number in reverse order: ", ''.join(reversed(int_number)))
print("Sort by increment: ",''.join(sorted(int_number)))
print("Sort by decrease: ",''.join(sorted(str(int_number), reverse=True)))