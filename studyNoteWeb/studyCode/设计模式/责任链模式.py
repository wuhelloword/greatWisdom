# 情景：员工需要请假，请3天内项目主管批假，5天内部门经理批假，10天内总经理批假，形成一个链结构

from abc import ABCMeta, abstractmethod


# 抽象处理者
class Handler(metaclass=ABCMeta):

    @abstractmethod
    def handle_leave(self,day):
        pass


# 具体处理者 链3
class GeneralManager(Handler):

    def handle_leave(self,day):
        if day <= 10:
            print('总经理请假')
        else:
            print('无法批假')


# 具体处理者 链2
class DepartmentManager(Handler):

    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self,day):
        if day <= 5:
            print('部门经理准假')
        else:
            self.next.handle_leave(day)


# 具体处理者 链1
class ProjectDirector(Handler):

    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管准假")
        else:
            self.next.handle_leave(day)


# 高层代码 client
day = 4
h = ProjectDirector()
h.handle_leave(day)

'''
适用场景：
    有多个对象可以处理一个请求，哪个对象处理由运行时决定
    在不明确接受者的情况下，向多个对象的一个提交一个请求
    
优点：
    降低耦合度：一个对象无需知道是其他哪个对象处理其请求
'''

