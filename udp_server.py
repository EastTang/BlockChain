import socketserver as ss
import json
ip_port = ('', 9527)


class SelfUdpHandler(ss.BaseRequestHandler):
    def handle(self):
        data, sender = self.request
        print('{}:\t{}'.format(sender, data.decode('utf-8').replace('\n', '')))
        # data = json.dumps(eval(data.decode('utf-8')), indent=2, ensure_ascii=False)
        # print(data)


if __name__ == '__main__':
    server = ss.ThreadingUDPServer(ip_port, SelfUdpHandler)
    print("Waiting ...")
    server.serve_forever()
