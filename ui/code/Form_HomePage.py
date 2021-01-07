import os
import sys
import time
from uuid import uuid4
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QPalette, QTextCursor, QCursor, QSyntaxHighlighter, QTextCharFormat, QFont, QColor, \
    QFontMetrics, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from ui.code.UI_HomePage import Ui_Form_HomePage

INIT_BALANCE = 100


class Form_HomePage(QWidget, Ui_Form_HomePage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 获取用户ID 和 注册时间
        self.user_id = str(uuid4())
        self.registration_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # 新用户红利 初始余额
        self.balance = INIT_BALANCE
        # 根据信息 重设界面
        self.reset_page()
        # 控件列表
        self.buttons = [self.pushButton_chain, self.pushButton_balance,
                        self.pushButton_transaction, self.pushButton_mine]
        # 初始化信号与槽连接
        self.handle_init()

    def reset_page(self):
        self.label_name_right.setText(self.user_id)
        self.label_time_right.setText(self.registration_time)
        self.label_balance_right.setText(str(self.balance))

    def handle_init(self):
        for i in self.buttons:
            i.clicked.connect(lambda: print(self.sender().objectName().split('_')[-1], 'Clicked !'))

    def append_output(self, info):
        print('New Message:\t', info)
        self.textBrowser_output.append(info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form_HomePage()
    window.show()
    sys.exit(app.exec_())
