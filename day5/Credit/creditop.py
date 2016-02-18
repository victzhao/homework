#!/bin/env python
import json
#添加账户，设置额度，冻结账户
#生成的用户字典格式如下：
'''
userdic = {
		zhaojianbo:{'password':'112233','amount':'2000','userstatus':'on','loginstatus':'y'},
		leifeng:{'password':'112233','amount':'2000','userstatus':'on','loginstatus':'y'}
}
'''
#信用卡账户管理函数
def creditaccoun():
    #获取用户字典
    with open('Credit/account','r') as user:
        user_info = user.read()
        if user_info:
            users = json.loads(user_info)
        else:
            users = {}
    #添加信用卡账户
    def write_file(args):
        users_str = json.dumps(args)
        with open('Credit/account','w') as wf:
            wf.write(users_str)
    def adduser():
        username = input('用户名:')
        password = input('密码:')
        amount = input('额度:')
        while True:
            userstatus = input('用户状态on/off:')
            if userstatus == 'on' or userstatus == 'off':
                users[username] = {"password":password,"amount":amount,"userstatus":userstatus,"loginstatus":"y"}
                break
            else:
                print('输入错误！')
                continue
        print('aaaaaaaaaaaaaaaaaa')
        write_file(users)

    #修改额度
    def setamount():
        print('现有账户如下：')
        for i in users.keys():
            print(i)
        while True:
            username = input('要修改的用户：')
            if username not in users.keys():
                print('用户不存在！')
                continue
            else:
                amount = input('修改的额度:')
                print(users)
                users[username]['amount'] =  amount
                write_file(users)
                break
    #删除账户
    def deluser():
        print('现有账户如下：')
        for i in users.keys():
            print(i)
        while True:
            username = input('要删除的用户：')
            if username not in users.keys():
                print('用户不存在！')
                continue
            else:
                del users[username]
                write_file(users)
                break
    #查询账户信息
    def catuserinfo():
        print('现有账户如下：')
        for i in users.keys():
            print(i)
        while True:
            username = input('要查询的用户：')
            if username not in users.keys():
                print('用户不存在！')
                continue
            else:
                print('''账户姓名：%s
账户额度：%s
账户状态：%s''' %(username,users[username]['amount'],users[username]['userstatus']))
                break




    #冻结(解冻)账户
    def lockuser():
        print('账户   状态')
        for i in users.keys():
            print('%s  %s' %(i,users[i]['userstatus']))
        flags = 1
        while flags == 1:
            username = input('要冻结(解冻)的用户：')
            if username not in users.keys():
                print('用户不存在！')
                continue
            else:
                while True:
                    op = input('冻结账户按0，解冻用户按1：')
                    if op == '0':
                        if users[username]['userstatus'] == 'on':
                            users[username]['userstatus'] = 'off'
                            flags = 0
                            break
                        elif users[username]['userstatus'] == 'off':
                            print('该账户已经是冻结状态，无需操作')
                            flags = 0
                            break
                    elif op == '1':
                        if users[username]['userstatus'] == 'off':
                            users[username]['userstatus'] = 'on'
                            flags = 0
                            break
                        elif users[username]['userstatus'] == 'on':
                            print('该账户已经是解冻状态，无需操作')
                            flags = 0
                            break
                    else:
                        print('输入错误！')
                        continue
        write_file(users)



    while True:
        print('''欢迎进入XX银行信用卡用户管理系统：
1  添加账户
2  删除账户
3  修改额度
4  冻结（解冻）账户
5  查询账户
6  查询账单
7  退出系统''')
        option = input('请输入功能代码：')
        if option == '1':
            adduser()
        elif option == '2':
            deluser()
        elif option == '3':
            setamount()
        elif option == '4':
            lockuser()
        elif option == '5':
            catuserinfo()
        elif option == '6':
            pass
        elif option == '7':
            break







#信用卡用户登陆
def login():
    pass

#结算功能
def pay(args):
    pass

#提现
def drawmoney():
    pass

#转账
def transfer():
    pass

#记录消费流水
def record():
    pass







