# -*- coding: utf-8 -*-
# @Time    : 2023/7/9 22:15
# @Author  : Garnetsky
# @FileName: __init__.py.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

#  中介模式：将原本分布于多个对象的行为集中在一起，作为一个独立的概念并将其封装在一个对象中，简化了对象之间的操作
# 举例 房东 中介 与租户

class Customer:
    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    # 查找房屋信息  要求  指定中介
    def findHouse(self,description,agency):
        return agency.getMatchInfos(description,self)

    def signContract(self,houseInfo,agency,houseown):
        print(self.getName(),"签订合同了，中介是",agency.getName(),"房东是：",houseown.getName())

class HouseInfo:
    def __init__(self,area,price,hasWindow,hasWc):
        self.__area = area
        self.__price = price
        self.__hasWindow = hasWindow
        self.hasWc = hasWc

