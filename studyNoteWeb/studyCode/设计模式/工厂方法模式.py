from abc import ABCMeta, abstractmethod


# 抽象
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 实体1
class Alipay(Payment):
    def __init__(self, huabei=False):
        self.huabei = huabei

    def pay(self, money):
        if self.huabei:
            print('花呗支付%d' %money)
        else:
            print('支付宝支付%d缘' %money)


# 实体2
class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d缘' %money)


# 生成实体的工厂抽象
class PaymentFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_payment(self):
        pass


# 生成实体1的工厂
class AlipayPaymentFactory(PaymentFactory):

    def create_payment(self):
        return Alipay()


# 生成实体2的工厂
class WechatPaymentFactory(PaymentFactory):

    def create_payment(self):
        return WechatPay()


# 生成实体3的工厂
class HuabeiPaymentFactory(PaymentFactory):

    def create_payment(self):
        return Alipay(huabei=True)


# client
huabeipayment = HuabeiPaymentFactory()
huabei = huabeipayment.create_payment()
huabei.pay(10)

'''
优点：
    每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
    隐藏了对象实现细节
    
缺点：
    每增加一个具体产品类，就必须增加一个相应的具体工厂类
'''

