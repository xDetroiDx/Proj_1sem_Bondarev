# Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).

import random

def func(l, n):
    return l[n:] + l[:n]

a = int(input("Введите длинну списка: "))
b = sorted([random.randint(0, a) for i in range(a)])
c = 1
print("Исходный список: ")
print(b)
print("Новый список: ")
print(func(b, -c))
