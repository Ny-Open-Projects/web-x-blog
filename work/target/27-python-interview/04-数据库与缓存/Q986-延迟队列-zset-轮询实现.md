---
title: [Q986] 延迟队列: zset 轮询实现
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q986 · 延迟队列: zset 轮询实现

> 难度:★★★★ | 标签:延迟队列, zset

**问**:订单 30 分钟未支付自动取消,用 Redis 怎么实现延迟任务?

**答**:zset 方案:member=任务标识(含业务键与唯一 ID),score=到期时间戳;生产者 ZADD 到期时间,定时器(每秒)执行 ZRANGEBYSCORE key 0 now LIMIT 0 10 取到期任务,处理成功 ZREM 删除。三个关键细节:一、取到与删除必须原子(Lua:取+删一个脚本),否则多实例同时抢到同一任务;二、处理失败要回队(重新 ZADD 延后)并计数防死循环;三、单 zset 有限,量大可按任务类型或时间分片多个 key 轮询。对比专业方案:RabbitMQ 死信/TTL、时间轮(Kafka/Netty)、数据库扫描,Redis 方案适合中小量、秒级精度足够的场景。精度受轮询间隔限制,`~` 保证不阻塞。

```python
# file: code/04_数据库与缓存/q986_delay_queue.py
"""zset 延迟队列: 原子取到期任务 + 失败回队"""
import time

class DelayQueue:
    def __init__(self):
        self.zset = {}                          # task -> due_ts

    def offer(self, task, delay_sec):
        self.zset[task] = time.monotonic() + delay_sec

    def poll_due(self, now=None, limit=5):
        now = now if now is not None else time.monotonic()
        due = sorted((t for t, d in self.zset.items() if d <= now))[:limit]
        for t in due:                           # 原子语义: 取出即移除
            del self.zset[t]
        return due

    def nack(self, task, delay_sec, max_retry):
        retry = self.retry.get(task, 0) + 1 if hasattr(self, "retry") else 1
        self.retry = getattr(self, "retry", {})
        self.retry[task] = retry
        if retry <= max_retry:
            self.offer(task, delay_sec)
        return retry <= max_retry

if __name__ == "__main__":
    dq = DelayQueue()
    dq.offer("order:1", 0.2)                    # 0.2 秒后到期(模拟30分钟)
    dq.offer("order:2", 0.5)
    for _ in range(6):
        due = dq.poll_due()
        if due:
            print(f"{time.monotonic():.1f} 到期任务:", due)
            for t in due:
                if t == "order:2":
                    dq.nack(t, 0.3, max_retry=1)
                    print("  order:2 处理失败, 延后重试")
        time.sleep(0.2)
```

**追问**:
- 为什么不用 keyspace notification?——过期事件通知不保证送达(过期删除是惰性+定期),用作延迟队列会丢任务,必须主动轮询。
- 多实例轮询怎么避免重复?——Lua 里 ZRANGEBYSCORE+ZREM 原子执行,或取到后用 SETNX task:lock 抢处理权;幂等消费仍是底线。

---
