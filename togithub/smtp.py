# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr
from email.header import Header
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.encoders import encode_base64

my_sender = 'xxxxx@qq.com'  # 发件人邮箱账号
my_pass = ''  # 发件人邮箱密码(当时申请smtp给的口令)
my_user = '378641588@qq.com'  # 收件人邮箱账号，我这边发送给自己


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr([Header(name, 'utf-8').encode(), addr])


def mail():
    ret = True
    try:
        # msg = MIMEText('填写邮件内容', 'plain', 'utf-8')  # 纯文本

        # html
        # msg = MIMEText('<html><body><p style="color:red">用Python发邮件</p><a href="https://www.baidu.com">baidu</a>'
        #                '</body></html>', 'html', 'utf-8')

        # msg['From'] = formataddr(['来自高笛淳', my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr(['cc', my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['Subject'] = '测试发邮件'  # 邮件的主题，也可以说是标题
        # msg = MIMEMultipart()
        msg = MIMEMultipart('alternative')
        msg['From'] = _format_addr('Python爱好者<%s>' % my_sender)
        msg['To'] = _format_addr('管理员<%s>' % my_user)
        msg['Subject'] = Header('来自SMTP的问候', 'utf-8').encode()

        # 图片作为附件
        msg.attach(MIMEText('send with file..', 'plain', 'utf-8'))
        msg.attach(MIMEText('<html><body><h1>Hello</h1><p>'
                            '<img style="width:60px,height:80px" src="cid:0"></p></body></html>', 'html', 'utf-8'))

        with open('../resource/timg.jpg', 'rb') as f:
            # 设置附件mime和文件名，这里是png类型
            mime = MIMEBase('image', 'png', filename='tst.jpg')
            # 加上必要的头信息
            mime.add_header('Content-Disposition', 'attachment', filename='tst.jpg')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')

            # 把附件内容读进来
            mime.set_payload(f.read())
            # 用Base64编码
            encode_base64(mime)
            # 添加到MIMEMultipart
            msg.attach(mime)

        server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print('邮件发送成功')
else:
    print('邮件发送失败')

