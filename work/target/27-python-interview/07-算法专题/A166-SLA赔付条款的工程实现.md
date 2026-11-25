---
title: [A166] SLA 赔付的工程实现：故障分账与赔付自动化
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A166 · SLA 赔付工程化

> 难度:★★★ | 标签:SLA, 赔付, 计费

**问**（笔试·编程+场景题）：向客户承诺 99.9% 可用性，违约赔付月费的 10%——赔付怎么自动化（故障时长判定/赔付计算/自动入账 vs 客户申请），「故障时长」的计法（从告警到恢复 vs 从客户上报到恢复——客户感知口径），赔付与「健康分」（A169）的关系（健康分差的月份自动免争议），赔付自动化的风险（误赔/被薅）怎么防？

**答**：① 自动化链路：监控系统（故障窗口判定：核心指标低于 SLO 水平的连续时段）→ 赔付计算引擎（ downtime 映射赔付比例：99.9-99.0% 赔 10%，<99% 赔 30%——阶梯表）→ 自动生成 credit（账单抵扣）→ 客户通知——**主动赔付**优于客户申请：省客服成本 + 信任建设。② 故障时长计法之争：服务方口径（告警→恢复）vs 客户口径（客户上报→恢复）——**客户感知口径为准**（SLA 是对客户体验的承诺）——工程实现：按租户维度记录「该租户实际受影响的窗口」（不是全站故障时长——B 机房挂了 A 机房客户没受影响就不赔 A 客户）。③ 健康分联动：健康分差的月份（A169 低分）= 已知质量问题主动赔付+说明（先赔后修，信任管理）；健康分好的月份客户投诉 → 用数据回应（「本月可用性 99.97%」）。④ 防薅：赔付基于**监控系统客观记录**（不接受客户单方口径）+ 重复申诉幂等（同故障窗口不重复赔）+ 赔付率监控（异常月份赔付率突增 = 系统问题或欺诈，人工复核）。

```python
# 全部标准库；demo 实现「SLA 赔付计算引擎」
import time

CREDIT_TIERS = [(99.0, 0.30), (99.5, 0.15), (99.9, 0.10)]   # (可用性下限, 赔付比例)

def credit_pct(uptime: float) -> float:
    """阶梯赔付：可用性越低赔越多。"""
    for floor, pct in CREDIT_TIERS:
        if uptime < floor:
            return pct
    return 0.0

class SLAEngine:
    def __init__(self, slo: float = 99.9):
        self.slo = slo
        self.issued: set[str] = set()          # 已赔付 (tenant, month) 幂等
    def monthly_credit(self, tenant: str, month: str, tenant_uptime: float,
                       monthly_fee: float) -> dict:
        key = (tenant, month)
        if key in self.issued:
            return {"duplicate": True}         # 同月不重复赔（防薅）
        pct = credit_pct(tenant_uptime)
        self.issued.add(key)
        credit = round(monthly_fee * pct, 2)
        return {"tenant": tenant, "month": month, "uptime": tenant_uptime,
                "credit_pct": pct, "credit": credit}
    def tenant_downtime(self, incidents: list[dict], tenant_region: str) -> float:
        """租户感知口径：只计影响该租户所在区域的故障。"""
        return sum(i["duration_min"] for i in incidents if tenant_region in i["regions"])

if __name__ == "__main__":
    eng = SLAEngine()
    r = eng.monthly_credit("acme", "2026-11", uptime=99.5, monthly_fee=10000)
    assert r["credit"] == 1500.0 and r["credit_pct"] == 0.15
    print("自动赔付:", r)
    r2 = eng.monthly_credit("acme", "2026-11", uptime=99.5, monthly_fee=10000)
    assert r2.get("duplicate")
    print("同月重复赔付拦截（幂等）✅")
    dt = eng.tenant_downtime(
        [{"duration_min": 30, "regions": ["cn-north"]},
         {"duration_min": 20, "regions": ["cn-south"]}], tenant_region="cn-north")
    assert dt == 30                           # 只计租户所在区域的故障
    print(f"租户感知口径: 该租户实际受影响 {dt}min（另一机房故障不赔）✅")
    print("阶梯:", CREDIT_TIERS)
    # 口径：主动赔付（省客服+建信任）；客户感知口径计时长；
    # 赔付基于监控客观记录+幂等防薅+赔付率监控。
```

**追问**：1) 为什么「主动赔付」比「客户申请审批」好？——主动赔付省掉申请-审核-争议的客服链路（每次争议成本 > 赔付本身）+ 主动赔付是信任信号（对 B 端客户尤其值钱）；风险（被薅）靠「客观监控记录+幂等」对冲。2) 「租户感知口径」的工程实现难点？（提示：故障影响面要按租户维度记录（故障系统的 region/tenant 标注，Q6014 多租户同构）——全站故障时长 ÷ 租户数是错的（未受影响的租户不该赔）；故障系统需要「影响租户清单」能力）3) 赔付率的「异常月份」怎么定？（提示：赔付总额/月费收入 > X%（如 5%）告警——可能是系统性故障（真要赔）或监控误判（误赔）——赔付率突增是信号不是结论，人工复核区分）

## 背诵要点
1. 赔付自动化链：监控判定故障窗口 → 阶梯计算（99.9-99.0 赔 10% 阶梯表）→ 自动 credit → 客户通知——主动赔付省客服建信任。
2. 故障时长按「客户感知口径」（租户实际受影响窗口），非全站故障时长——未受影响租户不赔。
3. 防薅三闸：客观监控记录、同月幂等、赔付率监控人工复核。

## 复盘追问
1. 客户说「我感知的故障比你系统记录的长」（监控绿但客户白屏 10 分钟），怎么办？（提示：先查客户侧链路（CDN/网络/客户端版本——可能在服务边界外）；真属服务问题则是监控盲区（覆盖不到该租户路径）——监控覆盖范围要纳入 SLA 口径或免责条款）
2. 大客户要求「超出标准 SLA 的专属赔付条款」，工程与商务怎么配合？（提示：专属 SLA=定制监控（租户专属探针+更严阈值）+ 赔付自动化引擎支持租户级配置（SLA 参数租户维度化）——工程先确认「专属承诺可监控可计算」，商务再签字——不可监控的承诺不签）
