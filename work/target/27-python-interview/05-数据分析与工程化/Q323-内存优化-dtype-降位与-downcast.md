---
title: [Q323] 内存优化:.dtype 降位与 downcast
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q323 · 内存优化:.dtype 降位与 downcast

> 难度:★★☆ | 标签:pandas, 内存

**问**:如何把一个吃掉大量内存的 DataFrame 瘦身?有哪些降位技巧?

**答**:核心是按数据实际范围选最小够用的 dtype:int64 降到 int32/int16/int8,float64 降到 float32,object 字符串转 category,重复率高的布尔转 bool。pandas 提供 `pd.to_numeric(downcast=...)` 自动降位;工程做法是写一个通用的 reduce_memory 函数,读取后统一处理再进入计算。注意降位有精度风险,金额类列建议保留 decimal 或 float64,降位前确认极值范围。

```python
# file: code/05_数据分析与工程化/q323_memory_downcast.py
try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def reduce_memory(df):
    for col in df.columns:
        t = df[col].dtype
        if pd.api.types.is_integer_dtype(t):
            df[col] = pd.to_numeric(df[col], downcast="integer")
        elif pd.api.types.is_float_dtype(t):
            df[col] = pd.to_numeric(df[col], downcast="float")
        elif pd.api.types.is_object_dtype(t):
            if df[col].nunique() / len(df) < 0.5:
                df[col] = df[col].astype("category")
    return df

if __name__ == "__main__":
    if PANDAS:
        rng = np.random.default_rng(0)
        df = pd.DataFrame({
            "a": rng.integers(0, 100, 50_000),        # int64 -> int8
            "b": rng.random(50_000),                  # float64 -> float32
            "c": rng.choice(["x", "y"], 50_000),      # object -> category
        })
        before = df.memory_usage(deep=True).sum()
        df = reduce_memory(df)
        after = df.memory_usage(deep=True).sum()
        print(f"{before/1e6:.2f}MB -> {after/1e6:.2f}MB")
        print(df.dtypes.to_dict())
    else:
        print("标准库思路:选择最小够用的数值类型,枚举列用整数编码")
```

**追问**:
- float64 降 float32 有什么风险?——精度损失与求和误差累积,金额、经纬度这类列不要降;特征矩阵可降,训练显存减半。
- int 列有空值降位会怎样?——强制升 float 并引入 NaN 的二进制噪声;应先转 nullable Int64 再降位。
- 降位后怎么验证无损?——对比降位前后 describe 的 min/max 与抽样值,超 int8 范围会被静默截断,to_numeric 返回值要检查 dtype 变化。

---
