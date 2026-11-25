---
title: [A167] SLO 分级与通知路由：谁该被半夜叫醒
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A167 · SLO 分级与通知路由

> 难度:★★☆ | 标签:SLO, 告警路由, 可靠性

**问**（笔试·场景题）：支付服务 SLO 99.95%、推荐服务 SLO 99%——SLO 等级怎么决定「告警发给谁/什么时间叫醒」（分级路由矩阵），SLO 与 oncall 责任域怎么对齐（「这个告警是我的」的判定），「跨域告警」（根因在 A 服务但报警的是 B 服务）怎么路由到对的人？

**答**：① 路由矩阵三输入：**SLO 等级**（T0 核心：7×24 page；T1 重要：工作时间 page + 夜间短信；T2 一般：ticket）、**违反速度**（快速燃烧立即 page、慢速燃烧 ticket——Q7008 燃烧率）、**时间窗**（工作时间/夜间——夜间只有 T0 快速燃烧才叫醒）。② 责任域对齐：告警元数据带 `owner_team`（与服务的 SLO 拥有者一致——SLO 是团队承诺，告警路由到承诺团队而非「代码在哪」）；服务的 owner 变更时告警路由自动跟随（服务目录驱动）。③ 跨域告警：B 服务报警但根因在 A——路由分两步：**即时通知 B**（它是症状承受方，先止血）+ **根因分派**（trace 归因 Q7519 确定根因服务 → 通知 A 团队，事件单关联）——「症状与根因分离路由」是跨域事故的标准姿势；根因归属有争议时按依赖地图（Q123）+ 仲裁流程裁决。

```python
# 全部标准库；demo 实现「SLO 分级路由矩阵」
import time

SLO_TIERS = {
    "payment": {"tier": "T0", "slo": 99.95, "team": "pay-team"},
    "recommend": {"tier": "T2", "slo": 99.0, "team": "rec-team"},
    "search": {"tier": "T1", "slo": 99.9, "team": "search-team"},
}

def route_alert(service: str, burn_rate: float, hour: int) -> dict:
    """路由三输入：SLO 等级 × 燃烧速度 × 时间窗。"""
    info = SLO_TIERS[service]
    tier, fast = info["tier"], burn_rate >= 14.4
    if tier == "T0" and fast:
        return {"action": "page", "team": info["team"], "why": "T0 快速燃烧"}
    if tier == "T0":
        return {"action": "page", "team": info["team"], "why": "T0 任何燃烧都 page"}
    if tier == "T1":
        if fast and 9 <= hour < 21:
            return {"action": "page", "team": info["team"], "why": "T1 工作时间快速燃烧"}
        return {"action": "ticket", "team": info["team"], "why": "T1 非工作时段"}
    return {"action": "ticket", "team": info["team"], "why": "T2 一律 ticket"}

def split_root_cause(symptom_team: str, root_team: str, event_id: str) -> dict:
    """跨域告警：症状方即时通知 + 根因方事件单分派。"""
    return {"notify_now": symptom_team, "assign_root_cause": root_team,
            "event": event_id}

if __name__ == "__main__":
    print("半夜支付慢燃烧:", route_alert("payment", 5.0, hour=3))
    print("白天搜索快速燃烧:", route_alert("search", 20.0, hour=14))
    print("推荐任何燃烧:", route_alert("recommend", 20.0, hour=3))
    assert route_alert("payment", 5.0, 3)["action"] == "page"      # T0 夜间也叫醒
    assert route_alert("recommend", 20.0, 3)["action"] == "ticket"  # T2 永远 ticket
    print("跨域:", split_root_cause("order-team", "pay-team", "INC-9"))
    # 口径：T0 夜间 page、T1 工作时间 page、T2 ticket；症状即时通知+根因分派。
```

**追问**：1) 为什么 T0「任何燃烧都 page」而 T1 只在工作时间？——T0 SLO 99.95% 意味着预算极薄（月 22 分钟），慢燃烧也在快速吃掉预算；T2 SLO 宽松（月 7 小时），夜间叫醒人的收益不抵疲劳成本（Q142 疲劳量化）——分级本质是「预算厚度决定叫醒阈值」。2) 「根因在 A 但报警的是 B」如果根因有争议（双方都说对方）怎么仲裁？（提示：依赖地图+trace 客观裁决（Q123）——trace 里谁先失败/谁的错误率先起飞就是根因方；争议超 30 分钟升级 SRE 仲裁——数据说话避免扯皮拉长 MTTR）3) 服务 owner 变更时告警路由漏改怎么办？（提示：服务目录（service catalog）是唯一事实源——告警路由从目录动态读取而非硬编码 team 字符串；目录变更事件触发路由规则同步（Q6013 webhook 同构））

## 背诵要点
1. 路由三输入：SLO 等级（T0/T1/T2）× 燃烧速度（快速/慢速）× 时间窗（工作时间/夜间）。
2. T0 任何燃烧都 page（预算薄）、T1 工作时间 page、T2 一律 ticket——预算厚度决定叫醒阈值。
3. 跨域告警两步路由：症状方即时通知 + trace 归因后根因方分派；服务目录驱动 owner 路由。

## 复盘追问
1. 「每个服务都定成 T0」（团队都想被认真对待），SLO 分级怎么治理？（提示：T0 意味着 7×24 oncall 成本（要配轮班人力）——分级与资源承诺绑定：要 T0 就配值班，不配就降 T2——用成本约束抑制分级通胀）
2. 半夜 T2 的 ticket 挤了 200 张没人看，出现真问题怎么办？（提示：ticket 也要分级处理（每日站会过队列）+ 真问题靠「业务哨兵」（A148）独立报警兜底——ticket 堆积是 T2 分级的设计预期，兜底在业务哨兵）
