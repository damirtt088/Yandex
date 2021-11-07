import sqlite3
import csv
from datetime import datetime


from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from recived import Ui_frm_recieved


NUM = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
Default = 1


class Recieved(QMainWindow, Ui_frm_recieved):
    def __init__(self):
        super().__init__()
        self.data = datetime.today()
        self.database = sqlite3.connect('eat.db')
        self.cur = self.database.cursor()
        self.product = ''
        self.setupUi(self)
        self.btn_calc.clicked.connect(self.recived)
        self.btn_grp_product.buttonClicked.connect(self.kind)

    def kind(self, btn):
        if btn.text() == 'Мясо':
            self.product = 'meat'
        if btn.text() == 'Морепродукты':
            self.product = 'fish'
        if btn.text() == 'Молочные продукты':
            self.product = 'milk'

    def recived(self):
        eat = self.txt_eat.toPlainText()
        gramm = self.txt_gramm.toPlainText()
        numtr = False
        if not eat:
            self.lbl_error.setText('Какой продукт-то?')
        for i in gramm:
            if i not in NUM:
                numtr = True
        if numtr or not gramm:
            gramm = 1
        else:
            gramm = int(gramm) / 100
        if not self.product:
            self.lbl_error.setText('Какой вид продукта Вы хотите посмотреть? Введите и ещё раз нажмите рассчитать')
            return 0
        text = f'SELECT Kkal FROM {self.product} WHERE Name = "{eat.lower()}"'
        info = self.cur.execute(text).fetchone()
        if not info:
            self.lbl_error.setText("Извините, но у нас нет такого продукта")
        else:
            self.lcd_gramm.display(info[0])
            self.lcd_recived.display(info[0] * gramm)
            self.tbl_info.setItem(0, 0, QTableWidgetItem(eat))
            self.tbl_info.setItem(0, 1, QTableWidgetItem(str(info[0])))
