#！/usr/bin/env python
# -*- coding:utf-8 -*-


ShoppingList = {
    '房子':2000000,
    '汽车':200000,
    '电脑':2000,
    '手机':1998,
    '水果':19,
    '冰箱':2975
    }



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
    print('*'*50)
    print('编号\t商品\t价格\t')
    for k,v in sorted(ShoppingList.items()):
        Num+=1
        print('%s\t\t%s\t%s' %(Num,k,v))
        ShoppingDic[Num] = k
    return ShoppingDic

while True:
    AllMoney = input('请输入您的所有积蓄：')
    check_result = check_input(AllMoney)
    if check_result == 1:
        print('请输入正确的数字！！！')
    else:
        break
#定义一个空的购物车字典
ShoppingCartDic = {}
while True:
    #打印商品列表
    ShoppingDic = ShowTable()
    #提示用户输入交互
    Opthons = input('购买商品请输入商品编号，修改购物车请按m，退出请按q：')
    #如果q，退出程序
    if Opthons == 'q':
        break
    #如果m，修改购物车
    elif Opthons == 'm':
        print('此功能暂时还没实现')
        pass
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
                #判断商品价格是否小于资金余额
                if int(ShoppingPrice) < int(AllMoney):
                    #求出新的余额
                    AllMoney = int(AllMoney)-int(ShoppingPrice)
                    #将商品加入购物车
                    #ShoppingCart.append(ShoppingName)
                    #打印余额和购物车列表
                    if ShoppingName not in ShoppingCartDic.keys():
                        ShoppingCartDic[ShoppingName] = 1
                    else:
                        ShoppingCartDic[ShoppingName] = ShoppingCartDic[ShoppingName]+1
                    print('您本次选择的商品为%s,您的最新余额为%s' %(ShoppingName,AllMoney))
                    print('''您的购物车商品如下：
商品名称\t商品数量''')
                    for k,v in ShoppingCartDic.items():
                        print('%s\t\t\t%s' %(k,v))
                else:
                    print('您的余额不足！')
                    continue

            else:
                print('你所选择的商品不存在，按任意键重新选择：')
                input()
                continue



