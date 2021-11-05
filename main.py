import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from mainform import Ui_MainWindow
from spent import Ui_frm_spent
from recived import Ui_frm_recieved


class Recieved(QMainWindow, Ui_frm_recieved):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_calc.clicked.connect(self.recived)

    def recived(self):
        eat = self.txt_eat.toPlainText()
        gramm = self.txt_gramm.toPlainText()
        if not gramm:
            gramm = 100
        if type(gramm) is not int:

        gramm = int(gramm)
        self.lcd_gramm.display(100)
        self.lcd_recived.display(100)


class Spent(QMainWindow, Ui_frm_spent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_spt.clicked.connect(self.spent)

    def spent(self):
        execi = self.txt_gum.toPlainText()
        time = self.txt_time.toPlainText()
        self.txt_gum.setText('')
        self.txt_time.setText('')
        if not execi or not time:
            self.lbl_spt.setText('Чего-то не хватает')
            self.lbl_spt.resize(self.lbl_spt.sizeHint())
            return 0
        self.lbl_spt.setText('0')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_spent.clicked.connect(self.spent)
        self.form_spent = Spent()
        self.form_received = Recieved()
        self.btn_received.clicked.connect(self.recived)

    def spent(self):
        self.form_spent.show()

    def recived(self):
        self.form_received.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())