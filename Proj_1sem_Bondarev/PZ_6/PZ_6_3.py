# Дан список размера N. Обнулить все его локальные максимумы (то есть числа,
# большие своих соседей).

import random

N = int(input("Введите размер списка: "))

A = [random.randint(0, 9) for i in range(N)]

print(A)

for i in range(1, N-1):
    if A[i-1] < A[i] and A[i] > A[i+1]:
        A[i] = 9999999
for i in range(1, N-1):
    if A[i] == 9999999:
        A[i] = 0

print("Результат:\n", A)
