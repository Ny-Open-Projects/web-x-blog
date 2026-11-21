---
title: [Q1586] add_reader / add_writer:fd 级事件回调
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1586 · add_reader / add_writer:fd 级事件回调

> 难度:★★★★ | 标签:事件循环, fd, 回调

**问**:不写协程,能不能直接用事件循环?add_reader 和 add_writer 的生命周期要注意什么?

**答**:能,事件循环的底座就是 fd 级回调:loop.add_reader(fd, cb) 在 fd 可读时于循环线程执行 cb,add_writer 同理管可写。两条纪律:回调必须是纯非阻塞的——send/recv 遇 BlockingIOError 直接返回,绝不 sleep;注册与注销必须配对——数据发完必须 remove_writer,否则选择器永远报告可写,回调空转烧满 CPU。还有一个 TCP 常识:三次 send 在对端被合并成一次 recv,fd 回调不保消息边界,协议要自己定义。另注意 Windows 的 Proactor 循环不支持 add_reader,跨平台要退回 selectors 或协程。

```python
# file: code/02_并发与网络工程/q1586_add_reader.py
"""add_reader / add_writer: 不写协程也能用事件循环。

事件循环的底座是 fd 级回调:
- add_reader(fd, cb): fd 可读时在循环线程里跑 cb;
- add_writer(fd, cb): fd 可写时跑 cb, 写完必须 remove_writer, 否则
  选择器持续报告可写 -> 回调空转烧 CPU;
- 回调必须是纯非阻塞的: send/recv 遇 BlockingIOError 直接返回。
"""
import asyncio
import socket
from collections import deque


async def main():
    loop = asyncio.get_running_loop()
    a, b = socket.socketpair()          # 本机双向管道, 当作最小"网络"
    a.setblocking(False)
    b.setblocking(False)

    outbox = deque([b"ping-1", b"ping-2", b"ping-3"])
    echoed = bytearray()
    expected = sum(len(x) for x in outbox)
    done = loop.create_future()

    def on_readable():
        try:
            data = b.recv(4096)
        except BlockingIOError:
            return
        if data:
            echoed.extend(data)         # 三次 send 可能被合并成一次 recv
            if len(echoed) >= expected:
                loop.remove_reader(b.fileno())
                if not done.done():
                    done.set_result(None)

    def on_writable():
        while outbox:
            try:
                sent = a.send(outbox[0])
            except BlockingIOError:
                return                  # 缓冲区满: 等下一轮可写
            if sent == len(outbox[0]):
                outbox.popleft()
            else:
                outbox[0] = outbox[0][sent:]
        loop.remove_writer(a.fileno())  # 发完注销, 防空转

    loop.add_reader(b.fileno(), on_readable)
    loop.add_writer(a.fileno(), on_writable)
    await asyncio.wait_for(done, timeout=3.0)
    loop.remove_reader(b.fileno())
    print("fd 回调累计收到:", bytes(echoed))
    assert bytes(echoed) == b"ping-1ping-2ping-3", "三条消息都应经回调送达"
    print("注意: 三次 send 在对端被合并成一次 recv——fd 回调不保消息边界")
    a.close()
    b.close()
    print("结论: 协程只是 fd 回调的糖; 回调注册/注销配对是 fd 级编程的生命线")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 回调里能直接改共享状态吗?——能,所有回调都跑在循环线程里,协程与回调之间天然无并发——这正是事件循环的安全模型。2) 「回调纯非阻塞」为什么是铁律?——回调跑在循环线程里,它阻塞=整个循环阻塞=所有连接卡死;BlockingIOError 是非阻塞 IO 的正常返回(EAGAIN),要当「暂无数据」处理而不是错误。3) 写事件的注册/注销节奏?——只在「有数据要发且上次没发完」时 add_writer,发完立即 remove_writer;一直注册会让 selector 每轮都报「可写」(socket 缓冲未满时几乎恒真),回调空转烧 CPU——这是 fd 级编程最经典的性能 bug。4) 生产陷阱?——回调里 sleep/阻塞调用;Windows Proactor 循环不支持 add_reader(跨平台分支);共享状态被回调与协程交叉修改时,误以为需要加锁(其实同线程,但跨 await 仍要防交错);remove_reader 时 fd 已关闭抛错(先 unregister 再 close,Q653)。

---
