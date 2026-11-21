---
title: [Q1040] 有序分类 CategoricalDtype 与业务排序
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1040 · 有序分类 CategoricalDtype 与业务排序

> 难度:★★★☆ | 标签:pandas, category

**问**:"低/中/高"这类等级字段,想让排序、比较、min/max 都按业务顺序走,怎么做?

**答**:定义 `CategoricalDtype(["低", "中", "高"], ordered=True)` 后 astype,该列就带上了业务序:sort_values 按类别序而不是字典序,`>`/`<` 比较合法,min/max、cut 分箱标签、groupby 输出都会遵循该顺序。这是报表按"高中低"排而非拼音序的标准解法。注意两个 dtype 的 categories 顺序不同则不相等,跨表统一口径时用同一个 CategoricalDtype 对象;未出现在类别列表里的值会变 NaN,新增等级要显式扩 categories。

```python
# file: code/05_数据分析与工程化/q1040_ordered_categorical.py
try:
    import pandas as pd
    from pandas.api.types import CategoricalDtype
except ImportError:
    pd = None

if pd is None:
    order = ["低", "中", "高"]
    rows = [("u1", "中"), ("u2", "高"), ("u3", "低")]
    for user, level in sorted(rows, key=lambda x: order.index(x[1])):
        print(user, level)
else:
    lvl = CategoricalDtype(["低", "中", "高"], ordered=True)
    df = pd.DataFrame({"user": ["u1", "u2", "u3"], "level": ["中", "高", "低"]})
    df["level"] = df["level"].astype(lvl)
    print(df.sort_values("level"), end="\n\n")
    print("min/max:", df["level"].min(), df["level"].max())
    print("比较过滤 高于中:", df[df["level"] > "中"]["user"].tolist())
```

**追问**:
- 追问 1:已有 category 想调整顺序呢?—— `cat.reorder_categories(["低", "中", "高"])`,或 set_categories 重建。
- 追问 2:无序 category 做比较会怎样?—— 直接抛 TypeError,这就是 ordered=False 的保护,提醒你别漏定义顺序。
