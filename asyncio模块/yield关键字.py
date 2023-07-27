# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 17:03
# @Author  : Garnetsky
# @FileName: yield关键字.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
def fun1():
    yield 1
    yield from fun2()
    yield 2

def fun2():
    yield 3
    yield 4

f1 = fun1()
for item in f1:
    print(item)