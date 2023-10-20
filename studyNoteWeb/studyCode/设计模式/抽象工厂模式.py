'''
例：生产一部手机，需要手机壳、cpu、操作系统三类对象进行组装，其中每类对象都有不同的种类。
    对每个具体工厂，生产一部手机所需要的三个对象
'''

# 相对工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品

from abc import ABCMeta, abstractmethod

# 抽象产品
class PhoneShell(metaclass=ABCMeta):

    @abstractmethod
    def shows_hell(self):
        pass


class CPU(metaclass=ABCMeta):

    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):

    @abstractmethod
    def show_os(self):
        pass


# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

# 具体产品
class BigShell(PhoneShell):
    def shows_hell(self):
        pass


class SmallShell(PhoneShell):
    def shows_hell(self):
        pass


class AppleShell(PhoneShell):
    def shows_hell(self):
        pass


class SnapDragon(CPU):
    def show_cpu(self):
        pass


class MediaTek(CPU):
    def show_cpu(self):
        pass


class AppleCpu(CPU):
    def show_cpu(self):
        pass


class Android(OS):
    def show_os(self):
        pass

class IOS(OS):
    def show_os(self):
        pass


# 具体工厂
class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_os(self):
        pass

    def make_cpu(self):
        pass
