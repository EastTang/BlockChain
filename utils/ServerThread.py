import threading
from utils.communicate_tool import *


class ServerThread(threading.Thread):
    def __init__(self, owner, ip_port):
        super().__init__()
        # 设置附属监听服务器
        self.server = ThreadingUDPServer(ip_port, MyUDPHandle.Creator(owner))
        print('附属服务器已创建...')

    def run(self) -> None:
        print('附属服务器已开始监听...')
        self.server.serve_forever()
