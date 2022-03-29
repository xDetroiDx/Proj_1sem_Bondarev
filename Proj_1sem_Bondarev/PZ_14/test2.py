# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.

import re

check = False # Задаём флаг

ip_address = open('ip_address.txt', 'r') # Открытие исходного файла
ip_address2 = open('ip_address2.txt', 'w') # Создание первого нового файла
ip_address3 = open('ip_address3.txt', 'w') # Создание второго нового файла

num1 = 0
num2 = 0

for str in open('ip_address.txt', encoding='UTF-8'):
    # переход к разделу
    flag = str.find('Частоупотребимые маски')
    if flag != -1:
        check = True
    if check:
        point = str.find('.')  # Находим точку
        if point > 2 and point < 4:  # Находим позицию точки
            search = re.search(r'[.][1-9]', str)
            if search:
                num1 += 1
                ip_address2.write(str)
            else:
                num2 += 1
                ip_address3.write(str)


print("Количество строк в первом файле:", num1)
print("Количество строк во втором файле:", num2)

ip_address2.close()
ip_address3.close()
ip_address.close()
