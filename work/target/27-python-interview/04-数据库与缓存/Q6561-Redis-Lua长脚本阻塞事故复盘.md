---
title: "[Q6561] Redis Lua 长脚本阻塞主线程事故复盘"
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6561 · Redis Lua 长脚本阻塞主线程事故复盘

难度：P6 ｜ 标签：Redis / Lua / 阻塞 / 事故复盘

**问**：一次批量统计任务里，运维把一段遍历 50 万个 key 的 Lua 脚本丢进 Redis 执行，随后所有业务命令超时、连接池打满，应用雪崩。复盘：为什么一段 Lua 能拖垮整个实例？Python 应用侧怎么防御？

**答**：

**结论**：Redis 执行 Lua/EVAL 期间是单线程原子执行，脚本没跑完就不会处理任何其他命令——这既是原子性的来源，也是阻塞的根源。50 万次循环哪怕每次 1 微秒也要几百毫秒起步，叠加网络栈不可调度，P99 直接从毫秒级飙到秒级，连接池排队打满后把故障传导到应用层。

**取舍**：Lua 的价值在于"把多步读改写压成一次网络往返 + 原子执行"，但它只适合 O(1)~O(logN) 的小操作。大批量遍历应该拆成：SCAN 分批 + 客户端聚合，或者预聚合（用 hash/zset 维护计数器，而不是事后全量扫描）。 Functions（Redis 7+）同样运行在主线程，不解决阻塞问题。

**实战**：三层防线——① 脚本上限门禁：code review 时约定循环内操作数上限，禁止在 Lua 里 SCAN/KEYS；② 应用侧给 eval 调用设独立的短超时（如 100ms），并与其他业务用不同连接池隔离，避免池被打满外溢；③ 监控上对 `latency monitor` 的 `lua-script` 事件与慢日志中含脚本 sha 的记录告警。事故当时的应急手段是 `SCRIPT KILL`（脚本未写过数据时可用；写过则只能 `SHUTDOWN NOSAVE`）。

```python
# 用单线程调度模拟 Redis 主线程：长 Lua 脚本独占 CPU，其他命令排队等待
# 仅标准库，Python 3.9+
from __future__ import annotations

import heapq
import time


class FakeRedisServer:
    """模拟单线程 Redis：命令按到达顺序执行，长脚本独占时间片。"""

    def __init__(self, command_cost_us: float = 2.0) -> None:
        self.command_cost_us = command_cost_us
        self.clock_us = 0.0  # 服务器内部时钟（微秒）
        self.queue: list[tuple[float, str]] = []  # (到达时刻, 命令名)
        self._arrive_order = 0

    def arrive(self, name: str) -> None:
        self._arrive_order += 1
        # heapq 用 (到达时刻, 序号) 保证 FIFO
        heapq.heappush(self.queue, (self.clock_us, self._arrive_order, name))
        heapq.heapify(self.queue)  # 保持结构（简单起见）

    def run(self, budget_cmds: int = 10**9) -> dict[str, float]:
        wait: dict[str, float] = {}
        served = 0
        while self.queue and served < budget_cmds:
            arrive, _, name = heapq.heappop(self.queue)
            wait[name] = self.clock_us - arrive
            if name.startswith("lua:"):
                cost = float(name.split(":")[2])  # 长脚本独占整个执行时长
            else:
                cost = self.command_cost_us
            self.clock_us += cost
            served += 1
        return wait


def main() -> None:
    srv = FakeRedisServer(command_cost_us=2.0)
    # 场景：一个 400ms 的 Lua 脚本执行期间，来了 5 条普通 GET
    srv.arrive("lua:stat:400000")  # 400000us = 400ms
    for i in range(5):
        srv.arrive(f"get:key{i}")
    waits = srv.run()
    print("每条命令的排队等待(us)：")
    for k, v in waits.items():
        print(f"  {k:<20} wait={v:>10.0f}")
    worst = max(waits.values())
    assert worst >= 398_000, "GET 应被 Lua 阻塞近 400ms"
    print(f"结论：单条 Lua 独占 400ms，后续 GET 最坏等待 {worst/1000:.0f}ms")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么 `SCRIPT KILL` 有时杀不掉？——脚本已经执行过写命令时，Redis 为保证原子性不允许半途终止，只能 `SHUTDOWN NOSAVE` 重启，丢掉未持久化数据；所以写脚本必须先想清楚终止路径。
- 追问 1.1：那 Redis 7 的 Functions 是不是就没这个问题了？——不是。Functions 只是脚本的组织方式（持久化、按库名管理），执行模型同样是主线程原子运行；真正的缓解是 7.x 的脚本超时 `busy-reply-threshold` 让客户端收到 BUSY 错误，但脚本本身仍会跑完。
- 追问 2：应用侧为什么建议给 eval 单独的连接池和超时？——共享池时，被阻塞的 eval 连接会占用池槽位，后续所有业务拿不到连接，故障从"一个慢脚本"放大为"全站不可用"；隔离后爆炸半径被限制在统计这条业务线上。

**背诵要点**：

1. Redis Lua 在主线程原子执行，脚本未结束不处理任何其他命令，O(N) 循环会把全实例 P99 打到秒级。
2. 应急分界：脚本没写过数据用 `SCRIPT KILL`，写过只能 `SHUTDOWN NOSAVE`；监控盯 `latency monitor` 的 lua 事件。
3. 防御三板斧：脚本循环上限门禁、eval 独立连接池+短超时隔离、大批量改 SCAN 分批客户端聚合。

**复盘追问**：

1. 如果这个统计需求没法改掉"全量扫描"，你如何在架构上把它与在线流量彻底隔离？
2. 连接池被打满导致雪崩的传导链，你会用哪些指标在哪个环节最先发现？
