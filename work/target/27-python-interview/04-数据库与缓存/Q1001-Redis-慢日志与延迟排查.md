---
title: [Q1001] Redis 慢日志与延迟排查
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1001 · Redis 慢日志与延迟排查

> 难度:★★★★ | 标签:慢日志, 排查

**问**:Redis 变慢,排查的完整思路是什么?slowlog 怎么配怎么看?

**答**:先分层定位:一、确认是"单命令慢"还是"整体延迟"——SLOWLOG GET 记录执行超 slowlog-log-slower-than(默认 10ms,建议 1ms)的命令,看到 KEYS/大集合全量命令/复杂 Lua 即元凶;二、单命令都很快但延迟抖动——查 fork(RDB/AOF 重写时 copy-on-write 卡顿,latest_fork_usec)、AOF 刷盘策略(everysec 阻塞到 2s)、内存交换、网络、单核 CPU 打满(infO CPU 的 sys 高说明碎片整理或 fork);三、延迟监控用 redis-cli --latency 与 LATENCY HISTORY 事件。经验值:生产禁用 KEYS、大 value 限制、everysec 换盘读写分离。排查顺序化:指标(命中率/RT) -> 慢日志 -> 系统层(fork/swap/IO)。

```python
# file: code/04_数据库与缓存/q1001_slowlog.py
"""模拟 slowlog: 记录超阈值命令并给出治理建议"""
import time
from collections import deque

class SlowLog:
    def __init__(self, threshold_ms=1.0, maxlen=128):
        self.threshold, self.log = threshold_ms, deque(maxlen=maxlen)

    def execute(self, cmd, cost_ms):
        if cost_ms >= self.threshold:
            self.log.appendleft((time.strftime("%H:%M:%S"), cmd, cost_ms))

    def report(self):
        tips = {"KEYS": "生产禁用, 改 SCAN", "HGETALL": "大 hash 拆分或 HSCAN",
                "SMEMBERS": "改 SSCAN", "LRANGE0-1": "限制范围", "EVAL": "缩短脚本"}
        for ts, cmd, ms in self.log:
            head = cmd.split()[0]
            tip = tips.get(cmd, tips.get(head, "检查数据规模"))
            print(f"{ts} {ms:6.1f}ms {cmd}  -> {tip}")

if __name__ == "__main__":
    sl = SlowLog()
    sl.execute("GET user:1", 0.2)                  # 未超阈值不记录
    sl.execute("KEYS *", 850.0)
    sl.execute("HGETALL feed:2", 120.0)
    sl.execute("EVAL ...", 45.0)
    sl.report()
    print("配置: slowlog-log-slower-than 1000 (微秒), slowlog-max-len 128")
```

**追问**:
- fork 卡顿怎么确认?——info stats 的 latest_fork_usec,大实例(10GB+)RDB 触发时可能几十上百毫秒,控制实例大小 10GB 内或低峰持久化。
- --latency 与 slowlog 的区别?——slowlog 只看命令执行时间,--latency 测端到端 RTT(含网络与排队),两者结合才能区分"命令慢"与"链路慢"。

---
