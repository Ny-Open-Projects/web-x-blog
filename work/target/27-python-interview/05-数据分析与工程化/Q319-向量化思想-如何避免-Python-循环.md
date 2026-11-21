---
title: [Q319] 向量化思想:如何避免 Python 循环
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q319 · 向量化思想:如何避免 Python 循环

> 难度:★★★ | 标签:numpy, 向量化

**问**:什么是向量化?给出把"逐行 if-else 循环"改写成向量化代码的思路。

**答**:向量化是把对单个元素的操作上升为对整个数组的批量运算,由 C 层的 numpy 完成循环,避免 Python 解释器开销和逐个装箱对象。改写思路:逐行条件赋值改 np.where 或 np.select(多分支)、逐行算术改列运算、字符串日期解析交给 pd.to_datetime、复杂逻辑尽量拆解为若干布尔掩码的组合。判断标准是:代码里不出现 `for ... in df.iterrows()`。

```python
# file: code/05_数据分析与工程化/q319_vectorization.py
try:
    import numpy as np
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({"x": np.arange(-5, 5), "y": np.arange(10) * 1.5})
    # 反例:for idx, row in df.iterrows(): 手写 if-else
    # 向量化:多分支用 np.select
    conditions = [df["x"] > 0, df["x"] < 0]
    choices = ["pos", "neg"]
    df["sign"] = np.select(conditions, choices, default="zero")
    # 条件赋值用 np.where
    df["clip_y"] = np.where(df["y"] > 10, 10, df["y"])
    print(df.head())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        xs = list(range(-5, 5))
        out = ["zero" if x == 0 else ("pos" if x > 0 else "neg") for x in xs]
        print(list(zip(xs, out)))
```

**追问**:
- iterrows 慢在哪?——每行构造一个 Series、逐元素装箱成 Python 对象;比向量化慢 1-2 个数量级,比 itertuples 更慢。
- np.select 什么时候用?——多分支条件赋值:`np.select([cond1, cond2], [v1, v2], default=0)`,替代嵌套 if 的逐行写法。
- 怎么训练团队写向量化?——评审硬指标:不出现 iterrows/apply(axis=1);复杂逻辑先想掩码组合,再想 numba/cython 兜底。

---
