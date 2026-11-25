---
title: [A144] SLA 赔偿条款：对外承诺的工程化
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A144 · SLA 赔偿条款

> 难度:★★★ | 标签:SLA, 对外承诺, 场景题

**问**（笔试·场景题）：销售给客户签了「99.9% 可用性，违反赔偿月费 10%」——工程团队拿到这个承诺怎么处理（先算「这个 SLA 我们能不能做到」），99.9% 的预算分配（每月允许停机 43.2 分钟——怎么分配给计划内/计划外），「赔偿计算」的数据口径（谁的监控算数），「依约赔偿」和「事故复盘」的联动机制是什么？

**答**：① 承诺评估：99.9% = 月停机预算 43.2 分钟——拆账：计划内维护（滚动发布/升级，约 20 分钟/月）+ 计划外（故障）≈ 23 分钟——**23 分钟/月 对应可用性 99.95% 的内部要求**（内部标准必须严于对外承诺，留缓冲）；做不到就谈条款（排除计划内维护窗/调低 SLA/缩赔偿范围），签完再发现做不到是双输。② 预算分配：43.2 分钟按风险分池——维护窗 20 分、单次故障平均 10 分（MTTR）→ 允许 ~2 次故障/月；单次故障超预算即吃赔偿——每次事故复盘必须记录「本月剩余 SLA 预算」，剩 5 分钟时的发布策略自动收紧（等效错误预算烧尽，Q7520 联动）。③ 计算口径：**以客户侧探针为准**（客户从它的网络访问的成功率——不是你自己的监控自说自话），第三方监控（StatusPage 类）仲裁；SLA 计算要排除条款约定的例外（客户自身网络问题/不可抗力/维护窗）。④ 赔偿与复盘联动：触发赔偿的事故自动升级（最高优先级复盘 + 行动项必须含「防复发」+ 下月同类事故赔偿翻倍条款（合同里写）——让「习惯性赔钱」不可持续。

```python
# 全部标准库；demo 实现「SLA 预算账 + 客户探针口径 + 赔偿触发升级」
import time

def sla_budget(availability: float = 0.999, days: int = 30) -> dict:
    total_min = days * 24 * 60
    budget_min = total_min * (1 - availability)
    planned = 20.0                              # 计划内维护（已排除在 SLA 外则扣回）
    unplanned_budget = budget_min - planned
    return {"budget_min": round(budget_min, 1), "planned_min": planned,
            "unplanned_budget_min": round(unplanned_budget, 1),
            "internal_availability_needed": round(1 - unplanned_budget / (total_min - planned), 5)}

def compensation(downtime_min: float, monthly_fee: float = 100000,
                 rate: float = 0.10, cap: float = 0.30) -> float:
    return min(downtime_min / 43.2 * rate, cap) * monthly_fee

class SLATracker:
    def __init__(self, monthly_budget_min: float = 23.0):
        self.budget = monthly_budget_min
        self.used = 0.0
        self.incidents: list[dict] = []
    def record_incident(self, downtime_min: float, root_cause: str):
        self.used += downtime_min
        comp = compensation(downtime_min)
        escalated = comp > 0
        self.incidents.append({"downtime": downtime_min, "comp_pct": comp / monthly_fee * 100,
                               "cause": root_cause, "escalated": escalated,
                               "remaining": max(0, self.budget - self.used)})
        return self.incidents[-1]
    def release_gate(self) -> str:
        remaining = self.budget - self.used
        if remaining < 5:
            return "发布收紧：SLA 预算 <5 分钟，仅 L1 热修可发布"
        if remaining < 10:
            return "发布降频：仅灰度小步发布"
        return "normal"

if __name__ == "__main__":
    b = sla_budget()
    print("SLA 预算账:", b)
    assert b["unplanned_budget_min"] == 23.2
    tr = SLATracker(budget_min=23.0)
    i1 = tr.record_incident(12, "缓存雪崩")
    print("事故 1:", i1, "→ 赔偿", f"{i1['comp_pct']:.1f}%")
    print("发布闸:", tr.release_gate())
    i2 = tr.record_incident(15, "发布引入（同型第二次）")
    print("事故 2:", i2, "→ escalated:", i2["escalated"], "（触发复盘升级+防复发条款）")
    assert tr.release_gate().startswith("发布收紧")
    print("SLA 预算 <5 分钟 → 发布自动收紧 ✅")
    # 口径：内部标准严于对外承诺；客户侧探针仲裁；赔偿触发自动升级复盘+防复发条款。
```

**追问**：1) 为什么「内部标准必须严于对外承诺」？——承诺是硬合同（赔偿+信誉），内部标准是达成承诺的手段；内部=对外（99.9 对 99.9）意味着任何小抖动直接吃赔偿——99.95 内对 99.9 外留 2 倍缓冲。2) 「客户侧探针为准」对我们意味着什么？（提示：我们的 P99 再好，客户网络慢也算我们不可用（从它的视角）——要么在 SLA 条款里定义「服务侧可用性」的精确测量点（API 网关 200 率），要么把客户网络问题排除条款写清——测量口径是 SLA 争议的第一战场）3) 赔偿翻倍条款合理吗？（提示：对「同型重复事故」合理（倒逼根因修复），但要限定「同根因」且复检通过后重置——无差别翻倍会让团队隐瞒事故，与 blameless 文化冲突）

## 背诵要点
1. 99.9% = 月停机 43.2 分钟，拆账：维护窗 20 分 + 计划外 23 分 → 内部要求 99.95（严于对外留缓冲）。
2. 赔偿口径以客户侧探针/第三方监控为准，条款例外（维护窗/不可抗力/客户网络）必须写清。
3. SLA 预算联动发布闸（剩 <5 分钟收紧发布）；赔偿触发自动升级复盘 + 同型翻倍条款。

## 复盘追问
1. 销售又接了一个「99.99% + 1 秒级响应」的客户，工程说做不到，怎么破局？（提示：拆承诺——99.99% 只对核心 API（简单只读）承诺，复杂接口不进 SLA；响应时间写「P95」不写「1 秒」（尾部不可承诺）；方案分级报价（高 SLA 高定价）——工程与销售同坐一桌谈条款，而不是签完抗议）
2. SLA 达标月（没赔偿）但客户流失了，为什么 SLA 没保护业务？（提示：SLA 只承诺「可用」不承诺「好用」——质量/性能/支持是另一层承诺；SLA 是底线不是竞争力，客户因体验流失与 SLA 无关——产品体验才是留存主战场）
