#!/usr/bin/env python
# -*- coding:utf-8 -*-


read_f = open('china.txt','rb')
for i in read_f:
    n = i.strip().split()

print(n[2])