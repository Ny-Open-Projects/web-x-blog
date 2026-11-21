---
title: [Q6649] Redis 客户端缓存与 CLIENT TRACKING
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6649 · Redis 客户端缓存与 CLIENT TRACKING

难度：P7 | 标签：Redis、client-side caching、性能工程、两级缓存

**问**：热点 key 的读 QPS 打满了 Redis 带宽。除了应用侧自建本地缓存+失效广播，Redis 6 的 client-side caching（CLIENT TRACKING）提供了什么？"服务端推失效"比"本地 TTL"好在哪，坑在哪？

**答**：
- **结论**：CLIENT TRACKING 让 Redis 服务端记录"这个连接读过哪些 key"，key 被写时服务端向该连接推送失效通知（RESP3 invalidation），客户端清掉本地副本。相比自建广播（pub/sub + 本地订阅），省掉了自建失效链路的可靠性负担——失效由 Redis 自己保证。收益：热 key 读不再出网络，Redis 带宽与 QPS 压力大幅下降。
- **取舍**：两个模式：default 模式记录具体 key（精确、连接级）；broadcast 模式按前缀广播（简单、失效风暴大）。坑：① 失效通知走的是这条连接——连接断开期间的失效会丢，重连后必须全量清空本地缓存；② 本地缓存在应用进程内，多实例各自为政，内存上限要自控；③ 只读连接才适合开 tracking，写连接开了纯浪费。
- **实战**：适用判据：极热 + 极小 + 读多写少的 key（配置、库存水位展示）。配合 redis-py 5+ 的 client-side-caching 支持（协议需 RESP3）。兜底：本地缓存条目仍设保守 TTL（如 5s），失效丢失时靠 TTL 自愈。监控"失效推送速率"——写高峰时失效风暴会占用客户端处理时间。

```python
"""Redis 客户端缓存（CLIENT TRACKING）语义模拟：服务端失效推送。"""
class Server:
    def __init__(self):
        self.data = {"stock:A": "10"}
        self.subscribers = []          # tracking 客户端
    def get(self, key):
        if self.subscribers:
            self.subscribers[-1].tracked.add(key)     # 记录该客户端读过的 key
        return self.data.get(key)
    def set(self, key, val):
        self.data[key] = val
        for c in self.subscribers:
            if key in c.tracked:
                c.invalidate(key)                     # 失效推送（RESP3 invalidation）

class Client:
    def __init__(self, server):
        self.server = server
        self.local = {}
        self.tracked = set()
        server.subscribers.append(self)
        self.invalidated = []
    def get(self, key):
        if key in self.local:
            return f"local:{self.local[key]}"
        v = self.server.get(key)
        self.local[key] = v
        return f"server:{v}"
    def invalidate(self, key):
        self.invalidated.append(key)
        self.local.pop(key, None)

server = Server()
c = Client(server)
print(c.get("stock:A"))            # 回源
print(c.get("stock:A"))            # 命中本地
server.set("stock:A", "11")        # 服务端写 -> 推送失效
print("失效通知:", c.invalidated, "本地缓存:", c.local)
print(c.get("stock:A"))            # 重新回源
print("要点：失效由服务端推、客户端不再轮询 TTL；连接断开期间失效丢失需全量清空")
```

**追问链**：
1. 追问一层：为什么连接断开要全量清空本地缓存？（失效通知随连接走，断连窗口内的写不会补发；不清空就是无限期旧值——这是 client-side caching 最经典的事故）
2. 追问二层：default 与 broadcast 模式怎么选？（key 少且集中用 default；前缀下 key 数量大或 set 场景用 broadcast——它不记录具体 key，代价是无关 key 的失效也推送）

**背诵要点**：
1. CLIENT TRACKING：服务端记录连接读过的 key，写时推失效（RESP3）。
2. 连接断开失效即丢，重连必须清空本地缓存，另配保守 TTL 兜底。
3. 适用极热小 value 读多写少；监控失效推送速率防写高峰风暴。

**复盘追问**：
1. 应用重启后读到旧值，为什么 tracking 没救？（重连后未清本地缓存，或 TTL 兜底没配）
2. 失效推送把客户端 CPU 打高了，怎么权衡？（改 broadcast 按需订阅前缀，或对低价值 key 退出 tracking）
