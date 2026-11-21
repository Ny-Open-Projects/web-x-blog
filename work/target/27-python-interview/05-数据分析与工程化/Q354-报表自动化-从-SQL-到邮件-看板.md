---
title: [Q354] 报表自动化:从 SQL 到邮件/看板
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q354 · 报表自动化:从 SQL 到邮件/看板

> 难度:★★☆ | 标签:自动化, 报表

**问**:如何把一张每日人工报表做成自动化流水线?架构上分几步?

**答**:四步:①取数 SQL 固化并参数化数据日期,入库到结果表而不是直接算完就走;②渲染层把结果表填进模板(Excel/openpyxl 或 HTML),样式与口径与人工版对齐;③分发层邮件/IM 机器人推送,失败重试;④治理层:同口径的指标走统一函数,报表数据日期缺失时告警而不是发空表,关键数值加同比环比自动校验防止口径漂移。原则:报表自动化后要有"守护者",上游表结构变更必须触发检查。

```python
# file: code/05_数据分析与工程化/q354_auto_report.py
import csv
import os
from datetime import date

def fetch_metrics(data_date):
    """生产上为参数化 SQL 查询结果表;此处模拟。"""
    return [["gmv", 10000], ["uv", 800], ["pay_rate", 0.12]]

def render_csv(metrics, data_date, path):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["metric", "value", "date"])
        for name, val in metrics:
            w.writerow([name, val, data_date])

def validate(metrics):
    names = {m[0] for m in metrics}
    required = {"gmv", "uv", "pay_rate"}
    missing = required - names
    if missing:                        # 缺指标就告警,不发空表
        raise ValueError(f"missing metrics: {missing}")
    return True

if __name__ == "__main__":
    today = date.today().isoformat()
    metrics = fetch_metrics(today)
    validate(metrics)
    render_csv(metrics, today, f"report_{today}.csv")
    print("report ready:", f"report_{today}.csv")
    os.remove(f"report_{today}.csv")
```

**追问**:
- 报表自动化的守护机制?——数据日期缺失不发空表、关键指标同比环比异常告警、上游 schema 变更触发检查;自动化之后没人盯着才最危险。
- 为什么结果先入库再渲染?——入库可复用、可校验、可追溯;SQL 直接到 Excel 的链路一变全重写。
- 邮件报表的常见事故?——口径漂移没人发现(加自动校验)、上游断供发空表(阻断)、收件人越来越多无人核对(定期清理)。

---
