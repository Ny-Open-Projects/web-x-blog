---
title: [Q321] 数据类型优化:category / datetime / nullable Int64
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q321 · 数据类型优化:category / datetime / nullable Int64

> 难度:★★★ | 标签:pandas, dtype

**问**:pandas 有哪些节省内存或提升正确性的数据类型?category 什么时候反而不能用?

**答**:低基数重复字符串列(性别、城市、状态)转 category 可省数倍到数十倍内存并加速 groupby;日期时间列转 datetime64 才能做时序运算和重采样;带缺失的整数列用 nullable 的 Int64(大写)避免被强制转 float 丢精度。category 的坑:只有基数远小于行数时才划算,基数过高(如用户 ID)会退化甚至更慢;且 category 列 merge/排序语义与 object 列有差异,若类别集合需动态扩展要用 `.cat.add_categories`。加载后先 `df.dtypes` 审计是数据工程的基本功。

```python
# file: code/05_数据分析与工程化/q321_dtype_optimize.py
try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    n = 100_000
    df = pd.DataFrame({
        "city": np.random.default_rng(0).choice(["BJ", "SH", "SZ"], n),
        "val": np.random.default_rng(1).integers(0, 1000, n),
        "cnt": pd.array([1, None] * (n // 2), dtype="Int64"),  # nullable int
    })
    before = df.memory_usage(deep=True).sum()
    df["city"] = df["city"].astype("category")
    after = df.memory_usage(deep=True).sum()
    print(f"memory {before/1e6:.1f}MB -> {after/1e6:.1f}MB")
    print(df["cnt"].dtype, df["city"].cat.categories.tolist())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        print("标准库层面:用整数编码枚举值 + 常量表模拟 category 思路")
```

**追问**:
- datetime 列为什么读 CSV 后常变成 object?因为原始格式混杂或未指定 parse_dates,需要 `pd.to_datetime(errors="coerce")` 统一,coerce 会把脏值变 NaT 便于后续排查。
- category 什么时候反而更慢?——高基数列(用户 ID)字典编码开销大、merge 时类别对齐成本高;经验阈值是唯一值数 < 行数的 50%。
- nullable Int64 解决什么?——含 NaN 的整数列不再被升为 float64 丢精度;计算生态兼容性(polars/sklearn)要先确认。
- 内存审计的入口?——`df.memory_usage(deep=True).sum()` 与 per-column 排名,object 列通常占大头,先转 category/datetime。
