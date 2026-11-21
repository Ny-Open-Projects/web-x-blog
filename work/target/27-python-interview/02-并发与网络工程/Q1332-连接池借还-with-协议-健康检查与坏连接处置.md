---
title: [Q1332] 连接池借还:with 协议、健康检查与坏连接处置
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1332 · 连接池借还:with 协议、健康检查与坏连接处置

> 难度:★★★☆ | 标签:连接池, 上下文管理器, 健康检查

**问**:手写一个连接池,借出去的连接可能被对端断掉、调用方可能抛异常,怎么保证池子不被慢慢腐蚀?

**答**:四个机制。一,借还走 with 协议:contextmanager 把 acquire/release 绑进语法结构,调用方想忘还连接都难。二,借出前健康检查:空闲连接放久了可能被对端/防火墙掐掉,acquire 时 ping 一下,坏的就地丢弃换新——否则调用方拿到死连接,第一次请求就失败。三,异常即弃用:借出期间抛了任何异常,连接状态已不可信(可能处于事务中间态),必须丢弃而不是归还,这是连接池慢慢"漏光"的头号原因。四,容量守恒:丢弃时 created 计数要减回去并 notify,否则池子会永久缩水到打不开新连接。下面的演示制造"死连接 + 调用方异常"两种事故,验证池子自我修复。

```python
# file: code/02_并发与网络工程/q1332_connection_pool.py
import threading
import time
from contextlib import contextmanager


class FakeConn:
    _id = 0

    def __init__(self) -> None:
        FakeConn._id += 1
        self.id = FakeConn._id
        self.alive = True

    def ping(self) -> bool:
        return self.alive

    def close(self) -> None:
        self.alive = False


class ConnectionPool:
    def __init__(self, max_size: int = 3) -> None:
        self._idle = []
        self._created = 0
        self._max = max_size
        self._cond = threading.Condition()
        self.discarded = 0

    @contextmanager
    def borrow(self, timeout: float = 1.0):
        conn = self._acquire(timeout)
        try:
            yield conn
        except Exception:
            self._discard(conn)           # 异常连接状态不可信, 弃用
            raise
        else:
            self._release(conn)

    def _acquire(self, timeout: float) -> FakeConn:
        deadline = time.monotonic() + timeout
        with self._cond:
            while True:
                while self._idle:
                    conn = self._idle.pop()
                    if conn.ping():
                        return conn       # 健康检查通过才借出
                    self.discarded += 1   # 空闲期被对端掐掉: 就地换新
                    self._created -= 1
                    conn.close()
                if self._created < self._max:
                    self._created += 1
                    return FakeConn()
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("连接池借出超时")
                self._cond.wait(remaining)

    def _release(self, conn: FakeConn) -> None:
        with self._cond:
            if conn.ping():
                self._idle.append(conn)
            else:
                self._created -= 1
                self.discarded += 1
            self._cond.notify()

    def _discard(self, conn: FakeConn) -> None:
        with self._cond:
            conn.close()
            self._created -= 1
            self.discarded += 1
            self._cond.notify()


def main() -> None:
    pool = ConnectionPool(max_size=2)

    # 事故一: 借出期间调用方抛异常 -> 连接弃用不归还
    try:
        with pool.borrow() as conn:
            conn.alive = False           # 模拟使用中坏掉
            raise RuntimeError("业务炸了")
    except RuntimeError:
        pass
    print(f"事故一: 弃用 {pool.discarded} 个, 池内未腐蚀")

    # 事故二: 空闲连接被对端掐掉 -> 借出前健康检查换新
    with pool.borrow() as c1:
        pass                             # 正常归还一个
    with pool.borrow() as c2:
        c2.alive = False                 # 归还后悄悄死掉
    with pool.borrow() as c3:
        assert c3.ping(), "健康检查应保证借出的连接是活的"
        print(f"事故二: 死连接被替换为新连接 id={c3.id}")
        assert c3.id > c2.id

    # 压力: 多线程借还, 容量守恒
    errs = []
    def hammer():
        for _ in range(50):
            try:
                with pool.borrow() as c:
                    time.sleep(0.0005)
                    assert c.ping()
            except Exception as exc:
                errs.append(exc)
    threads = [threading.Thread(target=hammer) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errs
    print(f"200 次并发借还零失败, created={pool._created} 守恒于 max=2, 弃用累计 {pool.discarded}")
    assert pool._created <= 2


if __name__ == "__main__":
    main()
```

**追问**:1) 健康检查本身有成本,每次借出都 ping 是否过重?——折中方案是"空闲超过 X 秒才检查",刚归还的连接直接复用;参数按对端的空闲断开策略来定。2) 「异常即弃用」为什么是头号纪律?——借出期间抛异常,连接可能停在事务中间态/协议半帧态,归还后下一个使用者拿到脏状态,故障像传染病一样扩散;DB 连接池(DBAPI 的 rollback)与自定义池都适用同一规则。3) 容量守恒的机制?——created 计数在「创建成功」时+1,「连接彻底关闭」时-1 并 notify 等待者;丢弃连接若忘了减计数,池子永久缩水,最终 acquire 永久等待——这是自研池最经典的内存级 bug。4) 生产陷阱?——健康检查用真实业务查询(副作用+慢);归还时没 reset 状态(残留事务隔离级别/会话变量);池上限与对端连接上限不匹配(对端先拒绝);异常路径里 close 也抛异常,计数还是没减回去(要双重兜底)。

---
