import sqlite3


from PyQt5.QtWidgets import QMainWindow, QInputDialog
from yourself import Ui_frm_yourself

YEAR = 0
WEIGHT = 0
HEIGHT = 0
GENDER = ''
A = 0
JOB = ''
BMR = 0


class Yourself(QMainWindow, Ui_frm_yourself):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = sqlite3.connect('info.db')
        self.cur = self.database.cursor()
        check = self.cur.execute("""SELECT * FROM yourself WHERE Name = 'YEAR'""").fetchone()
        if not check[1]:
            self.btn_input.setEnabled(True)
        else:
            YEAR = int(self.cur.execute("""SELECT * FROM yourself WHERE Name = ?""", ("YEAR",)).fetchone()[1])
            WEIGHT = int(self.cur.execute("""SELECT * FROM yourself WHERE Name = ?""", ("WEIGHT",)).fetchone()[1])
            HEIGHT = int(self.cur.execute("""SELECT * FROM yourself WHERE Name =? """, ("HEIGHT",)).fetchone()[1])
            GENDER = self.cur.execute("""SELECT * FROM yourself WHERE Name = ?""", ("GENDER",)).fetchone()[1]
            JOB = self.cur.execute("""SELECT * FROM yourself WHERE Name = ?""", ("JOB",)).fetchone()[1]
            A = self.cur.execute("""SELECT * FROM yourself WHERE Name = ?""", ("A",)).fetchone()[1]
            BMR = int(self.cur.execute("""SELECT * FROM yourself WHERE Name = ?""", ("BMR",)).fetchone()[1])
            self.lbl_bmr.setText(f'{BMR} каллорий')
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
                self.database.commit()
            self.btn_input.setEnabled(False)
        self.btn_input.clicked.connect(self.info)

    def info(self):
        YEAR, ok = QInputDialog.getInt(self, 'Возраст', "Сколько тебе лет?", 30, 1, 200, 1)
        WEIGHT, ok = QInputDialog.getInt(self, "Вес", "Сколько Вы весите(кг)", 60, 10, 10000, 1)
        HEIGHT, ok = QInputDialog.getInt(self, "Рост", "Чему равен Ваш рост(см)", 170, 50, 300, 1)
        GENDER, ok = QInputDialog.getItem(self, 'ПОЛ', 'Выберете свой пол', ('м', 'ж'))
        JOB, ok = QInputDialog.getItem(self, "Вид деятельности", "Чем Вы занимаетесь?",
                                     ('сидячая работа, отсутствие спорта',
                                      'легкие физические упражнения около 3 раз за неделю',
                                      'спорт до 5 раз за неделю',
                                      'активный образ жизни вкупе с ежедневными интенсивными тренировками',
                                      'максимальная активность - спортивный образ жизни'))
        if JOB == 'сидячая работа, отсутствие спорта':
            A = 1.2
        if JOB == 'легкие физические упражнения около 3 раз за неделю':
            A = 1.35
        if JOB == 'спорт до 5 раз за неделю':
            A = 1.55
        if JOB == 'активный образ жизни вкупе с ежедневными интенсивными тренировками':
            A = 1.75
        if JOB == 'максимальная активность - спортивный образ жизни':
            A = 1.95
        if GENDER == 'м':
            BMR = (10 * WEIGHT + 6.25 * HEIGHT - 5 * YEAR + 5) * A
        if GENDER == 'ж':
            BMR = (10 * WEIGHT + 6.25 * HEIGHT - 5 * YEAR - 161) * A
        self.lbl_bmr.setText(f'{BMR} каллорий')
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
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'YEAR'""", (YEAR,))
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'WEIGHT'""", (WEIGHT,))
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'HEIGHT' """, (HEIGHT,))
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'GENDER'""", (GENDER,))
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'A'""", (A,))
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'JOB'""", (JOB,))
        self.cur.execute("""UPDATE yourself
        SET Ser = ?
        WHERE Name = 'BMR'""", (BMR,))
        self.database.commit()