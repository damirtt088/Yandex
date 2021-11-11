import sys
import sqlite3


from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mainform2 import Ui_MainWindow
from Recived_Class import Recieved
from Spent_Class import Spent
from Add_Class import Addf
from Yourself_Class import Yourself


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = sqlite3.connect('info.db')
        self.cur = self.database.cursor()
        self.load()
        self.btn_spent.clicked.connect(self.spent)
        self.form_spent = Spent()
        self.form_received = Recieved()
        self.add = Addf()
        self.yourself = Yourself()

        self.btn_received.clicked.connect(self.recived)
        self.btn_add.clicked.connect(self.add_f)
        self.btn_youself.clicked.connect(self.youer)
        self.btn_info.clicked.connect(self.load)
        self.clc_data.clicked.connect(self.calender)
        self.btn_del.clicked.connect(self.delclc)

    def spent(self):
        self.form_spent.show()

    def recived(self):
        self.form_received.show()

    def add_f(self):
        self.add.show()
    def youer(self):
        self.yourself.show()

    def delclc(self):
        data = self.clc_data.selectedDate().toString('yyyy-MM-dd')
        info = self.cur.execute("""SELECT * FROM info WHERE DATA = ?""", (data,)).fetchall()
        if not info:
            self.lbl_error.setText("Такой даты у нас нет")
            return 0
        self.cur.execute("""DELETE from info
                WHERE DATA = ?""", (data,))
        self.database.commit()

    def load(self):
        info = self.cur.execute("""SELECT * FROM info""").fetchall()
        if not info:
            self.lbl_error.setText("У нас нет информации о Ваших усилиях:(")
            return 0
        self.tb_info.setRowCount(len(info))
        for i, elem in enumerate(info):
            for j, val in enumerate(elem):
                self.tb_info.setItem(i, j, QTableWidgetItem(str(val)))
        self.tb_info.setColumnWidth(1, 100)

    def calender(self):
        data = self.clc_data.selectedDate().toString('yyyy-MM-dd')
        info = self.cur.execute("""SELECT * FROM info WHERE DATA = ?""", (data,)).fetchall()
        if not info:
            self.lbl_error.setText("У нас нет информации о Ваших усилиях:(")
            return 0
        self.tb_info.setRowCount(len(info))
        for i, elem in enumerate(info):
            for j, val in enumerate(elem):
                self.tb_info.setItem(i, j, QTableWidgetItem(str(val)))
        self.tb_info.setColumnWidth(1, 100)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())