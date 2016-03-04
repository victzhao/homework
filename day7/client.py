
import socket
from public import method
import sys,os
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

islogin = 0
print('''------------------------------------------------------------------------------------------
                欢迎登陆ftp系统！
------------------------------------------------------------------------------------------
                        ###########################
                        #   登陆用户名    密码     #
                        #   tom           tom123  #
                        #   jack          jack123 #
                        ###########################
使用方法：
    put path/filename         #上传文件put和文件路径之间一个空格隔开
    get path/filename         #下载文件get和文件路径之间一个空格隔开
------------------------------------------------------------------------------------------
''')
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
        #获取要上传或者下载的文件名
        cmd_split = cmd.split(' ')
        #发送命令到服务端
        sk.sendall(bytes(cmd,'utf8'))
        #判断操作是上传还是下载
        if cmd.startswith('put'):
            sk.recv(1024)
            file_name = cmd_split[1]
            if os.path.exists(file_name):
                file_size = os.path.getsize(file_name)
                file_info = '%s:%s' %(file_name,file_size)
                sk.send(bytes(file_info,'utf8'))
                with open(file_name,'rb') as send_file:
                    for i in send_file:
                        sk.sendall(i)



        elif cmd.startswith('get'):
            pass





sk.close()


