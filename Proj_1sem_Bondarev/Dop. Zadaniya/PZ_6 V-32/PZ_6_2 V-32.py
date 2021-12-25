# Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент BK равен сумме элементов списка A с номерами от K до
# N

import random

n = int(input("Введите длинну списка: "))
a = sorted([random.randint(0, n) for i in range(n)])
s = 0
print("Исходный список: ")
print(a)
b = []
for i in range(n-1, -1, -1):
     s = s+a[i]
     b.insert(0, s)
print("Новый список: ")
print(b)
