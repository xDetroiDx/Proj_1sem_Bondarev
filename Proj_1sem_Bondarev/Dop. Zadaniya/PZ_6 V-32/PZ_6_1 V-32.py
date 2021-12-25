# Дан список размера N. Поменять местами его минимальный и максимальный
# элементы.

import random

N = int(input("Введите длинну списка: "))
a = sorted([random.randint(0, N) for i in range(N)])
print("Список без изменений: ")
print(a)
a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
print("Измененный список: ")
print(a)
