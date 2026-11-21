---
title: [Q1692] keyspace 通知: 过期事件为什么不可靠
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1692 · keyspace 通知: 过期事件为什么不可靠

> 难度:★★☆☆ | 标签:Redis, 事件

**问**:能靠订阅 key 过期事件来做业务定时任务吗?

**答**:不能,两个不可靠性决定了它只能做旁路。第一,过期事件的发出时机取决于过期键什么时候被处理:访问时懒检查、或后台周期抽样扫到,事件可能比 TTL 晚很多秒,延迟完全不可控。第二,pub/sub 是 fire-and-forget:订阅端掉线或重启期间的事件永久丢失,没有重放。所以 keyspace 通知适合做缓存清理的旁路观察、监控打点,不适合承载业务语义;真正的延迟任务用 zset 轮询、Stream 或 RabbitMQ 延迟插件实现,并用数据库对账兜底漏掉的任务。开启方式是配置 notify-keyspace-events,如 Ex 表示 expired 事件。

```python
# file: code/04_数据库与缓存/q1692_keyspace_notify.py
"""keyspace 通知: 过期事件何时发出 与 为什么不能当定时器用"""

class FakeRedis:
    def __init__(self):
        self.kv, self.expire_at = {}, {}
        self.events = []
        self.now = 1000.0

    def setex(self, key, ttl):
        self.kv[key] = "v"
        self.expire_at[key] = self.now + ttl

    def advance(self, dt):
        """时间推进; redis 的过期由访问时懒检查与后台周期抽样两条路径触发"""
        self.now += dt
        for k in list(self.kv):
            if self.now >= self.expire_at.get(k, 0):
                del self.kv[k]
                self.events.append(("expired", k, self.now))

r = FakeRedis()
r.setex("job:1", 5)
r.setex("job:2", 5)
r.advance(3)
print("3 秒后事件:", r.events, "-> 没人访问且后台未扫到, 事件还没发")
r.advance(10)
print("13 秒后事件:", r.events)
print("两个不可靠性:")
print("  1) 发出时机取决于到期后被访问或被周期抽样扫到, 延迟不可控")
print("  2) 订阅是 fire-and-forget, 订阅端掉线期间的事件永久丢失, 无重放")
print("正确姿势: keyspace 通知只做旁路观察与清理; 业务定时用延迟队列 zset 或 Stream, 外部调度器兜底对账")
```

**追问**:
- 懒过期与定期抽样的分工?——访问命中才检查省 CPU 但冷键赖着;后台每 100ms 抽样清理兼顾内存,两者共同决定事件时点。
- 需要可靠过期通知怎么办?——业务表存到期时间,调度器扫表,或用支持持久化投递的延迟队列,通知只当加速器不当保险。

---
