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
    return province_dic
print(GetProvinceDic())

