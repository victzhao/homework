#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
import subprocess
import logging
from public import method


def logger():
        logs = logging.getLogger('Ftplog')
        logs.setLevel(logging.INFO)
        #bin to file
        logfile = logging.FileHandler('log/ftp.log')
        logfile.setLevel(logging.INFO)
        #bin to console
        logconsole = logging.StreamHandler()
        logconsole.setLevel(logging.INFO)

        formaters =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logfile.setFormatter( formaters )
        logconsole.setFormatter(formaters)
        logs.addHandler( logfile )
        logs.addHandler(logconsole)
        return logs

class ftp() :

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.conn = None
        self.addr = None


    def listen(self):

        ip_port = (self.ip,int(self.port))
        sk = socket.socket()
        sk.bind(ip_port)
        sk.listen(5)

        print('欢迎进入ftp系统！')
        # conn,addr = sk.accept()
        # self.conn = conn
        # self.addr = addr

    def close(self):
        self.conn.close()






    def login(self):

        userinfo = {'tom': 'tom123', 'jack': 'jack123'}
        logs = logger()
        while True:

            self.conn,self.addr = self.sk.accept()
            username = str(self.conn.recv(1024), 'utf8')
            if username in userinfo.keys():
                self.conn.sendall(bytes('请输入%s的密码:' %username, 'utf8'))
                rec_pass = str(self.conn.recv(1024), 'utf8')
                encry_pass = method.encryptpass(userinfo[username])
                if rec_pass == encry_pass:
                    msg = '%s-%s-%s-登陆成功' %(self.addr[0],self.addr[1],username,)
                    logs.info(msg)
                    self.conn.sendall(bytes('登录成功', 'utf8'))
                else:
                    msg = '%s-%s-%s-密码错误' %(self.addr[0],self.addr[1],username,)
                    logs.info(msg)
                    self.conn.sendall(bytes('密码错误', 'utf8'))
            else:
                msg = '%s-%s-%s-用户名不存在' %(self.addr[0],self.addr[1],username,)
                logs.info(msg)
                self.conn.sendall(bytes('0', 'utf8'))
    def put(self):
        pass
    def get(self):
        pass



if __name__ == '__main__':
    servers = ftp('127.0.0.1','9999')
    servers.listen()
    servers.login()


