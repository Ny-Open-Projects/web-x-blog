---
title: [Q1118] runbook 与升级路径
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1118 · runbook 与升级路径

> 难度:★★★☆ | 标签:SRE, runbook

**问**:凌晨 3 点告警响了,值班同学怎么知道该干什么?runbook 里写什么?

**答**:runbook 是告警到处置的映射,每条告警链接一份 runbook,内容四段:确认(看哪个面板确认影响面)、处置(按序执行的命令与决策树,如"先回滚再查因")、升级(15 分钟未恢复升级到谁、联系方式)、恢复后动作(验证指标、记录时间线)。维护纪律:runbook 与告警同仓库评审,处置命令可复制执行,演练(值班交接时抽测)保证不是过期文档;值班手册还要有非技术段:何时叫醒谁、对外口径谁负责。

```python
# file: code/05_数据分析与工程化/q1118_runbook.py

RUNBOOK = {
    "api-5xx-激增": {
        "确认": ["打开 SLO 看板确认 burn rate", "区分全量还是部分实例"],
        "处置": ["回滚最近 30 分钟发布", "必要时扩容或开启限流"],
        "升级": ["15 分钟未恢复升级 P0 负责人与平台组"],
        "恢复后": ["确认错误预算消耗", "24h 内出复盘"],
    },
}

def show(name):
    rb = RUNBOOK[name]
    for section, steps in rb.items():
        print(f"## {section}")
        for i, s in enumerate(steps, 1):
            print(f"  {i}. {s}")

if __name__ == "__main__":
    show("api-5xx-激增")
    print("纪律:与告警同仓库评审,命令可复制执行,值班交接抽测防过期")
```

**追问**:
- 追问 1:runbook 怎么不变成一次性文档?—— 绑定告警链接、变更走 PR、值班交接演练抽测,三件事缺一不可。
- 追问 2:升级路径里的"叫醒策略"怎么定?—— 按级别:P0 立即电话,值班 15 分钟无响应自动升级 secondary,再无响应到 manager。
