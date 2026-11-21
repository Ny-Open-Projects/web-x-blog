---
title: [Q1034] 多键 merge 与 suffixes 冲突处理
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1034 · 多键 merge 与 suffixes 冲突处理

> 难度:★★★☆ | 标签:pandas, merge

**问**:按 user_id 加日期两列关联,两侧又有同名列,pandas 怎么处理?你有什么规范?

**答**:多键 merge 直接传列表 `on=["user_id", "dt"]`,键的组合相等才匹配;两侧同名的非键列会自动加 `_x`/`_y` 后缀,可读性差,规范做法是 merge 前就重命名或删掉冗余列,必须共存时用 `suffixes=("_fact", "_dim")` 给出业务化后缀。另一个高频坑:同一对键在任一侧重复都会按笛卡尔积展开,多键场景更容易隐形膨胀,所以多键 merge 同样要配 validate,并先检查"键组合"的唯一性而不是单列唯一性。

```python
# file: code/05_数据分析与工程化/q1034_multikey_suffix.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    facts = [("u1", "01-01", 100), ("u1", "01-02", 200)]
    dims = [("u1", "01-01", "vip")]
    for f in facts:
        match = [d for d in dims if d[0] == f[0] and d[1] == f[1]]
        print(f, "->", match[0] if match else None)
else:
    facts = pd.DataFrame({
        "user_id": ["u1", "u1", "u2"],
        "dt": ["01-01", "01-02", "01-01"],
        "amount": [100, 200, 50],
        "level": ["tmp", "tmp", "tmp"],
    })
    dims = pd.DataFrame({
        "user_id": ["u1", "u1", "u2"],
        "dt": ["01-01", "01-02", "01-01"],
        "level": ["vip", "normal", "normal"],
    })
    m = facts.drop(columns=["level"]).merge(
        dims, on=["user_id", "dt"], validate="1:1", suffixes=("_fact", "_dim")
    )
    print(m)
```

**追问**:
- 追问 1:键列在两侧名字不同怎么关联?—— 用 `left_on`/`right_on` 分别指定,merge 后两列都保留,注意去重。
- 追问 2:多键 merge 怎么快速验证唯一性?—— `df.duplicated(subset=["user_id", "dt"]).sum()` 应为 0,或 set_index 后 `index.is_unique`。
