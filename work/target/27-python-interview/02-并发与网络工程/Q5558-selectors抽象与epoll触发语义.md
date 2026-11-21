---
title: [Q5558] selectors 抽象与 epoll 水平/边沿触发语义
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5558 · selectors 抽象与 epoll 水平/边沿触发语义

> 难度:★★★★ | 标签:selectors, epoll, kqueue, 水平触发, 边沿触发

**问**：手写高性能代理时有人直接 `import epoll`，有人坚持 `selectors`。DefaultSelector 在各平台落到什么实现？水平触发和边沿触发的语义差异是什么？为什么 asyncio 默认选择水平触发？

**答**：`selectors` 是 Python 3.4 起的多路复用统一层：`DefaultSelector()` 按平台自动选最优实现——Linux 选 `EpollSelector`、macOS/BSD 选 `KqueueSelector`、Windows 选 `IocpSelector`（Proactor 语义）、都没有时退回 `SelectSelector`（select 的 1024 fd 限制）。统一 API：`register(fd, EVENT_READ|EVENT_WRITE, data)`、`select(timeout)` 返回 `(SelectorKey, events)`，data 可以直接挂回调/连接对象，业务代码零平台分支。触发语义是深水区：**水平触发（LT，epoll 默认）**——只要 fd 仍可读，每次 epoll_wait 都会再报，读不完下轮接着报，编程容错好；**边沿触发（ET，EPOLLET）**——只在状态**从不可读变可读**时报一次，必须循环 `recv` 直到 `BlockingIOError`（EAGAIN），漏读一次数据就永远挂在那。asyncio 的 selector 事件循环用 LT：省去"必须读尽"的心智负担，偶尔慢一点的唤醒容忍度换正确性；uvlib 级手写引擎才考虑 ET + 非阻塞读尽。直接用 `select.epoll` 的合理场景：需要 ET、需要 `epoll_ctl` 精细操作、或绑定特定内核特性——但要自己扛平台耦合与测试矩阵。教训句：**默认 selectors，证明 LT 是瓶颈再下沉**。

```python
# file: code/02_并发与网络工程/q5558_selectors.py
import os, selectors

r, w = os.pipe()

with selectors.DefaultSelector() as sel:
    sel.register(r, selectors.EVENT_READ, data="my-pipe")
    print("底层实现:", type(sel).__name__)   # mac=kqueue, linux=epoll, win=IOCP
    os.write(w, b"ping")
    for key, mask in sel.select(timeout=1.0):
        print("事件:", mask, "| data:", key.data, "| 内容:", os.read(key.fd, 16))
        # 水平触发: 若这里没读完, 下一轮 select 仍会再报

# 语义对照
print("水平触发 LT: fd 仍可读就每次都报, 漏读下轮补报")
print("边沿触发 ET: 仅状态跳变报一次, 必须循环读到 EAGAIN(BlockingIOError)")
print("asyncio 选 LT: 正确性优先; ET 只在自研引擎且能保证读尽时用")

# 混合就绪事件: 读写同时注册
with selectors.DefaultSelector() as sel:
    sel.register(r, selectors.EVENT_READ, "in")
    os.write(w, b"go")
    events = sel.select(timeout=0.5)
    print("select 返回 [(key, events)]:", [(k.data, ev) for k, ev in events])
```

**追问**：1) select/poll/epoll 的规模瓶颈差异？——select 每次传整个 fd 集合且有 1024 上限（FD_SETSIZE）、O(n) 扫描；poll 无 1024 限但仍 O(n) 拷贝；epoll 用红黑树注册 + 就绪链表，O(1) 注册、O(就绪数) 返回——万级以上连接只能 epoll/kqueue/IOCP。2) ET 模式下写事件怎么处理才不空转？——写缓冲通常永远可写，LT 会持续报写事件空转 CPU；正确做法是"有数据要发才注册 WRITE，发完立刻 unregister"（asyncio 的 Writer 就是这个策略）。3) `selectors` 的 `select()` 返回后 fd 被 close 了会怎样？——Key 对象仍有效但操作 fd 会 EBADF；框架要在回调里 try/except OSError 并 unregister，asyncio 内部就是这么兜的。

## 背诵要点
- `DefaultSelector()`：Linux=epoll、macOS/BSD=kqueue、Windows=IOCP、兜底 select（1024 fd 上限）；业务代码 register/select 零平台分支。
- 水平触发：可读就每次报、漏读下轮补报；边沿触发：只报状态跳变一次，必须循环读到 EAGAIN，漏读即悬挂。
- asyncio 用 LT 换正确性；写事件要"需发才注册、发完即注销"防空转；默认 selectors，证明瓶颈再下沉 epoll。

## 复盘追问
- 你们的高并发组件在哪一层做多路复用？有没有绕过 asyncio 自己写 epoll 的？（提示：盘点 import select.epoll / kqueue 的使用点，评估维护成本）
- 如果把服务迁到 epoll ET，哪些"读一半"的隐藏假设会爆？（提示：按 buffer 长度单次 recv、信任"select 返回即可一次读完"的代码全部要重审）
