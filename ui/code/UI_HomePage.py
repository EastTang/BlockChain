# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_HomePage(object):
    def setupUi(self, Form_HomePage):
        Form_HomePage.setObjectName("Form_HomePage")
        Form_HomePage.resize(1468, 690)
        Form_HomePage.setMinimumSize(QtCore.QSize(1468, 690))
        Form_HomePage.setMaximumSize(QtCore.QSize(1468, 690))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_HomePage.setWindowIcon(icon)
        Form_HomePage.setStyleSheet("#Form_HomePage {\n"
"    border-image: url(:/images/background.png);\n"
"}\n"
"QGroupBox > QLabel {\n"
"    font: 10pt \"幼圆\";\n"
"    color: rgb(98, 143, 186);\n"
"}\n"
"QGroupBox > QPushButton {\n"
"    border-image: url(:/images/background_btn_right.png);\n"
"    margin: -10px;\n"
"    border-radius: 5px;\n"
"    font: 14pt \"微软雅黑\";\n"
"    color: rgb(123, 172, 230);\n"
"}\n"
"QGroupBox > QPushButton:hover {\n"
"    border-image: url(:/images/background_btn_right_hover.png);\n"
"    margin: -10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QGroupBox > QPushButton:pressed {\n"
"    border-image: url(:/images/background_btn_right_pressed.png);\n"
"    margin: -10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QGroupBox {\n"
"    border: 2px solid rgba(166, 244, 244, 20%);\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; \n"
"    font: 50 10pt \"等线\";    \n"
"    color: rgb(25, 108, 187);\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    padding: 0 3px;\n"
"}\n"
"\n"
"\n"
"#textBrowser_output {\n"
"    border-image: url(:/images/background_textedit.png);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"#textEdit_chat {\n"
"    border-image: url(:/images/background_chat.png);\n"
"    border-radius: 10px;\n"
"    padding: 18px;\n"
"    margin: -8px;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    width:24px;\n"
"    background:rgba(253, 252, 100,5%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:24px;\n"
"    padding-bottom:24px;\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:24px;\n"
"    background:rgba(255, 255, 255, 50%);\n"
"    border-radius:8px;\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:24px;\n"
"    background:rgba(255,255,255,90%);\n"
"    border-radius:10px;\n"
"    min-height:20;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height:24px;width:24px;\n"
"    border-image: url(:/images/scroll_down.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::add-line:vertical:hover\n"
"{\n"
"    height:24px;width:24px;\n"
"    border-image: url(:/images/scroll_down_hover.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed\n"
"{\n"
"    height:24px;width:24px;\n"
"    border-image: url(:/images/scroll_down_pressed.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    height:24px;width:24px;\n"
"    border-image: url(:/images/scroll_top.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover\n"
"{\n"
"    height:24px;width:24px;\n"
"    border-image: url(:/images/scroll_top_hover.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed\n"
"{\n"
"    height:24px;width:24px;\n"
"    border-image: url(:/images/scroll_top_pressed.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
"{\n"
"    background:rgba(253, 252, 100,5%);\n"
"    border-radius:4px;\n"
"}")
        self.groupBox_btn_single = QtWidgets.QGroupBox(Form_HomePage)
        self.groupBox_btn_single.setGeometry(QtCore.QRect(50, 300, 221, 331))
        self.groupBox_btn_single.setObjectName("groupBox_btn_single")
        self.pushButton_chain = QtWidgets.QPushButton(self.groupBox_btn_single)
        self.pushButton_chain.setGeometry(QtCore.QRect(40, 50, 131, 51))
        self.pushButton_chain.setObjectName("pushButton_chain")
        self.pushButton_balance = QtWidgets.QPushButton(self.groupBox_btn_single)
        self.pushButton_balance.setGeometry(QtCore.QRect(40, 120, 131, 51))
        self.pushButton_balance.setObjectName("pushButton_balance")
        self.pushButton_transaction = QtWidgets.QPushButton(self.groupBox_btn_single)
        self.pushButton_transaction.setGeometry(QtCore.QRect(40, 190, 131, 51))
        self.pushButton_transaction.setObjectName("pushButton_transaction")
        self.pushButton_mine = QtWidgets.QPushButton(self.groupBox_btn_single)
        self.pushButton_mine.setGeometry(QtCore.QRect(40, 260, 131, 51))
        self.pushButton_mine.setObjectName("pushButton_mine")
        self.groupBox = QtWidgets.QGroupBox(Form_HomePage)
        self.groupBox.setGeometry(QtCore.QRect(50, 50, 491, 211))
        self.groupBox.setObjectName("groupBox")
        self.label_id_left = QtWidgets.QLabel(self.groupBox)
        self.label_id_left.setGeometry(QtCore.QRect(20, 40, 71, 31))
        self.label_id_left.setObjectName("label_id_left")
        self.label_name_right = QtWidgets.QLabel(self.groupBox)
        self.label_name_right.setGeometry(QtCore.QRect(100, 40, 341, 31))
        self.label_name_right.setText("")
        self.label_name_right.setObjectName("label_name_right")
        self.label_time_right = QtWidgets.QLabel(self.groupBox)
        self.label_time_right.setGeometry(QtCore.QRect(100, 80, 341, 31))
        self.label_time_right.setText("")
        self.label_time_right.setObjectName("label_time_right")
        self.label_time_left = QtWidgets.QLabel(self.groupBox)
        self.label_time_left.setGeometry(QtCore.QRect(20, 80, 71, 31))
        self.label_time_left.setObjectName("label_time_left")
        self.label_balance_left = QtWidgets.QLabel(self.groupBox)
        self.label_balance_left.setGeometry(QtCore.QRect(20, 120, 71, 31))
        self.label_balance_left.setObjectName("label_balance_left")
        self.label_balance_right = QtWidgets.QLabel(self.groupBox)
        self.label_balance_right.setGeometry(QtCore.QRect(100, 120, 341, 31))
        self.label_balance_right.setText("")
        self.label_balance_right.setObjectName("label_balance_right")
        self.groupBox_btn_mutil = QtWidgets.QGroupBox(Form_HomePage)
        self.groupBox_btn_mutil.setGeometry(QtCore.QRect(320, 300, 221, 331))
        self.groupBox_btn_mutil.setObjectName("groupBox_btn_mutil")
        self.pushButton_node_broadcast = QtWidgets.QPushButton(self.groupBox_btn_mutil)
        self.pushButton_node_broadcast.setGeometry(QtCore.QRect(50, 50, 131, 51))
        self.pushButton_node_broadcast.setObjectName("pushButton_node_broadcast")
        self.pushButton_chain_replace = QtWidgets.QPushButton(self.groupBox_btn_mutil)
        self.pushButton_chain_replace.setGeometry(QtCore.QRect(50, 190, 131, 51))
        self.pushButton_chain_replace.setObjectName("pushButton_chain_replace")
        self.pushButton_node_list = QtWidgets.QPushButton(self.groupBox_btn_mutil)
        self.pushButton_node_list.setGeometry(QtCore.QRect(50, 120, 131, 51))
        self.pushButton_node_list.setObjectName("pushButton_node_list")
        self.textBrowser_output = QtWidgets.QTextBrowser(Form_HomePage)
        self.textBrowser_output.setGeometry(QtCore.QRect(570, 60, 841, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_output.setFont(font)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.textEdit_chat = QtWidgets.QTextEdit(Form_HomePage)
        self.textEdit_chat.setGeometry(QtCore.QRect(560, 540, 701, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.textEdit_chat.setFont(font)
        self.textEdit_chat.setObjectName("textEdit_chat")
        self.pushButton_chat = QtWidgets.QPushButton(Form_HomePage)
        self.pushButton_chat.setGeometry(QtCore.QRect(1270, 550, 121, 81))
        self.pushButton_chat.setStyleSheet("#pushButton_chat {\n"
"    border-image: url(:/images/btn_chat.png);\n"
"    margin: -30px;\n"
"}\n"
"#pushButton_chat:hover {\n"
"    border-image: url(:/images/btn_chat_hover.png);\n"
"    margin: -30px;\n"
"}\n"
"#pushButton_chat:pressed {\n"
"    border-image: url(:/images/btn_chat.png);\n"
"    margin: -30px;\n"
"}")
        self.pushButton_chat.setText("")
        self.pushButton_chat.setObjectName("pushButton_chat")

        self.retranslateUi(Form_HomePage)
        QtCore.QMetaObject.connectSlotsByName(Form_HomePage)

    def retranslateUi(self, Form_HomePage):
        _translate = QtCore.QCoreApplication.translate
        Form_HomePage.setWindowTitle(_translate("Form_HomePage", "Form"))
        self.groupBox_btn_single.setTitle(_translate("Form_HomePage", "单节点"))
        self.pushButton_chain.setText(_translate("Form_HomePage", "链"))
        self.pushButton_balance.setText(_translate("Form_HomePage", "余额"))
        self.pushButton_transaction.setText(_translate("Form_HomePage", "交易"))
        self.pushButton_mine.setText(_translate("Form_HomePage", "挖矿"))
        self.groupBox.setTitle(_translate("Form_HomePage", "用户信息"))
        self.label_id_left.setText(_translate("Form_HomePage", "用户ID"))
        self.label_time_left.setText(_translate("Form_HomePage", "注册时间"))
        self.label_balance_left.setText(_translate("Form_HomePage", "余额"))
        self.groupBox_btn_mutil.setTitle(_translate("Form_HomePage", "多节点"))
        self.pushButton_node_broadcast.setText(_translate("Form_HomePage", "广播节点"))
        self.pushButton_chain_replace.setText(_translate("Form_HomePage", "同步最长链"))
        self.pushButton_node_list.setText(_translate("Form_HomePage", "节点列表"))
import resource_rc
