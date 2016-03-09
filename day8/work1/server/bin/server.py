

import socketserver
import os,sys,json
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
        #     msg = '客户端%s连接成功 ' %(self.client_address[0])
        #     logs =  log.logger()
        #     logs.info(msg)
            print('客户端退出')
        else:

            #转换收到的消息为str
            recv_str = str(recv_data)
            print(recv_str.split("|")[0])
            #判断收到的消息类型
            if recv_str.split("|")[0] == 'auth':#如果以auth开头则为认证信息，则做认证处理
                print('收到用户消息')
                username = recv_str.split("|")[1]
                password = recv_str.split("|")[2]
                with open('user/user_info.db','r') as rf:
                    for i in rf:
                        user_info = json.loads(i.strip())
                        if username in user_info.keys():
                            if password == user_info[username]['passwd']:
                                user_send = 'auth|True'
                                self.request.send(bytes(user_send,'utf8'))
                                print('登陆成功')
                                break
                            else:
                                user_send = "auth|False"
                                self.request.send(bytes(user_send,'utf8'))
                                print('密码错误')
                                break
                        else:

                            continue
                    else:
                        print('用户名不存在')
                        user_send = "auth|False"
                        self.request.send(bytes(user_send,'utf8'))


            else:
                pass








def start():
    ip_port = (setting.ip, setting.port)
    print('--------------ftp服务启动中---------------')
    proc = socketserver.ThreadingTCPServer(ip_port, ftpserver)
    proc.serve_forever()

def auth():
    pass
def trans():
    pass

