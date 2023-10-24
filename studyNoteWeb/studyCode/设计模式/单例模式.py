from abc import ABCMeta


class Singleton(metaclass=ABCMeta):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, value):
        self.value = value


# client
a = MyClass(20)
b = MyClass(10)
print(a.value)
print(b.value)