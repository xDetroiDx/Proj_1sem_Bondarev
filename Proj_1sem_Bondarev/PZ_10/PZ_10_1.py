# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы, умноженные на минимальный элемент:

import random
f1 = open('new_file_1.txt', 'w', encoding='UTF-8')
f1.write(str([random.randint(-10, 10) for i in range(10)]))
f1.write(" ")
f1.close()


f2 = open('new_file_2.txt', 'w', encoding='UTF-8')
f2.write(str([random.randint(-10, 10) for i in range(10)]))
f2.write(" ")
f2.close()

f1 = open('new_file_1.txt')
i = f1.read()
f1.close()
f2 = open('new_file_2.txt')
q = f2.read()
f2.close()

f3 = open('new_file_3.txt', 'w', encoding='UTF-8')
f3.write(" ")
f3.write(f1 + f2)
f3.close()

