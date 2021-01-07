import json
import socket

# ip_port = ('<broadcast>', 9527)
ip_port = ('255.255.255.255', 9527)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

if __name__ == '__main__':
    info = {
        'type': 'OldChainReply',
        'data': '{"index": 1, "timestamp": 1608741298.1858077, "transactions": [], "proof": 100, "previous_hash": 1}'
    }
    info = json.dumps(info, indent=2, ensure_ascii=False)
    client.sendto(bytes(info.encode('utf-8')), ip_port)
