# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).

print('Ввидите индекс последовательности Фибоначчи')
n = int(input())

fib = [0]
a = 1
b = 0
x = 1
y = 0
for i in range(n):
    temp = a + b
    a = b
    b = temp
    fib.append(temp)
    tmp = x - y
    x = y
    y = tmp
    fib.insert(0, tmp)

print(fib)