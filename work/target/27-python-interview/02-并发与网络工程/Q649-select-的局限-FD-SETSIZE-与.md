---
title: [Q649] select 的局限:FD_SETSIZE 与 O(n) 扫描
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q649 · select 的局限:FD_SETSIZE 与 O(n) 扫描

> 难度:★★★☆ | 标签:select, 多路复用, 复杂度

**问**:select 管理几千个连接时瓶颈在哪?为什么它每轮都慢?

**答**:两个硬伤:1) FD_SETSIZE(通常 1024)是 fd 编号上限,不是连接上限,超限直接失控;2) 每次调用要把整个 fd_set 从用户态拷到内核,内核线性扫描所有 fd,返回后用户态还要再线性遍历找就绪项——成本 O(n) 且与"就绪数"无关,1 万连接只有 10 个活跃时,9990 次检查全是浪费。结果就是活跃比例低的场景 select 延迟随连接数线性恶化。实验:注册不同数量的 fd 但只唤醒一个,对比 select 耗时随 n 的增长曲线。

```python
# file: code/02_并发与网络工程/q649_select_scale.py
import resource
import select
import socket
import time


def raise_limit() -> None:
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft < hard:
        try:
            resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        except (ValueError, PermissionError):
            pass


def bench(n_pairs: int) -> float:
    """n 个 fd 只有 1 个就绪, 测 select 单轮耗时。"""
    pairs = [socket.socketpair() for _ in range(n_pairs)]
    readers = [a for a, _ in pairs]
    writers = [b for _, b in pairs]
    writers[-1].send(b"x")  # 只唤醒最后一个

    rounds = 50
    t0 = time.perf_counter()
    for _ in range(rounds):
        r, _, _ = select.select(readers, [], [], 0)
        assert r
        r[0].recv(1)          # 消费数据
        writers[-1].send(b"x")  # 补上, 保持每轮都有就绪
    dt = (time.perf_counter() - t0) / rounds
    for a, b in pairs:
        a.close()
        b.close()
    return dt


if __name__ == "__main__":
    raise_limit()
    soft, _hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print(f"当前 fd 软限: {soft}")
    for n in (10, 50, 100, 200):
        max_pairs = min(n, soft // 2 - 16)
        if max_pairs < n:
            print(f"  n={n}: 受 fd 限制仅测 {max_pairs}")
            n = max_pairs
        dt = bench(n)
        print(f"  {n:>4} 个 fd, 1 个就绪: select 单轮 {dt * 1e6:7.1f} µs")
    print("扫描成本随 fd 数线性增长 — 这就是 select 的 O(n)")
```

**追问**:1) 那 poll 解决了什么、没解决什么?——poll 用 pollfd 数组取消 FD_SETSIZE 上限、支持事件掩码,但每轮仍要全量拷贝与 O(n) 扫描;真正的飞跃是 epoll/kqueue 的事件注册模型。2) FD_SETSIZE 限制的是什么?——fd_set 位图的位数(C 层通常 1024),限制的是 fd 编号上限不是连接数;编号超限 Python 抛 ValueError;把监听 fd 占住低位也无济于事,超规模必须换 poll/epoll。3) 为什么每轮成本与活跃数无关?——三次全量:构造 fd_set 拷入内核、内核线性扫描全部 fd、返回后用户态再线性找就绪项;1 万连接活跃 10 个时 9990 次检查全浪费——「注册一次、只返回就绪」的 epoll 就是为这个结构性浪费设计的(Q651)。4) 生产陷阱?——连接数逼近 1024 才发现上限(监控要盯最大 fd 编号);复用 fd_set 没每次重建,残留旧注册产生幽灵事件;select 的 timeout 单位是秒(浮点),与 poll 的毫秒混用。

---
