---
title: [Q1377] 容量水位估算:Little 定律落地
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1377 · 容量水位估算:Little 定律落地

> 难度:★★★ | 标签:容量, 性能

**问**:给你目标 QPS 和单请求耗时,怎么算要部署多少并发?水位怎么留?

**答**:用 Little 定律 `L = λ × W`:所需并发 = QPS × 平均耗时。例:500 QPS × 50ms = 25 平均并发,乘峰值系数(常见 2 倍,按流量波动定)得峰值并发,再乘安全余量(20%-40%)得到部署并发;反方向 `λ = L / W` 可验证"这套并发能扛的最大 QPS"。水位线的用途是**扩容触发器**:运行并发持续超过水位的 70%-80% 就扩容,而不是等打满。注意协程应用的理论并发上限不等于有效并发,IO 等待与下游连接池都会截断它,数字要靠压测校准。

```python
# file: code/03_Web后端开发/q1377_capacity_plan.py
"""Little 定律容量估算与水位(纯标准库)。"""


def capacity_plan(qps, latency_s, peak_factor=2.0, headroom=0.3):
    avg_conc = qps * latency_s                # Little 定律 L = λ W
    peak_conc = avg_conc * peak_factor
    provision = peak_conc * (1 + headroom)
    max_qps = provision / latency_s           # 反推可扛 QPS
    return {"avg_concurrency": round(avg_conc, 1), "peak": round(peak_conc, 1),
            "provision": round(provision, 1), "max_qps": round(max_qps)}


for name, qps, lat in (("读接口", 500, 0.05), ("导出接口", 20, 2.0), ("聚合接口", 2000, 0.08)):
    print(f"{name:6s}", capacity_plan(qps, lat))
print("扩容触发线:运行并发持续超过 provision 的 75%")
```

**追问**:
- 峰值系数从哪来?——历史流量按天/周取 P99 与均值之比,大促型业务再叠活动系数。
- 下游连接池怎么参与估算?——并发需求除以单请求占用连接数,池上限必须大于峰值并发,否则排队在池上表现为延迟抖动。
