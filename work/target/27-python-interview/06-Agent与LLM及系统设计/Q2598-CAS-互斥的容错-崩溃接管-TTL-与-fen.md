---
title: [Q2598] CAS 互斥的容错:崩溃接管 TTL 与 fencing 挡旧主
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2598 · CAS 互斥的容错:崩溃接管 TTL 与 fencing 挡旧主

> 难度:★★★☆ | 标签:分布式, 锁, 容错

**问**:持有者拿到锁就崩溃了,锁怎么解?它醒来后又写了一条数据怎么办?

**答**:两个机制接力:锁值带过期时刻,接管方的 cas 加上时间条件,过期即可强行接管,崩溃不释放也不会永久死锁;接管时 fencing 号单调递增,资源侧守卫只认不小于已知最大号的写入,旧主拿着过期号迟到提交会被当场拒绝。时序推演是关键:fencing 2 的旧主在 fencing 3 的新主接管后写入,守卫比对号大小直接拒收,这就是 fencing token 的全部意义——把"谁是当前合法持有者"从锁服务推到资源侧各点独立判定。TTL 的取值要覆盖持有者的最大合法执行时长加时钟误差,太短误接管、太长故障恢复慢。两个机制缺一不可:只有 TTL,旧主醒来还能写;只有 fencing,没人接管的死锁仍在。

```python
# file: code/06_Agent与LLM及系统设计/q2598_fencing.py
"""Q2598 CAS 互斥的容错:持有者崩溃后 TTL 到期可接管,fencing 挡旧主。

锁值带过期时刻,持有者崩溃不释放也能被接管;接管时 fencing 号
单调递增,资源侧守卫只认不小于签发时的最大 fencing 号,旧主
拿着过期号迟到写入会被当场拒绝。
"""


class LockStore:
    def __init__(self):
        self.holder = None
        self.expires = 0.0
        self.fencing = 0

    def cas_acquire(self, owner, now, ttl):
        if self.holder is not None and now < self.expires:
            return None
        self.fencing += 1
        self.holder = owner
        self.expires = now + ttl
        return self.fencing

    def cas_release(self, owner, now):
        if self.holder == owner and now < self.expires:
            self.holder = None
            return True
        return False


def guarded_write(current_fencing, fencing, log):
    if fencing >= current_fencing:
        log.append("write-ok:" + str(fencing))
        return True
    log.append("write-rejected-stale:" + str(fencing))
    return False


def main():
    s = LockStore()
    f1 = s.cas_acquire("A", now=0.0, ttl=5.0)
    assert f1 == 1
    assert s.cas_acquire("B", now=3.0, ttl=5.0) is None   # 未过期拿不到
    assert s.cas_release("B", now=3.0) is False           # 非持有人不能释放
    assert s.cas_release("A", now=3.0) is True
    f2 = s.cas_acquire("A", now=4.0, ttl=5.0)             # A 拿到锁后崩溃
    assert f2 == 2
    log = []
    guarded_write(f2, f2, log)                            # A 用 fencing=2 写
    f3 = s.cas_acquire("B", now=10.0, ttl=5.0)            # TTL 已过,B 接管
    assert f3 == 3
    guarded_write(f3, f2, log)                            # 旧主迟到写被拒
    guarded_write(f3, f3, log)
    assert log == ["write-ok:2", "write-rejected-stale:2", "write-ok:3"], log
    print("接管后 fencing 单调递增:", f2, "->", f3)
    print("资源侧守卫:", log[1], "← 崩溃旧主的迟到写被挡")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:fencing 号谁发?答:锁服务在授予时发,全局单调,资源侧只需比较大小,不需要全局时钟。
- 追问二:资源不支持守卫怎么办?答:典型如某些存储没有条件写,把 fencing 校验做在写入代理层,所有写经代理转发。
