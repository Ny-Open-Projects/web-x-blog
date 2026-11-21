---
title: [Q1735] schema 演进兼容矩阵
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1735 · schema 演进兼容矩阵

> 难度:★★★★ | 标签:schema, 兼容性

**问**:上游表要加列、改类型、删列,你怎么判定这次变更能不能直接上线?

**答**:兼容矩阵逐列判定:加列兼容,读端按需取用;类型加宽兼容,int 到 bigint;删列破坏,依赖的下游直接失败;类型收窄破坏;改名等价于删加组合,也破坏。判定器吃旧 schema 和新 schema,输出每列的变更类型与处置建议,结论明确能否直接上线,实测里一次含加列加宽删列的变更被判为不可直接上线。纪律是破坏性变更走两阶段:先加新列双写,下游全部迁完再下线旧列;读端永远防御式解析,多列缺列都不崩。矩阵本身进发布门禁,CI 跑一遍,破坏性变更没附迁移计划就拒绝合入。

```python
# file: code/05_数据分析与工程化/q1735_schema_compat.py
"""schema 演进兼容矩阵:逐列判定新增/删除/改型,输出兼容结论与动作"""

OLD = {
    "uid": "string",
    "amount": "int",
    "city": "string",
    "unused": "string",
}
NEW = {
    "uid": "string",
    "amount": "bigint",     # 加宽,兼容
    "city": "string",
    "pay_status": "int",    # 新增
    # unused 被删除
}

WIDEN = {("int", "bigint"), ("float", "double"), ("int", "double")}


def judge(old, new):
    diffs = []
    for col in new:
        if col not in old:
            diffs.append((col, "added", "兼容:下游按需取用,读取端可空"))
    for col in old:
        if col not in new:
            diffs.append((col, "removed", "破坏:依赖它的下游直接失败,先确认无引用或保留占位列"))
    for col in set(old) & set(new):
        if old[col] != new[col]:
            if (old[col], new[col]) in WIDEN:
                diffs.append((col, "type_widen", "兼容:类型加宽,读取端需感知精度"))
            else:
                diffs.append((col, "type_change", "破坏:类型收窄或不兼容,需停写迁移"))
    return diffs


if __name__ == "__main__":
    diffs = judge(OLD, NEW)
    for col, kind, note in diffs:
        print(f"  [{kind:<11}] {col:<12} {note}")
    breaking = any(k in ("removed", "type_change") for _, k, _ in diffs)
    print("结论:", "含破坏性变更,不能直接上线,走两阶段:先双写新列,确认下游迁移后再删旧列" if breaking else "兼容,可直接上线")
    print("要点:兼容矩阵是发布门禁——加列与加宽直通,删列改名必须两阶段;读端永远按'可能多列缺列'防御式解析")
```

**追问**:
- 追问 1:改名怎么平滑?—— 先加新列双写,下游迁完再下线旧列,中间状态用兼容视图兜底。
- 追问 2:枚举值新增算破坏吗?—— 对读取方一般兼容,但下游有穷举校验会失败,枚举演进也要进兼容矩阵评估。
