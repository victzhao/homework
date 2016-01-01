#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
#获取省和市的对应字典
def GetProvinceDic():
    province_dic = {}
    read_f = open('china.txt','r',encoding='utf8')
    for i in read_f.readlines():
        b = i.split()
        if b[0] not in province_dic.keys():
            province_list = [b[1]]
            province_dic[b[0]] = province_list
        else:
            if b[1] not in province_dic[b[0]]:
                province_list.append(b[1])
    read_f.close()
    return province_dic
#获取市和县的对应字典
def GetCountyDic():
    country_dic = {}
    read_f = open('china.txt','r',encoding='utf8')
    for i in read_f.readlines():
        b = i.split()
        if b[1] not in country_dic.keys():
            country_list = [b[2]]
            country_dic[b[1]] = country_list
        else:
            if b[2] not in country_dic[b[1]]:
                country_list.append(b[2])
    read_f.close()
    return country_dic


#获取各省的对应编号
def GetProvinceOfNu(args,**kwargs):
    NumOfProvinceDic={}
    NumOfProvince = 0
    for Province in sorted(args):
        NumOfProvince+=1
        NumOfProvinceDic[NumOfProvince] = Province
    return NumOfProvinceDic

#获取省下各市区的对应编号
def GetCountryOfNu(args1,args2):
    NumberOfCountryList = args1[args2]
    NumberOfCountryDic = {}
    NumOfCountry = 0
    for Country in NumberOfCountryList:
        NumOfCountry+=1
        NumberOfCountryDic[NumOfCountry] = Country
    return NumberOfCountryDic

def check_input(args):
    try:
        int(args)
    except ValueError:
        return 1

province_dic = GetProvinceDic()
nu_province = GetProvinceOfNu(province_dic)
step = 1
while step == 1:
    for num in sorted(nu_province):
        print('%s:   %s' %(num,nu_province[num]))
    print('*'* 100)
    Num = input('请输入以上省所对应的编号，按q退出,输入b返回上级菜单:')
    check_in = check_input(Num)
    print('*'* 100)
    if check_in == 1:
        if Num == 'q':
            print('您选择了退出，程序退出！')
            break
        elif Num == 'b':
            continue
    else:
        Num = int(Num)
        if Num > num:
            print('请输入小于%s的数字' %num )

        else:
            province = (nu_province[int(Num)])
            Country_dic = GetCountryOfNu(province_dic,province)
            step = 2
            while step == 2:

                for NumCountry in Country_dic.keys():
                    print('%s:  %s' %(NumCountry,Country_dic[NumCountry]))
                print('*'* 100)
                CountryNum = input('请输入以上市区所对应的编号，按q退出，按b返回上级菜单:')
                check_in2 = check_input(CountryNum)
                if check_in2 == 1:
                    if CountryNum == 'q':
                        print('您选择了退出，程序退出！')
                        sys(exit(0))
                    elif CountryNum == 'b':
                        break
                else:
                    CountryNum = int(CountryNum)
                    if CountryNum > NumCountry:
                        print('请输入小于%s的数字' %NumCountry )
                        continue
                    else:
                        CountryNum = int(CountryNum)
                        print('您选择的市为:%s,所包含的县如下:' %(Country_dic[CountryNum]))
                        country_dic = GetCountyDic()
                    for towns in country_dic[Country_dic[CountryNum]]:
                        print(towns)
                    confirm = input('请输入b返回上级菜单，输入f返回第一级菜单，输入q退出程序:')
                    if confirm == 'b':
                        continue
                    elif confirm == 'f':
                        break
                    elif confirm == 'q':
                        print('您选择了退出，程序退出！')
                        sys(exit(0))
























