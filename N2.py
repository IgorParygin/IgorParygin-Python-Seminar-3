# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

print('Ввидите длинну списка (число)')
n = int(input())

list = [random.randint(1, 100) for i in range(n)]
print(f'Сгенерированный список {list}')

result = []
x = int(n / 2 + 1)

for i in range(x):
    result.append(list[i] * list[-i-1])

print(result)