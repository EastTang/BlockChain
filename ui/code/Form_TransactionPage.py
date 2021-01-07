import os
import sys
import time
from uuid import uuid4
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QPalette, QTextCursor, QCursor, QSyntaxHighlighter, QTextCharFormat, QFont, QColor, \
    QFontMetrics, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from ui.code.UI_TransactionPage import Ui_Form_TransactionPage


class Form_TransactionPage(QWidget, Ui_Form_TransactionPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 控件列表
        self.lineEdits = [self.lineEdit_sender, self.lineEdit_receiver, self.lineEdit_number]
        # 链接提交按钮
        self.pushButton_submit.clicked.connect(lambda: print('submit Clicked'))
        # 调色板画背景
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(":images/background_transaction.png").scaled(self.size())))
        self.setPalette(palette)

    def clear(self):
        for i in self.lineEdits:
            i.setText('')

    def closeEvent(self, QCloseEvent):
        self.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form_TransactionPage()
    window.show()
    sys.exit(app.exec_())
