---
title: [Q1039] category 的内存收益与转化陷阱
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1039 · category 的内存收益与转化陷阱

> 难度:★★★☆ | 标签:pandas, 性能

**问**:什么情况下把字符串列转 category 收益最大?转化后有哪些容易踩的坑?

**答**:category 用整数 codes 加一张类别字典表示字符串,基数低、重复度高的列(城市、状态、渠道)内存能降一个数量级,groupby/sort 也更快。三个经典坑:切片后残留未使用的类别,占内存且会让 groupby 出空组,要 `cat.remove_unused_categories()`;两个 category 列合并时类别集合不一致会被升回 object,应先 `union_categoricals` 或统一 dtype;把高基数字段(用户 ID)转 category 反而膨胀,先算基数占比再决定。另外 groupby 默认会输出所有类别组合,加 `observed=True` 只保留实际出现的。

```python
# file: code/05_数据分析与工程化/q1039_category_memory.py
try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import Counter
    values = ["beijing", "shanghai"] * 50
    codes = {v: i for i, v in enumerate(sorted(set(values)))}
    print("类别字典:", codes)
    print("存储为 codes 列表长度:", len(values), "类别数:", len(codes))
else:
    big = pd.DataFrame({"city": ["beijing", "shanghai"] * 50_000})
    print("object 内存:", big.memory_usage(deep=True).sum())
    big["city_c"] = big["city"].astype("category")
    print("category 内存:", big["city_c"].memory_usage(deep=True).sum())
    sub = big[big["city"] == "beijing"]
    print("切片残留类别数:", len(sub["city_c"].cat.categories))
    print("清理后类别数:", len(sub["city_c"].cat.remove_unused_categories().cat.categories))
```

**追问**:
- 追问 1:怎么判断一列值不值得转 category?—— `nunique / len` 占比低(经验上百分之几以下)且是字符串时收益大。
- 追问 2:category 与 groupby 的 observed 参数什么关系?—— 不加 observed 会按类别全集分组输出空组,聚合结果行数虚高。
