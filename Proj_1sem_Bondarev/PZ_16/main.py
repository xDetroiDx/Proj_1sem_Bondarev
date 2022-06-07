import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить клиента', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск клиента", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score', 'cards', 'sum'), height=15, show='headings')

        self.tree.column('user_id', width=100, anchor=tk.CENTER)
        self.tree.column('name', width=220, anchor=tk.CENTER)
        self.tree.column('sex', width=180, anchor=tk.CENTER)
        self.tree.column('old', width=70, anchor=tk.CENTER)
        self.tree.column('score', width=80, anchor=tk.CENTER)
        self.tree.column('cards', width=140, anchor=tk.CENTER)
        self.tree.column('sum', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='Код клиента')
        self.tree.heading('name', text='Ф. И. О.')
        self.tree.heading('sex', text='Переодический платеж')
        self.tree.heading('old', text='Годовой %')
        self.tree.heading('score', text='Срок вклада')
        self.tree.heading('cards', text='Пластиковая карта')
        self.tree.heading('sum', text='Конечная сумма')

        self.tree.pack()

    def records(self, user_id, name, sex, old, score, cards, sum):
        self.db.insert_data(user_id, name, sex, old, score, cards, sum)
        self.view_records()

    def update_record(self, user_id, name, sex, old, score, cards, sum):
        self.db.cur.execute("""UPDATE users SET user_id=?, name=?, sex=?, old=?, score=?, cards=?, sum=? WHERE user_id=?""",
                            (user_id, name, sex, old, score, cards, sum, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, name):
        name = ("%" + name + "%",)
        self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    # def search_records(self, score):
    #     score = (score,)
    #     self.db.cur.execute("""SELECT * FROM users WHERE score>?""", score)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить клиента')
        self.geometry('490x330+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Код клиента')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=25)

        label_name = tk.Label(self, text='Ф. И. О.')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        label_sex = tk.Label(self, text='Переодический платеж')
        label_sex.place(x=50, y=75)
        self.entry_sex = ttk.Entry(self)
        self.entry_sex.place(x=200, y=75)

        label_old = tk.Label(self, text='Годовой %')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=200, y=100)

        label_score = tk.Label(self, text='Срок вклада')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=200, y=125)

        label_cards = tk.Label(self, text='Пластиковая карта')
        label_cards.place(x=50, y=150)
        self.entry_cards = ttk.Entry(self)
        self.entry_cards.place(x=200, y=150)

        label_sum = tk.Label(self, text='Конечная сумма')
        label_sum.place(x=50, y=175)
        self.entry_sum = ttk.Entry(self)
        self.entry_sum.place(x=200, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=350, y=220)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=270, y=220)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_sex.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get(),
                                                                       self.entry_cards.get(),
                                                                       self.entry_sum.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=255, y=220)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_sex.get(),
                                                                          self.entry_old.get(),
                                                                          self.entry_score.get(),
                                                                          self.entry_cards.get(),
                                                                          self.entry_sum.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD/saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER,
                old INTEGER,
                score INTEGER,
                cards INTEGER,
                sum INTEGER
                )""")

    def insert_data(self, user_id, name, sex, old, score, cards, sum):
        self.cur.execute("""INSERT INTO users(user_id, name, sex, old, score, cards, sum) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                             (user_id, name, sex, old, score, cards, sum))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Банк")
    root.geometry("930x375+300+200")
    root.resizable(False, False)
    root.mainloop()