---
title: [Q505] 计时时钟的选择:perf_counter 与 monotonic
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q505 · 计时时钟的选择:perf_counter 与 monotonic

> 难度:★★☆☆ | 标签:time, 计时

**问**:测代码耗时为什么不该用 time.time()?四个时间函数各适合什么?

**答**:time.time 是墙钟,受 NTP 校时与人工调整影响会回跳,测耗时可能出现负数;time.monotonic 保证单调递增,是计算时间间隔的正解;time.perf_counter 是最高分辨率的单调时钟,基准测量用它;time.process_time 只统计 CPU 时间(不含 sleep),衡量计算量而非性能感受。配套缓存语义同理(Q444 的 TTL 用 monotonic)。time.time 的正确用途是「挂钟语义」:日志时间戳、与外部系统对表。

```python
# file: code/01_语言核心与底层/q505_monotonic_clock.py
import time

if __name__ == "__main__":
    print("time.time()      :", time.time(), "wall clock")
    print("time.monotonic() :", time.monotonic(), "monotonic")
    print("time.perf_counter():", time.perf_counter(), "high-res")
    print("time.process_time():", time.process_time(), "cpu only")

    start_wall = time.perf_counter()
    start_cpu = time.process_time()
    time.sleep(0.05)                      # 睡眠计入墙钟,不计 CPU
    print("wall elapsed:", round(time.perf_counter() - start_wall, 4))
    print("cpu elapsed :", round(time.process_time() - start_cpu, 4))
    print("monotonic non-decreasing:", time.monotonic() >= start_wall)
```

**追问**:1) perf_counter 的起点是什么?——未定义的任意点(通常系统启动),不同进程间不可比;跨进程对时只能用 time.time 或 time.time_ns。2) 三种时钟怎么选?——time.time 墙钟(日志时间戳、对外对时)但可被调整;monotonic 保证单调,适合超时与重试间隔;perf_counter 高分辨率单调,适合 benchmark;process_time 只算 CPU 时间不含等待。3) 底层来源?——封装 OS 时钟(clock_gettime 的 CLOCK_MONOTONIC/CLOCK_MONOTONIC_RAW 等),分辨率与精度由内核与硬件决定,time.time_ns(3.7+)提供纳秒接口避免浮点丢精度。4) 生产陷阱?——用 time.time 做重试间隔,NTP 回拨让超时逻辑错乱;benchmark 用 time.time,分辨率不够测不出差异;两套时钟混着相减。
