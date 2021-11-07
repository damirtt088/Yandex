import sys


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
        self.loadTable()
        self.btn_spent.clicked.connect(self.spent)
        self.form_spent = Spent()
        self.form_received = Recieved()
        self.add = Addf()
        self.yourself = Yourself()
        self.btn_received.clicked.connect(self.recived)
        self.btn_add.clicked.connect(self.add_f)
        self.btn_youself.clicked.connect(self.youer)

    def spent(self):
        self.form_spent.show()

    def recived(self):
        self.form_received.show()

    def add_f(self):
        self.add.show()
    def youer(self):
        self.yourself.show()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())