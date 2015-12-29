#!/usr/bin/env python
# -*- coding:utf-8 -*-

privince_dic = {}
country_dic = {}
town_dic = {}
read_f = open('china.txt','r',encoding= 'utf8')
for i in read_f:
    b = i.split()
    for lines in b[0]:
        if lines in privince_dic.keys():
            pass
        else:
            privince_dic[lines] = b[1]


