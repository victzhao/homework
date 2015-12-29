#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


while True:
    read_f = open('account.txt','r')
    AllofUser = read_f.readlines()
    name = input('请输入您的用户名：').strip()
    read_lock_file = open('account-clock.txt','r')
    LockOfuser = (read_lock_file.readlines())

    if name in LockOfuser:
        print('帐号已锁定！')
        continue
    else:
        pass




    # for i in read_lock_file:
    #     if name not in i and name not in read_f:
    #         print('all not')
    #     else:
    #         print('您的帐号已锁定！')
    #         break
    # read_lock_file.close()













    #循环帐号列表并匹配账户是否存在
    # for i in read_f:
    #     #分割每行的帐号信息，取出帐号列
    #     name_list = i.split(':')
    #     #如果帐号存在，提示输入密码
    #     if name in name_list:
    #         #给三次输入机会
    #         for i in range(3):
    #             PassWd = input('请输入您的登录密码：')
    #             #如果密码正确，登录成功并退出程序
    #             if PassWd == name_list[1]:
    #                 print('登录成功！')
    #                 sys(exit(0))
    #             #如果密码错误，提示
    #             else:
    #                 print('密码错误，请重试！')
    #         #三次错误后锁定帐号，并退出程序
    #         write_lock_file = open('account-clock.txt','a')
    #         write_lock_file.write(name)
    #         write_lock_file.write('\n')
    #         write_lock_file.close()
    #         print('错误登录次数超过三次，您的帐号%s被锁定' %(name))
    #
    #         sys(exit(1))
    # else:
    #     print('帐号不存在，请重试！')
    # #关闭句柄
    # read_f.close()



