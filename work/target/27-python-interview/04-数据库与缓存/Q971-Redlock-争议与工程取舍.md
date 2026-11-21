---
title: [Q971] Redlock 争议与工程取舍
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q971 · Redlock 争议与工程取舍

> 难度:★★★★★ | 标签:分布式锁, 一致性

**问**:Redlock 是什么?Martin Kleppmann 与 antirez 的争论核心是什么?工程上怎么选?

**答**:Redlock 向 N 个独立 Redis 节点依次加同一把锁,多数派(>N/2)成功且总耗时小于锁有效期才算获锁,意图解决单点故障导致的锁丢失。争议:Martin 指出锁的正确性依赖时间假设——客户端 GC 停顿/时钟跳变会让"未过期"的锁实际已失效,Redlock 无法给出绝对安全,必须配合 fencing token(递增令牌,存储端拒绝旧令牌写);antirez 回应时钟问题可控且 fencing 需要存储端配合、弱化了 Redis 锁的意义。工程取舍:如果锁只做"效率优化"(防重复计算),单实例 SET NX EX + owner 校验足够;如果锁保护"正确性"(资金),不要指望任何基于租约的锁,用数据库唯一约束/条件更新或 zk/etcd 这类共识系统,并在设计上让误持锁的后果可恢复。

```python
# file: code/04_数据库与缓存/q971_redlock_quorum.py
"""Redlock 多数派获取模拟 + fencing token 概念"""
import time

class Node:
    def __init__(self, name, fail=False):
        self.name, self.locked, self.fail = name, None, fail

    def lock(self, token, ttl):
        if self.fail:
            return False
        self.locked = token
        return True

def redlock(nodes, token, ttl=1.0):
    won = [n for n in nodes if n.lock(token, ttl)]
    return len(won) > len(nodes) // 2, [n.name for n in won]

if __name__ == "__main__":
    nodes = [Node(f"n{i}") for i in range(5)]
    nodes[3].fail = True                      # 一个节点故障
    ok, won = redlock(nodes, "t1")
    print("多数派获锁:", ok, "赢得节点:", won)

    # fencing token: 存储端拒绝旧令牌
    class Store:
        def __init__(self):
            self.max_token = 0
        def write(self, token):
            if token <= self.max_token:
                return "rejected: 旧令牌"
            self.max_token = token
            return "ok"
    store = Store()
    print("持锁方写入 token=7:", store.write(7))
    print("停顿后旧会话写入 token=7:", store.write(7), "<- fencing 兜底")
```

**追问**:
- fencing token 从哪来?——由锁服务或存储侧提供单调递增号(如版本号、zk 的 zxid),Redis 本身不产生,需要额外组件,这正是争论的实用要点。
- 多数派获锁后某节点宕机算持锁吗?——Redlock 语义下算,但少数派恢复后可能残留旧锁信息,依赖各节点 TTL 自动过期收敛。

---
