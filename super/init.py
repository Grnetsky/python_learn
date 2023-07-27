# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 19:59
# @Author  : Garnetsky
# @FileName: __init__.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

# MRO 每个类会把自己和父类做个排序 广度优先  mro使用的c3算法
# 获取 类.mro()
# super在python中只是个普通函数
class Animal(object):
    def __init__(self,weight):
        self.weight = weight

class Person(Animal):
    def __init__(self,weight,name):
        super().__init__(weight)
        self.name = name

class Male(Person):
    def __init__(self,weight,name,age):
        # super().__init()
        super(Male, self).__init__(weight,name)
        self.age = age


p = Male(100,"小明", 20)
print()

