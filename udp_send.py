# -*- coding: UTF-8 -*-
import socket
import numpy as np
import cv2
import struct

send_addr = ('<broadcast>', 9527)
BUF_SIZE = 2048


def main_msg():
    # 定义Socket 指定网络类型和协议 绑定监听IP和端口 UDP IP为空 则监听所有IP
    send_msg = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send_msg.bind(send_addr)
    send_msg.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # 定义传输内容
    msg = struct.pack('20sI', bytes('send msg'.encode('utf-8')), 22)
    # 传输数据
    send_msg.sendto(msg, send_addr)
    print('发送成功')
    # 等待响应
    print('响应：\t', send_msg.recvfrom(1024)[0].decode('utf-8'))
    # 释放 Socket
    send_msg.close()


def main_img():
    send_img = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_img.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # 载入图片 再编码 压缩内容 并tostring转为bytes类型
    image = cv2.imread('./data/test_pic.png')
    image_encode = cv2.imencode('.png', image)[1]
    data = image_encode.tostring()
    # 定义文件头 记录并传输文件总长度
    fhead = struct.pack('ll', len(data), BUF_SIZE)
    # 广播 文件头
    send_img.sendto(fhead, send_addr)
    # 分组按序传输图片
    print('开始传输文件')
    total_epoch = len(data) // BUF_SIZE + (0 if len(data) % BUF_SIZE == 0 else 1)
    for i in range(total_epoch):
        if i == total_epoch - 1:
            send_img.sendto(data[BUF_SIZE * i:], send_addr)
        else:
            send_img.sendto(data[BUF_SIZE * i:BUF_SIZE * (i + 1)], send_addr)
        print('\r文件传输中... {}/{}'.format(i + 1, total_epoch), end='')
    print('\n文件传输结束')
    # 等待传输完成的消息应答
    print('应答：', send_img.recvfrom(1024)[0].decode('utf-8'))
    # 释放
    send_img.close()


if __name__ == '__main__':
    # main_msg()
    main_img()
