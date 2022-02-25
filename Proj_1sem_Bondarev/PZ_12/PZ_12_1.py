# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

from tkinter import *


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('500x650+0+0')
window.resizable(False, False)


# фоны
frame = Frame(window, bg='#99ff33')
frame.place(relx=0.05, rely=0.03, relwidth=0.9, relheight=0.9)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.08, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.14, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.20, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.30, relwidth=0.82, relheight=0.12)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.43, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.49, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.59, relwidth=0.82, relheight=0.12)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.72, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.78, relwidth=0.82, relheight=0.05)
frame = Frame(window, bg='#009933')
frame.place(relx=0.09, rely=0.79, relwidth=0.82, relheight=0.04)



# строки записи
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.09, relwidth=0.5, relheight=0.03)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.15, relwidth=0.5, relheight=0.03)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.21, relwidth=0.5, relheight=0.03)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.31, relwidth=0.5, relheight=0.10)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.44, relwidth=0.5, relheight=0.03)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.50, relwidth=0.5, relheight=0.03)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.73, relwidth=0.5, relheight=0.03)
txt = Entry(window, width=40)
txt.place(relx=0.4, rely=0.79, relwidth=0.5, relheight=0.03)





# заголовки
lbl = Label(window, text="Step 1: Your details", fg='green', bg='#99ff33', font='15')
lbl.place(x=50, y=25)
lbl = Label(window, text="Step 2: Delivery address", fg='green', bg='#99ff33', font='15')
lbl.place(x=50, y=170)
lbl = Label(window, text="Step 3: Card details", fg='green', bg='#99ff33', font='15')
lbl.place(x=50, y=360)



# подписи
lbl = Label(window, text="Name", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=55)
lbl = Label(window, text="Email", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=95)
lbl = Label(window, text="Phone", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=135)
lbl = Label(window, text="Address", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=200)
lbl = Label(window, text="Post code", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=285)
lbl = Label(window, text="Country", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=325)
lbl = Label(window, text="Card type", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=385)
lbl = Label(window, text="Security code", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=470)
lbl = Label(window, text="Name on card", fg='black', bg='#009933', font='5')
lbl.place(x=50, y=510)

# карты
var = IntVar()
var.set(0)
rV = Radiobutton(window, text="VISA", fg='black', bg='#009933', font='5', variable=var, value=1)
rV.place(x=90, y=430)
rA = Radiobutton(window, text="AmEx", fg='black', bg='#009933', font='5', variable=var, value=2)
rA.place(x=220, y=430)
rM = Radiobutton(window, text="Mastercard", fg='black', bg='#009933', font='5', variable=var, value=3)
rM.place(x=340, y=430)



# кнопки
btn = Button(window, text="BAY IT!", bg="#006600")
btn.place(x=210, y=545)


window.mainloop()
