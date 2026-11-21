---
title: [Q1032] merge 的 validate 防键膨胀
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1032 · merge 的 validate 防键膨胀

> 难度:★★★☆ | 标签:pandas, merge

**问**:两表 join 之后行数翻了几倍,你有什么手段在 merge 阶段就把这类问题拦住?

**答**:用 `merge` 的 `validate` 参数声明预期的键关系:`"1:1"` 一对一、`"1:m"`/`"m:1"` 一对多、`"m:m"` 多对多。实际数据不满足时 pandas 直接抛 `MergeError`,把"上游脏数据"从静默膨胀变成立刻失败,这比事后 `assert len(df) == n` 早得多、也准得多。工程上凡是有业务含义的一对多关系(订单对用户)都应显式声明 m:1,凡期望唯一的主数据关联一律声明 1:1,配合 merge 前的 `drop_duplicates(subset=键)` 使用效果最好。

```python
# file: code/05_数据分析与工程化/q1032_merge_validate.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import Counter
    users = [("u1", "vip"), ("u2", "normal")]
    orders = [("o1", "u1"), ("o2", "u1"), ("o3", "u2")]
    cnt = Counter(uid for _, uid in orders)
    for uid, level in users:
        print(uid, level, "订单数", cnt.get(uid, 0))
    dup = [("u1", "vip"), ("u1", "old")]  # 用户表键不唯一,m:1 校验会失败
    print("用户表键重复:", [k for k, v in Counter(u for u, _ in dup).items() if v > 1])
else:
    users = pd.DataFrame({"user_id": ["u1", "u2"], "level": ["vip", "normal"]})
    orders = pd.DataFrame({"order_id": ["o1", "o2", "o3"], "user_id": ["u1", "u1", "u2"]})
    m = orders.merge(users, on="user_id", validate="m:1")
    print(m, end="\n\n")
    bad_users = pd.DataFrame({"user_id": ["u1", "u1", "u2"], "level": ["vip", "old", "normal"]})
    try:
        orders.merge(bad_users, on="user_id", validate="m:1")
    except pd.errors.MergeError as e:
        print("键膨胀被拦截:", e)
```

**追问**:
- 追问 1:validate 检查的是哪一侧的键?—— 关系两侧都检查,任何一侧不满足声明就报错。
- 追问 2:如果业务真的需要 m:m?—— 显式声明 `validate="m:m"` 表示接受,但要在注释里写清膨胀是预期行为并评估行数。
