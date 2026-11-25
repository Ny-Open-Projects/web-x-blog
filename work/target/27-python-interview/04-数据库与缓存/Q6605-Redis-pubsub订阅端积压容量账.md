---
title: [Q6605] Redis pub/sub 订阅端积压与缓冲区容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6605 · Redis pub/sub 订阅端积压与缓冲区容量账

难度：P7 ｜ 标签：Redis / pub-sub / 容量规划

**问**：用 Redis pub/sub 广播缓存失效通知，某个 Python 订阅端发布新版后卡了（GIL 阻塞在一段重计算），之后 Redis 把这个订阅连接直接踢掉，其他订阅端也开始丢消息。pub/sub 不是实时广播吗？消息为什么会丢、连接为什么被踢？

**答**：
- **结论**：pub/sub 是**无积压的即发即弃**广播：Redis 不为频道存历史，消息只在订阅端在线时投递到其连接的输出缓冲区（`client-output-buffer-limit pubsub`）。订阅端消费不动时缓冲区按两个维度增长——**硬上限（bytes）或超时上限（秒级持续超 soft limit）**——任一触发 Redis 就主动断开该客户端。被踢的订阅端丢失的是断开期间全部消息；更隐蔽的是"没被踢但缓冲区在 soft limit 附近抖动"的订阅端，消息延迟在秒到分钟级随机抖动。所以容量账的核心不是"频道 QPS"，而是**每个慢订阅端的瞬时积压字节**。
- **取舍**：设计选项：① 治慢订阅端——消费循环里不做重活，收到消息只入内存队列/转线程处理；② 调缓冲区——`client-output-buffer-limit pubsub 64mb 16mb 60` 给慢消费者留余量，但这只是把丢消息变成"晚丢"，不解决丢；③ 要"不丢"就换 Stream（XADD + 消费组 + PEL，可ACK可重放），代价是占用内存/需要清理 MAXLEN；④ 广播 + 确认混合：通知类走 pub/sub（丢了有 TTL 兜底回源），事实类走 Stream。
- **实战**：容量账三步：① 估算峰值消息体 × 频道 QPS × 最坏消费延迟 = 单订阅端积压字节；② 硬上限设为该值的 2-3 倍，soft limit（持续秒数）按"消费端 GC/重启最长间隔"定；③ 监控 `INFO clients` 的输出缓冲区分布 + 断连计数，Python 侧对 pub/sub 客户端做"心跳频道 + 断线重连 + 重连后全量刷新缓存"兜底。

```python
# pub/sub 订阅端积压容量账 + 慢消费者治理（标准库模拟）
# 基线：Python 3.9+；真实实现 redis-py 5.x（redis.asyncio 同理）

import threading
import time
from collections import deque


class PubsubBuffer:
    """模拟 Redis 侧的订阅端输出缓冲区与踢除逻辑"""

    def __init__(self, hard_bytes: int, soft_bytes: int, soft_seconds: float) -> None:
        self.hard = hard_bytes
        self.soft = soft_bytes
        self.soft_secs = soft_seconds
        self.buf = 0
        self.over_since: float | None = None
        self.kicked = False

    def publish(self, msg_bytes: int, now: float) -> None:
        if self.kicked:
            return                      # 消息直接丢弃：即发即弃
        self.buf += msg_bytes
        if self.buf > self.hard:
            self.kicked = True          # 硬上限：立刻断连
        elif self.buf > self.soft:
            self.over_since = self.over_since or now
            if now - self.over_since > self.soft_secs:
                self.kicked = True      # soft 超时：断连
        else:
            self.over_since = None

    def consume(self, n: int) -> None:
        self.buf = max(0, self.buf - n)


def plan_buffer(msg_avg_bytes: int, qps: int, worst_lag_s: float) -> int:
    """单订阅端最坏积压 = 峰值速率 × 最坏消费延迟，硬上限取 3 倍"""
    worst = msg_avg_bytes * qps * worst_lag_s
    return int(worst * 3)


def main() -> None:
    t0 = 0.0
    # 场景：4KB 消息 × 1000 QPS 广播，慢订阅端 2 秒没消费
    buf = PubsubBuffer(hard_bytes=32 * 1024 * 1024, soft_bytes=8 * 1024 * 1024, soft_seconds=60)
    for i in range(500):                 # 500 条 × 4KB = 2MB，未超 soft
        buf.publish(4096, t0 + i * 0.001)
    assert not buf.kicked and buf.buf == 500 * 4096

    # 广播 3 秒 × 1000 QPS，消费端卡死：12MB 超 soft，但未超 60s
    for i in range(4000):
        buf.publish(4096, t0 + 3 + i * 0.001)
    assert buf.buf > 16 * 1024 * 1024
    assert not buf.kicked, "仍在 soft 宽限期内"

    # 再持续超时：soft 超时触发踢除，之后消息全丢
    buf.publish(4096, t0 + 70)
    assert buf.kicked
    before = buf.buf
    buf.publish(4096, t0 + 71)
    assert buf.buf == before, "被踢后消息即发即弃"

    # 容量规划：给最坏 lag 2s 的消费端算硬上限
    need = plan_buffer(4096, 1000, 2)
    assert need >= 23 * 1024 * 1024
    print(f"规划硬上限 {need/1024/1024:.0f}MB（最坏积压×3）")
    print("OK: 硬上限/软超时/即发即弃语义与容量账")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"缓存失效通知"这类场景可以容忍 pub/sub 丢消息？
→ 一句话提示：通知只是"提前触发回源"的优化，丢了走 TTL 到期回源兜底，正确性不受影响；但如果消息内容是事实本身（订单状态变更），就必须用 Stream/消息队列。

**追问 2**：Redis Stream 的消费者组怎么解决 pub/sub 的两个核心缺陷？
→ 一句话提示：持久化（消息在 Stream 里等消费者，不随连接消失）+ 消费确认（PEL 记录未 ACK，可 XAUTOCLAIM 转移给别的消费者），代价是内存占用与 MAXLEN 清理运维。

## 背诵要点
- pub/sub 无历史积压：消息只投给在线订阅端，`client-output-buffer-limit pubsub` 的硬上限/软超时任一触发即断连，断开期间消息全丢。
- 容量账按"最坏积压字节"算：消息体 × 峰值 QPS × 最坏消费延迟，硬上限取 2-3 倍；被踢后要有"重连 + 全量刷新"兜底。
- 订阅端消费循环只入队不干重活；要可靠就换 Stream（消费组 + ACK + MAXLEN），通知类可容忍丢、事实类不可。

## 复盘追问
- 怎么发现"没被踢但在丢消息边缘"的订阅端？提示：`INFO clients` 里 `oldest_client`/输出缓冲区分布、`client list` 按 pubsub 类过滤看 `omem`，Python 侧再对比"发布计数 vs 收到计数"的差值曲线。
- GIL 阻塞在重计算时，redis-py 的订阅线程会怎样？提示：纯 Python 回调共用事件循环/线程时被 GIL 卡住，socket 缓冲区继续涨；正确姿势是订阅回调只做 `queue.put`，worker 线程/进程消费。
