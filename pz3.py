# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
rand_list = [randint(1, 20) for _ in range(10)]
rez = 0
for i in range(0, len(rand_list), 2):
    rez = rez + rand_list[i]
print(rand_list)
print(rez)



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
rand_list = [randint(1, 20) for _ in range(10)]
new_list = []
for i in range(0, (len(rand_list) - 1) // 2 + 1):
    new_list.append(rand_list[i] * rand_list[len(rand_list) - 1 - i])
print(rand_list)
print(new_list)



# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

f_list = [float(input()) for _ in range(int(input()))]
min = 1
for x in f_list:
    if x % 1 < min and x % 1 != 0:
        min = x % 1
    else:
        if x % 1 > max:
            max = x % 1
print(max, min)
print(max - min)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input())
binary = '' 
while n > 0:
    binary = str(n % 2) + binary
    n = n // 2
print(binary)