# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 16:13
# @Author  : Garnetsky
# @FileName: index.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

# 类默认由type创建
class Foo:
    def __init__(self):
        self.name = 666

    def func(self):
        self.name = 123
        return


def func(self):
    self.name = 123


fo = type('Foo', (object,), {"name": 666, "func": func})

a = Foo()
print(a.name, a.func(), a.name)
b = fo()
print(b.name, b.func(), b.name)


# 这两种声明累的方法都一样


# 元类声明类
class MyType(type):  # 继承type
    # 先执行new 再执行init

    def __new__(cls, *args, **kwargs):  # 默认有四个参数
        # 可扩建自己的功能
        new_cls = super().__new__(cls, *args, **kwargs)
        return new_cls

    # __call__ 方法用于对象呗调用时触发
    def __call__(self, *args, **kwargs):
        #1 调用__new__方法 去创建对象
        empty_object = self.__new__(self)
        # 2.调用__init__方法初始化对象
        self.__init__(empty_object, *args, **kwargs)
        print("被实例化")
        return empty_object



# 将类想成对象v将元类想成类即可
# Fo类是MyType的一个对象
class Fo(metaclass=MyType):  # 声明元类由MyType创建 metaclass=
    def __init__(self):
        self.name = 123


a = Fo()
