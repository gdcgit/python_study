# -*- coding: utf-8 -*-

import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM tcp连接协议

s.bind(('127.0.0.1', 9999))

s.listen(5)

print("等待连接。。。。")

while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新的线程处理tcp连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


