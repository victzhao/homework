#!/usr/bin/env python
# -*- coding:utf-8 -*-

from twisted.internet import reactor, protocol #导入模块


# a client protocol

class EchoClient(protocol.Protocol):#定义自定义类，继承protocol.Protocol
    """Once connected, send a message, then print the result."""

    def connectionMade(self): #连接一旦建立就执行该方法
        self.transport.write("hello alex!")#发送消息

    def dataReceived(self, data):#如果有数据收到，则调用该方法
        "As soon as any data is received, write it back."
        print "Server said:", data
        self.transport.loseConnection() #关闭连接

    def connectionLost(self, reason):#关闭异常连接时调用该方法
        print "connection lost"

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient #重写方法

    def clientConnectionFailed(self, connector, reason):#连接失败时候执行
        print "Connection failed - goodbye!"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()#创建客户端基类
    reactor.connectTCP("localhost", 1234, f)#连接server端，交给reactor
    reactor.run()#交给reactor运行

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()