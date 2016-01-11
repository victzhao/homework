#!/usr/bin/env python


#商品列表
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
    print('\033[;35m*\033[0m'*80)
    print('\033[41;33m编号\t商品\t价格\033[0m')
    for k,v in sorted(ShoppingList.items()):
        Num+=1
        print('\033[42;34m%s\t\t%s\t%s\033[0m' %(Num,k,v))
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

def main():
    while True:
        AllMoney = input('\033[;31m请输入您的所有积蓄：\033[0m')
        check_result = check_input(AllMoney)
        if check_result == 1:#表示用户输入的不是数字
            print('请输入正确的数字！！！')
        else:
            break
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
        Opthons = input('\033[;32m购买商品请输入商品编号，查看购物车请按s，查询余额请按c,修改购物车请按m，退出请按q：\033[0m')
        #如果q，退出程序
        if Opthons == 'q':
            break
        elif Opthons == 'c':
            print('您的当前余额为\033[;31m%s\033[0m' %AllMoney)
        elif Opthons == 's':
            print('\033[;32m*\033[0m'*80)
            print('''您的购物车商品如下：
\033[41;33m商品名称\t商品数量\033[0m''')
            for k,v in ShoppingCartDic.items():
                print('\033[42;34m%s\t\t\t%s\033[0m' %(k,v))
            print('\033[;32m*\033[0m'*80)
            input('按任意键继续！')

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
                        print('请输入q或者正确的商品编号,按任意键继续:')
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
                                    print('请输入正确的数字,按任意键继续:')
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
                                    AllMoney = counts*price+AllMoney #商品单价*商品数量+之前的余额
                                    deleting = 1
                                    break
                                else:
                                    print('请输入正确的商品数量！')
                                    break
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
                    #判断商品价格是否小于资金余额
                    if int(ShoppingPrice) <= int(AllMoney):
                        #求出新的余额
                        AllMoney = int(AllMoney)-int(ShoppingPrice)
                        #将商品加入购物车
                        #ShoppingCart.append(ShoppingName)
                        #打印余额和购物车列表
                        if ShoppingName not in ShoppingCartDic.keys():
                            ShoppingCartDic[ShoppingName] = 1
                        else:
                            ShoppingCartDic[ShoppingName] = ShoppingCartDic[ShoppingName]+1
                        print('\033[;33m*\033[0m'*80)
                        print('您本次选择的商品为\033[;31m%s\033[0m,您的最新余额为\033[;31m%s\033[0m' %(ShoppingName,AllMoney))
                    else:
                        print('您的余额不足！')
                        continue

                else:
                    print('你所选择的商品不存在，按任意键重新选择：')
                    input()
                    continue



if __name__ == "__main__":
    main()




