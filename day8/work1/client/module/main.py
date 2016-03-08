import  socket,sys

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
                    self.sock = socket.socket(self.argvs[self.argvs.index('-h')+1],int(self.argvs.index('-p')+1))
                    self.sock.connect()

                except Exception as e:
                    print(e)
        else:
            self.help()


    def help(self):
        print('''执行参数：
-h ip_of_ftp_server      :ftp address
-p port_of_ftp_server    :ftp server port
''')

