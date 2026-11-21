---
title: [Q651] epoll:红黑树、就绪链表与两种触发模式
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q651 · epoll:红黑树、就绪链表与两种触发模式

> 难度:★★★★ | 标签:epoll, LT ET, 多路复用

**问**:epoll 为什么能把每轮成本降到 O(就绪数)?LT 和 ET 的区别在工程上意味着什么?

**答**:epoll 把"注册"与"等待"分离:epoll_create 建实例,epoll_ctl 把 fd 挂进内核红黑树(注册一次,非每轮重传);fd 就绪时内核回调把它挂入就绪链表,epoll_wait 只返回就绪列表——O(就绪数),且省掉每轮全量拷贝。触发模式:LT(水平,默认)只要缓冲区还有数据每次 wait 都报,编程简单不易漏;ET(边缘)仅在状态变化时报一次,必须一次读到 EAGAIN,否则事件丢失,配合非阻塞 fd 使用。Nginx 常用 ET 追求极致;Redis 的 epoll 后端使用 LT(`ae_epoll.c` 从不设置 `EPOLLET`)。ET 需显式设置且必须配非阻塞 fd 一次读到 EAGAIN,并非性能默认项,大多数应用 LT 足够。

```python
# file: code/02_并发与网络工程/q651_epoll.py
import select
import socket
import time


def main() -> None:
    if not hasattr(select, "epoll"):
        print("epoll 仅 Linux 可用; 在 macOS 上用 selectors 层演示 LT 语义")
        demo_level_trigger()
        return

    ep = select.epoll()
    a, b = socket.socketpair()
    a.setblocking(False)
    ep.register(a, select.EPOLLIN)  # 注册一次, 挂入红黑树

    b.send(b"chunk-1")
    print("LT 模式: 写入一次, 连续两次 wait")
    for i in range(2):
        events = ep.poll(timeout=0.5)
        print(f"  第{i + 1}次 wait: fd 就绪 {[fd for fd, ev in events]} (LT: 未读完一直报)")
    data = a.recv(1024)
    print("  读出:", data)
    events = ep.poll(timeout=0.1)
    print(f"  读空后再 wait: {events} (无数据不再报)")

    b.send(b"chunk-2")
    ep.poll(timeout=0.5)
    a.recv(1024)
    ep.unregister(a)
    ep.close()
    a.close()
    b.close()


def demo_level_trigger() -> None:
    sel = select.select  # 用 select 近似演示"水平触发"语义
    a, b = socket.socketpair()
    a.setblocking(False)
    b.send(b"data")
    for i in range(2):
        r, _, _ = sel([a], [], [], 0.2)
        print(f"LT 语义 第{i + 1}次: 就绪={bool(r)} (未读取就持续就绪)")
    a.recv(64)
    r, _, _ = sel([a], [], [], 0.1)
    print(f"读空后: 就绪={bool(r)}")
    a.close()
    b.close()


if __name__ == "__main__":
    main()
```

**追问**:1) ET 模式下漏读会怎样?——该 fd 永远不再被报告,连接假死;所以 ET 必须循环 recv 直到 EAGAIN,并且 accept 循环同理,这是 ET 编程复杂度的来源。2) 红黑树+就绪链表怎么把成本降到 O(就绪数)?——epoll_ctl 注册进内核红黑树(一次,非每轮重传);fd 就绪时回调把节点挂入就绪链表,epoll_wait 只遍历链表;省掉 select/poll 的每轮全量拷贝与全量扫描,「注册与等待分离」是结构性收益。3) LT 与 ET 的编程模型差异?——LT(默认)缓冲还有数据就每轮都报,可以读一点下次再读;ET 只在状态变化时报一次,必须循环读到 EAGAIN,漏读=该 fd 永不再报=连接假死,所以 ET 强制配非阻塞 fd 并循环 accept。4) 生产陷阱?——手写 ET 忘循环 recv/accept;LT 下应用读不动导致同一 fd 疯狂返回(要配合读上限或暂停订阅);把「换 epoll」当万能优化——连接少且活跃高时差异可忽略,瓶颈常在应用层。

---
