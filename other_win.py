import sys
import time
from uuid import uuid4
import re
import json
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.Qt import QPixmap
from PyQt5.QtWidgets import QApplication, QStackedLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QIcon
from ui.code.UI_HomePage import Ui_Form_HomePage
from ui.code.Form_TransactionPage import Form_TransactionPage
from utils.communicate_tool import *
from utils.ServerThread import *
from chain import Blockchain

INIT_BALANCE = 0
SYSTEM_REWARD = 10.0
IP_PORT = ('192.168.80.201', 9527)


# def get_config_from_json(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         config = json.load(f)
#         f.close()
#     return config
#
#
# config = get_config_from_json('./config.json')
# IP_PORT = (config['ip'], config['port'])


class MainWindow(QWidget, Ui_Form_HomePage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 获取用户ID 和 注册时间
        self.user_id = str(uuid4())
        self.registration_time = self.get_format_time()
        # 新用户红利 初始余额
        self.balance_min = INIT_BALANCE
        self.balance_max = INIT_BALANCE
        # 设置当前应用主链
        self.block_chain = Blockchain()
        # 设置交易子窗口
        self.subpage_transaction = Form_TransactionPage()
        self.subpage_transaction.hide()
        # 根据信息 重设界面
        self.reset_page()
        # 控件列表
        self.buttons = [self.pushButton_chain, self.pushButton_balance,
                        self.pushButton_transaction, self.pushButton_mine]
        # 初始化信号与槽连接
        self.handle_init()
        # 多节点要素补充
        self.users = set()
        self.users.add('0')
        self.users.add('Test')
        self.ip_port = IP_PORT
        # 创建附属监听线程
        self.is_running = True
        self.listen_thread = ServerThread(owner=self, ip_port=('', self.ip_port[1]))
        self.listen_thread.start()

    @staticmethod
    def get_format_time(pattern="%Y-%m-%d %H:%M:%S") -> str:
        return str(time.strftime(pattern, time.localtime()))

    def get_format_info(self, title='', info=None):
        if info is None:
            info = {}
        return '{title:#^66}\n{info}\n{time:#^66}'.format(
            title=title,
            info=json.dumps(info, indent=2, ensure_ascii=False),
            time=self.get_format_time()
        )

    def reset_page(self):
        # 设置标题
        self.setWindowTitle('基于分布式账本的交易网络_Demo')
        self.subpage_transaction.setWindowTitle('交易窗口_Demo')
        # 设置主页用户信息
        self.label_name_right.setText(self.user_id)
        self.label_time_right.setText(self.registration_time)
        self.label_balance_right.setText('{}(未入账)\t{}(已入账)'.format(self.balance_min, self.balance_max))

    def closeEvent(self, QCloseEvent):
        self.is_running = False
        self.subpage_transaction.close()
        MySocket.send_data(msg_type='Quit', msg_data='Quit', target_ip_port=self.ip_port,
                           from_user='Quit')

    def append_output(self, info):
        print('New Message:\t', info)
        self.textBrowser_output.append(info + '\n')

    def handle_init(self):
        self.pushButton_chain.clicked.connect(self.show_chain)
        self.pushButton_balance.clicked.connect(self.show_balance)
        self.pushButton_transaction.clicked.connect(self.open_subpage_transaction)
        self.pushButton_mine.clicked.connect(self.mine)
        self.subpage_transaction.pushButton_submit.clicked.connect(self.add_transaction)
        # 多节点按钮
        self.pushButton_node_broadcast.clicked.connect(self.broadcast_this_node)
        self.pushButton_node_list.clicked.connect(self.show_nodes)
        self.pushButton_chain_replace.clicked.connect(self.update_chain)
        # 聊天室按钮
        self.pushButton_chat.clicked.connect(self.send_chatting_message)

    def show_error_msg(self, title, msg):
        QMessageBox.warning(self, title, msg, QMessageBox.Ok)

    def show_chain(self):
        info = {
            '链': self.block_chain.chain,
            '长度': len(self.block_chain.chain)
        }
        self.append_output(info=self.get_format_info(' Show Full Chain ', info))

    def show_nodes(self):
        info = {
            '节点': list(self.block_chain.nodes),
            '节点总数': len(self.block_chain.nodes),
            '用户': list(self.users),
            '已注册用户数': len(self.users)
        }
        self.append_output(info=self.get_format_info(' Show Node List ', info))

    def get_balance_min_and_max(self):
        max_balance_dict = self.block_chain.get_max_balance()
        min_balance_dict = max_balance_dict.copy()
        for i in self.block_chain.currentTransaction:
            sender = i['sender']
            recipient = i['recipient']
            amount = i['amount']
            balance_old = float(min_balance_dict[sender]) if sender in min_balance_dict.keys() else 0.0
            min_balance_dict[sender] = balance_old - float(amount)
            balance_old = float(min_balance_dict[recipient]) if recipient in min_balance_dict.keys() else 0.0
            min_balance_dict[recipient] = balance_old + float(amount)
        return min_balance_dict, max_balance_dict

    def update_balance_min_and_max(self, min_balance_dict, max_balance_dict):
        self.balance_max = max_balance_dict[self.user_id] if self.user_id in max_balance_dict.keys() else 0.0
        self.balance_min = min_balance_dict[self.user_id] if self.user_id in min_balance_dict.keys() else 0.0
        self.label_balance_right.setText('{}(未入账)\t{}(已入账)'.format(self.balance_min, self.balance_max))

    def show_balance(self):
        min_dict, max_dict = self.get_balance_min_and_max()
        self.update_balance_min_and_max(min_dict, max_dict)
        self.append_output(info=self.get_format_info(' Show Balance True', max_dict))
        self.append_output(info=self.get_format_info(' Show Balance Current', min_dict))

    def open_subpage_transaction(self):
        self.subpage_transaction.show()
        self.subpage_transaction.lineEdit_sender.setText(self.user_id)
        self.subpage_transaction.lineEdit_sender.setEnabled(False)

    def add_transaction(self):
        p = self.subpage_transaction
        if self.is_input_legal():
            idx = self.block_chain.new_transaction(
                sender=p.lineEdit_sender.text(),
                recipient=p.lineEdit_receiver.text(),
                amount=p.lineEdit_number.text()
            )
            _i, _j = self.get_balance_min_and_max()
            self.update_balance_min_and_max(_i, _j)
            info = '{time}\t该交易信息将会被添加到 区块{idx} 在下一次挖矿后...'.format(time=self.get_format_time(), idx=idx)
            self.append_output(info=info)
            self.broadcast_last_transaction()
            p.clear()
            p.hide()
        else:
            # 隐显确保窗口置前端
            p.hide()
            p.show()

    def is_input_legal(self):
        p = self.subpage_transaction
        ans = True
        info = None
        if p.lineEdit_receiver.text() not in self.users:
            info = '接收方ID有误，用户记录查无此人'
            ans = False
        elif re.match(r'^\d+\.?\d*$', p.lineEdit_number.text()) is None:
            info = '交易数额有误，请填入正确数字'
            ans = False
        elif float(p.lineEdit_number.text()) > self.balance_min:
            info = '余额不足，请检查交易额或更新余额'
            ans = False
        if info is not None:
            self.show_error_msg(title='Error', msg=info)
            self.append_output(info='{}\t{}'.format(self.get_format_time(), info))
        return ans

    def mine(self):
        last_block = self.block_chain.last_block
        last_proof = last_block['proof']
        t = time.time()
        proof = self.block_chain.proof_of_work(last_proof)
        t = time.time() - t
        info = {
            '信息': '挖矿取得新区块Proof',
            '耗时': '{:.8f} s'.format(t),
            '工作量证明': proof
        }
        self.append_output(info=self.get_format_info(' Get New Proof ', info))

        self.block_chain.new_transaction(
            sender='0',
            recipient=self.user_id,
            amount=str(SYSTEM_REWARD)
        )

        previous_hash = self.block_chain.hash(last_block)
        block = self.block_chain.new_block(proof=proof, previous_hash=previous_hash)

        _i, _j = self.get_balance_min_and_max()
        self.update_balance_min_and_max(_i, _j)

        info = {
            '信息': "New Block Forged",
            '索引值': block['index'],
            '交易信息': block['transactions'],
            '工作量证明': block['proof'],
            '前导区块Hash': block['previous_hash'],
        }
        self.append_output(info=self.get_format_info(' Add New Block ', info))

    def broadcast_this_node(self):
        info = '{}\t{}'.format(self.get_format_time(), '登陆上线，已将本节点广播到网络中...')
        self.append_output(info=info)
        MySocket.send_data(msg_type='NewNodeAdded', msg_data=self.ip_port,
                           target_ip_port=('<broadcast>', self.ip_port[1]), from_user=self.user_id)

    def register_user_id(self, user_id):
        self.users.add(user_id)
        info = '{}\t{}'.format(self.get_format_time(), '已同步节点，并添加 用户{} 到记录'.format(user_id))
        self.append_output(info=info)

    def register_old_node(self, ip_port_from, *args, **kwargs):
        ip_port_from = tuple(ip_port_from)
        self.block_chain.nodes.add(str(ip_port_from))
        info = '{}\t{}'.format(self.get_format_time(), '收到回拨信息并将 节点 {} 添加到列表'.format(ip_port_from))
        self.append_output(info=info)
        self.register_user_id(user_id=kwargs['from_user'])

    def register_new_node(self, ip_port_from, *args, **kwargs):
        ip_port_from = tuple(ip_port_from)
        self.block_chain.nodes.add(str(ip_port_from))
        info = '{}\t{}'.format(self.get_format_time(), '已添加 节点{} 到列表，并向其回拨本节点'.format(ip_port_from))
        self.append_output(info=info)
        MySocket.send_data(msg_type='OldNodeReply', msg_data=self.ip_port, target_ip_port=ip_port_from,
                           from_user=self.user_id)
        self.register_user_id(user_id=kwargs['from_user'])

    def update_chain(self):
        if len(self.block_chain.nodes) == 0:
            info = '{}\t{}'.format(self.get_format_time(), '节点列表为空，请先广播本节点以同步其他节点信息')
            self.append_output(info=info)
            return
        for node in self.block_chain.nodes:
            node = tuple(eval(node))
            info = '{}\t{}'.format(self.get_format_time(), '已向 节点{} 发送消息，请求同步最长链...'.format(node))
            self.append_output(info=info)
            MySocket.send_data(msg_type='UpdateChain', msg_data=self.ip_port, target_ip_port=node,
                               from_user=self.user_id)

    def send_chain(self, ip_port_from, *args, **kwargs):
        ip_port_from = tuple(ip_port_from)
        info = '{}\t{}'.format(self.get_format_time(), '发送当前链信息到 节点{}'.format(ip_port_from))
        self.append_output(info=info)
        MySocket.send_data(msg_type='ExistingChain', msg_data=self.block_chain.chain, target_ip_port=ip_port_from,
                           from_user=self.user_id)

    def replace_chain(self, new_chain, *args, **kwargs):
        if len(new_chain) < len(self.block_chain.chain):
            self.append_output('{}\t{}'.format(self.get_format_time(), '接收到新链，但不是最长链，已舍弃'))
            return
        elif not self.block_chain.valid_chain(new_chain):
            self.append_output('{}\t{}'.format(self.get_format_time(), '接收到新链，但属于非法链，已舍弃'))
            return
        else:
            self.block_chain.chain = new_chain
            self.append_output('{}\t{}'.format(self.get_format_time(), '接收到新链，比对验证无误，已替换'))

            _i, _j = self.get_balance_min_and_max()
            self.update_balance_min_and_max(_i, _j)

    def broadcast_last_transaction(self):
        info = '{}\t{}'.format(self.get_format_time(), '交易产生，已广播交易信息到网络...')
        self.append_output(info=info)
        MySocket.send_data(msg_type='NewTransaction', msg_data=self.block_chain.currentTransaction[-1],
                           target_ip_port=('<broadcast>', self.ip_port[1]), from_user=self.user_id)

    def add_transaction_from_net(self, transaction_info, *args, **kwargs):
        self.block_chain.new_transaction(
            sender=transaction_info['sender'],
            recipient=transaction_info['recipient'],
            amount=transaction_info['amount']
        )

        _i, _j = self.get_balance_min_and_max()
        self.update_balance_min_and_max(_i, _j)

        self.append_output('{}\t{}'.format(self.get_format_time(), '从其他节点接收到交易信息并添加到交易列表'))

    def send_chatting_message(self):
        msg = self.textEdit_chat.toPlainText()
        if msg == '':
            self.show_error_msg(title='Warning', msg='发送内容不能为空')
            return
        data = {'time': self.get_format_time(), 'msg': msg}
        MySocket.send_data(msg_type='ChatMessage', msg_data=data, target_ip_port=('<broadcast>', self.ip_port[1]),
                           from_user=self.user_id)
        self.textEdit_chat.setText('')
        self.show_chatting_message(data['time'], self.user_id, data['msg'])

    def show_chatting_message(self, msg_time, msg_user, msg_data):
        info = '{}\t{}\n\t{}'.format(msg_time, msg_user, msg_data)
        self.append_output(info=info)

    def receive_chatting_message(self, data, *args, **kwargs):
        self.show_chatting_message(data['time'], kwargs['from_user'], data['msg'])
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
