# 对于一个文件，操作有查看内容，修改内容的情况下
'''
代理模式有三种类型：
    远程代理（需要远程服务器，这里没有例子）
    虚代理
    保护代理
'''

from abc import ABCMeta, abstractmethod


# 抽象实体
class Subject(metaclass=ABCMeta):
    """"
    实体和代理都继承的接口，这样可以让高层代码统一的调用代理，而不用区分实体和代理
    """
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')   # 文件如果有中文，需要加编码
        self.conten = f.read()
        f.close()

    def get_content(self):
        return self.conten

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


# 虚代理
class VirtualProxy(Subject):
    '''
    如果具体文件很大，在创建文件对象的时候，就直接读文件的全部内容，导致内存浪费
    虚代理实现，只有在具体获取文件内容的时候，才对文件内容进行打开读取
    '''
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


# 保护代理
class ProtectedProxy(Subject):
    '''
    当只有读权限，没有写权限时
    '''

    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise "没有写权限"


# 高层代码 client
subj = VirtualProxy('test.txt')
print(subj.get_content())

subj = ProtectedProxy('test.txt')
print(subj.get_content())
print(subj.set_content('test set'))

'''
内容： 为其他对象提供一种代理以控制对这个对象的访问
优点：
    远程代理：可以隐藏对象位于远程地址空间的事实
    虚代理：可以进行优化，例如根据要求创建对象
    保护代理：允许在访问一个对象时有一些附加的内务处理    
'''