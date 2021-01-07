# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_TransactionPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_TransactionPage(object):
    def setupUi(self, Form_TransactionPage):
        Form_TransactionPage.setObjectName("Form_TransactionPage")
        Form_TransactionPage.resize(756, 426)
        Form_TransactionPage.setMinimumSize(QtCore.QSize(756, 426))
        Form_TransactionPage.setMaximumSize(QtCore.QSize(756, 426))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_TransactionPage.setWindowIcon(icon)
        Form_TransactionPage.setStyleSheet("#Form_TransactionPage {\n"
"    border-image: url(:/images/background_transaction.png);\n"
"}\n"
"#label_title {\n"
"    font: 50 20pt \"等线\";    \n"
"    color: rgba(25, 108, 187, 50%);\n"
"}\n"
".QLabel {\n"
"    font: 14pt \"幼圆\";\n"
"    color: rgb(98, 143, 186);\n"
"}\n"
".QLineEdit{\n"
"    border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255, 70%);\n"
"}\n"
"#pushButton_submit {\n"
"    border-image: url(:/images/background_btn_right.png);\n"
"    margin: -10px;\n"
"    border-radius: 5px;\n"
"    font: 14pt \"微软雅黑\";\n"
"    color: rgb(123, 172, 230);\n"
"}\n"
"#pushButton_submit:hover {\n"
"    border-image: url(:/images/background_btn_right_hover.png);\n"
"    margin: -10px;\n"
"    border-radius: 5px;\n"
"}\n"
"#pushButton_submit:pressed {\n"
"    border-image: url(:/images/background_btn_right_pressed.png);\n"
"    margin: -10px;\n"
"    border-radius: 5px;\n"
"}")
        self.label_sender = QtWidgets.QLabel(Form_TransactionPage)
        self.label_sender.setGeometry(QtCore.QRect(30, 130, 121, 41))
        self.label_sender.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sender.setObjectName("label_sender")
        self.label_receiver = QtWidgets.QLabel(Form_TransactionPage)
        self.label_receiver.setGeometry(QtCore.QRect(30, 200, 121, 41))
        self.label_receiver.setAlignment(QtCore.Qt.AlignCenter)
        self.label_receiver.setObjectName("label_receiver")
        self.label_number = QtWidgets.QLabel(Form_TransactionPage)
        self.label_number.setGeometry(QtCore.QRect(30, 270, 121, 41))
        self.label_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number.setObjectName("label_number")
        self.pushButton_submit = QtWidgets.QPushButton(Form_TransactionPage)
        self.pushButton_submit.setGeometry(QtCore.QRect(560, 350, 131, 51))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.label_title = QtWidgets.QLabel(Form_TransactionPage)
        self.label_title.setGeometry(QtCore.QRect(260, 40, 211, 41))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.lineEdit_sender = QtWidgets.QLineEdit(Form_TransactionPage)
        self.lineEdit_sender.setGeometry(QtCore.QRect(190, 130, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_sender.setFont(font)
        self.lineEdit_sender.setObjectName("lineEdit_sender")
        self.lineEdit_receiver = QtWidgets.QLineEdit(Form_TransactionPage)
        self.lineEdit_receiver.setGeometry(QtCore.QRect(190, 200, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_receiver.setFont(font)
        self.lineEdit_receiver.setObjectName("lineEdit_receiver")
        self.lineEdit_number = QtWidgets.QLineEdit(Form_TransactionPage)
        self.lineEdit_number.setGeometry(QtCore.QRect(190, 270, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.lineEdit_sender.raise_()
        self.label_sender.raise_()
        self.label_receiver.raise_()
        self.label_number.raise_()
        self.pushButton_submit.raise_()
        self.label_title.raise_()
        self.lineEdit_receiver.raise_()
        self.lineEdit_number.raise_()

        self.retranslateUi(Form_TransactionPage)
        QtCore.QMetaObject.connectSlotsByName(Form_TransactionPage)

    def retranslateUi(self, Form_TransactionPage):
        _translate = QtCore.QCoreApplication.translate
        Form_TransactionPage.setWindowTitle(_translate("Form_TransactionPage", "Form"))
        self.label_sender.setText(_translate("Form_TransactionPage", "发送方"))
        self.label_receiver.setText(_translate("Form_TransactionPage", "接收方"))
        self.label_number.setText(_translate("Form_TransactionPage", "交易额"))
        self.pushButton_submit.setText(_translate("Form_TransactionPage", "提交"))
        self.label_title.setText(_translate("Form_TransactionPage", "新建交易"))
import resource_rc
