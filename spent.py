# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_spent(object):
    def setupUi(self, frm_spent):
        frm_spent.setObjectName("frm_spent")
        frm_spent.resize(680, 505)
        self.txt_gum = QtWidgets.QTextEdit(frm_spent)
        self.txt_gum.setGeometry(QtCore.QRect(90, 0, 421, 31))
        self.txt_gum.setObjectName("txt_gum")
        self.lbl_exe = QtWidgets.QLabel(frm_spent)
        self.lbl_exe.setGeometry(QtCore.QRect(0, 10, 121, 21))
        self.lbl_exe.setObjectName("lbl_exe")
        self.lbl_time = QtWidgets.QLabel(frm_spent)
        self.lbl_time.setGeometry(QtCore.QRect(0, 50, 141, 21))
        self.lbl_time.setObjectName("lbl_time")
        self.txt_time = QtWidgets.QTextEdit(frm_spent)
        self.txt_time.setGeometry(QtCore.QRect(150, 40, 421, 31))
        self.txt_time.setObjectName("txt_time")
        self.btn_spt = QtWidgets.QPushButton(frm_spent)
        self.btn_spt.setGeometry(QtCore.QRect(170, 110, 161, 41))
        self.btn_spt.setObjectName("btn_spt")
        self.verticalLayoutWidget = QtWidgets.QWidget(frm_spent)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 161, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbtn_sport = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_sport.setObjectName("rbtn_sport")
        self.btn_info = QtWidgets.QButtonGroup(frm_spent)
        self.btn_info.setObjectName("btn_info")
        self.btn_info.addButton(self.rbtn_sport)
        self.verticalLayout.addWidget(self.rbtn_sport)
        self.rbtn_usualy = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_usualy.setObjectName("rbtn_usualy")
        self.btn_info.addButton(self.rbtn_usualy)
        self.verticalLayout.addWidget(self.rbtn_usualy)
        self.tbl_spent = QtWidgets.QTableWidget(frm_spent)
        self.tbl_spent.setGeometry(QtCore.QRect(0, 281, 256, 221))
        self.tbl_spent.setRowCount(1)
        self.tbl_spent.setColumnCount(2)
        self.tbl_spent.setObjectName("tbl_spent")
        self.lbl_sp = QtWidgets.QLabel(frm_spent)
        self.lbl_sp.setGeometry(QtCore.QRect(0, 190, 141, 31))
        self.lbl_sp.setObjectName("lbl_sp")
        self.lcd_spent = QtWidgets.QLCDNumber(frm_spent)
        self.lcd_spent.setGeometry(QtCore.QRect(150, 190, 271, 41))
        self.lcd_spent.setObjectName("lcd_spent")
        self.label = QtWidgets.QLabel(frm_spent)
        self.label.setGeometry(QtCore.QRect(170, 80, 111, 31))
        self.label.setObjectName("label")
        self.lbl_error = QtWidgets.QLabel(frm_spent)
        self.lbl_error.setGeometry(QtCore.QRect(360, 80, 241, 51))
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")

        self.retranslateUi(frm_spent)
        QtCore.QMetaObject.connectSlotsByName(frm_spent)

    def retranslateUi(self, frm_spent):
        _translate = QtCore.QCoreApplication.translate
        frm_spent.setWindowTitle(_translate("frm_spent", "Form"))
        self.lbl_exe.setText(_translate("frm_spent", "Вид упражнения:"))
        self.lbl_time.setText(_translate("frm_spent", "Потраченное время (часов)"))
        self.btn_spt.setText(_translate("frm_spent", "Рассчитать"))
        self.rbtn_sport.setText(_translate("frm_spent", "Спортивные упражнения"))
        self.rbtn_usualy.setText(_translate("frm_spent", "Повседневыне задачи"))
        self.lbl_sp.setText(_translate("frm_spent", "Потраченные каллории:"))
        self.label.setText(_translate("frm_spent", "По умолчанию 1 час"))
