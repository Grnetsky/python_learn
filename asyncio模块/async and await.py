# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 17:18
# @Author  : Garnetsky
# @FileName: async and await.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

# 与
import asyncio


async def fun1():
    print(1)
    await asyncio.sleep(2)  # 遇到IO耗时操作 自动切换到tasks中的其他任务
    print(2)


async def fun2():
    print(3)
    await asyncio.sleep(2)  # 遇到IO耗时操作 自动切换到tasks中的其他任务
    print(4)


# 定义任务列表


# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# py3.7
async def main():
    tasks = [
        asyncio.create_task(fun1()),  # asyncio.create_task 将任务添加到事件循环
        asyncio.create_task(fun2())
    ]
    done, pending = await asyncio.wait(tasks,timeout=2)
    print(done)
if __name__ == '__main__':
    asyncio.run(main())
