import  socket,sys,json,os
import sys

import hashlib

def md5sum(filename):
    fd = open(filename,"r")
    fcont = fd.read()
    fd.close()
    fmd5 = hashlib.md5(fcont.encode())

    res = fmd5.hexdigest()
    return  res
class ftp_client(object):
    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_handle()


    def argv_handle(self):
        if len(self.argvs) < 5:
            self.help()
        elif len(self.argvs) == 5:
            if "-h" in self.argvs and '-p' in self.argvs:
                try:
                    #连接服务器
                    self.sock = socket.socket()
                    self.sock.connect((self.argvs[self.argvs.index('-h')+1],int(self.argvs[self.argvs.index('-p')+1])))
                    #开始认证并判断认证是否成功
                    status,user = self.auth()
                    self.user = user
                    if status:
                        #认证成功后开始处理数据
                        self.send_data()

                except Exception as e:
                    print(e)
        else:
            self.help()


    def help(self):
        print('''执行参数：
-h ip_of_ftp_server      :ftp address
-p port_of_ftp_server    :ftp server port
''')

    def auth(self):#登陆方法
        '''
        :param auth:用户登陆验证模块
        :param args:
        :return: 0:登陆失败，1:登陆成功
        '''
        while True:
            username = input('input your name:').strip()
            if not username:continue
            while True:
                password = input('input your password:').strip()
                if not password:continue
                break
            user_send = "auth|%s|%s" %(username,password)
            #发送账号密码信息到服务端
            self.sock.sendall(bytes(user_send,'utf8'))
            break
        print('开始收取消息')
        #收取服务端返回的信息
        user_recv = str(self.sock.recv(1024),'utf8')
        print(user_recv)
        if user_recv.split('|')[1] == 'True':
            return True,username
        elif user_recv.split('|')[1] == 'False':
            return False,username






    def send_data(self):#处理发送数据函数
        ''' 客户端发送数据给server端
        :param send_data: 客户端发送数据给服务端
        :param args: 无
        :return: 无'''
        while True:
            do_sth = input('<%s>' %self.user)
            if do_sth.startswith('put'):
                self.put(do_sth)
            elif do_sth.strip('get'):
                self.get(do_sth)
            else:
                self.command(do_sth)


    def get(self, args):
        pass
    def put(self,args):
        file_name = args.split(' ')[1]
        file_size = os.path.getsize(file_name)
        file_md5 = md5sum(file_name)
        data = 'put|%s|%s|%s' %(file_name,file_size,file_md5)
        self.sock.sendall(bytes(data,'utf8'))
        ack = str(self.sock.recv(1024),'utf8')
        print(ack)
        #确认消息后开始发送文件
        if ack == 'ReadyToPut':
            with open(file_name,'rb',encoding= 'gbk') as put_file:
                for i in put_file:
                    self.sock.sendall(i)


    def command(self, args):
        pass




