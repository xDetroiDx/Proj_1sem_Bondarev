# Дано целое число N (1 < N < 26). Вывести N последних строчных (то есть маленьких)
# букв латинского алфавита в обратном порядке (начиная с буквы «z»).


N = int(input("Введите число: "))

while (N < 1) or (N > 26):
    print("Число не соответствует условию")
    N = int(input("Введите число: "))

A = ('abcdefghijklmonpqrstuvwxyz')

print(''.join(reversed(A[N-N-N:26])))
