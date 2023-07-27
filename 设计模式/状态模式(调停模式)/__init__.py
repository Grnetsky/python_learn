# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 22:42
# @Author  : Garnetsky
# @FileName: __init__.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

from abc import ABCMeta, abstractmethod


# 状态模式(调停模式) 是指一个对象拥有多个状态 首先有个基类 及 该对象的基本单元类 另一个是抽象出啦来的状态类，在不同状态下拥有不同的行为

class Water:
    def __init__(self, state):
        self.__temperature = 25  # 初始值设置为25摄氏度
        self.__state = state  # 初始化状态 为状态对象

    # 设置water的状态
    def setState(self, state):
        self.__state = state

    # 状态改变的触发函数
    def changeState(self, state):
        if self.__state:
            print("由", self.__state.getName(), "变为", state.getName())
        else:
            print("初始化为", state.getName())
        self.__state = state  # 更改状态

    # 温度提升函数
    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    # 温度下降函数
    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    # 执行不同状态下的行为
    def behavior(self):
        self.__state.behavior(self)

    # 设置温度 根据温度逻辑实时变换状态
    def setTemperature(self, temp):
        self.__temperature = temp
        if self.__temperature <= 0:
            self.changeState(SolidState("固态"))
        elif self.__temperature >= 100:
            self.changeState(GaseousState("气态"))
        else:
            self.changeState(LiquidState("液态"))

    def getTemperature(self):
        return self.__temperature


class State(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        pass


class SolidState(State):

    def __init__(self, name):
        # python3.5
        super().__init__(name)

    def behavior(self, water):
        print("这是固态冰的行为方法 当前温度", str(water.getTemperature()))


class LiquidState(State):

    def __init__(self, name):
        super(LiquidState, self).__init__(name)

    def behavior(self, water):
        print("这是液态水的行为方法，当前温度", str(water.getTemperature()))


class GaseousState(State):
    def __init__(self, name):
        super(GaseousState, self).__init__(name)

    def behavior(self, water):
        print("这是气态水的行为方法，当前温度", str(water.getTemperature()))


w = Water(LiquidState("液态"))
w.riseTemperature(100)
w.behavior()
w.reduceTemperature(80)
w.behavior()
w.reduceTemperature(50)
w.behavior()


# 核心思想为 同一个物体在不同状态下的行为模式不同
# 上述内容有个致命的问题 就是为了描述 水的状态 却要创建 5个类 （water 基类  state抽象类 solidwater liquidState gaseousState）
# 无疑增大了内存开销以及项目的复杂度 而在未来面对多个对象需要开发的时候 体积庞大到无法估计，另外 water的setTemperature方法不满足开放封闭原则
# 并且固态类只能拥有一个实例 应该采用单例模式构建为此完善此抽象层代码 抽象出状态模型


