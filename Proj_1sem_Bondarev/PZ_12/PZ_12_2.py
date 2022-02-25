# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ № 3 – 8.

# С помощью функций получить вертикальную и горизонтальную линии.
# Линия проводится многократной печатью символа.
# Заключить слово в рамку из полученных линий.

from tkinter import *



def ramka(a, b):

    r = ('-' * a + '\n' + '|' + b.center(a - 2) + '|' + '\n' + '-' * a)
    return r







w = Tk()
w.title('PZ_5_1')
w.geometry('420x300')
w.resizable(False, False)

Label(text="Введите слово: ").grid(row=1, column=0)
c = text = Entry(w, width=40)
c.grid(row=1, column=1)
b = str(c)
a = len(b) + 2

Label(text="Слово с рамкой: ").grid(row=5, column=0)
Label(text=ramka(a, b)).grid(row=5, column=1)

button1 = Button(text="Рамка")
button1.grid(row=4, column=1)

button1.bind('<Button-1>', ramka(a, b))
print(ramka(a, b))

w.mainloop()