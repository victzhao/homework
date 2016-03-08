from bin import server
import sys


if  __name__ == "__main__":
    # server.start()
    try:
        sys.argv[1]
        if sys.argv[1] == 'start':
            #用反射获取方法名字
            print('start')
        elif sys.argv[1] == 'stop':
            #用反射获取方法名字
            print('stop')
    except IndexError as e:
        #提示用法
        print('参数错误')

