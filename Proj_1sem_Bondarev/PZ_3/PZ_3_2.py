# Мастям игральных карт присвоены порядковые номера:
# 1– пики, 2 – трефы, 3 – бубны, 4 – червы.
# Достоинству карт, старших десятки, присвоены номера:
# 11 – валет, 12 – дама, 13 – король, 14 – туз.
# Дано трехзначное число, в котором первая цифра указывает на масть,
# а вторые две на достоинство карты.
# Вывести соответствующее название карты вида «дама червей», «туз треф» и т.п.

a = input("Введите трехзначное число: ")

while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправельно ввели! ")
        a = input("Введите трехзначное число: ")

    try:
        while a < 99 or a > 1000:
            print("Введено неправильное число")
            a = input("Введите трехзначное число: ")
    except TypeError:
        continue

if (a // 100 == 1) and (a % 100 == 11):
    print("Валет пики")

elif (a // 100 == 1) and (a % 100 == 12):
    print("Дама пики")

elif (a // 100 == 1) and (a % 100 == 13):
    print("Король пики")

elif (a // 100 == 1) and (a % 100 == 14):
    print("Туз пики")

elif (a // 100 == 2) and (a % 100 == 11):
    print("Валет треф")

elif (a // 100 == 2) and (a % 100 == 12):
    print("Дама треф")

elif (a // 100 == 2) and (a % 100 == 13):
    print("Король треф")

elif (a // 100 == 2) and (a % 100 == 14):
    print("Туз треф")

elif (a // 100 == 3) and (a % 100 == 11):
    print("Валет буби")

elif (a // 100 == 3) and (a % 100 == 12):
    print("Дама буби")

elif (a // 100 == 3) and (a % 100 == 13):
    print("Король буби")

elif (a // 100 == 3) and (a % 100 == 14):
    print("Туз буби")

elif (a // 100 == 4) and (a % 100 == 11):
    print("Валет черви")

elif (a // 100 == 4) and (a % 100 == 12):
    print("Дама черви")

elif (a // 100 == 4) and (a % 100 == 13):
    print("Король черви")

elif (a // 100 == 4) and (a % 100 == 14):
    print("Туз черви")

else:
    print("Нет такой карты")
