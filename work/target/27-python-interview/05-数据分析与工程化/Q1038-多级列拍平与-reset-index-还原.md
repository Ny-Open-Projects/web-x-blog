---
title: [Q1038] 多级列拍平与 reset_index 还原
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1038 · 多级列拍平与 reset_index 还原

> 难度:★★☆☆ | 标签:pandas, 透视

**问**:groupby 多函数聚合后列是双层结构,导出 Excel 前怎么拍平最稳?

**答**:两层列拍平的标准写法是列表推导 `"|".join(map(str, col))`,把元组列名拼成 `amount|sum` 这样的单层字符串列;若只想去掉某一层用 `droplevel(0/1)`;行方向的多层索引用 `reset_index(level=...)` 选择性还原。导出前统一拍平是团队规范,因为 Excel、BI 工具和下游脚本大多不认嵌套表头;拍平时建议用下划线或竖线做分隔符并立刻 rename 成业务可读名。

```python
# file: code/05_数据分析与工程化/q1038_flatten_columns.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:把 (列, 函数) 元组拼成单层列名")
    cols = [("amount", "sum"), ("amount", "mean")]
    print(["_".join(map(str, c)) for c in cols])
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北", "华北"],
        "amount": [10, 20, 30, 40],
    })
    g = df.groupby("region").agg({"amount": ["sum", "mean"]})
    print("双层列:", g.columns.tolist(), end="\n\n")
    g.columns = ["_".join(map(str, c)) for c in g.columns]
    print(g.reset_index())
```

**追问**:
- 追问 1:`reset_index()` 什么都不传会发生什么?—— 还原全部行索引层,多层时按外层到内层顺序生成多列。
- 追问 2:droplevel 后列名重复怎么办?—— pandas 允许重复列但后续操作易错,拍平时加序号或业务前缀保证唯一。

```mermaid
flowchart LR
    A[长表 键列值列] --> B[unstack 或 pivot]
    B --> C[宽表 多级列]
    C --> D[stack 回到长表]
    C --> E[拍平 join 列名或 droplevel]
    E --> F[单层列 便于导出 Excel]
```
