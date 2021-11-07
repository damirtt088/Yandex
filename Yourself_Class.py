from PyQt5.QtWidgets import QMainWindow, QInputDialog
from yourself import Ui_frm_yourself

YEAR = 0
WEIGHT = 0
HEIGHT = 0


class Yourself(QMainWindow, Ui_frm_yourself):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_input.clicked.connect(self.info)

    def info(self):
        YEAR, ok = QInputDialog.getInt(self, 'Возраст', "Сколько тебе лет?", 30, 1, 200, 1)
        WEIGHT, ok = QInputDialog.getInt(self, "Вес", "Сколько Вы весите(кг)", 60, 10, 10000, 1)
        HEIGHT, ok = QInputDialog.getInt(self, "Рост", "Чему равен Ваш рост(см)", 170, 50, 300, 1)
        self.index = round(WEIGHT / (HEIGHT / 100) ** 2)
        self.lbl_imt_go.setText(str(self.index))
        if self.index <= 18:
            self.lbl_norma.setText('У Вас дефицит веса')
        elif 18 < self.index <= 25:
            self.lbl_norma.setText("Норма")
        elif 25 > int(self.index) <= 30:
            self.lbl_norma.setText("У Вас избыток веса")
        elif self.index > 30:
            self.lbl_norma.setText("У Вас ожирение")