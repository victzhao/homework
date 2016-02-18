#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import json
import pickle

def login():
    while True:
        read_f = open('shopping/account.txt','r',encoding='utf8')
        name = input('请输入您的用户名：').strip()
        read_lock_file = open('shopping/account-clock.txt','r',encoding='utf8')
        UserOfLockList = []
        for i in read_lock_file:
           UserOfLockList.append(i.strip())
        read_lock_file.close()

        if name in UserOfLockList:
            print('该账户已经锁定')
            continue
        #循环帐号列表并匹配账户是否存在
        for i in read_f:
            #分割每行的帐号信息，取出帐号列
            name_list = i.split(':')
            #如果帐号存在，提示输入密码
            if name in name_list:
                #给三次输入机会
                for i in range(3):
                    PassWd = input('请输入您的登录密码：')
                    #如果密码正确，登录成功并退出程序
                    if PassWd == name_list[1]:
                        print('登录成功！')
                        return True
                    #如果密码错误，提示
                    else:
                        print('密码错误，请重试！')
                #三次错误后锁定帐号，并退出程序
                write_lock_file = open('shopping/account-clock.txt','a',encoding='utf8')
                write_lock_file.write(name)
                write_lock_file.write('\n')
                write_lock_file.close()
                print('错误登录次数超过三次，您的帐号%s被锁定' %(name))

        else:
            print('帐号不存在，请重试！')
        #关闭句柄
        read_f.close()

def wrapper(func):
    def inner():
        login()
        func()
    return inner

#商品列表
ShoppingList = {
    'house':2000000,
    'car':200000,
    'pc':2000,
    'phone':1998,
    'fruit':19,
    'tv':2975
    }
def price():
    shopping_list = json.dumps(ShoppingList)
    with open('shopping/obj_price.txt','w') as price_file:
        price_file.write(shopping_list)






#定义检查用户输入的金额是否是数字
def check_input(args):
    try:
        int(args)
    except ValueError:
        return 1

#定义函数执行列出商品列表
def ShowTable():
    ShoppingDic = {}
    Num = 0
    print('\033[;35m*\033[0m'*80)
    print('\033[41;33m编号\t商品\t价格\033[0m')
    for k,v in sorted(ShoppingList.items()):
        Num+=1
        print('\033[42;34m%s\t\t%s\t￥%s\033[0m' %(Num,k,v))
        ShoppingDic[Num] = k
    print('\033[;35m*\033[0m'*80)
    return ShoppingDic

#获取购物车内的商品和编号对应关系并打印
def ShowShoppingCart(args):
    ShoppingCart = {}
    Num = 0
    print('\033[;31m*\033[0m'*80)
    print('\033[41;33m编号\t商品\t数量\033[0m')
    for k,v in sorted(args.items()):
        Num+=1
        print('\033[42;34m%s\t\t%s\t%s\033[0m' %(Num,k,v))
        ShoppingCart[Num] = k
    return ShoppingCart
@wrapper
def  main():

    #定义一个空的购物车字典

    ShoppingCartDic = {}

    while True:
        #删除购物车中商品数量为0的商品
        a = [] #定义空列表来存放数量为0 的商品名称
        for k,v in ShoppingCartDic.items():#循环购物车字典，取出数量为0的商品存入列表a中
            if v == 0:
                a.append(k)
        for b in a:#循环列表中的商品名称，删除字典中的key值
            ShoppingCartDic.pop(b)

        #打印商品列表
        ShoppingDic = ShowTable()
        #提示用户输入交互
        Opthons = input('\033[;32m购买商品请输入商品编号，查看购物车请按s,修改购物车请按m，按a提交订单，退出请按q：\033[0m')
        #如果q，退出程序
        if Opthons == 'q':
            break
        elif Opthons == 's':
            print('\033[;32m*\033[0m'*80)
            print('''您的购物车商品如下：
\033[41;33m商品名称\t商品数量\033[0m''')
            for k,v in ShoppingCartDic.items():
                print('\033[42;34m%s\t\t\t%s\033[0m' %(k,v))
            print('\033[;32m*\033[0m'*80)
            input('按任意键继续！')
        elif Opthons == 'a':
            order = {}
            for items in ShoppingCartDic.keys():
                order[items] = [ShoppingCartDic[items],ShoppingList[items]]

            order_dic = json.dumps(order)
            print(order_dic)
            with open('shopping/order.txt','w') as order_file:
                order_file.write(order_dic)
            print(order)




        #如果m，修改购物车
        elif Opthons == 'm':
            if len(ShoppingCartDic) == 0:
                print('购物车为空，不能修改！')
                continue
            deleting = 0
            while deleting == 0:
                #打印购物车商品，和编号供用户选择
                ShoppingCart = ShowShoppingCart(ShoppingCartDic)
                DleteShoppingNum = input('请输入您要删除的商品编号,或者输入b返回上级菜单:')
                #检查输入，如果输入的非数字，给出提示。
                if check_input(DleteShoppingNum) == 1:
                    if DleteShoppingNum == 'b':
                        deleting = 1
                    else:
                        print('请输入b或者正确的商品编号,按任意键继续:')
                        input()
                        continue
                else:
                    #判断输入的商品编号是否在购物车列表里。
                    if int(DleteShoppingNum) <= len(ShoppingCartDic):
                        #输入的编号存在，则继续输入删除的商品数量
                        while True:
                            DleteShoppingCount = input('请输入您要删除的商品数量,或者按b返回上级菜单:')
                            #判断输入的如果不是数字，给出提示
                            if check_input(DleteShoppingCount) == 1:
                                if DleteShoppingCount == 'b':
                                    break
                                else:
                                    print('请输入b或者正确的商品数量,按任意键继续:')
                                    input()
                                    continue
                            else:
                                #判断输入的商品数量是否超过实际数量
                                if int(DleteShoppingCount) <= ShoppingCartDic[ShoppingCart[int(DleteShoppingNum)]]:
                                    DleteShppingName = ShoppingCart[int(DleteShoppingNum)] #此为删除的商品名称
                                    #如果没有超过实际数量，则在购物车里减去要删除的数量
                                    ShoppingCartDic[ShoppingCart[int(DleteShoppingNum)]] = ShoppingCartDic[DleteShppingName]-int(DleteShoppingCount)
                                    #并在金额里加上此商品的价格
                                    counts  = (int(DleteShoppingCount)) #删除的商品数量
                                    price  = (int(ShoppingList[DleteShppingName])) #所删除的商品价格
                                    #1
                                    # AllMoney = counts*price+AllMoney #商品单价*商品数量+之前的余额
                                    deleting = 1
                                    break
                                else:
                                    print('请输入正确的商品数量！')
                                    continue
                    else:
                        print('请输入正确的商品编号！')
                        continue


        else:
            #用户输入非m和q，则判断输入的是否是数字
            check_result = check_input(Opthons)
            #如果不是数字给出提示
            if check_result == 1:
                print('请输入正确的数字,按任意键积蓄:')
                input()
                continue
            #如果用户输入数字，则判断是否在商品列表内
            else:
                Opthons = int(Opthons)
                #判断输入的标号是否在商品列表内
                if Opthons <= len(ShoppingList):
                    #取出选购商品名称
                    ShoppingName = ShoppingDic[Opthons]
                    #取出所选商品的价格
                    ShoppingPrice = ShoppingList[ShoppingName]
                        #打印余额和购物车列表
                    if ShoppingName not in ShoppingCartDic.keys():
                        ShoppingCartDic[ShoppingName] = 1
                    else:
                        ShoppingCartDic[ShoppingName] = ShoppingCartDic[ShoppingName]+1
                    print('\033[;33m*\033[0m'*80)
                    print('您本次选择的商品为\033[;31m%s\033[0m' %(ShoppingName))


                else:
                    print('你所选择的商品不存在，按任意键重新选择：')
                    input()
                    continue



def aaa():
    with open('shopping/order.txt','r',encoding='utf8') as rf:
        print(rf.read())