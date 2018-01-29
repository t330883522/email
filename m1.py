# coding: utf8
import poplib
from email.parser import Parser

import win32api

import time
import os


def get_parsed_msg():
    useraccount = 'ivanzgj@sina.com'  # 登陆账号
    password = 'zgj123'  # 登陆密码
    pop3_server = 'pop.sina.com'
    server = poplib.POP3(pop3_server)  # 开始连接到服务器
    # 可选项： 打开或者关闭调试信息，1为打开，会在控制台打印客户端与服务器的交互信息
    # server.set_debuglevel(1)
    # 可选项： 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    print(server.getwelcome().decode('utf8'))
    # 开始进行身份验证
    server.user(useraccount)
    server.pass_(password)
    # 使用list()返回所有邮件的编号，默认为字节类型的串
    resp, mails, octets = server.list()
    # 下面单纯获取最新的一封邮件
    total_mail_numbers = len(mails)
    # 默认下标越大，邮件越新，所以total_mail_numbers代表最新的那封邮件
    response_status, mail_message_lines, octets = server.retr(total_mail_numbers)
    msg_content = b'\r\n'.join(mail_message_lines).decode('gbk')
    # 邮件原始数据没法正常浏览，因此需要相应的进行解码操作
    msg = Parser().parsestr(text=msg_content)
    server.close()
    return msg

def get_details(msg):
    # 获取主题信息，也就是标题内容
    subject = msg.get('Subject')
    return subject



if __name__ == '__main__':
    while True:
        msg = get_parsed_msg()
        detail = get_details(msg)
        # os.system(detail)
        content = detail.split('#')
        print('content[0]',content[0])
        print('content[1]',content[1])
        if content[0] != '0':
            os.system(content[1])
        else:
            time.sleep(3)

        time.sleep(3)

