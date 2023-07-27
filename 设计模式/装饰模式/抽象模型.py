# -*- coding: utf-8 -*-
# @Time    : 2023/7/9 23:34
# @Author  : Garnetsky
# @FileName: 抽象模型.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

# python 内部提供了装饰器模式

def decorator(func):
    def warpFunc(*args, **kwargs):
        print("这在执行前进行操作")
        func(*args, **kwargs)
        print("这在执行后进行操作")

    return warpFunc

@decorator
def func(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


# 不用装饰器版本
# decoratorFunc = decorator(func)
# decoratorFunc("jane", 18, 180, weight=300, speak="chinese")

# 用装饰器版本
func("jane", 18, 180, weight=300, speak="chinese")

# 装饰器 带参数 与 不带参数
pass
