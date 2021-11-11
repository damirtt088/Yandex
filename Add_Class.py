import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow
from add import Ui_Frm_add

NUM = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.'])


class Addf(QMainWindow, Ui_Frm_add):
    def __init__(self):
        super().__init__()
        self.main = ''
        self.subjec = ''
        self.setupUi(self)
        self.btn_gr_main.buttonClicked.connect(self.what)
        self.btn_gr_eatnm.buttonClicked.connect(self.kindeat)
        self.btn_gr_sport.buttonClicked.connect(self.kindsport)
        self.btn_gr_add.buttonClicked.connect(self.do)

    def kindeat(self, btn):
        if btn.text() == 'Мясо':
            self.subjec = 'meat'
        if btn.text() == 'Морепродукты':
            self.subjec = 'fish'
        if btn.text() == 'Молочные продукты':
            self.subjec = 'milk'

    def kindsport(self, btn):
        if btn.text() == 'Спорт':
            self.subjec = 'sport'
        if btn.text() == 'Повседневные задачи':
            self.subjec = 'usu'

    def what(self, btn):
        if btn.text() == 'Упражнения':
            self.main = 'exesi.db'
            self.rbtn_fish.setEnabled(False)
            self.rbtn_meat.setEnabled(False)
            self.rbtn_milk.setEnabled(False)
            self.rbtn_sport.setEnabled(True)
            self.rbtn_usualy.setEnabled(True)
            self.subjec = ''
        else:
            self.main = 'eat.db'
            self.rbtn_fish.setEnabled(True)
            self.rbtn_meat.setEnabled(True)
            self.rbtn_milk.setEnabled(True)
            self.rbtn_sport.setEnabled(False)
            self.rbtn_usualy.setEnabled(False)
            self.subjec = ''

    def do(self, btn):
        kind = self.txt_name.toPlainText().lower()
        minkkal = self.txt_minut.toPlainText()
        if not kind:
            self.lbl_error.setText('Что надо-то?')
            return 0
        if not self.main or not self.subjec:
            self.lbl_error.setText('Чего-то не хватает')
            return 0
        database = sqlite3.connect(self.main)
        cur = database.cursor()
        numtr = False
        if btn.text() == "Добавить":
            for i in minkkal:
                if i not in NUM:
                    numtr = True
                    break
            if not minkkal or numtr:
                self.lbl_error.setText('Вы что-то не заполнили')
                return 0
            text = f'INSERT INTO {self.subjec} VALUES("{kind.lower()}", {minkkal})'
            cur.execute(text)
        if btn.text() == "Изменить":
            for i in minkkal:
                if i not in NUM:
                    numtr = True
                    break
            if not minkkal or numtr:
                self.lbl_error.setText('Вы что-то не заполнили')
                return 0
            text = f'SELECT Kkal FROM {self.subjec} WHERE Name = "{kind.lower()}"'
            if not cur.execute(text).fetchone():
                self.lbl_error.setText('Такого элемента нет')
                return 0
            text = f'UPDATE {self.subjec} SET Kkal = {minkkal} WHERE Name = "{kind.lower()}"'
            cur.execute(text)
        if btn.text() == "Удалить":
            text = f'SELECT Kkal FROM {self.subjec} WHERE Name =  "{kind.lower()}"'
            if not cur.execute(text).fetchone():
                self.lbl_error.setText('Такого элемента нет')
                return 0
            text = f'DELETE from {self.subjec} where Name = "{kind.lower()}"'
            cur.execute(text)
        database.commit()
        self.lbl_error.setText('Всё готово')
