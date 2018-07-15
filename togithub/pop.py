# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser

email = "xxxx@qq.com"
password = ""
pop3_server = "pop.qq.com"

# 连接pop3服务器
server = poplib.POP3_SSL(pop3_server, 995)

# server.set_debuglevel(1)

print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

resp, mails, octets = server.list()

print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')

msg = Parser().parsestr(msg_content)

server.quit()