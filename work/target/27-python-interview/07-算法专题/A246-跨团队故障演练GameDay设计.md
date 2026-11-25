---
title: [A246] 跨团队故障演练 GameDay：场景选取、注入与安全阀
date: 2026-11-23
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A246 · 跨团队 GameDay 设计

> 难度:★★★ | 标签:GameDay, 故障演练, 跨团队, 安全阀

**问**（笔试·场景题）：季度 GameDay，5 个团队联合演练——① 场景怎么选（风险矩阵看哪几维，为什么优先选「跨团队依赖断链」而不是「单服务 CPU 打满」）；② 组织怎么分工（控制官、观察员、记录员、被演练团队各管什么，被演练团队该不该提前知道具体场景，黑盒还是白盒）；③ 注入怎么做（能直接注入的用工具，碰不了别人服务时用什么替代：故障工单 / 契约层注入 / 对方自行执行）；④ 安全阀有哪些（爆炸半径预算、变更冻结窗、全局中止、双人确认、外部知情），少一个会怎样；⑤ 复盘产出什么（时间线、MTTD/MTTR、**跨团队交接损耗**、行动项与复测），怎么避免产出「加强监控」这类无法验收的空话？与 A151（混沌工程假设驱动）、A169（单团队生产注入边界）、A237（回滚能力演练）区别在哪？

**答**：① 分工：A151 讲「混沌 = 验证稳定态假设」，A169 讲单团队在生产注入的准入与爆炸半径，A237 是「回滚能力」的周期性专项；GameDay 考的是**组织协作**——同样的故障，单团队能自愈，跨团队就会暴露「告警没人认领、升级链断、信息不同步、权责不清」。所以场景必须跨团队，否则测的还是技术不是组织。② 场景选取：三维打分——**业务影响**（1-5）× **发生概率**（1-5）× **跨团队跨度**（参与团队数做放大），再乘一个「预案从未验证」的加权。优先选「高影响 + 跨 3 个以上团队 + 现有预案是纸面」的场景（支付链路下游对账不可用、区域机房断网、对外证书过期）；不选「单服务 CPU 打满」——单团队能自愈、已有压测覆盖（A121）、暴露不了协作缝隙。选型用贪心就够（场景数很少，0/1 背包属于过度设计）。③ 组织与知情范围：**控制官**唯一有权注入与中止、且不参与救火（既当裁判又当运动员必然手软）；**观察员**只记录不插手（一插手就污染了「真实响应时间」）；**记录员**维护结构化时间线（注入/首次告警/首个响应/升级/定位/缓解/恢复）；**被演练团队**只被告知「本周某天有 GameDay、影响边界是什么」，不告知具体场景与注入点——知道细节就会提前写脚本、临时加监控，测出来的是表演能力。首次演练用白盒（降低真事故风险），成熟后转黑盒。④ 注入方式三档：能直接操作的（kill pod、网络延迟、依赖返回 5xx）用混沌工具；**碰不了别人服务**时用「故障工单」（发一张 P1 工单模拟依赖故障，测对方的响应与升级链——最安全但最不真实）、「契约层注入」（在网关/服务网格给目标依赖的响应打错或加延迟，不改对方代码，真实度最高）、「对方自行执行」（控制官给脚本，对方值班按令执行，责任与操作都在对方）。所有注入必须可逆、带 TTL、有全局 kill switch。⑤ 安全阀五件套：爆炸半径预算（影响用户数/订单数上限，超了自动中止）、变更冻结窗（演练期间禁止任何团队发布，否则故障无法归因）、全局中止开关（且**事前预演过**，没试过的开关等于没有）、双人确认（控制官 + 值班经理）、外部知情（客服/业务方/法务提前知道，避免把演练当真实事故对外通报）。少任何一个都可能把 GameDay 变成一次未授权生产事故（A169 的准入条件在跨团队场景下更严）。⑥ 复盘产出：结构化时间线 → MTTD（注入→首次告警）、MTTR（告警→恢复，口径要写死，否则各部门各算各的）、**交接损耗**（跨团队 handoff 的空转时长，这是 GameDay 最有价值的独有指标）、告警准确性（首次告警是否指向真因、有没有漏报）。行动项必须可验收：不是「加强监控」，而是「把支付成功率告警路由到 payments 团队，阈值改为 99.5%，下次 GameDay 复测」——owner、期限、验证方式三件套，下次演练先复测上期项（A237 的复验门禁同构）。

```python
# 全部标准库；跨团队 GameDay 编排：场景打分选型 + 安全阀 + 时间线与 MTTD/MTTR
from dataclasses import dataclass


@dataclass
class Scenario:
    name: str
    impact: int        # 业务影响 1-5
    likelihood: int    # 发生概率 1-5
    teams: int         # 涉及团队数
    minutes: int       # 预计占用时长
    unverified: bool   # 相关预案是否从未被验证

    def score(self):
        """风险分 = 影响 × 概率 × 跨团队放大 × 未验证加权。"""
        base = self.impact * self.likelihood * (1 + 0.2 * (self.teams - 1))
        return round(base * (1.25 if self.unverified else 1.0), 2)


def plan(scenarios, budget_min, max_count=3):
    """贪心选型：按分排序，装得下就选（要最优解就是 0/1 背包，规模小没必要）。"""
    chosen, used = [], 0
    for s in sorted(scenarios, key=lambda x: (-x.score(), x.name)):
        if len(chosen) >= max_count:
            break
        if used + s.minutes <= budget_min:
            chosen.append(s)
            used += s.minutes
    return chosen, used


@dataclass
class SafetyGate:
    blast_user_cap: int          # 爆炸半径：允许影响的用户数上限
    freeze: tuple                # 变更冻结窗 (start_ts, end_ts)
    oncall_online: bool          # 值班在线且知情
    kill_switch_tested: bool     # 全局中止开关已预演
    notify_done: bool            # 客服/业务方已提前知情

    def check(self, now, est_users):
        problems = []
        if est_users > self.blast_user_cap:
            problems.append(f"预计影响 {est_users} 用户 > 预算 {self.blast_user_cap}")
        if self.freeze[0] <= now < self.freeze[1]:
            problems.append("落在变更冻结窗内")
        if not self.oncall_online:
            problems.append("值班不在线/不知情")
        if not self.kill_switch_tested:
            problems.append("全局中止开关未验证")
        if not self.notify_done:
            problems.append("客服/业务方未提前知情")
        return problems


@dataclass
class Event:
    ts: int
    kind: str        # inject / alert / ack / escalate / mitigate / recover
    team: str
    note: str = ""


def metrics(events):
    """从结构化时间线算 MTTD / MTTR / 跨团队交接损耗。"""
    first = {}
    for e in events:
        first.setdefault(e.kind, e)
    res = {}
    if "inject" in first and "alert" in first:
        res["mttd_s"] = first["alert"].ts - first["inject"].ts
    if "alert" in first and "recover" in first:
        res["mttr_s"] = first["recover"].ts - first["alert"].ts
    if "inject" in first and "ack" in first:
        res["first_ack_s"] = first["ack"].ts - first["inject"].ts
    gaps = []
    for prev, cur in zip(events, events[1:]):
        if prev.kind in ("alert", "escalate", "ack") and cur.kind in ("ack", "escalate"):
            if cur.team != prev.team:
                gaps.append((prev.team, cur.team, cur.ts - prev.ts))
    res["handoff_gaps"] = gaps
    res["handoff_total_s"] = sum(g[2] for g in gaps)
    return res


def report(scenario, events, m):
    lines = [f"场景: {scenario.name}（影响{scenario.impact}/概率{scenario.likelihood}/"
             f"{scenario.teams} 团队）"]
    lines.append(f"MTTD={m['mttd_s']}s  MTTR={m['mttr_s']}s  首个响应={m['first_ack_s']}s")
    for a, b, gap in m["handoff_gaps"]:
        lines.append(f"交接损耗: {a} -> {b} 空转 {gap}s")
    lines.append(f"交接总损耗: {m['handoff_total_s']}s")
    return "\n".join(lines)


if __name__ == "__main__":
    pool = [
        Scenario("支付链路下游对账服务不可用", 5, 3, 4, 90, True),
        Scenario("单服务 CPU 打满", 2, 4, 1, 30, False),
        Scenario("区域机房整体断网", 5, 2, 5, 120, True),
        Scenario("对外证书过期", 4, 3, 2, 45, True),
    ]
    chosen, used = plan(pool, budget_min=210, max_count=3)
    names = [s.name for s in chosen]
    assert names == ["支付链路下游对账服务不可用", "区域机房整体断网"], names
    assert used == 210
    assert "单服务 CPU 打满" not in names        # 单团队场景暴露不了协作问题
    print("选型:", " / ".join(f"{s.name}({s.score()})" for s in chosen))

    gate = SafetyGate(blast_user_cap=20000, freeze=(0, 2000),
                      oncall_online=False, kill_switch_tested=False,
                      notify_done=False)
    bad = gate.check(now=1000, est_users=50000)
    assert len(bad) == 5
    print("安全阀(未就绪):", len(bad), "项拦截 ->", bad[0], "…")

    gate2 = SafetyGate(blast_user_cap=20000, freeze=(0, 2000),
                       oncall_online=True, kill_switch_tested=True,
                       notify_done=True)
    assert gate2.check(now=3000, est_users=12000) == []
    print("安全阀(就绪): GO ✅")

    events = [
        Event(3000, "inject", "platform", "注入对账服务 5xx"),
        Event(3150, "alert", "platform", "支付成功率告警"),
        Event(3210, "ack", "payments", "支付团队接单"),
        Event(3300, "escalate", "payments", "怀疑对账侧，升级"),
        Event(3420, "ack", "infra", "基础架构接单"),
        Event(3900, "mitigate", "infra", "切备用对账集群"),
        Event(4200, "recover", "infra", "成功率回到基线"),
    ]
    m = metrics(events)
    assert m["mttd_s"] == 150
    assert m["mttr_s"] == 1050
    assert m["handoff_total_s"] == 180          # 支付→平台 60 + 支付→基础架构 120
    print(report(chosen[0], events, m))
    print("结论: 告警指向平台，首个接单却是支付团队——告警归属需要改路由 ✅")
```

**追问**：1) 为什么被演练团队不该提前知道具体场景？——知道「今晚要拔对账服务的网线」就会提前把预案贴在屏幕上、把监控阈值调松、把专家叫到工位，测到的是「准备过的能力」而不是「日常真实能力」；这与 A237 的随机抽检、A169 的随机注入同一个道理。折中是：告知时间窗与影响上限（保证安全），不告知故障类型与注入点（保证真实）。2) 跨团队注入碰不了别人服务，三档替代怎么选？——故障工单最安全但测不到技术链路（只测组织响应）；契约层注入真实度最高（依赖行为真的变了），但要求网关/服务网格支持按规则改响应，且要防止误伤非演练流量；对方自行执行介于两者之间，责任清晰但操作质量取决于对方。选择标准是「这次想验证组织响应还是技术降级」——两者都要就组合使用。3) GameDay 复盘最容易产出哪类无效行动项？——「加强监控」「加强培训」「提升意识」这类不可验收的动词；以及只报 MTTD/MTTR、不报交接损耗，导致组织问题被技术指标掩盖。可验收的写法是「具体对象 + 具体变更 + 可观测验证」，例如「把 X 告警的接收方从平台组改为支付组，下次演练首个响应 < 3 分钟」。

## 背诵要点
1. GameDay 测的是跨团队协作缝隙：场景按 影响×概率×跨团队跨度×未验证 打分，不选单团队能自愈的场景。
2. 角色分离（控制官/观察员/记录员），被演练团队只知时间窗不知场景；注入三档：工具直注 > 契约层 > 故障工单。
3. 安全阀五件套：爆炸半径预算、变更冻结、全局中止（预演过）、双人确认、外部知情；复盘核心指标是 MTTD/MTTR + 跨团队交接损耗，行动项必须可验收并复测。

## 复盘追问
1. GameDay 当天真的触发了生产事故，怎么界定「演练失败」还是「演练成功暴露问题」？——看影响是否在预设的爆炸半径与注入边界内：在内 = 弱点暴露（是产出，进行动项）；超出 = 演练事故（立即全停、按真实事故流程处理、复盘演练设计本身）。这条边界必须演练前写进方案，事后争论没有意义。
2. 管理层觉得 GameDay「没产出、还占人力」，怎么用数据说服？（提示：把演练发现的交接损耗换算成真实故障的 MTTR 增量，再乘年故障次数得到期望损失；对比演练投入的人天——和 A106 降级预案的成本论证同一套算法）
