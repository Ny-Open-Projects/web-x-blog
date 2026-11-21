---
title: [Q650] poll:无上限但仍是 O(n)
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q650 · poll:无上限但仍是 O(n)

> 难度:★★☆ | 标签:poll, 多路复用, 对比

**问**:poll 相比 select 改进了什么?API 上有什么不同?

**答**:poll 用 `[(fd, events)]` 结构体数组代替位图:不再受 FD_SETSIZE 限制(上限是系统内存),events/revents 分离让注册与结果同位;POLLHUP/POLLERR 无需注册自动上报。但根本瓶颈未变:每次 poll 调用仍传全量数组进内核、内核线性扫全部 fd,连接多而活跃少时依然浪费。API 习惯:register/unregister 语义要自己维护数组;`poll()` 只接受位置参数(timeout 毫秒),不能 `poll(timeout=500)` 关键字调用;跨平台注意 Windows 没有 poll(Windows 生态用 WSAPoll/select)。代码演示事件掩码注册、就绪处理与 POLLHUP。

```python
# file: code/02_并发与网络工程/q650_poll.py
import select
import socket
import time


def main() -> None:
    if not hasattr(select, "poll"):
        print("本平台无 select.poll (如 Windows), 概念见 select/kqueue 对应题")
        return

    a1, b1 = socket.socketpair()
    a2, b2 = socket.socketpair()
    b2.close()  # 模拟对端关闭 → POLLHUP

    p = select.poll()
    p.register(a1, select.POLLIN)          # 注册事件掩码
    p.register(a2, select.POLLIN)
    b1.send(b"poll-data")

    t0 = time.perf_counter()
    events = p.poll(500)                   # 位置参数: poll.poll() 不接受 kwargs
    dt = time.perf_counter() - t0
    print(f"就绪事件 ({dt * 1000:.1f}ms): {events}")
    for fd, ev in events:
        if ev & select.POLLIN:
            sock = {a1.fileno(): a1, a2.fileno(): a2}[fd]
            print(f"  fd={fd} POLLIN 数据: {sock.recv(64)!r}")
        if ev & select.POLLHUP:
            print(f"  fd={fd} POLLHUP 对端已关闭, 注销")
            p.unregister({a1.fileno(): a1, a2.fileno(): a2}[fd])

    # 修改注册: a1 改为监听可写
    p.modify(a1, select.POLLOUT)
    events = p.poll(100)                   # 位置参数, 同上
    print("修改后 events:", [(fd, hex(ev)) for fd, ev in events])
    p.unregister(a1)
    a1.close()
    a2.close()


if __name__ == "__main__":
    main()
```

**追问**:1) poll 的 events 和 revents 为什么分两个字段?——注册意图(events)与实际发生(revents)分离,revents 可以报告未注册的异常事件(POLLERR/POLLHUP/POLLNVAL),避免"没订阅错误就永远不知道出错"。2) poll 的 API 陷阱在哪?——poll() 只接受位置参数且 timeout 单位毫秒,poll(timeout=500) 是 TypeError;返回 (fd, revents) 列表要自己反查对象,selectors 层(Key 机制)帮你维护映射(Q653)。3) 为什么说 poll 只是「无上限的 select」?——每轮仍全量拷贝+内核 O(n) 扫描,改进只在容量(数组替代位图)与表达力(事件掩码、POLLHUP/POLLERR 自动上报);性能模型没变,上万连接还是要事件注册模型。4) 生产陷阱?——Windows 没有 poll(WSAPoll 历史行为差异多);POLLNVAL(无效 fd)不处理,fd 关闭后忘移除就每轮报错;把 revents 里的 POLLHUP/POLLERR 当普通可读处理导致死循环。

---
