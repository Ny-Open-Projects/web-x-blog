---
title: [Q1456] 上游 schema 变更防护
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1456 · 上游 schema 变更防护

> 难度:★★★☆ | 标签:schema 校验, 数据契约

**问**:上游团队说"我们加个字段不影响你们",你信吗?你的防护机制是什么?

**答**:不信口头承诺,用机器做契约。注册每个上游表的期望 schema(列名、类型、语义),每次读取前先做 diff,按变更类型分级处置:删除列或类型变更属阻断级,任务直接失败并通知上游,绝不能静默吞掉——静默的结果是三个月后发现报表字段全是 NULL;新增列属警告级,放行但要记录,因为新增列可能改变默认解析行为(比如 CSV 多了一列导致列错位)。配套三件事:schema 快照按天留存,变更可追溯;上游发版流程里加"schema 变更需提前 N 天在契约平台登记"的硬约束;下游对新增列的策略是"显式 opt-in",不用白不用,用了才纳入期望 schema。这套机制的哲学是:契约的价值不在阻止变更,而在让变更成本显性化、通知自动化。

```python
# file: code/05_数据分析与工程化/q1456_schema_guard.py
"""上游 schema 变更防护:新增列放行、删列与类型变更阻断"""

EXPECTED = {
    "order_id": "str",
    "user_id": "int",
    "amount": "decimal",
    "created_at": "datetime",
}

ACTUAL_V2 = {
    "order_id": "str",
    "user_id": "str",       # 类型变更 -> BLOCK
    "amount": "decimal",
    "created_at": "datetime",
    "channel": "str",       # 新增列 -> WARN
}


def schema_diff(expected, actual):
    blockers, warnings = [], []
    for col, typ in expected.items():
        if col not in actual:
            blockers.append(f"列被删除: {col}")
        elif actual[col] != typ:
            blockers.append(f"类型变更: {col} {typ} -> {actual[col]}")
    for col in actual:
        if col not in expected:
            warnings.append(f"新增列: {col} {actual[col]}")
    return blockers, warnings


def gate(expected, actual):
    blockers, warnings = schema_diff(expected, actual)
    decision = "BLOCK" if blockers else "PASS"
    return decision, blockers, warnings


if __name__ == "__main__":
    decision, blockers, warnings = gate(EXPECTED, ACTUAL_V2)
    print("决策:", decision)
    for b in blockers:
        print("  [阻断]", b)
    for w in warnings:
        print("  [警告]", w)
    print("原则:阻断性变更让下游任务直接失败并通知上游,而不是静默吞掉脏数据")
```

**追问**:
- 追问 1:类型变宽(int 到 long)要阻断吗?—— 语义兼容的变宽可降级为警告,但收窄或语义变更必须阻断,分级标准写进契约文档。
- 追问 2:schema 校验放读取时还是入库后?—— 读取时,越早失败损失越小;入库后才校验意味着脏数据已经进湖,清理成本高一个量级。
