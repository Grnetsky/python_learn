# -*- coding: utf-8 -*-
# @Time    : 2023/7/9 22:45
# @Author  : Garnetsky
# @FileName: __init__.py.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

from abc import ABCMeta, abstractmethod, ABC


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def ware(self):
        print("着装")

    def say(self):
        print(123)


class Teacher(Person):
    def __init__(self, name, skill):
        super(Teacher, self).__init__(name)
        self.__skill = skill

    def getSkills(self):
        return self.__skill

    def ware(self):
        print("我是" + self.__skill)
        super(Teacher, self).ware()


class Engineer(Person):
    def __init__(self, name, skill):
        super(Engineer, self).__init__(name)
        self.__skill = skill

    def getSkills(self):
        return self.__skill

    def ware(self):
        print("我是" + self.__skill)
        super(Engineer, self).ware()


# 服装基类
class ClothingDecorator(Person):
    def __init__(self, person):
        self.__decorator = person

    def ware(self):
        self.__decorator.ware()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class XiuXianKu(ClothingDecorator):
    def __init__(self, person):
        super(XiuXianKu, self).__init__(person)

    def decorate(self):
        print("一条休闲裤")


class LiuZaiWaiTao(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件牛仔外套")


class DuanKu(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条短裤")


class ChenShan(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件衬衫")


Tony = Teacher("tony", "老师")
sy = ChenShan(Tony)
kz = DuanKu(sy)
kz.ware()

jane = Engineer("jane", "工程")
jane_sy = LiuZaiWaiTao(jane)
jane_kz = XiuXianKu(jane_sy)
jane_kz.ware()

"""
我是老师
着装
一件衬衫
一条短裤
我是工程
着装
一件牛仔外套
一条休闲裤
"""