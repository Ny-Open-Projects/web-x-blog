---
title: [Q1122] 代码评审 checklist
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1122 · 代码评审 checklist

> 难度:★★★☆ | 标签:code review, 协作

**问**:review 每次都只看"有没有明显 bug",怎么让评审有系统性?

**答**:把 checklist 做成清单而非凭记忆:正确性(逻辑与边界)、测试(改逻辑必动测试)、可读性(命名、函数长度)、安全(输入校验、密钥)、运维性(日志、回滚说明)五维。工具先挡低级问题(lint、格式、覆盖率门禁),人评重点放在设计与行为。规模纪律:PR 控制在 400 行内,超限拆分;评审 SLA 与优先级(线上修复优先)。评审产出以"问题 + 建议"为主,风格之争交给格式化工具,不做人身评判。

```python
# file: code/05_数据分析与工程化/q1122_review_checklist.py

def review(pr):
    issues = []
    if pr["additions"] + pr["deletions"] > 400:
        issues.append("改动超过 400 行,建议拆分 PR")
    if pr["logic_touched"] and not pr["tests_changed"]:
        issues.append("改了逻辑但没动测试")
    if pr["title"] == "update":
        issues.append("标题无信息量,写清动机与影响面")
    if not pr["rollback_note"]:
        issues.append("缺少回滚说明")
    return issues or ["LGTM"]

PR = {"title": "update", "additions": 520, "deletions": 30,
      "tests_changed": False, "logic_touched": True, "rollback_note": ""}
for line in review(PR):
    print("-", line)
```

**追问**:
- 追问 1:评审挂在人身上太久怎么办?—— SLA(如工作日 4 小时首评)+ 轮值 reviewer 池 + 机器人提醒,超时自动升级。
- 追问 2:哪些检查必须机器做而不是人做?—— 格式、静态检查、覆盖率、依赖安全扫描,机器做过的人不重复,人专注语义。
