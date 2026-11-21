---
title: [Q2533] 字段级 diff 报告生成
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2533 · 字段级 diff 报告生成

> 难度:★★★☆ | 标签:diff, 变更报告

**问**:昨天和今天的快照表,除了行数变化,怎么生成一份能直接贴周报的变更说明?

**答**:三层 diff 一次出。行级:按主键求差集,新增 o4、删除 o3;字段级:交集行逐字段比较,列出"o1: amt 100 到 120"这样的变更明细,谁变了、变了什么一目了然;列级:汇总每列的变更行数,实测 amt 变了 1 行、city 变了 0 行,直接回答"哪张字段在动"。报告模板固定三段:新增删除计数、变更明细、列级汇总,贴周报或发变更通知都够用。实现上纯字典比较就够,数据大了用 pandas 外连接加 indicator 一行得出 added/removed/both,再逐列比较。注意 diff 的键必须是业务主键,主键错了 diff 全错;时间戳、更新时间这类元数据列默认从字段级比较里剔除,否则每行都"变了"。

```python
# file: code/05_数据分析与工程化/q2533_field_diff_report.py
"""字段级 diff 报告: 新增 删除 变更与列级汇总"""

try:
    import pandas as pd
except ImportError:
    pd = None

OLD = {
    "o1": {"city": "北京", "amt": 100},
    "o2": {"city": "上海", "amt": 200},
    "o3": {"city": "深圳", "amt": 300},
}
NEW = {
    "o1": {"city": "北京", "amt": 120},
    "o2": {"city": "上海", "amt": 200},
    "o4": {"city": "广州", "amt": 400},
}
FIELDS = ["city", "amt"]


def diff(old, new):
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = {}
    for k in sorted(set(old) & set(new)):
        field_changes = [(f, old[k][f], new[k][f]) for f in FIELDS if old[k][f] != new[k][f]]
        if field_changes:
            changed[k] = field_changes
    return added, removed, changed


def render(added, removed, changed):
    lines = [f"新增 {len(added)} 行: {','.join(added) or '无'}",
             f"删除 {len(removed)} 行: {','.join(removed) or '无'}",
             f"变更 {len(changed)} 行:"]
    col_hits = {f: 0 for f in FIELDS}
    for k, changes in changed.items():
        detail = ", ".join(f"{f}: {o}->{n}" for f, o, n in changes)
        lines.append(f"  {k}: {detail}")
        for f, _, _ in changes:
            col_hits[f] += 1
    lines.append("列级汇总: " + ", ".join(f"{f} 变更 {c} 行" for f, c in col_hits.items()))
    return lines, col_hits


if __name__ == "__main__":
    added, removed, changed = diff(OLD, NEW)
    lines, col_hits = render(added, removed, changed)
    print("\n".join(lines))
    assert added == ["o4"] and removed == ["o3"]
    assert col_hits == {"city": 0, "amt": 1}, "只有 amt 变了 1 行"
    if pd is not None:
        df_o = pd.DataFrame([{"k": k, **v} for k, v in OLD.items()])
        df_n = pd.DataFrame([{"k": k, **v} for k, v in NEW.items()])
        m = df_o.merge(df_n, on="k", how="outer", suffixes=("_old", "_new"), indicator=True)
        print("pandas 视角: ", m["_merge"].value_counts().to_dict())
    print("要点: 行级 diff 告诉谁变了, 字段级 diff 告诉变了什么, 列级汇总是发周报和写变更说明的素材")
```

**追问**:
- 追问 1:数值字段的浮点误差怎么处理?—— 比较前按精度归一,金额统一到分、浮点用相对误差阈值,否则伪变更刷屏。
- 追问 2:百万行级别的 diff 怎么做?—— 先按分区或主键哈希分桶,只在同桶内做行级比较,跳过哈希一致的桶,IO 从全量降到变更量级。
