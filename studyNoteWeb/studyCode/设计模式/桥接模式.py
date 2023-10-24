# 定义实现部分的接口
class TVImpl:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def set_channel(self, channel):
        pass

# 具体的实现类A
class TVA(TVImpl):
    def power_on(self):
        print("TV A power on")

    def power_off(self):
        print("TV A power off")

    def set_channel(self, channel):
        print(f"TV A set channel to {channel}")

# 具体的实现类B
class TVB(TVImpl):
    def power_on(self):
        print("TV B power on")

    def power_off(self):
        print("TV B power off")

    def set_channel(self, channel):
        print(f"TV B set channel to {channel}")

# 定义抽象部分的接口
class RemoteControl:
    def __init__(self, tv_impl):
        self.tv_impl = tv_impl

    def power_on(self):
        self.tv_impl.power_on()

    def power_off(self):
        self.tv_impl.power_off()

    def set_channel(self, channel):
        self.tv_impl.set_channel(channel)

# 实现类A的遥控器
class RemoteControlA(RemoteControl):
    pass

# 实现类B的遥控器
class RemoteControlB(RemoteControl):
    pass

# 使用桥接模式
tv_a = TVA()
tv_b = TVB()

remote_a = RemoteControlA(tv_a)
remote_b = RemoteControlB(tv_b)

remote_a.power_on()  # 输出: TV A power on
remote_a.set_channel(5)  # 输出: TV A set channel to 5
remote_a.power_off()  # 输出: TV A power off

remote_b.power_on()  # 输出: TV B power on
remote_b.set_channel(7)  # 输出: TV B set channel to 7
remote_b.power_off()  # 输出: TV B power off