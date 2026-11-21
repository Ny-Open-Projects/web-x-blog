---
title: [Q1849] 对象池的空闲驱逐与健康探活:TTL 管浪费 validator 管腐化
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1849 · 对象池的空闲驱逐与健康探活:TTL 管浪费 validator 管腐化

> 难度:★★★ | 标签:对象池, 健康检查, 后台回收

**问**:池里的对象长期借不出去会怎样?借出去才发现是死连接怎么办?

**答**:两个卫生机制分别管两种腐化:空闲驱逐管 '浪费'——守护线程周期扫描,空闲超过 TTL 的对象调 closer 销毁,把内存和连接额度还给系统;健康探活管 '腐烂'——borrow 时先跑 validator,坏对象直接丢弃重建,绝不递给调用方。

- 借出的对象不受 TTL 影响,驱逐只清 idle 队列,否则会把正在用的资源抢走;

- validator 失败要继续找下一个或现场新建,不能把坏对象还回去让调用方踩雷;

- 演示里 conn-1 空闲超时被 reaper 销毁,conn-2 被手动弄坏后在借出前被探活拦下,工厂累计三次调用,借出方每次都拿到活对象。

数据库连接池的 idle timeout 与 test-on-borrow 正是这两个机制的工业版本。

```python
# file: code/02_并发与网络工程/q1849_pool_idle_evict.py
# -*- coding: utf-8 -*-
"""对象池的空闲驱逐与健康探活: 借出前校验, 空闲超时回收。

- reaper 守护线程周期扫描空闲对象, 超过 TTL 的视为闲置浪费, 调 closer 销毁;
- borrow 时跑 validator 探活: 坏对象直接丢弃重建, 绝不把死连接递给调用方;
- 驱逐与探活是池的两个独立卫生机制: 一个管浪费, 一个管腐烂。
"""
import threading
import time


class Conn:
    _seq = 0

    def __init__(self):
        Conn._seq += 1
        self.cid = "conn-%d" % Conn._seq
        self.alive = True


class HealthPool:
    def __init__(self, size, ttl=0.3):
        self._size = size
        self._ttl = ttl
        self._cond = threading.Condition()
        self._idle = []                       # [(conn, since)]
        self._in_use = set()
        self._factory_calls = 0
        self.idle_evicted = []
        self.sick_dropped = []
        self.destroyed = []

    def _factory(self):
        self._factory_calls += 1
        return Conn()

    def _destroy(self, conn, reason):
        conn.alive = False
        self.destroyed.append((conn.cid, reason))

    def borrow(self, timeout=2.0):
        with self._cond:
            deadline = time.monotonic() + timeout
            while True:
                if self._idle:
                    conn, _ = self._idle.pop(0)
                    if conn.alive:            # 借出前探活
                        self._in_use.add(conn.cid)
                        return conn
                    self.sick_dropped.append(conn.cid)
                    continue                  # 坏的丢弃, 继续找/建
                if len(self._in_use) + len(self._idle) < self._size:
                    conn = self._factory()
                    self._in_use.add(conn.cid)
                    return conn
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("池已耗尽且等待超时")
                self._cond.wait(remain)

    def give_back(self, conn):
        with self._cond:
            if conn.cid not in self._in_use:
                raise ValueError("非法归还")
            self._in_use.discard(conn.cid)
            self._idle.append((conn, time.monotonic()))
            self._cond.notify()

    def reap_loop(self):
        while True:
            time.sleep(0.05)
            now = time.monotonic()
            with self._cond:
                keep = []
                for conn, since in self._idle:
                    if now - since > self._ttl:
                        self.idle_evicted.append(conn.cid)
                        self._destroy(conn, "idle-ttl")
                    else:
                        keep.append((conn, since))
                self._idle = keep


def main():
    pool = HealthPool(size=2, ttl=0.3)
    threading.Thread(target=pool.reap_loop, daemon=True).start()

    c1 = pool.borrow()
    print("第一次借出:", c1.cid)
    time.sleep(0.5)                            # 借出的对象不受 TTL 影响
    pool.give_back(c1)
    time.sleep(0.5)                            # 空闲超过 TTL, reaper 驱逐
    assert c1.alive is False, "空闲超时对象应被销毁"
    assert len(pool.idle_evicted) == 1, "reaper 应驱逐一个空闲对象"
    print("reaper 驱逐记录:", pool.destroyed)

    c2 = pool.borrow()                         # 池空了, 现场新建
    c2.alive = False                           # 手动弄坏: 模拟连接腐化
    pool.give_back(c2)
    c3 = pool.borrow()                         # 探活发现坏的, 丢弃重建
    print("坏对象处理:", pool.sick_dropped, "新借出的健康对象:", c3.cid)
    assert c3.alive, "借出的一定是探活通过的对象"
    assert len(pool.sick_dropped) == 1, "腐化对象应被丢弃"

    print("工厂累计调用:", pool._factory_calls, "销毁记录:", pool.destroyed)
    assert pool._factory_calls == 3, "驱逐一个重建一个, 工厂共三次"
    print("结论: TTL 管闲置浪费, validator 管腐化, 借出前最后一道闸")


if __name__ == "__main__":
    main()
```

**追问**:1) 驱逐线程销毁对象时,它会不会正被别人归还?——要在同一把池锁内完成扫描与摘除,归还方也走同一把锁;真正的竞态窗口在于对象 '刚被归还还未入册' 的瞬间,用统一的锁临界区就能闭合。2) 「借出的对象不受 TTL 影响」为什么必须?——reaper 若扫到借出对象并销毁,持有者会拿到悬空资源(使用中崩溃);驱逐只作用于 idle 队列,这条边界与租约回收(Q1571)的「只回收泄漏槽」是同一原则:回收范围必须精确。3) validator 的成本怎么控制?——探活有成本(ping 一次),折中是「空闲超过 X 秒才探」(Q1332);validator 要短(单次往返,不做业务校验);失败的对象销毁计数与重建计数要分别统计,腐化率是容量与健康度的输入。4) 生产陷阱?——reaper 与归还并发摘除无锁(竞态,见原问);validator 抛异常被吞(坏对象仍被借出);TTL 太短(对象反复销毁重建,工厂成为热点);驱逐只减不增计数,池容量账不平;借出方持有期间对象被 reaper 误销(范围泄漏)。


---
