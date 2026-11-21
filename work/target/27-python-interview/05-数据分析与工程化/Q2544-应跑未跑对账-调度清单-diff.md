---
title: [Q2544] 应跑未跑对账:调度清单 diff
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2544 · 应跑未跑对账:调度清单 diff

> 难度:★★★☆ | 标签:调度对账, 巡检

**问**:怎么在数据事故发生前发现"有个任务今天根本没跑"?

**答**:调度系统自己的成功率只回答"跑了的成功率",不回答"该跑的都跑了吗"。做法是两份清单求差:调度计划(每天必跑的任务集合)与执行台账(任务名、逻辑日期),差集即漏跑,反向差集即计划外任务。实测 2026-03-01:etl_users 的台账记录落在 02-28,对账立即报出漏跑;adhoc_backfill 不在计划里,报出计划外并要求补登记。关键细节是对账按逻辑日期而非执行时间:凌晨补跑昨天的任务,台账逻辑日期要记昨天,否则"补跑昨天的任务救不了今天的分区"这种错位永远对不平。漏跑处置是立即补跑加回填水位;计划外任务补登记,否则血缘与影响面分析永远有暗账。这个巡检挂在调度之外独立运行,成本极低(两个集合求差),收益是漏跑从"下游炸了才知道"提前到"当天上午就看见"。

```python
# file: code/05_数据分析与工程化/q2544_schedule_recon.py
"""应跑未跑对账: 调度清单与执行台账的差集"""

SCHEDULE = {"etl_orders", "etl_payments", "etl_users"}     # 每日必跑任务
LEDGER = [
    ("etl_orders", "2026-03-01"),
    ("etl_payments", "2026-03-01"),
    ("etl_users", "2026-02-28"),        # 跑了但跑错日期
    ("adhoc_backfill", "2026-03-01"),   # 计划外临时任务
]


def reconcile(schedule, ledger, day):
    executed = {t for t, d in ledger if d == day}
    missing = sorted(schedule - executed)
    orphans = sorted(executed - schedule)
    return missing, orphans


if __name__ == "__main__":
    day = "2026-03-01"
    missing, orphans = reconcile(SCHEDULE, LEDGER, day)
    print(f"{day} 对账: 漏跑 {missing or '无'}, 计划外 {orphans or '无'}")
    assert missing == ["etl_users"], "etl_users 昨天跑的不算今天数"
    assert orphans == ["adhoc_backfill"], "临时任务必须显式登记计划"
    print("处置: 漏跑任务立即补跑并回填水位; 计划外任务补登记, 否则依赖对账永远有暗账")
    missing2, _ = reconcile(SCHEDULE, LEDGER + [("etl_users", day)], day)
    assert not missing2, "补跑后应清零"
    print("要点: 台账按 逻辑日期 对账而不是按执行时间, 补跑昨天的任务救不了今天的分区")
```

**追问**:
- 追问 1:低频任务(周跑月跑)怎么对账?—— 计划模型带频率与锚点,期望实例按日历展开生成,周任务只在锚点日要求出现。
- 追问 2:补跑顺序怎么定?—— 按依赖拓扑排序补,上游就绪检查通过才放行下游,防止补跑时读半截数据。
