# В матрице элементы второго столбца возвести в квадрат.

import random


row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]
print("Матрица: ", matrix)
s = [matrix[j][1]*matrix[j][1] for j in range(row)]
a = [matrix[j].insert(1, s[j]) for j in range(row)]
b = [matrix[j].pop(2) for j in range(row)]
print(matrix)