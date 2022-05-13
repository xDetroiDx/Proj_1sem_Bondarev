# Сгенерировать матрицу, в которой все нечетные элементы заменяются на 0

import random


s = []
row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]
print(matrix)
s = [[0 for i in range(1)] for j in range(row)]
[[s[j].append(matrix[j][i]) if matrix[j][i] % 2 == 0 else s[j].append(0) for i in range(column)] for j in range(row)]
[[s[j].pop(0) for i in range(1)] for j in range(row)]
print(s)
