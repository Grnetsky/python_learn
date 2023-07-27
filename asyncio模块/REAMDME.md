# 协程（微线程 用户态上下文切换技术）
计算机中不存在 操作系统之提供进程和线程 是由程序员认为创造出来的
通过一个线程实现代码块中的互相切换

# 如何实现协程？
* greenlet 早期模块
* yield关键字
* asyncio 模块  python3.4引入  
* async、await python3.5

# greenlet实现协程
