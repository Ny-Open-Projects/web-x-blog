---
title: [Q7520] LLM 应用的 SLO：质量预算与延迟分位
date: 2026-11-19
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7520 · LLM 应用 SLO

> 难度:★★★ | 标签:SLO, 延迟, 质量

**问**：LLM 应用怎么定 SLO——「P99 延迟」在流式生成场景是什么含义（TTFT vs 总时长）？「回答质量」这种主观指标怎么写成可测的 SLO（抽样评分 / 用户信号代理）？错误预算用完（质量 SLO 跌破）时该做什么——和传统服务的错误预算有什么不同？

**答**：① 延迟 SLO 双指标：**TTFT**（time-to-first-token，用户「开始看到反应」的体验锚点，P99 < 2s）与**总时长**（P95 < 15s，长回答容忍度高）——流式场景只盯总延迟会掩盖「用户等第一个字等了 10s」的最痛体验。② 质量 SLO 可测化三代理：**抽样人工/LLM 评分**（每日随机 100 条回答 LLM-as-judge 打分，P95 ≥ 4/5）、**用户信号**（点赞率/复制率/追问重述率——重述率高=没答对）、**任务完成率**（代码类：编译通过率；抽取类：字段校验通过率——能自动化验证的任务优先）。③ 错误预算差异：传统服务预算 = 可用性缺口时间；LLM 应用预算 = **质量亏损条数**（跌破评分阈值的回答占比）——预算耗尽时做的事也不同：不是「停止发布」，而是**冻结 prompt/模型版本 + 排查漂移**（上游模型静默更新是质量 SLO 突跌的头号嫌疑）。

```python
# 全部标准库；demo 实现 SLO 记账（双延迟指标 + 质量抽样 + 预算）
import random, statistics, time
from collections import deque

class LLM_SLO:
    def __init__(self, ttft_p99=2.0, total_p95=15.0, quality_p95=4.0,
                 budget_ratio=0.05):
        self.ttft_p99, self.total_p95, self.q_p95 = ttft_p99, total_p95, quality_p95
        self.budget = budget_ratio
        self.recent = deque(maxlen=2000)
    def record(self, ttft: float, total: float, quality: float | None,
               user_signal: str | None = None):
        self.recent.append({"ttft": ttft, "total": total, "q": quality,
                            "sig": user_signal})
    def report(self) -> dict:
        ttfts = sorted(r["ttft"] for r in self.recent)
        totals = sorted(r["total"] for r in self.recent)
        qs = [r["q"] for r in self.recent if r["q"] is not None]
        restate = sum(1 for r in self.recent if r["sig"] == "restate")
        ttft_p99 = ttfts[int(0.99 * len(ttfts))] if ttfts else 0
        total_p95 = totals[int(0.95 * len(totals))] if totals else 0
        q_p95 = statistics.quantiles(qs, n=20)[18] if len(qs) >= 20 else 5.0
        bad_q = sum(1 for q in qs if q < 3) / max(len(qs), 1)   # 质量亏损率
        budget_left = self.budget - bad_q
        return {"ttft_p99": round(ttft_p99, 2), "total_p95": round(total_p95, 1),
                "quality_p95": round(q_p95, 2),
                "quality_budget": f"{budget_left:+.2%}",
                "restate_rate": f"{restate/len(self.recent):.1%}",
                "action": "FREEZE_VERSION+查上游漂移" if budget_left <= 0 else "healthy"}

if __name__ == "__main__":
    random.seed(5)
    slo = LLM_SLO()
    for _ in range(300):
        slo.record(ttft=random.uniform(0.8, 2.5), total=random.uniform(5, 20),
                   quality=random.uniform(3.0, 5.0) if random.random() < 0.1 else None,
                   user_signal="restate" if random.random() < 0.15 else "ok")
    r = slo.report()
    print(r)
    assert r["ttft_p99"] > 2.0, "演示数据应触发 TTFT 违约"
    assert r["action"].startswith("healthy") or "FREEZE" in r["action"]
    print("SLO 记账：TTFT P99 / 总时长 P95 / 质量抽样评分 / 预算四指标齐备 ✅")
    # 口径：质量亏损预算（如 5% 低分回答）耗尽 → 冻结版本查上游漂移，
    # 不是传统服务的「停止发布」——漂移源在供应商侧。
```

**追问**：1) 为什么 TTFT 是流式体验的第一指标？——用户对「开始响应」极敏感（<1s 感觉即时），对「总时长」宽容（长答案反而说明认真）；TTFT 由首 token 生成速度决定（模型 prefill + 网关排队），优化方向与总时长完全不同（路由排队 vs 生成速度）。2) 抽样评分的样本偏差怎么控？——随机抽样（非投诉驱动——投诉样本质量天然差）、分层抽样（按场景/时段）、评分器与业务指标对齐（Q7501 校准）；样本偏差会让 SLO 虚高虚低。3) 上游模型静默漂移怎么发现？——固定回归集每日跑（Q7509 评估固定集回归），分数异常日检报告；这是「质量 SLO 突跌但没人改任何东西」的标准排查第一步。

## 背诵要点
1. 流式延迟双指标：TTFT P99（体验锚点）+ 总时长 P95——只盯总延迟掩盖首 token 痛点。
2. 质量 SLO 三代理：抽样评分（LLM-judge 校准）、用户信号（重述率）、任务完成率（可自动化验证优先）。
3. 质量预算耗尽的动作 = 冻结版本 + 查上游静默漂移（固定回归集日检）——与传统「停发布」不同。

## 复盘追问
1. 你的质量 SLO P95=4.5 但用户投诉不断，哪个环节错了？（提示：抽样偏差（采样频率/分层）、评分器与用户实际标准脱节——重述率等用户信号与评分背离时信用户）
2. SLO 四指标全绿但成本爆了，SLO 设计漏了什么？（提示：成本也是 SLO 的一部分（$/千次会话），四指标之外加成本护栏，Q7519 灰度的成本指标联动）
