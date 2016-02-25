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
        status = gameall.login()
        if status:

            sun = roles_op.monkey('孙悟空','20','100','大师兄')
            sun.jump()
            print(sun.name)

    elif opt_num == '3':
        sys.exit('退出游戏')


