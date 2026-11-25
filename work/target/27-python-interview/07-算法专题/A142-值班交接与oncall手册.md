---
title: [A142] 值班交接与 oncall 手册
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A142 · 值班交接与 oncall 手册

> 难度:★★☆ | 标签:oncall, 值班, 治理

**问**（笔试·场景题）：周一值班交接——「上位的值班知道什么」（交接清单里必须有什么），oncall 手册的标准条目是什么（每条告警的处理步骤写到什么粒度），「半夜 3 点的告警」怎么决定「立即处理还是早上再说」（分级处置），值班疲劳（一周 50 次告警）对事故率的影响怎么量化治理？

**答**：① 交接清单：**在途事项**（进行中的变更/未闭环的告警/升级中的问题及当前状态）、**已知风险**（脆弱点：刚改过的东西/已知但未修的 bug）、**近期变更**（过去一周发布清单——事故高相关）。交接用书面+口头双轨，书面记录进值班系统（可追溯）。② 手册条目粒度：每条告警 = `现象描述 → 影响面判断（是否资损）→ 处置步骤（具体命令/开关位置）→ 升级路径（何时叫谁）→ 事后动作`——粒度标准：**新值班拿着手册能独立处置**（不需要问人）；写不出处置步骤的告警 → 不该是告警（降级或修根因）。③ 半夜分级：**P0**（资损/全站不可用）立即处理；**P1**（核心功能受损）1 小时内；**P2**（体验问题）工作时间处理——分级标准预写在告警元数据，半夜靠分级不靠人的判断力（半夜判断力是最差资源）。④ 疲劳治理：告警/周 >30 次即「告警污染」，误报率与 MTTR 上升量化关联——治理=降噪（Q7039）+ 轮换密度（每周单人告警 ≤20 次）+ 夜班补偿（不是道德要求是可持续性要求）。

```python
# 全部标准库；demo 实现「交接清单 + 分级处置路由」
import time

HANDOFF_TEMPLATE = ["in_progress", "known_risks", "recent_changes", "open_alerts"]

class OncallSystem:
    def __init__(self):
        self.handoff: dict[str, list] = {k: [] for k in HANDOFF_TEMPLATE}
        self.alert_rules = {                       # 告警名 -> (P 级, 处置提示)
            "db_down": ("P0", "立即：切换只读降级，叫 DBA"),
            "payment_fail_spike": ("P0", "立即：查支付渠道状态，切备用渠道"),
            "p99_degraded": ("P1", "1h 内：查 trace 归因，必要时扩容"),
            "log_disk_80": ("P2", "工作时间：扩容或清理"),
        }
        self.weekly_alerts: dict[str, int] = {}
    def route(self, alert: str, now_hour: int) -> str:
        level, action = self.alert_rules[alert]
        self.weekly_alerts[alert] = self.weekly_alerts.get(alert, 0) + 1
        if level == "P0" or (level == "P1" and now_hour in range(9, 21)):
            return f"立即处理: {action}"
        return f"工作时间处理: {action}"            # P1 夜间/P2 默认次日
    def fatigue_check(self, oncall: str) -> str:
        total = sum(self.weekly_alerts.values())
        if total > 50:
            return f"{oncall}: {total} 次/周 → 告警污染（P0 可能被淹没），强制降噪"
        if total > 30:
            return f"{oncall}: {total} 次/周 → 预警，安排降噪"
        return f"{oncall}: {total} 次/周 → 健康"

if __name__ == "__main__":
    sys_ = OncallSystem()
    print("半夜 3 点 db_down →", sys_.route("db_down", now_hour=3))
    print("半夜 3 点 p99 →", sys_.route("p99_degraded", now_hour=3))
    print("白天 p99 →", sys_.route("p99_degraded", now_hour=14))
    assert "立即" in sys_.route("db_down", now_hour=3)
    assert "工作时间" in sys_.route("p99_degraded", now_hour=3)
    print("分级路由（P0 夜间立即 / P1 夜间次日 / 白天 P1 立即）✅")
    for _ in range(55): sys_.route("log_disk_80", now_hour=12)
    print(sys_.fatigue_check("zhang"))
    assert "污染" in sys_.fatigue_check("zhang")
    print("疲劳治理：55 次/周触发强制降噪 ✅")
    # 手册粒度口径：新值班能独立处置；写不出处置步骤的告警不该是告警。
```

**追问**：1) 为什么「写不出处置步骤的告警」不该存在？——它要么是真风险但无人懂（知识缺口，要补手册不是留着），要么是噪声（无处置价值）；留着它=每次响都人工考古，是疲劳源。2) P1 夜间「次日处理」会不会升级成 P0？（提示：可能——所以 P1 夜间不是「忽略」而是「降级记录+趋势监控」（指标恶化自动升级 P0）；分级路由是路由不是关断）3) 值班疲劳和事故率的量化关联怎么建立？（提示：按周统计告警数 vs 该周 MTTR/漏报事故——相关性数据是申请降噪/轮换资源的依据；没有数据，疲劳治理永远是「感觉」）

## 背诵要点
1. 交接清单四项：在途事项/已知风险/近期变更/未闭环告警，书面+口头双轨。
2. 手册粒度标准 = 新值班能独立处置；每条告警五要素（现象/影响/步骤/升级/事后）。
3. 半夜分级靠预写元数据不靠人的判断力；告警 >30 次/周预警、>50 次强制降噪（疲劳可量化）。

## 复盘追问
1. 手册 500 条没人维护，和代码一样漂移了，怎么治理？（提示：手册条目与告警规则关联（告警必带 runbook 链接，Q7039）+ 告警触发时采集「手册是否有用」反馈 + 半年审计——手册当代码管，版本化+review）
2. 「半夜 P1 次日处理」连续三天同一告警，会发生什么？（提示：三次次日处理=三天未修根因——同一告警夜间重复触发 N 次自动升级 P0（重复即升级规则），防「永远明天」）
