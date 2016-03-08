

import socketserver
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting
from logs import log
def test():

    print(setting.ip)

class ftpserver(socketserver.BaseRequestHandler):
    def handle(self):
        # while True:
        #j接收客户端发来的数据
        recv_data = str(self.request.recv(1024),'utf8')
        #把数据交给handle_data处理
        self.handle_data(recv_data)

    def handle_data(self,recv_data):
        if not recv_data.split('|'): #如果没数据收到程序退出
            msg = '客户端%s连接成功 ' %(self.client_address[0])
            logs =  log.logger()
            logs.info(msg)
        else:
            print(recv_data)






def start():
    ip_port = (setting.ip, setting.port)
    print('--------------ftp服务启动中---------------')
    proc = socketserver.ThreadingTCPServer(ip_port, ftpserver)
    proc.serve_forever()

def auth():
    pass
def trans():
    pass

