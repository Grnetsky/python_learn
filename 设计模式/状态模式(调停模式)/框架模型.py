# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 00:20
# @Author  : Garnetsky
# @FileName: 框架模型.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

# 抽象层代码
from abc import abstractmethod, ABCMeta


class Context(metaclass=ABCMeta):
    def __init__(self):
        self.__states = []
        self.__curState = None
        self.__stateInfo = 0  # 状态变化依赖的属性

    def addState(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def removeState(self, state):
        if state in self.__states:
            self.__states.remove(state)

    def changeState(self, state):
        if state is None:
            return False
        if self.__curState is None:
            print("初始化状态为", state.getName())
        else:
            print("状态由", self.__curState.getName(), "变为", state.getName())
        self.__curState = state
        self.addState(state)

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def isMatch(self, stateInfo):
        pass

    @abstractmethod
    def behavior(self):
        pass


def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


class Water(Context):
    def __init__(self):
        super().__init__()
        self.addState(SolidState("固态"))
        self.addState(LiquidState("液态"))
        self.addState(GaseousState("气态"))
        self.setTemperature(25)

    def setTemperature(self, temp):
        self._setStateInfo(temp)

    def getTemperature(self):
        return self._getStateInfo()

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        self.getState().behavior()


@singleton
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return 0 < stateInfo < 100

    def behavior(self):
        print("液态的行为方法")


@singleton
class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo <= 0

    def behavior(self):
        print("固态的行为方法")


@singleton
class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self):
        print("气态的行为方法")


w = Water()
w.riseTemperature(100)
w.behavior()
w.reduceTemperature(80)
w.behavior()
w.reduceTemperature(50)
w.behavior()
