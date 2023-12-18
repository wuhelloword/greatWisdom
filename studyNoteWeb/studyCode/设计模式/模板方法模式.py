# 蛋糕五花八门，不变的有两种东西：奶油和面包。其余材料随意搭配，就凑成了各式各样的蛋糕

from abc import ABCMeta, abstractmethod

class Cake(metaclass=ABCMeta):

    def make(self):
        print('开始准备材料')
        self.bread()
        self.cream()
        self.other()
        print('制作完成')


    def bread(self):
        pass

    def cream(self):
        pass

    @abstractmethod
    def other(self):
        pass


class StrawberryCake(Cake):
    def other(self):
        print('加 strawberry')


class CherryCake(Cake):
    def other(self):
        print('加 Chery')


# client
cherry = CherryCake()
cherry.make()
starwberry = StrawberryCake()
starwberry.make()


# 在父类中定义了需要实现的步骤，将共用的方法抽取到父类中，将个性化的方法放到具体的子类中取实现。
# 也就是将公用的方法提取到父类，在父类中预留可变的方法，最后子类去实现可变的方法
