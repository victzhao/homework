

import socketserver
from conf import setting

class ftpserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        client_addr = self.client_address


def start():
    ip_port = (setting.ip, setting.port)
    proc = socketserver.ThreadingTCPServer(ip_port, ftpserver)
    proc.serve_forever()
    print('Ftp 服务启动成功')
def auth():
    pass
def trans():
    pass

