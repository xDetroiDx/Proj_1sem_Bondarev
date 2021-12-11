# Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать
# строку, выполнив циклическую замену каждой буквы на букву того же регистра,
# расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
# K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё»
# в алфавите не учитывать, знаки препинания и пробелы не изменять.

A = input("Введите слово или предложение: ")
K = int(input("Введите число: "))
i = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
l = i.swapcase()
while (K < 0) or (K > 10):
    print("Число не соответствует условию")
    K = int(input("Введите число: "))

A1 = []

for p in range(len(A)):
    A1.append(A[p])

for p in range(len(A)):
    for a in range(len(i)):
        if a >= len(i)-K+1:
            if A1[p] in i[a] or A1[p] in l[a]:
                if A1[p].isupper():
                    A1[p] = i[a + K - a].capitalize()
                    break
                else:
                    A1[p] = i[a + K - a]
                    break
        else:
            if A1[p] in i[a] or A1[p] in l[a]:
                if A1[p].isupper():
                    A1[p] = i[a + K + 1].capitalize()
                    break
                else:
                    A1[p] = i[a + K + 1]
                    break
t = 0
while t < len(A)-1:
    A1[0] += A1[1]
    del A1[1]
    t += 1
print(A1[0])
