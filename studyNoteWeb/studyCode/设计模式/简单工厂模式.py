from abc import ABCMeta, abstractmethod


# 抽象
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 实体1
class Alipay(Payment):
    def pay(self, money):
        print('支付宝支付%d缘' %money)


# 实体2
class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d缘' %money)


# 生成实体的工厂
class PaymentFactory:
    @classmethod
    def create_payment(cls, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        else:
            raise TypeError("No such payment method")


# client
payment= PaymentFactory().create_payment('alipay')
payment.pay(10)


'''
优点：
    隐藏了对象创建的实现细节
    客户端不需要修改代码
    
缺点：
    违反了单一职责原则，将创建逻辑集中到一个工厂类里
    当添加新产品类时，需要修改工厂类代码，违反了开闭原则
思考：
    那就是说，工厂方法，如果要添加新的产品类，只需要添加一个工厂类而不是修改工厂类，就没有违反开闭原则？
'''

