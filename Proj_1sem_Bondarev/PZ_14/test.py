# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные адреса» перенести в первый
# файл строки с ненулевыми первым и вторым октетами, а во второй – все остальные. Посчитать количество
# полученных строк в каждом файле.

import re

check = False # Задаём флаг

ip_address = open('ip_address.txt', 'r') # Открытие исходного файла
first_file = open('first_file.txt', 'w') # Создание первого нового файла
second_file = open('second_file.txt', 'w') # Создание второго нового файла

num1 = 0
num2 = 0

for str in open('ip_address.txt', encoding='UTF-8'):
    # переход к разделу
    flag = str.find('Зарезервированные адреса')
    if flag != -1:
        check = True
    if check:
        point = str.find('.')  # Находим точку
        if point < 4 and point > 0:  # Находим позицию точки
            match = re.match(r'[1-9][.][1-9][.]', str)
            if match:
                num1 += 1
                first_file.write(str)
            else:
                num2 += 1
                second_file.write(str)


print("Количество строк в первом файле:", num1)
print("Количество строк во втором файле:", num2)

first_file.close()
second_file.close()
ip_address.close()
