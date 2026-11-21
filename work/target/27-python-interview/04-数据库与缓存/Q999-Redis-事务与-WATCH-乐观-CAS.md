---
title: [Q999] Redis 事务与 WATCH: 乐观 CAS
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q999 · Redis 事务与 WATCH: 乐观 CAS

> 难度:★★★☆ | 标签:事务, WATCH

**问**:MULTI/EXEC 是什么?WATCH 怎么实现"检查再改"的原子性?与 Lua 怎么选?

**答**:MULTI 开启事务,后续命令入队不执行,EXEC 一次性按序执行(无回滚——某条失败其余照常,与 SQL 事务不同),DISCARD 放弃。WATCH 提供乐观锁:EXEC 前若被 watch 的键被任何客户端修改过,整个事务返回 nil,客户端重试——标准 CAS 循环。与 Lua 选型:WATCH+MULTI 是客户端重试模式,简单场景够用但网络往返多、高竞争下重试风暴;Lua 服务端原子,无重试、可带逻辑,复杂"检查再写"首选 Lua。注意 WATCH 的键会占用客户端内存与版本追踪,用完 UNWATCH。

```python
# file: code/04_数据库与缓存/q999_watch_cas.py
"""WATCH + MULTI 的 CAS 循环模拟: 竞争下重试直到成功"""
import threading
import time

class Store:
    def __init__(self):
        self.kv = {"stock": 10}
        self.version = {}
        self.lock = threading.Lock()

    def get(self, k):
        with self.lock:
            return self.kv.get(k)

    def watch_exec(self, watched_key, mutate):
        """模拟 WATCH: 版本未变才提交"""
        with self.lock:
            v0 = self.version.get(watched_key, 0)
        snapshot = self.kv[watched_key]           # 读快照
        new_val = mutate(snapshot)
        with self.lock:
            if self.version.get(watched_key, 0) != v0:
                return None                        # 被他人修改, 事务作废
            self.kv[watched_key] = new_val
            self.version[watched_key] = v0 + 1
            return new_val

def cas_decrement(store, key, want):
    for attempt in range(1, 5):
        result = store.watch_exec(key, lambda v: v - want)
        if result is not None:
            return attempt, result
        time.sleep(0.01)                           # 退避后重试
    return -1, None

if __name__ == "__main__":
    s = Store()
    out = []
    def buyer():
        out.append(cas_decrement(s, "stock", 1))
    ts = [threading.Thread(target=buyer) for _ in range(3)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("各买家(重试次数, 剩余):", out)
    print("高竞争下重试多 -> 这种场景换 Lua 一次原子扣减更优")
```

**追问**:
- Redis 事务为什么不支持回滚?——antirez 的设计取舍:命令错误在入队时即报错,运行期错误多为类型 bug,回滚救不了编程错误还拖慢常态路径。
- WATCH 的键很多会怎样?——每个客户端的 watched 集合让服务端维护版本比较成本上升,大量键时改用 Lua 或拆分热点。

---
