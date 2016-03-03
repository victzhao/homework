


class common_role(object):
    def __init__(self,name,age,life):
        self.name = name
        self.life = life
        self.age = age


class monkey(common_role):
    def __init__(self,name,age,life,role):
        super(monkey,self).__init__(name,age,life)
        self.role = role
    def jump(self):
        print('一个跟头十万八千里！')

class zhu(common_role):
    def __init__(self,name,age,life,role):
        super(zhu,self).__init__(name,age,life)
        self.role = role
    def speaking(self):
        print('猴儿哥！')
class sha(common_role):
    def __init__(self,name,age,life,role):
        super(sha,self).__init__(name,age,life)
        self.role = role
    def talking(self):
        print('二师兄，师傅呢？')
class tang(common_role):
    def __init__(self,name,age,life,role):
        super(tang,self).__init__(name,age,life)
        self.role = role
    def read(self):
        print('善哉善哉！')
