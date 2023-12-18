# 给子系统中的一组接口，提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一自己系统更加容易使用


# 子系统类
class CPU:
    def run(self):
        print('CPU开始运行')

    def stop(self):
        print('CPU停止运行')


# 子系统类
class Disk:
    def run(self):
        print('Disk开始运行')

    def stop(self):
        print('Disk停止运行')


# 子系统类
class Memory:
    def run(self):
        print('Memory开始运行')

    def stop(self):
        print('Memory停止运行')


# 外观
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = Disk()

    def run(self):
        # 可以调整规定子系统的运行顺序
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# client
obj = Computer()
obj.run()
obj.stop()


# 不让用户类直接调用子系统的方法，而是通过外观来调用
# 缩小底层代码和高层代码的耦合
