
'''
{"backend": "test.oldboy.org","record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}
{'backend': 'www.baidu.com', 'record': {'server': '1.1.1.1', 'maxconn': '200', 'weight': '100'}}
'''
import collections
import json
import sys
#查找记录，通过用户给出的backend域名来查看其所有的记录
def find(domain):
    FindOut = []
    with open('haproxy.conf','r') as read_file:
        card = False
        for line in read_file.readlines():
            line = line.strip('\n')
            if line == 'backend %s' %(domain):
                card = True
            if card and line:
                FindOut.append(line)
            if not card and line.startswith('backend'):
                card = False
    return FindOut
#添加记录
def add(info):
    print('add a recored')
def delete(info):
    print('del a recored')

def main():
    while True:
        print('''
    +++++++++++++++++欢迎进入运维配置管理系统+++++++++++++++++''')
        OptionNum = input('''                        1   查找记录
                        2   增加记录
                        3   删除记录
                        0   退出系统
请按照说明输入操作编号：''')
        if OptionNum == str(1):
            while True:
                BackendName = input('输入域名查询，或者q退出，b返回上级菜单:')
                if BackendName == 'b':
                    break
                elif BackendName == 'q':
                    print('退出系统！')
                    sys.exit(0)
                else:
                    result = find(BackendName)
                    if result:
                        print(result)
                        break
                    else:
                        print('您查找的记录为空,请重新输入！')
                        continue
            #打印出查找结果
        elif OptionNum == str(2):
            flag = True
            while flag:
                #UserInfo = json.loads(input('请输入您要增加的记录：'))
                UserInfo = input('请输入您要增加的记录：')
                try:
                    UserInfo = json.loads(UserInfo)
                except ValueError:
                    print("输入格式有误，请重新输入！")
                    continue
                else:
                    flag = False
            add(UserInfo)
        elif OptionNum == str(3):
            flag = True
            while flag:
                #UserInfo = json.loads(input('请输入您要增加的记录：'))
                UserInfo = input('请输入您要删除的记录：')
                try:
                    UserInfo = json.loads(UserInfo)
                except ValueError:
                    print("输入格式有误，请重新输入！")
                    continue
                else:
                    flag = False
            delete(UserInfo)
        elif OptionNum == str(0):
            print('退出系统！')
            sys.exit(0)

if __name__ == '__main__':
     main()













