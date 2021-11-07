import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow
from spent import Ui_frm_spent

NUM = '1234567890'


class Spent(QMainWindow, Ui_frm_spent):
    def __init__(self):
        super().__init__()
        self.exer = ''
        self.setupUi(self)
        self.database = sqlite3.connect('exesi.db')
        self.cur = self.database.cursor()
        self.btn_info.buttonClicked.connect(self.kind)
        self.btn_spt.clicked.connect(self.spent)

    def kind(self, btn):
        if btn.text() == 'Спортивные упражнения':
            self.exer = 'sport'
        if btn.text() == 'Повседневные задачи':
            self.exer = 'usu'

    def spent(self):
        exe = self.txt_gum.toPlainText()
        time = self.txt_time.toPlainText()
        if not self.exer:
            self.lbl_error.setText('Какой вид занятий?')
            return 0
        if time not in NUM:
            time = 1
        if not exe:
            self.lbl_error.setText('Чем занимались?')
            return 0
        text = f'SELECT Name FROM {self.exer} WHERE Name = "{exe}"'
        info = self.cur.execute(text).fetchone()
        if not info:
            self.lbl_error.setText(f"Извините, мы не знаем {exe}")
        else:
            text = f"SELECT Name FROM {self.exer} WHERE Name = {exe}"
            info = self.cur.execute(text).fetchall()
            self.lcd_spent.display(time * info[1])
            self.tbl_spent.setItem(0, 0, info[0])
            self.tbl_spent.setItem(0, 1, info[1])