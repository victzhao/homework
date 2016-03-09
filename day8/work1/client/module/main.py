import  socket,sys,json

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
                    self.sock = socket.socket()
                    self.sock.connect((self.argvs[self.argvs.index('-h')+1],int(self.argvs[self.argvs.index('-p')+1])))
                    if self.auth():
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
            self.sock.sendall(bytes(user_send,'utf8'))
            break
        user_recv = self.sock.recv(1024)



    def send_data(self):#处理发送数据函数
        ''' 客户端发送数据给server端
        :param send_data: 客户端发送数据给服务端
        :param args: 无
        :return: 无'''
        pass



