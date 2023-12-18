class C:
    shared_variable = None

    @classmethod
    def initialize(cls, a):
        if cls.shared_variable is None:
            print("Initializing class C...")
            cls.shared_variable = a


class A:
    def __init__(self):
        C.initialize(1)

    def do_something(self):
        print("Class A using shared variable:", C.shared_variable)


class B:
    def __init__(self):
        C.initialize(2)

    def do_something(self):
        print("Class B using shared variable:", C.shared_variable)

if __name__ == '__main__':

    # 测试类共享变量
    # 创建一个类A的对象并调用方法
    obj_a = A()
    obj_a.do_something()  # 输出: "Class A using shared variable: Shared Variable Value"

    # 创建一个类B的对象并调用方法
    obj_b = B()
    obj_b.do_something()

    # 我们定义了一个名为C的类，其中包含一个共享变量shared_variable。
    # 类C的方法initialize()用于初始化共享变量，并将其设置为某个值。
    # 在类A和类B中，我们在构造函数中调用了C的initialize()方法，这样在每个类的实例化过程中都会检查共享变量是否已经初始化。
    # 通过这种方式，我们可以实现只初始化一次类C，并且在类A和类B之间共享变量的目的。