#/usr/bin/env python
#-*- coding: utf-8 -*-
import hashlib

#加密密码
def encryptpass(args):
    pas = hashlib.sha256()
    pas.update(args.encode())
    return pas.hexdigest()
def login():
    while True:
        read_f = open('db/account.txt','r',encoding='utf8')
        name = input('请输入您的用户名：').strip()
        read_lock_file = open('db/account-clock.txt','r',encoding='utf8')
        UserOfLockList = []
        for i in read_lock_file:
           UserOfLockList.append(i.strip())
        read_lock_file.close()

        if name in UserOfLockList:
            print('该账户已经锁定')
            break
        #循环帐号列表并匹配账户是否存在
        for i in read_f:
            #分割每行的帐号信息，取出帐号列
            name_list = i.split(':')
            #如果帐号存在，提示输入密码
            if name in name_list:
                #给三次输入机会
                for i in range(3):
                    PassWd = input('请输入您的登录密码：')
                    PassWd = encryptpass(PassWd)
                    #如果密码正确，登录成功并退出程序
                    if PassWd == name_list[1]:
                        print('登录成功！')
                        return True
                    #如果密码错误，提示
                    else:
                        print('密码错误，请重试！')
                #三次错误后锁定帐号，并退出程序
                write_lock_file = open('db/account-clock.txt','a',encoding='utf8')
                write_lock_file.write(name)
                write_lock_file.write('\n')
                write_lock_file.close()
                print('错误登录次数超过三次，您的帐号%s被锁定' %(name))

        else:
            print('帐号不存在，请重试！')
        #关闭句柄
        read_f.close()

#密码加密函数



#检查用户输入是否为数字
def CheckInputIsNum(args):
    try:
        int(args)
    except ValueError:
        return 1
def register():
    roles = ['Tangseng','Sunwukong','Shaseng','Zhubajie','Baigujing']
    print('欢迎进入三打白骨精游戏注册页面:')
    #设置用户名
    while True:
        name = input('请输入您的用户名：')
        if not name.strip():
            print('输入不能为空！')
            continue
        else:
            break

    #设置密码
    while True:
        pwd = input('请输入您的密码：')
        if not pwd:
            print('密码不能为空')
            continue
        else:
            while True:
                pwd2 = input('请再次输入密码：')
                if not pwd2:
                    print('密码不能为空！')
                    continue
                else:
                    break
        if pwd == pwd2:
            encryptpwd = encryptpass(pwd)
            break
        else:
            print('两次密码不一致')
            continue
    #设置角色名称
    while True:
        for m,n in enumerate(roles):
            print(m,n)
        RoleOfNum = input('请输入您的角色：')
        if CheckInputIsNum(RoleOfNum) == 1:
            print('请输入数字')
            continue
        else:
            if int(RoleOfNum) >= len(roles):
                print('请输入正确的数字')
                continue
            else:
                RoleOfu = roles[int(RoleOfNum)]
                print('注册成功')
                with open(r'db/account.txt','a') as write_f:
                    write_f.write('%s:%s:3:%s\n' %(name,encryptpwd,RoleOfu))

                break




