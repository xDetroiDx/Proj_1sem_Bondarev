# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.

D = 0
T = float(1.2)
A = input("Введите цену 1-ого кг : ")  # Ввод переменной

while type(A) != float:  # обработка исключений
    try:
        A = float(A)
    except ValueError:
        print("Неправельно ввели! ")
        A = input("Введите первое число: ")

while T < 2:
    D = A * T
    print(round(D, 1), "Цена за", round(T, 1), "кг")
    T += 0.2
