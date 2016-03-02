#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
import subprocess
from public import method

ip_port = ('127.0.0.1',9998)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
userinfo = {'tom':'tom123','jack':'jack123'}

conn,addr = sk.accept()
while True:

    username = str(conn.recv(1024),'utf8')
    print(username)
    if username in userinfo.keys():
        conn.sendall(bytes('请输入%s的密码:' %username,'utf8'))
        rec_pass = str(conn.recv(1024),'utf8')
        encry_pass = method.encryptpass(userinfo[username])
        if rec_pass == encry_pass:
            print('登录成功！')

            conn.sendall(bytes('登录成功','utf8'))
        else:
            print('密码错误！')
            conn.sendall(bytes('密码错误-------','utf8'))
    else:
        print('用户名不存在！')
        conn.sendall(bytes('用户名不存在,回车后重新登录！','utf8'))
conn.close()


