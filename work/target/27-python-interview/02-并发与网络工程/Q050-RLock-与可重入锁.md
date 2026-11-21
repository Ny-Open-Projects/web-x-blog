---
title: [Q050] RLock 与可重入锁
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q050 · RLock 与可重入锁

> 难度:★★★ | 标签:threading, RLock, 可重入

**问**:RLock 和 Lock 的区别是什么?什么场景必须用 RLock?

**答**:Lock 不可重入,同一线程在持有期间再次 acquire 会死锁;RLock 记录持有线程与重入次数,同线程可多次 acquire,需对应次数的 release。典型场景是递归函数或 A 方法内部调用同类的 B 方法,两者都要拿同一把锁。

```python
# file: code/02_并发与网络工程/q050_rlock.py
import threading

rlock = threading.RLock()


def inner() -> None:
    with rlock:  # 同一线程再次进入, RLock 允许
        print("inner 拿到锁")


def outer() -> None:
    with rlock:
        print("outer 拿到锁")
        inner()
        print("outer 释放前 depth 正确")


if __name__ == "__main__":
    outer()

    plain = threading.Lock()
    got = plain.acquire()
    result = {}
    def try_reacquire() -> None:
        result["got"] = plain.acquire(timeout=0.1)
    t = threading.Thread(target=try_reacquire)
    t.start()
    t.join()
    print("Lock 同线程再次 acquire 是否成功:", bool(result.get("got")), "(False 表示死锁被超时解除)")
    plain.release()
```

**追问**:
- RLock 开销比 Lock 大吗?——略大,因为要记录 owner 和计数,但差异很小;只有需要重入时才用。
- 什么信号说明需要 RLock 而不是重构?——递归遍历持锁结构、公有方法内部调用同样加锁的私有方法;更干净的做法是把加锁收敛到唯一入口。
- RLock 重入有上限吗?——没有固定上限,受递归深度限制;release 次数必须与 acquire 严格配对,否则锁永远不归还。
- `with` 语句对 RLock 有效吗?——有效,上下文协议就是 acquire/release,重入语义不变。
