# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы, умноженные на минимальный элемент:

import random
d = 0
a = []
b = []
f1 = open('new_file_1.txt', 'w', encoding='UTF-8')
for i in range(10):
    a.append(random.randint(-10, 10))
    f1.write(str(a[i]))
    f1.write(" ")
f1.close()


f2 = open('new_file_2.txt', 'w', encoding='UTF-8')
for i in range(10):
    b.append(random.randint(-10, 10))
    f2.write(str(b[i]))
    f2.write(" ")
f2.close()

f1 = open('new_file_1.txt', 'r')
i = f1.read()
f1.close()
f2 = open('new_file_2.txt', 'r')
q = f2.read()
f2.close()


f3 = open('new_file_3.txt', 'w', encoding='UTF-8')
f3.write("Исходные данные: \n")
f3.write(i)
f3.write(q)
f3.write('\n')
f3.write("Количество элементов: \n")
f3.write(str(len(a) + len(b)))
f3.write('\n')

f3.close()
d += int([i])
print(d)
