

import socketserver,subprocess
import os,sys,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting
from logs import log


class ftpserver(socketserver.BaseRequestHandler):
    def handle(self):
        # while True:
        #j接收客户端发来的数据
        while True:
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
            print(recv_str)
            #判断收到的消息类型
            if recv_str.split('|')[0] == 'auth':#如果以auth开头则为认证信息，则做认证处理
                username = recv_str.split("|")[1]
                self.username= username
                password = recv_str.split("|")[2]
                with open('user/user_info.db','r') as rf:
                    for i in rf:
                        user_info = json.loads(i.strip())
                        if username in user_info.keys():
                            if password == user_info[username]['passwd']:
                                user_send = 'auth|True'
                                self.request.send(bytes(user_send,'utf8'))
                                #记录日志
                                msg = '%s登录成功 ' %(username)
                                logss =  log.logger()
                                logss.info(msg)
                                return
                            else:
                                user_send = "auth|False"
                                self.request.send(bytes(user_send,'utf8'))
                                msg = '密码错误 '
                                logs =  log.logger()
                                logs.info(msg)
                                break
                        else:

                            continue
                    else:
                        msg = '用户名%s不存在 ' %(username)
                        logs =  log.logger()
                        logs.info(msg)
                        user_send = "auth|False"
                        self.request.send(bytes(user_send,'utf8'))


            elif recv_str.split('|')[0] == 'put': #如果以put开头则上传文件
                print('putting')
                self.request.send(b"ReadyToPut")
                recv_size = 0
                file_name = recv_str.split('|')[1].split('/')[-1]
                while recv_size < int(recv_str.split('|')[2]):
                    with open('user/%s/%s'%(self.username,file_name),'ab') as recv_file:
                        data = self.request.recv(500)
                        recv_file.write(data)
                        recv_size += len(data)
                else:
                    print('文件上传完成！')
                    return




            elif recv_str.split('|')[0] == 'get': #如果以get开头则下载文件
                pass
            else:#其他的则执行命令
                pass








def start():
    ip_port = (setting.ip, setting.port)
    print('--------------ftp服务启动中---------------')
    proc = socketserver.ThreadingTCPServer(ip_port, ftpserver)
    proc.serve_forever()



