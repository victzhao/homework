
import socket
from public import method
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

islogin = 0
while True:

    while islogin == 0:
        username = input('输入你的用户名：')
        sk.sendall(bytes(username,'utf8'))
        data_rec = sk.recv(1024)
        if str(data_rec,'utf8') == '0':
            print('用户名不存在！')
            continue
        else:
            passwd = input(str(data_rec,'utf8'))
            encry_passwd = method.encryptpass(passwd)
            sk.sendall(bytes(encry_passwd,'utf8'))
        result_login = str(sk.recv(1024),'utf8')
        if result_login == '登录成功':
            print('登录成功')
            islogin = 1
        else:
            print(result_login)
    while True:
        cmd = input('ftp:')
        if not len(cmd):continue
        sk.sendall(bytes(cmd,'utf8'))
        cmd_result = str(sk.recv(1024))
        if str(cmd_result) == 'Null':
            print('命令错误或者无返回结果')
            continue
        print(cmd_result)




sk.close()


