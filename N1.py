# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

print('Ввидите длинну списка (число)')
n = int(input())

list = [random.randint(1, 100) for i in range(n)]
print(f'Сгенерированный список {list}')

summ = 0

for i in range(n):
    if i % 2 == 0:
        summ += list[i]
print(summ)