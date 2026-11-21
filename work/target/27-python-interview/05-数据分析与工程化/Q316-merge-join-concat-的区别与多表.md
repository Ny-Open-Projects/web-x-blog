---
title: [Q316] merge / join / concat 的区别与多表关联陷阱
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q316 · merge / join / concat 的区别与多表关联陷阱

> 难度:★★★ | 标签:pandas, merge

**问**:merge、join、concat 各自的用途是什么?多表关联时最容易踩哪些坑?

**答**:merge 按列(键)横向关联,等价 SQL join,支持 inner/left/right/outer;join 是基于索引的 merge 语法糖;concat 是纵向堆叠或横向拼接,不按键匹配。经典陷阱:关联键重复导致笛卡尔积让行数暴涨(先检查键唯一性)、浮点/字符串类型不一致导致 join 不上、outer join 后键列出现 NaN、以及 left join 后误以为行数不变。生产守则:merge 前断言键唯一、merge 后断言行数符合预期。

```python
# file: code/05_数据分析与工程化/q316_merge_join_concat.py
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    orders = pd.DataFrame({"uid": [1, 2, 2, 3], "amt": [10, 20, 30, 40]})
    users = pd.DataFrame({"uid": [1, 2, 2], "name": ["a", "b", "b2"]})
    # 陷阱演示:users 的 uid 重复,join 后行数膨胀
    m = orders.merge(users, on="uid", how="left")
    assert len(m) > len(orders), "键不唯一导致笛卡尔积"
    print(len(orders), "->", len(m))
    # 生产守则:先验证唯一性再 merge
    assert users["uid"].is_unique, "users.uid 存在重复"
    concat_df = pd.concat([orders, orders], ignore_index=True)
    print(concat_df.shape)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        orders = [(1, 10), (2, 20), (2, 30), (3, 40)]
        users = {1: "a", 2: "b"}  # 唯一键字典,天然防重复
        for uid, amt in orders:
            print(uid, amt, users.get(uid))
```

**追问**:
- validate 参数有什么用?`merge(..., validate="m:1")` 会在键基数不满足时直接抛错,把"行数膨胀"从静默 bug 变成显式失败,推荐默认开启。
- merge 后行数怎么断言?——关联前后 `len(df)` 对比 + validate 参数;m:m 关联几乎总是设计错误。
- 键类型不一致的典型现象?——int64 对 object 关联结果为空且不报错;merge 前 `astype` 统一键类型。
- outer join 的 NaN 怎么处理?——键列 NaN 说明某侧缺记录,按业务填「未匹配」标记而不是 0,否则统计口径污染。
