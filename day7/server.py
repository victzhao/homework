#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
import subprocess,sys,os
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
        conn,addr = sk.accept()
        self.conn = conn
        self.addr = addr
    def close(self):
        self.conn.close()
    def login(self):
        userinfo = {'tom': ['tom123','data_rec/tom/'], 'jack': ['jack123','data_rec/jack/']}
        logs = logger()
        while True:
            username = str(self.conn.recv(1024), 'utf8')
            if username in userinfo.keys():
                self.conn.sendall(bytes('请输入%s的密码:' %username, 'utf8'))
                rec_pass = str(self.conn.recv(1024), 'utf8')
                encry_pass = method.encryptpass(userinfo[username][0])
                if rec_pass == encry_pass:
                    msg = '%s-%s-%s-登陆成功' %(self.addr[0],self.addr[1],username,)
                    logs.info(msg)
                    self.conn.sendall(bytes('登录成功', 'utf8'))
                    while True:
                        client_data = str(self.conn.recv(1024),'utf8')
                        if client_data.startswith('put'):
                            self.conn.send(bytes('Ready to put!','utf8'))
                            #接收文件名和文件大小
                            file_info = str(self.conn.recv(1024),'utf8')
                            file_info = file_info.split(':')
                            file_name = file_info[0].split('/')[-1]
                            file_size = file_info[1]
                            received_size = 0
                            rec_path  = userinfo[username][1]
                            rec_file = '%s%s' %(rec_path,file_name)
                            #判断是否已经存在文件名
                            if os.path.exists(rec_file): #文件已经存在则断点续传
                                pass
                            else:
                                while received_size < int(file_size):
                                    with open('data_rec/%s/%s' %(username,file_name),'ab') as write_file:

                                        data = self.conn.recv(500)
    #                                    sdata = str(data,'utf8')

                                        write_file.write(data)
                                        #self.conn.send(b'ack')
                                        received_size += len(data)
                                else:
                                    #print('文件传输完毕')
                                    msg = '%s-%s-%s-%s-上传完成' %(self.addr[0],self.addr[1],username,file_name)
                                    logs.info(msg)




                        elif client_data.startswith('get'):
                            pass


                else:
                    msg = '%s-%s-%s-密码错误' %(self.addr[0],self.addr[1],username,)
                    logs.info(msg)
                    self.conn.sendall(bytes('密码错误', 'utf8'))
            else:
                msg = '%s-%s-%s-用户名不存在' %(self.addr[0],self.addr[1],username,)
                logs.info(msg)
                self.conn.sendall(bytes('0', 'utf8'))





if __name__ == '__main__':
    servers = ftp('127.0.0.1','9999')
    servers.listen()
    loginstatus = servers.login()




