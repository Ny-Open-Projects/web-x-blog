---
title: [Q579] 事件循环的 select 实现原理:手写迷你循环
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q579 · 事件循环的 select 实现原理:手写迷你循环

> 难度:★★★★ | 标签:事件循环, select, 原理

**问**:事件循环一轮到底做了什么?为什么 IO 多路复用能同时等几万个连接?

**答**:每轮迭代做三件事:计算最近的定时器到期时间作为 select 超时;调用 `selectors.select()` 阻塞等待 fd 就绪(没有定时任务且没有就绪 fd 时才真的阻塞);把就绪 fd 的回调、到点定时器、call_soon 队列的回调依次执行。select/epoll 的价值是把"等 N 个 fd"压缩成一次系统调用,内核负责睡眠与唤醒,Python 层只处理就绪的那几个,所以连接数增加不增加等待成本(epoll)。下面用 selectors + 定时器堆 + 生成器任务写一个 80 行的迷你循环,跑通"写 socket 的任务"和"等 socket 的任务"。

```python
# file: code/02_并发与网络工程/q579_mini_loop.py
import heapq
import selectors
import socket
import time
from collections import deque


class MiniLoop:
    def __init__(self) -> None:
        self._ready: deque = deque()
        self._timers = []  # 堆: (deadline, seq, task)
        self._seq = 0
        self._sel = selectors.DefaultSelector()
        self._fd_task = {}  # fd -> task

    def spawn(self, gen) -> None:
        self._ready.append({"gen": gen, "value": None})

    def sleep(self, delay: float):
        return ("sleep", delay)  # 生成器 yield 这个元组表示 trap

    def read(self, sock):
        return ("read", sock)

    def _step(self, task: dict) -> None:
        try:
            trap = task["gen"].send(task["value"])
        except StopIteration:
            return
        op = trap[0]
        if op == "sleep":
            self._seq += 1
            heapq.heappush(self._timers, (time.monotonic() + trap[1], self._seq, task))
        elif op == "read":
            sock = trap[1]
            sock.setblocking(False)
            self._sel.register(sock, selectors.EVENT_READ, task)
            self._fd_task[sock.fileno()] = sock

    def run(self) -> None:
        while self._ready or self._timers or self._fd_task:
            timeout = None
            if not self._ready:
                if self._timers:
                    timeout = max(0.0, self._timers[0][0] - time.monotonic())
                for key, _ in self._sel.select(timeout):
                    sock = self._fd_task.pop(key.fd)
                    self._sel.unregister(sock)
                    task = key.data
                    task["value"] = sock.recv(1024)  # 内核代劳读取后回传
                    self._ready.append(task)
            now = time.monotonic()
            while self._timers and self._timers[0][0] <= now:
                task = heapq.heappop(self._timers)[2]
                task["value"] = None
                self._ready.append(task)
            if self._ready:
                self._step(self._ready.popleft())
            elif self._timers:
                continue  # 没有就绪任务, 回去 select 等最近定时器


def producer(sock: socket.socket, loop: MiniLoop) -> None:
    for i in range(3):
        sock.sendall(f"msg{i} ".encode())
        yield loop.sleep(0.1)
    print("producer 结束")


def consumer(sock: socket.socket, loop: MiniLoop) -> None:
    got = b""
    for _ in range(3):
        chunk = yield loop.read(sock)  # 挂起等 fd 就绪, 恢复时拿到数据
        got += chunk
        print("consumer 收到:", chunk.decode())
    print("consumer 汇总:", got.decode())


if __name__ == "__main__":
    a, b = socket.socketpair()
    loop = MiniLoop()
    loop.spawn(consumer(b, loop))
    loop.spawn(producer(a, loop))
    t0 = time.perf_counter()
    loop.run()
    print(f"迷你事件循环跑完, 耗时 {time.perf_counter() - t0:.2f}s")
```

**追问**:1) epoll 相比 select 的两个关键改进是什么?——fd 集合放内核红黑树避免每次全量拷贝,就绪列表让返回值只含就绪 fd,把每轮 O(n) 降为 O(就绪数)。2) 迷你循环的核心结构?——selector.register(fd, EVENT, data) 注册;select(timeout) 取就绪;回调分发;data 携带 handler——这就是 selectors 模块封装的模型,asyncio 的 proactor/selector 事件循环同构。3) LT 与 ET 的区别?——level-triggered:就绪状态持续上报(默认,好写);edge-triggered:状态变化时一次(要一次读干净,配非阻塞);Python selectors 用 LT 简化。4) 生产陷阱?——阻塞 socket 混入循环卡死全部;注册后忘 unregister 泄漏;timeout=0 自旋烧 CPU。

---
