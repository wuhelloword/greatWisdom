# 适用于抽象物体组成的树形结构的情况，例如，目录和文件、公司组织结构、菜单和菜单项

# 情景：处理一个公司组织结构，公司由多个部门组成，而部门又由员工和下属部门组成。


from abc import ABCMeta, abstractmethod


# 抽象组件类
class Component(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass


# 定义具体组合对象，包含子节点的Component对象
class Department(Component):

    def __init__(self, name):
        self.name = name
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def show(self):
        print(self.name)
        for child in self._children:
            child.show()


# 叶子节点
class Employee(Component):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


# 创建组织架构
dept1 = Department("data")
dept1.add(Employee("风光好"))
dept2 = Department("web")
dept2.add(Employee("小口天"))
emp = Department("foxconn")
emp.add(dept1)
emp.add(dept2)

emp.show()


# 叶子节点和组合节点都继承的Component，在客户端代码里，不需要考虑是处理单个对象还是组合对象，都可以以相同的方式处理
