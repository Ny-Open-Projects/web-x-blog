---
title: [Q374] time.time、time.monotonic 与 perf_counter 怎么选
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q374 · time.time、time.monotonic 与 perf_counter 怎么选

> 难度:★★☆ | 标签:time, 时钟, 性能测量

**问**:测量代码耗时为什么不该用 `time.time()`?

**答**:`time.time()` 是墙钟,可能被 NTP 回拨或人为调整,测量间隔不可靠。`time.monotonic()` 单调不减、不受系统时间影响,适合算耗时、限速器和超时判断;`time.perf_counter()` 是最高精度的单调时钟,包含睡眠,专用于基准测试;`time.process_time()` 只计 CPU 时间不含 IO 等待。规则:对外展示用 `time.time()`/datetime,对内计时一律 monotonic 系。

```python
# file: code/02_并发与网络工程/q374_monotonic.py
"""三种时钟的选择演示。"""
import time

if __name__ == "__main__":
    # 基准测量:perf_counter 精度最高
    start = time.perf_counter()
    sum(range(1_000_000))
    print(f"CPU 耗时 perf_counter: {time.perf_counter() - start:.6f}s")

    # 业务限速/超时:monotonic
    deadline = time.monotonic() + 0.2
    while time.monotonic() < deadline:
        pass
    print("deadline 轮询结束, 未超时:", time.monotonic() <= deadline + 0.05)

    # 墙钟:用于日志时间戳、对外展示
    print("wall clock:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 对比:process_time 不含 sleep
    s = time.process_time()
    time.sleep(0.1)
    print(f"sleep 0.1s 后 process_time 只增加 {time.process_time() - s:.6f}s")
```

**追问**:
- 事件序号可以用 time.time() 生成吗?不可靠,同一毫秒可能重复且可能回拨;用单调递增序列、UUID 或 ULID。
- monotonic 会跨进程一致吗?——不会,每个系统起点不同且不可跨机器比较;跨主机计时用 NTP 校准的墙钟并接受误差。
- perf_counter 包含 sleep 吗?——包含(挂钟类单调时钟);process_time 不含等待只算 CPU,压测报告要写清用的哪个。
- 超时判断为什么禁止 time.time()?——NTP 回拨会让已超时的调用「重新变未超时」;所有 deadline 计算用 monotonic。
