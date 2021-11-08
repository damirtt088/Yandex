import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from spent import Ui_frm_spent
from datetime import datetime
from Yourself_Class import WEIGHT

NUM = '1234567890'


class Spent(QMainWindow, Ui_frm_spent):
    def __init__(self):
        super().__init__()
        self.exer = ''
        self.setupUi(self)
        self.database = sqlite3.connect('exesi.db')
        self.cur = self.database.cursor()
        self.datainfo = sqlite3.connect('info.db')
        self.curinfo = self.datainfo.cursor()
        self.btn_info.buttonClicked.connect(self.kind)
        self.btn_spt.clicked.connect(self.spent)


    def kind(self, btn):
        if btn.text() == 'Спортивные упражнения':
            self.exer = 'sport'
        if btn.text() == 'Повседневные задачи':
            self.exer = 'usu'
        text = f'SELECT * FROM {self.exer}'
        info = self.cur.execute(text).fetchall()
        self.tbl_spent.setRowCount(len(info))
        for i, elem in enumerate(info):
            for j, val in enumerate(elem):
                self.tbl_spent.setItem(i, j, QTableWidgetItem(str(val)))
        self.tbl_spent.setColumnWidth(1, 100)

    def spent(self):
        if not WEIGHT:
            self.lbl_error.setText('Сначала заполните информацию о себе')
            return 0
        exe = self.txt_gum.toPlainText().lower()
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
            self.lcd_spent.display(time * info[1] * WEIGHT)
            self.tbl_spent.setItem(0, 0, info[0])
            self.tbl_spent.setItem(0, 1, info[1])
            data = datetime.now().date()
            search = self.curinfo.execute("""SELECT * FROM info WHERE DATA = ?""", (data,)).fetchone()
            if not search:
                self.curinfo.execute("""INSERT INTO info VALUES(?, ?, ?, ?, ?)""", (data, 0, 0, 0, 0))
                self.datainfo.commit()
            self.curinfo.execute("""UPDATE info
                SET Spentk += ?
                WHERE DATA = ?""", (time * info[1] * WEIGHT, data))
            self.curinfo.execute("""UPDATE info
                            SET Spenttime += ?
                            WHERE DATA = ?""", (time, data))
            self.datainfo.commit()


