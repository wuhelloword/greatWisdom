# 定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。观察者模式又称发布-订阅模式

from abc import ABCMeta, abstractmethod


# 订阅者抽象
class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, notice):
        pass


# 发布者抽象
class Notice:
    """发布者"""
    def __init__(self):
        self.objserve = []      # 订阅者列表

    def attach(self, obs):
        # 订阅
        self.objserve.append(obs)
        pass

    def detach(self, obs):
        # 取消订阅
        self.objserve.remove(obs)

    def notify(self):
        for i in self.objserve:
            i.update(self)


# 发布者具体
class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, company_info):
        self.__company_info = company_info
        self.notify()


# 订阅者具体
class Staff(Observer):
    def __init__(self):
        self.company_info = None

        self.notice_list = []

    def update(self, notice):
        self.company_info = notice.company_info


# 客户端代码
n = StaffNotice()
n.company_info = 'foxconn'
s = Staff()

# 一开始是没有company info的
print(s.company_info)

# 订阅者手动更新后，company info同发布者一致
s.update(n)
print(s.company_info)

# 发布者更新company info，订阅者不会自动更新
n.company_info = 'new foxconn'
print(s.company_info)

# 发布者里有订阅者关注后，发布者更新company info，订阅者自动更新
n.attach(s)
n.company_info = 'new new foxconn '
print(s.company_info)
