# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 17:07
# @Author  : Garnetsky
# @FileName: asyncio模块.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import asyncio


@asyncio.coroutine
def fun1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作 自动切换到tasks中的其他任务
    print(2)


@asyncio.coroutine
def fun2():
    print(3)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作 自动切换到tasks中的其他任务
    print(4)


# 定义任务列表
tasks = [
    asyncio.ensure_future(fun1()),
    asyncio.ensure_future(fun2())
]

loop = asyncio.get_event_loop()  # 生成或者获取一个事件循环
loop.run_until_complete(asyncio.wait(tasks))  # 将任务放到任务列表
