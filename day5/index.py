#!/bin/env python


from Credit import creditop
from shopping import set
import sys


while True:
    print('''欢迎进入XX商城系统：
0   退出系统
1   商城购物
2   购物结算
3   信用卡账户管理
4   ATM取款
5   信用卡还款

''')
    option = input('请输入功能代码：')
    if option == '1':
        set.price()
        set.main()
    elif option == '2':
        pass
    elif option == '3':
        creditop.creditaccoun()
    elif option == '4':
        pass
    elif option == '5':
        pass
    elif option == '0':
        sys.exit('退出系统')
