from abc import ABC, abstractmethod


class Order:
    def __init__(self, order_type, amount):
        self.order_type = order_type
        self.amount = amount


class OrderCalculator(ABC):
    @abstractmethod
    def calculate_total(self, order):
        pass


class RegularOrderCalculator(OrderCalculator):
    def calculate_total(self, order):
        return order.amount


class MemberOrderCalculator(OrderCalculator):
    def calculate_total(self, order):
        return order.amount * 0.9


class DiscountOrderCalculator(OrderCalculator):
    def calculate_total(self, order):
        return order.amount * 0.8


class OrderProcessor:
    def __init__(self, calculator):
        self.calculator = calculator

    def process_order(self, order):
        total = self.calculator.calculate_total(order)
        print(f"The total amount for the {order.order_type} order is: ${total}")


# 使用策略模式进行订单处理
order1 = Order("Regular", 100)
order2 = Order("Member", 100)
order3 = Order("Discount", 100)

regular_calculator = RegularOrderCalculator()
member_calculator = MemberOrderCalculator()
discount_calculator = DiscountOrderCalculator()

processor_regular = OrderProcessor(regular_calculator)
processor_member = OrderProcessor(member_calculator)
processor_discount = OrderProcessor(discount_calculator)

processor_regular.process_order(order1)
processor_member.process_order(order2)
processor_discount.process_order(order3)