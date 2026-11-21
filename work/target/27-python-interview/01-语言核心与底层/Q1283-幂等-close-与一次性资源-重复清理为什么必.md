---
title: [Q1283] 幂等 close 与一次性资源:重复清理为什么必须无害
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1283 · 幂等 close 与一次性资源:重复清理为什么必须无害

> 难度:★★★☆☆ | 标签:资源管理, 上下文管理器, 防御式

**问**:close() 被调两次会怎样?为什么「清理代码必须幂等」是硬要求?关闭后再使用该报什么错?

**答**:资源清理在真实系统里必然被多次触发:with 的 __exit__ 调一次、finally 兜底调一次、上层框架 teardown 再调一次——所以 close 必须幂等:第二次起直接返回而不是抛错(对比 some DB-API 的重复 close 行为,标准库 socket/file 都幂等)。实现就是 `self._closed` 标志位 + 早退。反方向必须严格:关闭后继续使用要立刻抛错(通常是 ValueError("I/O on closed ..."))——静默吞掉等于把 bug 推迟到更难查的地方。一次性上下文(不可重入,Q450)再进 with 也要抛错,防止把「用完即弃」的资源当连接池用。三个语义(幂等清理、关闭后即错、不可重用)合起来才是完整的资源生命周期契约。

```python
# file: code/01_语言核心与底层/q1283_idempotent_close.py


class ManagedResource:
    def __init__(self, name):
        self.name = name
        self._closed = False

    def close(self):
        if self._closed:
            return                      # 幂等:重复 close 无害
        self._closed = True
        print("closing", self.name)

    def write(self, data):
        if self._closed:
            raise ValueError("I/O on closed resource: %s" % self.name)
        print("write", data)

    def __enter__(self):
        if self._closed:
            raise ValueError("cannot reuse closed resource")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False


if __name__ == "__main__":
    r = ManagedResource("conn-1")
    with r:
        r.write("hello")
    r.close()                           # with 之后再来一次:静默幂等
    r.close()
    try:
        r.write("again")
    except ValueError as e:
        print("after close ->", e)
```

**追问**:1) 为什么 finally 里再调 close 是好习惯而不是多余?——__exit__ 只在「确实进入了 with 体」时执行;构造函数抛异常、__enter__ 半途失败等路径不经过 __exit__,finally 是最后防线。2) 幂等 close 的实现要素?——内部 _closed 标志、句柄置 None、重复调用直接返回;io 对象的 close 自带幂等;自定义资源要照此实现。3) 清理路径全景?——with/__exit__、try/finally、异常退出钩子、GC 兜底(finalize)——调用次数不可控是常态,所以幂等是契约不是优化。4) 生产陷阱?——二次 close 抛错让 finally 崩掉掩盖原异常;close 里做非幂等操作(计数扣减、二次退款);只靠引用计数回收,忘记显式 close 的路径泄漏。
