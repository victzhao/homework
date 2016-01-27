#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = '赵建波'
'''
思路：
1. 先计算括号内
2. 去除括号后再计算乘除
3. 剩下的加减一起计算
乘除计算：匹配乘除的表达式，取出乘除号左右两侧的数字（右侧的数字要包含+-号，取出中间的运算符号，判断运算符号，如果是*则进行乘法计算，如果是/则进行除法计算）
加减计算：加减统一按照加法进行计算
         匹配加减的表达式，取出加减号左右两侧的数字（两侧的数字都包含+-号），对两侧的数字进行相加
所有的计算流程：
          先找出要计算的表达式，用temp将其替换掉，再进行计算，然后把计算的结果换回temp，依次类推。

函数说明：
    remove_space 去除空格
    compute_and_sub 计算加减法
    compute_mul_div 计算乘除法
    remove_sub 合并正负号
    remove_brackets 计算括号内的表达式
    main 入口函数
'''
import re



# 除去空格
def remove_space(args):
    return  re.sub('\s','',args,count=0)
#计算加减法
def compute_and_sub(args):
    #FindOut = re.search('\d+\.?\d*[\+\-]\d+\.?\d*',args) #查找加法或者减法,此处注意匹配小数点
    FindOut = re.search('[\+\-]{0,}\d+\.?\d*[\+\-]\d+\.?\d*',args) #查找加法或者减法,此处注意匹配小数点
    if not FindOut:
        return args
    FindAndSub = FindOut.group()
    Replaced  = args.replace(FindAndSub,'temp') #用临时temp替换查找到的加减表达式

    #GetInt = re.findall('\d+\.?\d*',FindMulDiv) #准备计算加减法,取出加减号左右两侧的数字
    GetInt = re.findall('[\+\-]{0,1}\d+\.?\d*',FindAndSub) #准备计算加减法,取出加减号左右两侧的数字
    Result = float(GetInt[0])+float(GetInt[1])
    Result = str(Result) #将计算结果转换成字符串
    args = Replaced.replace('temp',Result) #把计算出来的值替换回去
    args = remove_sub(args)
    return compute_and_sub(args) #递归依次重复处理

#计算乘除，从左往右一次只计算一个表达式如2*3，首先找到乘法或者除法的表达式用temp将其从原表达式中替换，然后把计算的结果再替换回去，一直到得到一个只剩加减法的表达式
def compute_mul_div(args):
    #FindOut = re.search('\d+\.?\d*[\/\*]\d+\.?\d*',args) #查找乘法或者除法,此处注意匹配小数点
    FindOut = re.search('\d+\.?\d*[\/\*][\+\-]{0,}\d+\.?\d*',args) #查找加法或者减法,此处注意匹配小数点

    if not FindOut:
        return args
    FindMulDiv = FindOut.group()
    Replaced  = args.replace(FindMulDiv,'temp') #用临时temp替换查找到的乘除表达式

    #GetInt = re.findall('\d+\.?\d*',FindMulDiv) #准备计算乘除法,取出乘除号左右两侧的数字
    GetInt = re.findall('[\+\-]{0,}\d+\.?\d*',FindMulDiv) #准备计算乘除法,取出乘除号左右两侧的数字
    GetLink = re.search('[\/\*]',FindMulDiv).group() #取出运算符号
    if GetLink == '/':
        Result  =  float(GetInt[0])/float(GetInt[1]) #计算除法
    if GetLink == '*':
        Result =  float(GetInt[0])*float(GetInt[1]) #计算乘法
    Result = str(Result) #将计算结果转换成字符串
    args = Replaced.replace('temp',Result) #把计算出来的值替换回去
    args = remove_sub(args)
    return compute_mul_div(args) #递归依次重复处理

#合并正负号
def remove_sub(args):
    args = args.replace('++','+')
    args = args.replace('+-','-')
    args = args.replace('--','+')
    args = args.replace('-+','-')
    return args

#除去小括号
def remove_brackets(args):
    args = remove_space(args)
    FindOut = re.search('\([^(]+[^)]\)',args)
    if not FindOut:
        return args
    FindBrackets = FindOut.group()
    Replaced  = args.replace(FindBrackets,'temp') #用临时temp替换查找到的括号表达式
    result1 = compute_mul_div(FindBrackets) #计算乘除
    result2 = compute_and_sub(result1) #计算加减
    result2 = result2.replace('(','')
    result2 = result2.replace(')','') #把结果里的小括号去掉
    args = Replaced.replace('temp',result2) #用计算结果替换之前替换的temp
    return remove_brackets(args)


def main(args):
    # #首先计算括号内的表达式
    r1 = remove_brackets(args)
    # #其次计算乘法和除法
    r2 = compute_mul_div(r1)
    # #合并正负号
    r3 = remove_sub(r2)
    # #计算加减
    r4 = compute_and_sub(r3)
    print('本次计算结果为：%s' %r4)

if __name__ == '__main__':
    expression = input('''\033[;35m++++++++++++++++++++++++++++++++++++++欢迎进入计算器系统++++++++++++++++++++++++++++++++++++++\033[0m
\033[;32m本计算器可以计算类似这样的格式，您可以直接copy此表达式计算：
'1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'\033[0m

\033[;31m请按照以上格式输入您的表达式：\033[0m
''')
    result = main(expression)
