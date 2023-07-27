# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 22:50
# @Author  : Garnetsky
# @FileName: __init__.py.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
# 单例模式 保证类只有一个实例，并且提供一个访问器去访问他的全局方法

# 实现方法一

class Singleton(object):
    # 类属性 python中实例可访问类属性
    __instance = None
    __first = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__first:
            self.name = name
            Singleton.__first = True


s1 = Singleton("ch")
s2 = Singleton('hc')

print(s1 is s2)


# True

## 实现方式二  元类限制

class Singleton2(type):  # 继承type 元类
    def __init__(cls, *args, **kwargs):
        super(Singleton2, cls).__init__(*args, **kwargs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class CustomClass(metaclass=Singleton2):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


s3 = CustomClass('bmy')
s4 = CustomClass('lb')

print(s3 is s4)  # True  is是判断地址是否一样  == 判断两对象属性是否一样


# 最优解
# 实现方式三 装饰器

def singletonDecorator(cls, *args, **kwargs):
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton


@singletonDecratore
class Singleton3:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


s5 = Singleton3('qq')
s6 = Singleton3('ww')

print(s5 is s6)  # True
