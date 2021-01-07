import json
import socket as sk
from socketserver import ThreadingUDPServer, BaseRequestHandler
from utils.encrypt_tool import DESUtils


class MyUDPHandle(BaseRequestHandler):
    def __init__(self, request, client_address, server, owner):
        self.owner = owner
        self.mapping_dict = {
            'NewNodeAdded': self.owner.register_new_node,
            'OldNodeReply': self.owner.register_old_node,
            'UpdateChain': self.owner.send_chain,
            'ExistingChain': self.owner.replace_chain,
            'NewTransaction': self.owner.add_transaction_from_net,
            'ChatMessage': self.owner.receive_chatting_message,
            'Quit': self.stop_server,
            # 'Default': self.stop_server
        }
        super().__init__(request, client_address, server)

    def handle(self):
        message, sender = self.request
        # 原始 未加密
        # message = eval(message.decode('utf-8'))
        # 1228版本 DES加密
        message = eval(DESUtils.decrypt_des(message))
        if message['from_user'] != self.owner.user_id and (
                message['to_ip'] == '<broadcast>' or message['to_ip'] == self.owner.ip_port[0]
        ):
            print('type:{}\ndata:{}'.format(message['type'], message['data']))
            self.mapping_dict[message['type']](message['data'], from_user=message['from_user'])

    def stop_server(self, data, *args, **kwargs):
        if not self.owner.is_running:
            self.server.shutdown()
        return

    @classmethod
    def Creator(cls, *args, **kwargs):
        def _HandleCreator(request, client_address, server):
            cls(request, client_address, server, *args, **kwargs)

        return _HandleCreator


class MySocket:
    client = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    client.setsockopt(sk.SOL_SOCKET, sk.SO_BROADCAST, 1)

    @staticmethod
    def send_data(msg_type='Default', msg_data=None, target_ip_port=None, from_user='None'):
        msg_data = msg_data or 'Default_text'
        target_ip_port = target_ip_port or ('<broadcast>', 9527)
        message = {'type': msg_type, 'data': msg_data, 'to_ip': target_ip_port[0], 'from_user': from_user}
        # 原始 为加密
        # message_bytes = bytes(json.dumps(message, indent=2, ensure_ascii=False).encode('utf-8'))
        # 1228版本 DES加密
        message_bytes = DESUtils.encrypt_des(json.dumps(message, indent=2, ensure_ascii=False))
        MySocket.client.sendto(message_bytes, target_ip_port)


if __name__ == '__main__':
    # ip_port = ('', 9527)
    # server = ThreadingUDPServer(ip_port, MyUDPHandle.Creator('Test_Creator'))
    # print("Waiting ...")
    # server.serve_forever()

    MySocket.send_data(msg_type='NewNodeAdded', msg_data=('127.0.0.2', 9527),
                       # target_ip_port=('192.168.80.201', 9527),
                       # target_ip_port=('255.255.255.255', 9527),
                       from_user='Test')
