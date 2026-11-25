---
title: [A238] 备份恢复 RTO/RPO：指标口径与实测脚本化验收
date: 2026-11-23
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A238 · RTO/RPO 口径与实测验收

> 难度:★★☆ | 标签:备份, RTO, RPO, 可观测

**问**（笔试·场景题）：A148 已经定了「备份要演练、四层口径、频率分级」，但一到验收还是扯皮——运维说「RTO 20 分钟达标」，业务说「明明 33 分钟才恢复」；「RPO 5 分钟」到底是时间口径还是事务数口径？本题只咬住两件事：**RTO/RPO 的指标口径怎么定义才不扯皮**（起点/终点/时钟源），以及**实测怎么脚本化**（事件打点→自动计算→断言 SLA→可追溯报告），让同一个演练每次跑出可复现、可回归的数字。

**答**：① RTO 口径三歧义：**起点**（告警触发 / 故障确认 / 决策恢复——必须冻结为「故障确认时刻」，告警触发含误报、决策时刻主观）、**终点**（进程起来 / 端口通 / 业务指标回到阈值——冻结为「业务指标回到阈值」，进程起来≠业务可用）、**时钟源**（各机器本地时钟有漂移——全部打点统一 UTC + 单一时钟源，A236 UTC 锚定同构）。口径不冻结，同一个演练能算出 20min 和 33min 两个 RTO。② RPO 口径双维度：**时间口径** = 故障时刻 − 最新可恢复点（全量+增量链下由最新可恢复点决定，不是「上次全量备份时间」）；**事务数口径** = 故障点到可恢复点之间丢失的事务条数（业务更直观）；两者要同时报告，SLA 写「最坏丢 N 分钟 / 不超过 M 条」。③ 实测脚本化：拒绝人肉秒表——在故障注入、故障确认、恢复开始、进程可用、业务恢复、数据校验各点**打事件时间戳**（带口径版本号），脚本自动算 RTO/RPO、断言 SLA、输出含原始时间戳与口径版本的报告；同一脚本每月跑同一口径 → 数字可复现、口径变更前后可对齐回归。④ 与 A148 的分工：A148 管「要不要演练/演练制度/闭环」，A238 管「这两个数字怎么算才唯一、怎么自动算」——口径是制度的技术地基；口径没冻结，A148 的行动项会基于错误数字去优化。

```python
# 全部标准库；demo 实现「口径显式化 + 事件打点自动算 RTO/RPO + 断言报告」
from datetime import datetime, timezone

CALIBER = "rto-rpo-v2-frozen"          # 口径版本号写进报告，变更可追溯

def parse_ts(iso: str) -> datetime:
    """统一 UTC 解析：所有打点都用带时区的 ISO8601，消除本地时钟漂移。"""
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(timezone.utc)

def measure(events: dict[str, str], sla: dict) -> dict:
    """按冻结口径从事件戳算 RTO/RPO 并断言 SLA。"""
    t_fail = parse_ts(events["failure_confirmed"])          # RTO 起点（口径冻结）
    t_biz_ok = parse_ts(events["biz_metric_recovered"])     # RTO 终点（口径冻结）
    t_point = parse_ts(events["latest_recoverable_point"])  # RPO 锚点
    rto_min = (t_biz_ok - t_fail).total_seconds() / 60
    rpo_min = (t_fail - t_point).total_seconds() / 60
    lost_txns = int(events.get("lost_transactions", 0))     # RPO 事务数口径（辅助维度）
    rto_pass, rpo_pass = rto_min <= sla["rto_min"], rpo_min <= sla["rpo_min"]
    return {"caliber": CALIBER,
            "rto_min": round(rto_min, 1), "rpo_min": round(rpo_min, 1),
            "rpo_lost_txns": lost_txns,
            "verdict": "PASS" if rto_pass and rpo_pass else "FAIL",
            "breaches": [k for k, ok in (("RTO", rto_pass), ("RPO", rpo_pass)) if not ok],
            "raw_events": dict(events)}                      # 原始时间戳留档，可回归

if __name__ == "__main__":
    events = {
        "failure_confirmed": "2026-11-23T02:00:00Z",
        "latest_recoverable_point": "2026-11-23T01:52:00Z",  # RPO = 8min
        "restore_started": "2026-11-23T02:05:00Z",
        "process_up": "2026-11-23T02:20:00Z",                # 进程起来≠业务可用
        "biz_metric_recovered": "2026-11-23T02:33:00Z",      # RTO = 33min（终点按口径）
        "lost_transactions": "412",
    }
    r = measure(events, {"rto_min": 30, "rpo_min": 5})
    assert r["rto_min"] == 33.0 and r["rpo_min"] == 8.0
    assert r["rpo_lost_txns"] == 412
    assert r["verdict"] == "FAIL" and r["breaches"] == ["RTO", "RPO"]
    print("口径:", r["caliber"])
    print("实测:", r["rto_min"], "min RTO /", r["rpo_min"], "min RPO /",
          r["rpo_lost_txns"], "条 →", r["verdict"], r["breaches"])
    # 若终点误取 process_up，RTO 被算成 20min（假通过）——口径冻结是脚本化的前提
    wrong = dict(events, biz_metric_recovered=events["process_up"])
    assert measure(wrong, {"rto_min": 30, "rpo_min": 5})["rto_min"] == 20.0
    print("口径错取「进程可用」会假装达标（20min）——证明冻结终点定义的价值 ✅")
```

**追问**：1) 为什么 RTO 终点取「业务指标回到阈值」而不是「进程可用 / 端口通」？——进程起来只证明自己活着，不证明依赖的 DB/缓存/配置都正确（恢复库连上了但 schema 版本不对，业务全 500）——RTO 衡量的是「业务重新可服务」，终点必须落在业务可观测指标上，否则是自欺欺人的假达标。2) RPO 的两个口径哪个更该写进对外 SLA？——时间口径（丢 N 分钟）对内便于工程优化（缩短备份间隔/上增量），事务数口径（丢 M 条）对客户更直观（「最多丢 412 笔」）——对内对外分开写，同一演练同时算两个，避免「5 分钟对客户到底丢多少」的翻译扯皮。3) 脚本化验收和 A148 的行动项闭环怎么衔接？——脚本输出的 breaches（RTO/RPO 哪项不达标）直接生成行动项（A148 已有机制）：RTO 超时→优化恢复脚本/预占资源，RPO 超标→缩短备份间隔/补 binlog 实时性——脚本化让行动项的触发依据客观可复现，不再靠人工判断「好像慢了」。

## 背诵要点
1. RTO 口径三冻结：起点=故障确认、终点=业务指标回阈值、时钟源=UTC 单一源；不冻结则同演练可差出一倍数字。
2. RPO 双维度：时间口径=故障点−最新可恢复点，事务数口径=丢失事务条数，SLA 写「丢 N 分钟 / 不超 M 条」。
3. 实测脚本化：事件打点→自动算→断言→带口径版本+原始时间戳的报告，可复现可回归；与 A148 制度分工（A238 是技术地基）。

## 复盘追问
1. 演练报告显示 RTO 达标但业务投诉「恢复后半小时才敢用」，口径还缺什么？（提示：缺「数据追平/一致性校验完成」这个终点——业务敢用=数据完整可信，RTO 终点可能还要加「数据校验通过」，把校验打点纳入事件序列）
2. 两次演练数字差很大（20min vs 33min），查不出原因，最先查什么？（提示：查口径版本与打点时刻是否一致——大概率是有人手工改了终点定义或用了本地时钟打点；报告留口径版本+原始时间戳就是为了这种回归定位）
