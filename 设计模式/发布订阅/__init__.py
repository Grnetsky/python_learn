# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 19:28
# @Author  : Garnetsky
# @FileName: __init__.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

from abc import ABCMeta, abstractmethod, ABC


# 被观察者基类
class Observer:
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, obj):
        for o in self.__observers:
            o.update(self, obj)


class Watcher(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observer, obj):
        pass


class Water(Observer):
    def __init__(self):
        super().__init__()
        self.temp = 25

    def setTemperature(self, temp):
        self.temp = temp
        self.notifyObservers(self.temp)


class Bath(Watcher, ABC):
    def __init__(self):
        super(Bath, self).__init__()
        self.defaultV = 25

    def update(self, observer, obj):
        if obj > self.defaultV:
            print("可以洗澡")
        else:
            print("再等会吧")


