---
title: "[Q6786] 通知收着收着就断了：PG LISTEN/NOTIFY 的丢通知与轮询兜底"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6786 · 通知收着收着就断了：PG LISTEN/NOTIFY 的丢通知与轮询兜底

难度：P6 ｜ 标签：PostgreSQL、LISTEN/NOTIFY、通知丢失、队列溢出、轮询兜底

基线：Python 3.12；用事件表模拟 NOTIFY 的"事务提交才可见、连接断开即丢弃、通道队列容量上限"三特性，实现"通知加速 + 轮询兜底"的混合消费模型，全标准库实跑。

**问**：用 PG 的 LISTEN/NOTIFY 做配置变更推送，偶尔有几台实例没收到更新，重启后也没补——LISTEN/NOTIFY 到底会不会丢消息？它和 MQ 的可靠性边界在哪？通知队列 8KB 上限是怎么回事？正确用法是不是"纯通知 + 定期轮询兜底"？

**答**：
- **结论**：LISTEN/NOTIFY 是**尽力而为的通知**，不是消息队列，三条丢失路径：① **连接断开**——NOTIFY 只投递给"在 NOTIFY 提交时正保持 LISTEN 的连接"，消费者断线重连的窗口里发生的通知，**不会为它重放**，也没位置可回溯；② **队列溢出**——所有未消费通知存在服务端全局队列（默认上限约 8GB 内存或单事务累计超大 payload 时直接给订阅连接报错），大 payload（>8000 字节的 payload 会被截断行为差异）与高频通知会挤压队列，极端时通知失败/客户端被断；③ **未提交回滚**——NOTIFY 与事务绑定，事务回滚通知消失（这是特性不是缺陷）。正确架构是**通知做加速器、查询做事实源**：业务变更写一张带自增序号的事件表（或直接用逻辑解码），消费者平时靠 LISTEN 秒级响应，同时低频轮询"上次已消费序号之后的事件"做兜底对账——通知丢了最多慢一个轮询周期，不会丢事实。这和本地缓存广播失效 + TTL 兜底（Q6531/Q2489）是同一个模式：**易失的推送层必须叠一层确定的拉取层**。
- **取舍**：① NOTIFY 的 payload 上限 8000 字节，且 payload 放大队列内存——规范是通知里只放"事件 ID/表名"，细节由消费者回查（引用式通知）；② 轮询周期的选择：兜底周期 = 可容忍的最终一致窗口，成本是每实例一个轻量索引查询，几十台实例 30s 轮询毫无压力；③ 连接占用：LISTEN 持有专用连接（连接池事务模式下 LISTEN 会话语义会被破坏，Q6511 PgBouncer 陷阱），每个消费者实例要独占一条连接，实例多时核算连接预算；④ 消费顺序：NOTIFY 无跨事务顺序保证（两个并发提交的到达顺序不定），事件表的自增序号才是顺序事实源，消费端按序号推进。
- **实战**：① 消费者状态机：记 `last_seq` → LISTEN 收到通知触发"拉 last_seq 之后的全部事件"（批量推进，避免每通知一次查询）→ 兜底定时器同样拉增量——通知与轮询走同一条消费路径，只是触发器不同；② 通知风暴合并：一次事务改 500 行会发 500 条 NOTIFY，消费端按事务分组（NOTIFY 的同一 payload 可带事务号）合并处理；③ 监控两个指标：`pg_stat_activity` 里 LISTEN 连接的存活数、消费端"通知触发/轮询触发"的比例——纯靠轮询说明通知链路已失效；④ 别用 NOTIFY 当任务队列：无 ack、无重试、无死信，任务队列用 SKIP LOCKED 表队列或 MQ（Q985 Stream 同族讨论）。

```python
"""Q6786 LISTEN/NOTIFY 丢失模拟: 断线窗口丢通知, 通知加速+序号轮询兜底。"""
import itertools

SEQ = itertools.count(1)                      # 事件表自增序号 = 事实源
EVENTS: dict[int, str] = {}                   # seq -> 事件内容


def producer(event: str, notify_channel: list[str] | None) -> int:
    """业务提交: 事件表写入由消费模拟的 run() 按 seq 回放, 此处先登记通知."""
    seq = next(SEQ)
    if notify_channel is not None:            # 提交后推送
        notify_channel.append(seq)
    return seq


class Consumer:
    def __init__(self, poll_every_n: int):
        self.last_seq = 0
        self.poll_every_n = poll_every_n
        self._ticks = 0
        self.via_notify = 0
        self.via_poll = 0

    def on_notify(self) -> int:
        """通知触发: 通知只当'来活了'的信号, 事实从事件表拉."""
        self.via_notify += 1
        return self._drain()

    def on_poll(self) -> int:
        self.via_poll += 1
        return self._drain()

    def _drain(self) -> int:
        got = 0
        while (self.last_seq + 1) in EVENTS:   # 按序号推进, 不依赖通知内容
            self.last_seq += 1
            got += 1
        return got


def run(channel: list[str], consumers: list[Consumer], drop: set[int]) -> int:
    """逐事件: 先落事件表(事实), 再派发通知; drop 中的通知因断线窗口丢失."""
    delivered = 0
    for seq in channel:
        EVENTS[seq] = f"event-{seq}"           # 事务提交: 事实先落事件表
        for c in consumers:
            if seq not in drop:
                c.on_notify()                  # 通知触发 -> 拉事件表推进
                delivered += 1
        for c in consumers:                    # 周期性兜底轮询
            c._ticks += 1
            if c._ticks % c.poll_every_n == 0:
                c.on_poll()
    for c in consumers:                        # 下一轮兜底轮询补齐断线窗口
        c.on_poll()
    return delivered


if __name__ == "__main__":
    channel: list[str] = []
    for i in range(10):
        producer(f"config-v{i}", channel)
    drop = {4, 7}                             # 两次通知正逢断线窗口 -> 丢失
    lost = Consumer(poll_every_n=3)
    delivered = run(channel, [lost], drop)
    print(f"产生 10 条事件, 通知送达 {delivered} 条, 断线丢失 {len(drop)} 条")
    print(f"消费者 last_seq={lost.last_seq} (通知触发 {lost.via_notify} / "
          f"轮询触发 {lost.via_poll}) -> 最终一致: {'是' if lost.last_seq == 10 else '否'}")
    ok = (lost.last_seq == 10 and lost.via_poll > 0 and delivered == 8)
    print(f"校验: 通知有丢但序号轮询兜底补齐 -> {'通过' if ok else '异常'}")
    print("结论：NOTIFY 是易失加速器(断线丢/无重放/与事务绑定), 事件表序号是事实源;")
    print("      推送+拉取双通道, 通知慢一点没关系, 事实不能少一条")
```

**追问一**：为什么"把 LISTEN/NOTIFY 当队列用"注定失败？它和 Redis Stream 的可靠性差距具体在哪几项？

→ 解析：队列的四个核心承诺 NOTIFY 一条都不给：① **at-least-once 投递**：NOTIFY 是 at-most-once，消费者断开的那条通知直接蒸发，Stream 靠 consumer group 的 pending 列表保证未 ack 消息可重投（Q985）；② **消费位点**：NOTIFY 无位置概念，重连只能从头 LISTEN（新通知）或靠外部序号自己补，Stream 的 XREADGROUP 有显式游标；③ **离线消费**：NOTIFY 只对在线连接有效，消费者全下线期间事件"不在场"，Stream 消息持久化在 Stream 结构里等消费者回来；④ **死信与积压治理**：NOTIFY 无 ack/重试/死信语义，积压治理无从谈起，Stream 有 XAUTOCLAIM 与 MAXLEN（Q6749）。NOTIFY 的正确生态位是**低延迟提示信号**：它胜在进程内级延迟（微秒级）与零部署成本（PG 自带），适合"配置变更提醒、缓存失效广播、轻量级联触发"这类丢了能用兜底补齐的场景。选型判据一句话：**丢了这条通知，业务会不会有实质损失？会——上队列；不会（只是慢一个轮询周期）——NOTIFY 够用。**

**追问二**：NOTIFY 队列溢出在生产上是什么形态？除了"引用式通知"还有什么减负手段？

→ 解析：溢出的形态有两种：① 服务端队列内存膨胀（未消费通知堆积），极端时单条事务携带海量 NOTIFY 直接触发 `out of memory` 或强制断开订阅连接；② 大 payload 逼近 8KB 截断线，消费者拿到的 payload 不完整——两者都表现为"收不到/收不全"而不是明确报错，容易被误诊为网络抖动。减负手段按层次：① **payload 瘦身**：只发事件 ID 与类型（几十字节），把 500 行变更合并成 1 条"批次通知"（带事务号），消费端按事务号回查——通知数从 O(行数) 降到 O(事务数)；② **订阅端提速**：消费慢是堆积的根因，通知到达后批量拉事件表（一次拉 500 条）而不是每条通知一次查询；③ **频道分流**：高扇出的广播（如缓存失效）与高精度的事件流分开频道，避免慢消费者拖累全通道；④ **监控先行**：`pg_notification_queue_usage()` 返回队列使用比例，超 50% 告警——这是官方给出的队列水位探针，纳入巡检（Q2785）。总账：NOTIFY 的成本模型是"订阅端必须比生产端快"，一旦倒挂就堆积；把这个不等式做成监控，比任何修复手段都重要。
