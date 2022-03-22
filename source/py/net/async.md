# Python 协程与异步 IO

python 一直在进行并发编程的优化， 比较熟知的是使用 thread 模块多线程和 multiprocessing 多进程，后来慢慢引入基于 yield 关键字的协程。

对于 IO 密集型任务我们有一种选择就是协程。协程，又称微线程，英文名 Coroutine，是运行在单线程中的“并发”，协程相比多线程的一大优势就是省去了多线程之间的切换开销，获得了更高的运行效率。Python 中的异步 IO 模块 asyncio 就是基本的协程模块。

Python 中的协程经历了很长的一段发展历程。最初的生成器 yield 和 send() 语法，然后在Python3.4 中加入了 asyncio 模块，引入 @asyncio.coroutine 装饰器和 yield from 语法，在 Python3.5 上又提供了 async/await 语法，目前正式发布的 Python3.6 中 asynico 也由临时版改为了稳定版。

yield 是迭代器，yield + send 是协程。此时 yield 语句不再只是 yield xxxx 的形式，还可以是 var = yield xxxx 的赋值形式。它同时具备两个功能，一是暂停并返回函数，二是用 var 接收外部 send() 方法发送过来的值，重新激活函数。

## 协程

协程的切换不同于线程切换，是由程序自身控制的，没有切换的开销。协程不需要多线程的锁机制，因为都是在同一个线程中运行，所以没有同时访问数据的问题，执行效率比多线程高很多。

因为协程是单线程执行，那怎么利用多核 CPU 呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

进程/线程：操作系统提供的一种并发处理任务的能力。

协程：程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧。

多进程和多线程体现的是操作系统的能力，而协程体现的是程序员的流程控制能力。

因为 send() 方法的参数会成为暂停的 yield 表达式的值，所以，仅当协程处于暂停状态时才能调用 send() 方法，例如 my_coro.send(10)。不过，如果协程还没激活（状态是'GEN_CREATED'），就立即把 None 之外的值发给它，会出现 TypeError。因此，始终要先调用next(my_coro) 激活协程（也可以调用 my_coro.send(None)），这一过程被称作预激活。

## @asyncio.coroutine 与 yield from

`yield from range(10)` 等价于 `for i in range(10): yield i`

`yield from` 其实就是等待另外一个协程的返回

```python
import asyncio
import datetime

@asyncio.coroutine  # 声明一个协程
def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(2)  # 阻塞直到协程 sleep(2) 返回结果

loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]

loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的 tasks 完成
loop.close()
```

## async 和 await

**推荐使用** Python3.5 中对协程提供了更直接的支持，引入了 async/await 关键字。上面的代码可以这样改写：使用 async 代替@asyncio.coroutine，使用 await 代替 yield from，代码变得更加简洁可读。从 Python 设计的角度来说，async/await 让协程独立于生成器而存在，不再使用 yield 语法。

```python
import asyncio
import datetime

async def display_date(num, loop):      # 注意这一行的写法
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)  # 阻塞直到协程 sleep(2) 返回结果

loop = asyncio.get_event_loop()  # 获取一个 event_loop
tasks = [display_date(1, loop), display_date(2, loop)]

loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的 tasks 完成
```

## asyncio 模块

asyncio 的使用可分三步走

- 创建事件循环
- 指定循环模式并运行
- 关闭循环

通常我们使用 asyncio.get_event_loop() 方法创建一个循环。

运行循环有两种方法：一是调用 run_until_complete() 方法，二是调用 run_forever() 方法。run_until_complete() 内置 add_done_callback 回调函数，run_forever() 则可以自定义 add_done_callback()，具体差异请看下面两个例子。

使用 run_until_complete() 方法：

```python
import asyncio

async def func(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    print(loop.is_running())   # 查看当前状态时循环是否已经启动
    loop.run_until_complete(future)
    print(future.result())
    loop.close()
```

使用 run_forever() 方法：

```python
import asyncio

async def func(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def call_result(future):
    print(future.result())
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    future.add_done_callback(call_result)        # 注意这行
    try:
        loop.run_forever()
    finally:
        loop.close()
```

## 参考

[协程与异步 IO](https://www.liujiangblog.com/course/python/83)