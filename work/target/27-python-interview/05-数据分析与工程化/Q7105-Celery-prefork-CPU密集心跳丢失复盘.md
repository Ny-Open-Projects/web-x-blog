---
title: [Q7105] Celery prefork 下 CPU 密集任务心跳超时任务丢失事故复盘
date: 2026-11-21
categories: [Python数据分析与工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7105 · Celery prefork CPU 密集任务阻塞心跳导致任务丢失事故复盘

难度：P7 ｜ 标签：Celery / prefork / 事故复盘

**问**：Celery worker（prefork 池）跑一批 CPU 密集的数据转换任务，某次任务单条要跑 20 分钟。期间监控看到 worker 心跳丢失告警，之后一批任务既没失败也没重试，"凭空消失"。CPU 密集任务为什么会弄丢心跳？丢的任务去哪了？

**答**：
- **结论**：prefork 池里**主进程（负责心跳/事件与 broker 通信）和子进程（执行任务）是分开的**，理论上纯 CPU 任务不挡主进程心跳。丢任务的真正链路是组合拳：① 任务超时被 `time_limit` 硬杀（SIGKILL），子进程死前不回 ACK；② broker 的 visibility_timeout（Redis broker 默认 1 小时）到期后，消息被当作"未确认"重新投递——但 worker 可能已经完成过一部分，重新执行造成重复；③ 如果 worker 用的是 gevent/eventlet 池或任务里在**主进程上下文**做重计算（如并发下 task 元数据处理、自定义 rate limit），GIL 持有超时直接冻结心跳，K8s 的 liveness probe 或 `worker_lost_wait` 把 worker 判死重启，正在跑的任务没有 ACK 也没有 NACK，在 visibility 窗口里处于"薛定谔"状态：窗口内没人重投 → 任务"消失"；窗口后又重复执行。"既没失败也没重试"多发生在主进程被杀、事件未落盘的组合下。
- **取舍**：治理选项：① CPU 密集任务改**分片**：20 分钟任务拆成 5 分钟粒度，超时/重试/恢复都可控（首选）；② `time_limit`/`soft_time_limit` 设出真实余量，超时走明确的 `SoftTimeLimitExceeded` 清理路径而不是被 SIGKILL；③ broker 侧：Redis broker 下 `visibility_timeout` 调大（但要理解它同时是重投延迟），或改用 RabbitMQ（ACK 语义不同，无 visibility 窗口，靠 prefetch/连接恢复）；④ 任务幂等 + 结果落库（任务 ID 作幂等键），重复执行不产生副作用，这是把"丢失"变"重复"的前提；⑤ 监控三件套：心跳告警、队列积压、任务完成率与"执行中但无事件"的任务数。
- **实战**：事故剧本：① 从 Celery 事件流 + broker 队列深度还原时间线，确认丢的是"worker 重启 + visibility 未到"窗口内的消息；② 手动从 broker dump 消息重放（Redis broker 用 unacked 队列排查）；③ 任务改造：分片 + 幂等键 + `on_failure` 记录快照；④ 复盘项：`task_acks_late=True` 与 `worker_prefetch_multiplier=1` 的组合评审（保证长任务不丢但吞吐下降），CPU 密集任务与 IO 任务分不同队列/worker 部署。

```python
# 任务分片与幂等重放治理（标准库模拟 Celery 语义）
# 基线：Python 3.9+；真实实现 Celery 5.x + Redis broker

import time
from dataclasses import dataclass, field


@dataclass
class Broker:
    unacked: dict[str, float] = field(default_factory=dict)   # task_id -> 交付时间
    visibility_timeout: float = 3600.0
    done_ids: set[str] = field(default_factory=set)

    def requeue_stale(self, now: float) -> list[str]:
        """visibility 超时的任务重新可见（可能重复执行）"""
        stale = [tid for tid, t in self.unacked.items() if now - t > self.visibility_timeout]
        for tid in stale:
            del self.unacked[tid]
        return stale


@dataclass
class IdempotentTask:
    task_id: str
    shard: int
    results: dict[str, str] = field(default_factory=dict)     # 幂等结果表

    def run(self, broker: Broker, now: float) -> str:
        if self.task_id in broker.done_ids:
            return f"{self.task_id} 已完成过，幂等跳过"
        broker.done_ids.add(self.task_id)
        broker.unacked[self.task_id] = now          # 交付未确认
        self.results[self.task_id] = f"shard-{self.shard} done"
        return f"{self.task_id} executed shard-{self.shard}"


def main() -> None:
    broker = Broker(visibility_timeout=1.0)
    t = IdempotentTask("t-1", shard=3)

    print(t.run(broker, now=0.0))     # 第一次执行
    print(t.run(broker, now=0.5))     # broker 重投后重复执行 → 幂等跳过，无副作用

    stale = broker.requeue_stale(now=2.0)
    assert stale == ["t-1"], "超 visibility 的任务会重投"
    assert t.run(broker, now=2.5) == "t-1 已完成过，幂等跳过"
    print("OK: 分片任务 + 幂等键把『丢失』降级为『重复且无害』")


if __name__ == "__main__":
    main()
```

**追问 1**：`task_acks_late=True` 有什么代价？
→ 一句话提示：任务完成才 ACK，worker 崩溃时消息会重投（不丢但重复）；配合 prefetch=1 防止一个 worker 预取一堆长任务；吞吐下降、重复副作用要求任务必须幂等。

**追问 2**：为什么 CPU 密集和 IO 密集任务要分开队列部署？
→ 一句话提示：CPU 密集任务占满 prefork 子进程时，同队列的 IO 快任务被排队，P99 由最慢任务决定；分队列隔离后再分别调 pool 类型（CPU 用 prefork/单进程，IO 用 gevent）与并发度。

## 背诵要点
- 丢任务链路 = 超时硬杀/worker 判死 + ACK 未回 + visibility_timeout 窗口：窗口内"消失"，窗口后重复；Redis broker 特有 visibility 语义要吃透。
- 治理组合：任务分片（20 分钟→5 分钟）+ 幂等键落库 + soft_time_limit 优雅退出 + acks_late/prefetch=1。
- CPU 密集与 IO 任务分队列分池部署，避免长任务拖垮同队列 P99。

## 复盘追问
- 为什么"监控心跳告警"这次没救回来？提示：心跳恢复后任务仍在 visibility 窗口内，监控缺的是"执行中任务数 vs 完成事件数"的对账指标；事件流是最终一致，不能只看实时告警。
- gevent/eventlet 池跑 CPU 密集任务会发生什么？提示：协程切换靠 IO 阻塞点触发，纯 CPU 计算不 yield，单 worker 内所有并发任务与心跳全部冻结——CPU 任务绝不能上协程池。
