# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yourself.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_yourself(object):
    def setupUi(self, frm_yourself):
        frm_yourself.setObjectName("frm_yourself")
        frm_yourself.resize(656, 480)
        self.lbl_info = QtWidgets.QLabel(frm_yourself)
        self.lbl_info.setGeometry(QtCore.QRect(0, 10, 351, 41))
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_imt_info = QtWidgets.QLabel(frm_yourself)
        self.lbl_imt_info.setGeometry(QtCore.QRect(10, 170, 161, 41))
        self.lbl_imt_info.setObjectName("lbl_imt_info")
        self.lbl_imt_go = QtWidgets.QLabel(frm_yourself)
        self.lbl_imt_go.setGeometry(QtCore.QRect(180, 170, 81, 41))
        self.lbl_imt_go.setText("")
        self.lbl_imt_go.setObjectName("lbl_imt_go")
        self.label = QtWidgets.QLabel(frm_yourself)
        self.label.setGeometry(QtCore.QRect(10, 210, 141, 31))
        self.label.setObjectName("label")
        self.lbl_slle_info = QtWidgets.QLabel(frm_yourself)
        self.lbl_slle_info.setGeometry(QtCore.QRect(10, 250, 141, 51))
        self.lbl_slle_info.setText("")
        self.lbl_slle_info.setObjectName("lbl_slle_info")
        self.lbl_information = QtWidgets.QLabel(frm_yourself)
        self.lbl_information.setGeometry(QtCore.QRect(0, 40, 231, 41))
        self.lbl_information.setObjectName("lbl_information")
        self.btn_input = QtWidgets.QPushButton(frm_yourself)
        self.btn_input.setGeometry(QtCore.QRect(0, 80, 101, 31))
        self.btn_input.setObjectName("btn_input")
        self.lbl_norma = QtWidgets.QLabel(frm_yourself)
        self.lbl_norma.setGeometry(QtCore.QRect(280, 160, 291, 61))
        self.lbl_norma.setText("")
        self.lbl_norma.setObjectName("lbl_norma")
        self.lbl_bmr_info = QtWidgets.QLabel(frm_yourself)
        self.lbl_bmr_info.setGeometry(QtCore.QRect(10, 250, 201, 51))
        self.lbl_bmr_info.setObjectName("lbl_bmr_info")
        self.lbl_bmr = QtWidgets.QLabel(frm_yourself)
        self.lbl_bmr.setGeometry(QtCore.QRect(220, 260, 121, 31))
        self.lbl_bmr.setText("")
        self.lbl_bmr.setObjectName("lbl_bmr")

        self.retranslateUi(frm_yourself)
        QtCore.QMetaObject.connectSlotsByName(frm_yourself)

    def retranslateUi(self, frm_yourself):
        _translate = QtCore.QCoreApplication.translate
        frm_yourself.setWindowTitle(_translate("frm_yourself", "?? ????????"))
        self.lbl_info.setText(_translate("frm_yourself", "?????????? ???? ???????????? ?????????????????? ???????????????????? ?? ????????"))
        self.lbl_imt_info.setText(_translate("frm_yourself", "?????? ???????????? ?????????? ???????? ??????????"))
        self.label.setText(_translate("frm_yourself", "?????? ?????????? ???? 18,5 ???? 25"))
        self.lbl_information.setText(_translate("frm_yourself", "?????????????? ???????????? ?? ?????????????? ????????????????????"))
        self.btn_input.setText(_translate("frm_yourself", "????????????"))
        self.lbl_bmr_info.setText(_translate("frm_yourself", "???????? ???????????????? ?????????? ???????????????? ??????????"))
