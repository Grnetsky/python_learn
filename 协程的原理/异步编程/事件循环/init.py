# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 17:32
# @Author  : Garnetsky
# @FileName: __init__.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top


# 类似 js的事件循环
tasks = []
while 1:
    if len(tasks) == 0:
        break

