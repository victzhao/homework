from conf import setting
from logs import log
import json
class user_handle():
    def __init__(self,name, passwd,quotation):
        self.name = name
        self.passwd = passwd
        self.quotation = quotation
    def add_user(self):

        user_info = {self.name: {'passwd': self.passwd,
                                'quota': self.quotation, }
                     }
        user_i = json.dumps(user_info)
        with open('user/user_info.db','a') as user_file:
            user_file.write('%s\n' %user_i)
        msg = '创建用户%s成功 ' %(self.name)
        logs =  log.logger()
        logs.info(msg)

    def del_name(self):
        user_dic = json.loads('user/user_info.db')
        while True:
            if self.name not in user_dic.keys():
                print('用户名不存在！')




