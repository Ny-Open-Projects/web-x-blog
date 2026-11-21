---
title: [Q6514] Redis 实现延迟队列：ZSET+轮询 vs Stream
date: 2026-11-19
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6514 · Redis 延迟队列

> 难度:★★★ | 标签:Redis, 延迟队列, 订单超时

**问**：「订单 15 分钟未支付自动取消」用什么实现——ZSET 轮询方案怎么写、为什么必须配 Lua？`BRPOPLPUSH`/Stream 的消费确认怎么做？延迟队列的 at-least-once 语义在哪一环兜底？

**答**：ZSET 方案：score=到期时间戳，member=任务 ID；轮询者每秒 `ZRANGEBYSCORE key now limit 10` 取到期任务，**取出+投递必须原子**（Lua：ZRANGEBYSCORE → ZREM → LPUSH 一体），否则两个轮询者同时取到同一任务 = 重复执行（若任务不幂等就是事故）。Stream 方案（Redis 5+）：`XADD` 投递 → `XREADGROUP` 消费 → 处理完 `XACK`；未 ACK 的消息留在 PEL（pending entries list），消费者组用 `XAUTOCLAIM` 认领死消费者遗留消息——原生 at-least-once。兜底链：投递侧「业务先落 DB 再入队」（发件箱模式，队列丢也不丢事）→ 队列侧 ACK/PEL → 执行侧业务幂等。取舍：小规模低精度用 ZSET（秒级精度够）；要求投递确认语义直接用 Stream（或干脆上专业 MQ）。

```python
# 全部标准库（redis 客户端标注基线 redis-py 5 / Redis 6-7）；缺库降级见文末
# 三段口径：ZSET 轮询（Lua 原子）→ Stream ACK（PEL 兜底）→ 业务幂等
import time, uuid

ZSET_ADD_LUA = """
local ok = redis.call('ZADD', KEYS[1], ARGV[1], ARGV[2])
return ok
"""
ZSET_POLL_LUA = """
-- 到期取出+删除+投递，三步原子：防多轮询者重复消费
local jobs = redis.call('ZRANGEBYSCORE', KEYS[1], 0, ARGV[1], 'LIMIT', 0, 10)
for i, id in ipairs(jobs) do
  redis.call('ZREM', KEYS[1], id)
  redis.call('RPUSH', KEYS[2], id)
end
return jobs
"""
STREAM_LUA = """
-- Stream 版：XADD 由应用直接调，无需脚本（XADD 自身原子）
redis.call('XADD', KEYS[1], '*', 'job', ARGV[1], 'due', ARGV[2])
"""

def demo_zset_semantics():
    """无 Redis 环境：用纯 Python 模拟 ZSET 轮询的原子语义（口径演示）。"""
    zset = []                                  # (due_ts, job_id) 有序列表模拟 ZSET
    ready = []
    lock_held = True                           # Lua 的原子性 = 轮询期间独占（单线程脚本语义）
    def poll(now, limit=10):
        global lock_held
        assert lock_held, "Lua 脚本串行执行，模拟原子"
        due = [j for (t, j) in zset if t <= now][:limit]
        for j in due:
            zset.remove(next((t, j) for (t, jj) in zset if jj == j))
            ready.append(j)                    # ZREM + LPUSH 在同一脚本内：不可分割
        return due
    now = time.time()
    zset += [(now - 1, "job-A"), (now + 60, "job-B")]     # A 到期，B 未到
    got = poll(now)
    assert got == ["job-A"] and "job-A" in ready and "job-B" not in ready
    print("ZSET 轮询原子语义 OK（到期取出+删除+投递一体）")

def demo_stream_semantics():
    """Stream at-least-once：未 ACK 留 PEL，XAUTOCLAIM 认领遗留消息。"""
    pel = {}                                   # consumer -> [未 ACK 消息]
    delivered = []
    def xreadgroup(consumer, msg_id, job):
        pel.setdefault(consumer, []).append((msg_id, job))
        delivered.append(job)                  # 投递成功
    def xack(consumer, msg_id):
        pel[consumer] = [m for m in pel[consumer] if m[0] != msg_id]
    def xautoclaim(dead_consumer, new_consumer):
        mine = pel.pop(dead_consumer, [])
        pel.setdefault(new_consumer, []).extend(mine)
        return mine
    xreadgroup("c1", "1-1", "job-A")
    xack("c1", "1-1")                          # 正常处理完 ACK
    xreadgroup("c1", "1-2", "job-B")           # c1 死了没 ACK
    pending = xautoclaim("c1", "c2")
    assert [j for _, j in pending] == ["job-B"]
    print("Stream PEL 认领 OK：死消费者的未 ACK 消息被 c2 接手（at-least-once）")

if __name__ == "__main__":
    demo_zset_semantics()
    demo_stream_semantics()
    # 生产口径：Redis 6.2+ XAUTOCLAIM 自带最小空闲时间（min-idle-time），替代旧 XCLAIM；
    # ZSET 方案轮询间隔=精度下限（1s 轮询 → 最多 1s 延迟）；要毫秒精度换专业 MQ。
```

**追问**：1) ZSET 方案多实例轮询怎么减争用？——实例按任务 ID 分片轮询（只扫自己负责的 hash 槽）或接受 Lua 原子保护下的轻微争用（取到即删，重复率≈0）；但**投递到执行队列后**的重复仍要业务幂等兜底。2) 为什么订单超时不用数据库扫描？——每秒扫全表订单 WHERE expired 是灾难；ZSET 把「谁到期」变成 O(log N) 有序结构；但超时后的取消动作仍要检查订单状态（可能已支付），取消必须条件更新（status=unpaid 才取消）。3) Stream vs 专业 MQ 的分界？——Stream 无权限/路由/延迟投递原语、持久化绑 Redis 内存；千万级消息或复杂路由上 Kafka/RabbitMQ，Redis 队列适合中小规模 + 已有 Redis 运维。

## 背诵要点
1. ZSET 延迟队列：score=到期时间戳，取出+删除+投递必须 Lua 原子（防多轮询者重复）；精度=轮询间隔。
2. Stream at-least-once：XREADGROUP→处理→XACK；未 ACK 留 PEL，XAUTOCLAIM 认领死消费者消息。
3. 兜底链三层：业务先落 DB（发件箱）→ 队列 ACK/PEL → 执行幂等（取消动作条件更新 status）。

## 复盘追问
1. 轮询者挂了 30 秒，期间到期的任务怎么保证不丢？（提示：ZRANGEBYSCORE 范围从上次水位到 now——水位要持久化，或全量扫描兜底）
2. 取消订单和支付回调并发到达怎么处理？（提示：DB 条件更新谁先谁赢（status 状态机），输的一方读最新状态自适应，参考 A102）
