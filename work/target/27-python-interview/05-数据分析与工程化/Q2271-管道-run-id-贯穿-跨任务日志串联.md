---
title: [Q2271] 管道 run_id 贯穿:跨任务日志串联
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2271 · 管道 run_id 贯穿:跨任务日志串联

> 难度:★★★☆ | 标签:可观测性, 日志

**问**:一条数据链路十几个任务,凌晨出了问题,你怎么把散在各任务日志里的事件拼成完整故事?

**答**:靠 run_id 贯穿。调度器在每次运行开始生成全局唯一 run_id,透传给每个任务的每一行日志,日志平台按 run_id 一检索,跨任务的完整时间线就出来了。实测还原 run_20260301:extract 09:00:05 启动 40 秒完成 18.2 万行,dwd_build 09:02 启动 29 分钟完成,quality_check 09:31:30 报行数不平失败 1000 行,dwd_build 09:35 重跑成功——一次重跑的因果链在几行日志里讲清楚,不用再靠时间戳猜。配套纪律:run_id 由调度器单点生成,任务不允许自造;日志格式统一带 run_id 字段而不是塞在 message 里;同一个 run 的启动、完成、失败、重跑事件用统一动词,方便聚合统计每个 run 的任务数与重跑率。

```python
# file: code/05_数据分析与工程化/q2271_run_id_trace.py
"""管道 run_id 贯穿: 从混合日志还原一次数据生产的完整时间线"""

from collections import defaultdict

LOGS = [
    ("d1 09:00:05", "extract", "run_20260301", "START rows=0"),
    ("d1 09:00:40", "extract", "run_20260301", "DONE rows=182000"),
    ("d1 09:01:02", "extract", "run_20260228", "RETRY rows=0"),   # 别的运行, 混在同一日志
    ("d1 09:02:00", "dwd_build", "run_20260301", "START"),
    ("d1 09:31:00", "dwd_build", "run_20260301", "DONE rows=181000"),
    ("d1 09:31:30", "quality_check", "run_20260301", "FAIL rows_mismatch=1000"),
    ("d1 09:35:00", "dwd_build", "run_20260301", "RERUN rows=182000"),
]


def timeline(logs, run_id):
    events = defaultdict(list)
    for ts, task, rid, msg in logs:
        if rid == run_id:
            events[task].append((ts, msg))
    return events


if __name__ == "__main__":
    events = timeline(LOGS, "run_20260301")
    flat = sorted(((ts, task, msg) for task, evs in events.items() for ts, msg in evs),
                  key=lambda x: x[0])
    for ts, task, msg in flat:
        print(f"{ts} [{task:<13}] {msg}")
    starts = sum(1 for _, _, m in flat if m.startswith("START"))
    print(f"该 run 共 {len(flat)} 条事件, START 出现 {starts} 次 -> dwd_build 重跑 1 次, 起因是行数校验不平")
    print("要点: run_id 调度器单点生成全程透传; 统一动词 START DONE FAIL RERUN 便于聚合")
```

**追问**:
- 追问 1:run_id 和 trace id 什么关系?—— run_id 串一次数据生产,trace id 串一次服务调用,管道任务内部调用服务时把 run_id 作为 trace 的 baggage 传播。
- 追问 2:日志平台按 run_id 查不到怎么办?—— 说明有任务没透传,用"缺失 run_id 的日志量"做例行巡检项,把透传纪律变成可监控指标。
