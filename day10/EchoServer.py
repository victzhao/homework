#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.internet import protocol  #导入twisted模块
from twisted.internet import reactor #导入twisted模块

class Echo(protocol.Protocol): #自定义echo类，次类中的内容是包含所有自己要执行的操作，并且该类一定要继承protocol.protocol
    def dataReceived(self, data):#data为收到的数据内容
        self.transport.write(data)#接收数据data

def main():
    factory = protocol.ServerFactory()#定义server工程，初始化实例
    factory.protocol = Echo #将上面定义的类赋值给factory.protocol，注册事件

    reactor.listenTCP(1234,factory)#监听服务，传入端口号和factory参数
    reactor.run()#触发事件，开始运行

if __name__ == '__main__':
    main()