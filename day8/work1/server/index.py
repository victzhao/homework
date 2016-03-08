

from bin import server
from module import main
import sys



if   __name__ ==  '__main__':
    while True:
         option1 = '''---------------请输入操作编号-----------------
                0---> 启动服务
                1---> 新建用户
                2---> 退出程序
----------------------------------------------
'''
         print(option1)
         msg = input('请输入编号:')
         if msg == '0':
             server.start()
             break
         elif msg == '1':
             while True:#提示用户输入用户名，密码，磁盘配额等信息
                name = input('Input Name:')
                passwd = input("Input Password:")
                try:
                    quota = input("Input Quota:")
                    int(quota)
                except Exception as e:
                    print('Quotation must be a num!')
                    continue
                else:

                    users = main.user_handle('zhaojianbo','zhaojianbo123','1000') #初始化创建用户实例
                    users.add_user()#创建用户
                break
         elif msg == '2':
             sys.exit('程序退出')
         else:
             print('输入错误')
             continue


