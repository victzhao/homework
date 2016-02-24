


class common_role(object):
    def __init__(self,name,age,life,sex):
        self.name = name
        self.life = life
        self.age = age
        self.sex = sex


class monkey(common_role):
    def __init__(self,name,age,life,sex,jump):
        super(monkey,self).__init__(name,age,life,sex)
        self.jump = jump
