from core import gameall,roles_op
from conf import var
import sys
#gameall.login()
# gameall.register()

while True:
    print(var.welcome)
    opt_num = input('输入您的操作序号：')
    if opt_num == '1':
        gameall.register()
    elif opt_num == '2':
        users = gameall.login()
        if users:
            with open('db/account.txt','r') as user_file:
                for i in user_file:
                    roles = i.strip('\n').split(':')
                    if roles[0] == users:
                        role = roles[3]


        if role == 'Sunwukong':
            me = roles_op.monkey('孙悟空','20','100','大师兄')
            print('我是%s' %(me.name))
            me.jump()
        elif role == 'Tangseng':
            me = roles_op.tang('唐僧','40','100','师傅')
            print('我是%s' %(me.name))
            me.read()
        elif role == 'Shaseng':
            me = roles_op.sha('沙僧','30','100','沙师弟')
            print('我是%s' %(me.name))
            me.talking()
        elif role == 'Zhubajie':
            me = roles_op.zhu('猪八戒','30','100','二师兄')
            print('我是%s' %(me.name))
            me.speaking()
        elif role == 'Baigujing':
            pass

    elif opt_num == '3':
        sys.exit('退出游戏')


