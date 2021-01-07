# -*- coding: UTF-8 -*-
import socket
import numpy as np
import cv2
import struct

recv_addr = ('', 9527)


def main_msg():
    # 定义Socket 指定网络类型和协议 绑定监听IP和端口 UDP IP为空 则监听所有IP
    recv_msg = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_msg.bind(recv_addr)
    print('Socket 初始化完成 监听端口...')
    # 接收msg
    fmt = '20sI'
    buf_size = struct.calcsize(fmt)
    print('buffer size = ', buf_size)
    data, form_addr = recv_msg.recvfrom(buf_size)
    print('接收成功')
    # 格式化 接收到的数据
    data = struct.unpack(fmt, data)
    print('接收到的数据为', data)
    print('数据来源为', form_addr)
    # 应答
    recv_msg.sendto('已接收'.encode('utf-8'), form_addr)
    # 释放 Socket
    recv_msg.close()


def main_img():
    recv_img = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_img.bind(recv_addr)
    # 接收文件头
    fmt = 'll'
    fhead_size = struct.calcsize(fmt)
    buf, from_addr = recv_img.recvfrom(fhead_size)
    print(buf)
    data_size, buf_size = struct.unpack(fmt, buf)
    print('从文件头获取得 文件流总长度为{} 分段长度为{}'.format(data_size, buf_size))
    total_data = b''
    total_epoch = data_size // buf_size + (0 if data_size % buf_size == 0 else 1)
    print('开始接收文件数据段')
    for i in range(total_epoch):
        buf, from_addr = recv_img.recvfrom(buf_size)
        total_data += buf
        print('\r文件接收中... {}/{}'.format(i + 1, total_epoch), end='')
    print('\n文件接收结束')
    recv_img.sendto('接收完成'.encode('utf-8'), from_addr)
    # 文件后处理
    # 这里虽然fromstring 但是 total_data 是 b'' 即bytes 不能转str 会报错
    img_data = np.fromstring(total_data, dtype=np.uint8)
    img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)
    print(img.shape, type(total_data))
    cv2.imshow('test', img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # main_msg()
    main_img()
