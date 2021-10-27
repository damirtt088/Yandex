import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from main import


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())