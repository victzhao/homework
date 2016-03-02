
import socket
from public import method
ip_port = ('127.0.0.1',9998)

sk = socket.socket()
sk.connect(ip_port)

while True:

    username = input('输入你的用户名：')
    sk.sendall(bytes(username,'utf8'))
    data_rec = sk.recv(1024)
    passwd = input(str(data_rec,'utf8'))
    encry_passwd = method.encryptpass(passwd)
    sk.sendall(bytes(encry_passwd,'utf8'))
    result_login = str(sk.recv(1024),'utf8')
    if result_login == '登录成功':
        print('登录成功')

    else:
        print(result_login)


sk.close()


