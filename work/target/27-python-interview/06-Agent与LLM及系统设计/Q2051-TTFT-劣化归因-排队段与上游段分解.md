---
title: [Q2051] TTFT 劣化归因:排队段与上游段分解
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2051 · TTFT 劣化归因:排队段与上游段分解

> 难度:★★★☆ | 标签:LLM运维, 时延, 归因

**问**:TTFT 破线了,是你们排队排的,还是供应商变慢了?怎么定位?

**答**:把 TTFT 拆成两段记账:排队段从进入到拿到上游配额,上游段从发出到首 token 回来,两段之和必须拼回总时延,这是记账正确性的断言。归因规则用基线对比:上游段 p95 与健康基线比,暴涨一点五倍以上判上游劣化;排队段 p95 逼近甚至超过上游基线判排队劣化。演示里一成样本撞上限流、排队飙到九百毫秒,归因指向 queue;供应商变慢的场景指向 upstream;都正常时报 none。归因结论决定处置动作:排队型扩容或限流,上游型换路或降速,方向错了烧钱白费。

```python
# file: code/06_Agent与LLM及系统设计/q2051_ttft_attribution.py
"""TTFT 劣化归因:首 token 时延拆成排队段与上游段,p95 劣化定位到具体段。"""


def p95(xs):
    if not xs:
        return 0.0
    xs = sorted(xs)
    return xs[max(0, min(len(xs) - 1, int(round(0.95 * len(xs))) - 1))]


def attribute(samples):
    """samples: [{ttft, queue, upstream}] 返回分段 p95 与劣化主导段。"""
    seg = {}
    for k in ("queue", "upstream"):
        seg[k] = round(p95([s[k] for s in samples]), 1)
    base_upstream = round(p95([s["upstream"] for s in samples if not s.get("anomaly")]), 1)
    if seg["queue"] >= base_upstream * 1.5:
        dominant = "queue"
    elif seg["upstream"] >= base_upstream * 1.5:
        dominant = "upstream"
    else:
        dominant = "none"
    for s in samples:
        assert abs(s["queue"] + s["upstream"] - s["ttft"]) < 0.01, "分段必须能拼回总时延"
    return {"queue_p95": seg["queue"], "upstream_p95": seg["upstream"],
            "baseline_upstream_p95": base_upstream, "dominant": dominant}


if __name__ == "__main__":
    # 基线:上游稳定 200ms,排队 20ms
    normal = [{"ttft": 220, "queue": 20, "upstream": 200}] * 20

    # 场景一:10% 样本撞上限流,排队飙到 900ms,上游不变
    queued = normal[:]
    for _ in range(2):
        queued.append({"ttft": 1100, "queue": 900, "upstream": 200})
    a1 = attribute(queued)
    assert a1["dominant"] == "queue", a1
    assert a1["queue_p95"] == 900 and a1["upstream_p95"] == 200

    # 场景二:上游供应商变慢,排队正常
    slow = normal[:10] + [{"ttft": 1200, "queue": 20, "upstream": 1180, "anomaly": True}
                          for _ in range(12)]
    a2 = attribute(slow)
    assert a2["dominant"] == "upstream", a2
    assert a2["upstream_p95"] > a2["baseline_upstream_p95"] * 1.5

    # 场景三:都正常
    a3 = attribute(normal)
    assert a3["dominant"] == "none"
    print("归因通过:排队型劣化指认 queue,上游型指认 upstream,分段可拼回总时延")
```

**追问**:
- 基线怎么取? 答:取近期健康时段的分位数滚动更新,重大变更后重置基线
- 段还可以再拆吗? 答:可以,上游段内再拆网络与首字生成,拆分粒度跟着埋点成本走
