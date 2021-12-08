# Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
# положительного числа K, а также их сумму S (K — входной, C и S — выходные параметры
# целого типа). С помощью этой функции найти количество и сумму цифр для каждого из
# пяти данных целых чисел.

import random


def digitcountsum(k, result):
    s = str(k)
    n = len(s)
    _sum = 0
    for i in range(n):
        _sum += int(s[i])
    result['C'] = n
    result['S'] = _sum


for i in range(5):
    K = random.randrange(1, 10000)
    print("Исходное: ", K)

print()

r = {'C': None, 'S': None}
for i in range(5):
    K = random.randrange(1, 10000)
    digitcountsum(K, r)

    print("Число ", i + 1, ": ", K)
    print('Количество цифр = ', r['C'])
    print('Сумма цифр = ', r['S'])
    print()
