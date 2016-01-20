'''
代码说明：
总体思路：
1. 查找记录，通过域名查找记录。
2. 修改记录：增加记录，删除记录
首先找到要修改的记录，循环文件把除了要修改的记录的内容全部写入新文件，然后再根据需求写要修改的记录（包括添加和删除）
'''
import collections
import json
import sys
import os
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
            if card and line.startswith('backend'):
                pass
    return FindOut
#添加记录
def add(info):
    add_domain = info['backend']
    add_record = info['record']
    add_record_strs  = '        server %s %s weitht %s maxconn %s' %(add_record['server'],add_record['server'],add_record['weight'],add_record['maxconn'])
    find_record = find(add_domain)
    if find_record:
        with open('haproxy.conf','r') as read_file,open('haproxy.conf.new','w') as write_file:
            card = False
            add_backend = 'backend %s' %(add_domain)
            for line in read_file:
                line = line.strip('\n') #去除换行符
                if add_backend == line: #找到backend修改标志位
                    card = True
                    continue #修改标志位后进行下一行的循环
                if card and line.startswith('backend'):#直到下一个backend记录为止，修改标志位
                    card = False
                if not card and 'backend %s' %(add_domain) != line:#所有标志位为False的行都写入新文件
                    write_file.write('%s\n' %(line))
            #下面开始写添加的记录，把原来的backend记录和新加的记转换成一个列表
            find_record.append(add_record_strs)
            for i in find_record:      #把需要添加的backend连同他的记录一起写进配置文件
                write_file.write('%s\n'%i)
        #删除原来的文件，重命名新文件
        os.remove('haproxy.conf')
        os.rename('haproxy.conf.new','haproxy.conf')
    else:#backend不存在，需要添加backend和所有记录
        with open('haproxy.conf','r') as read_file,open('haproxy.conf.new','w') as write_file:
            #先把原来的全部文件内容全部写入新文件
            for line in read_file:
                write_file.write(line)
            #开始写入新加的记录，把新加的记录转成一个列表
            add_list = ['backend %s' %(add_domain),add_record_strs]
            #把新加的记录写入到新文件中
            for line in add_list:
                write_file.write('%s\n' %(line))
        #删除原来的文件，重命名新文件
        os.remove('haproxy.conf')
        os.rename('haproxy.conf.new','haproxy.conf')
def delete(info):
    #提取删除的域名
    del_domain = info['backend']
    #提取删除的记录
    del_record = info['record']
    #把删除的记录转换成字符串
    del_record_strs  = '        server %s %s weitht %s maxconn %s' %(del_record['server'],del_record['server'],del_record['weight'],del_record['maxconn'])
    find_record = find(del_domain)
    #如果用户给出的记录存在先把除了要删除的backed内容外的内全部写入新文件
    if del_record_strs in find_record:
        with open('haproxy.conf','r') as read_file,open('haproxy.conf.new','w') as write_file:
            card = False
            add_backend = 'backend %s' %(del_domain)
            for line in read_file:
                line = line.strip('\n') #去除换行符
                if add_backend == line: #找到backend修改标志位
                    card = True
                    continue #修改标志位后进行下一行的循环
                if card and line.startswith('backend'):#直到下一个backend记录为止，修改标志位
                    card = False
                if not card and 'backend %s' %(del_domain) != line:#所有标志位为False的行都写入新文件
                    write_file.write('%s\n' %(line))
            #如果要删除的backend下面只有一个记录，则把记录和backend都删除，也就是不需要再写任何内容了。
            if len(find_record) <= 2:
                pass
            #若有一个以上记录，则只删除一个记录即可
            else:
                find_record.remove(del_record_strs)
                for line in find_record:
                    write_file.write('%s\n' %line)
        os.remove('haproxy.conf')
        os.rename('haproxy.conf.new','haproxy.conf')
    else:#如果要删除的backend不存在，给出用户提示
        print('您要删除的记录不存在，请重新输入！')
def main():
    while True:
        print('''\033[;32m
    +++++++++++++++++欢迎进入运维配置管理系统+++++++++++++++++''')
        OptionNum = input('''                    1       查找记录
                    2       增加记录
                    3       删除记录
                    0       退出系统
请按照说明输入操作编号：\033[0m''')
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
                        print('\033[41;33m您查找的记录如下：\033[0m')
                        for i in result:
                            print('\033[;35m%s\033[0m'%i)
                        break
                    else:
                        print(result)
                        print('您查找的记录为空,请重新输入！')
                        continue
            #打印出查找结果
        elif OptionNum == str(2):
            flag = True
            while flag:
                UserInfo = input('''{"backend": "test.oldboy.org","record":{"server": "2.2.2.2","weight": "20","maxconn": "300"}}
{"backend": "www.baidu.com","record": {"server": "1.1.1.1","weight": "20","maxconn": "200"}}
请严格按照如上格式输入您要增加的记录：''')
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
                UserInfo = input('''{"backend": "test.oldboy.org","record":{"server": "2.2.2.2","weight": "20","maxconn": "300"}}
{"backend": "www.baidu.com","record": {"server": "1.1.1.1","weight": "20","maxconn": "200"}}
请严格按照如上格式输入您要增加的记录：''')
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













