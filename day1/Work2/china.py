#!/usr/bin/env python
# -*- coding:utf-8 -*-

def GetProvinceDic():
    province_dic = {}
    read_f = open('china.txt','r',encoding= 'utf8')
    for i in read_f.readlines():
        b = i.split()
        if b[0] not in province_dic.keys():
            province_list = [b[1]]
            province_dic[b[0]] = province_list
        else:
            if b[1] not in province_dic[b[0]]:
                province_list.append(b[1])
            else:
                pass
    read_f.close()
    return province_dic

def GetCountryDic():
    country_dic = {}
    read_f = open('china.txt','r',encoding= 'utf8')
    for i in read_f.readlines():
        b = i.split()
        if b[1] not in country_dic.keys():
            country_list = [b[2]]
            country_dic[b[1]] = country_list
        else:
            if b[2] not in country_dic[b[1]]:
                country_list.append(b[2])
            else:
                pass
    read_f.close()
    return country_dic



def GetProvinceOfNu(args,**kwargs):
    NumOfProvinceDic={}
    NumOfProvince = 0
    for Province in args.keys():
        NumOfProvince+=1
        NumOfProvinceDic[NumOfProvince] = Province
    return NumOfProvinceDic

a = GetProvinceDic()

print(a)





def GetCountryOfNu(args):
    pass







