---
title: [Q1449] AB 实验的护栏:SRM、污染与护栏指标
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1449 · AB 实验的护栏:SRM、污染与护栏指标

> 难度:★★★★ | 标签:AB 测试, 实验质量

**问**:实验组转化率涨了 5%,你敢直接上报吗?上线前你会先查什么?

**答**:先查三条护栏,任何一条不过都不能看业务指标。第一是 SRM 样本比完整性校验:配置五五分的实验,实际分桶比若显著偏离预期(z 检验超过 1.96),说明分流服务有 bug、埋点丢失或过滤逻辑不对,这时的"提升"大概率是假的;第二是样本污染检测:同一用户出现在多个实验组,说明分流粘性失效,通常是缓存键用错或登录态切换导致;第三是护栏指标:延迟、错误率、崩溃率等工程指标若在实验组显著劣化,即使转化率涨了也要停——那是用体验换的数字。这三条都过了,再看业务指标并结合置信区间判断。护栏检查要自动化:实验平台每天跑一次,失败自动冻结实验并通知 owner,而不是靠人记得去查。

```python
# file: code/05_数据分析与工程化/q1449_ab_guardrail.py
"""AB 实验护栏:SRM 校验、样本污染检测与护栏指标突变"""

import math
from statistics import NormalDist


def srm_check(observed, expected_ratio, z=1.96):
    """样本比完整性校验:实际分桶比偏离配置比过大说明分流有 bug"""
    total = sum(observed.values())
    ratios = list(expected_ratio.values())
    base = sum(ratios)
    worst = None
    for name, n in observed.items():
        expect = total * ratios[list(observed).index(name)] / base
        sigma = math.sqrt(total * (expect / total) * (1 - expect / total))
        zz = (n - expect) / sigma if sigma else 0.0
        if worst is None or abs(zz) > abs(worst[1]):
            worst = (name, zz)
    name, zz = worst
    return {"worst_bucket": name, "z": round(zz, 2),
            "srm_violated": abs(zz) > z}


def pollution_check(assignments):
    """同一用户出现在多个实验组,分流服务粘性失效的典型信号"""
    seen = {}
    polluted = set()
    for user, group in assignments:
        if user in seen and seen[user] != group:
            polluted.add(user)
        seen[user] = group
    return polluted


GUARD_BASELINE = {"p99_latency_ms": 200, "error_rate": 0.01}


def guardrail_check(current):
    alerts = []
    if current["p99_latency_ms"] > GUARD_BASELINE["p99_latency_ms"] * 1.1:
        alerts.append("p99 延迟涨幅超 10%")
    if current["error_rate"] > GUARD_BASELINE["error_rate"] * 1.5:
        alerts.append("错误率涨幅超 50%")
    return alerts


if __name__ == "__main__":
    print("SRM:", srm_check({"control": 5210, "treatment": 4790},
                            {"control": 1, "treatment": 1}))
    polluted = pollution_check([("u1", "control"), ("u1", "treatment"), ("u2", "treatment")])
    print("污染用户:", polluted or "无")
    print("护栏:", guardrail_check({"p99_latency_ms": 260, "error_rate": 0.008}) or "全部正常")
    print("三条护栏任一失败都应先停实验再分析业务指标")
```

**追问**:
- 追问 1:SRM 的常见根因有哪些?—— 分流哈希键变更、机器人流量集中在单组、埋点客户端崩溃差异、按天剔除用户造成不对称。
- 追问 2:发现污染后怎么修?—— 以用户首次进入的组为准重算,或直接宣布实验作废重跑;修补分桶逻辑后数据不能拼接。
