# -*- coding: utf-8 -*-

import socket
import threading


def updlink(sock, addr):
    while True:
        data, addr = s.recvfrom(1024)
        print('received from %s:%s' % addr)
        s.sendto(b'hello %s!' % data, addr)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议

# 绑定端口
s.bind(('127.0.0.1', 9999))

print("bind udp on 9999")

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('received from %s:%s' % addr)
    s.sendto(b'hello %s!' % data, addr)

