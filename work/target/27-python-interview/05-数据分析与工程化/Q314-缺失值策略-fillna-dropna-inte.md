---
title: [Q314] 缺失值策略 fillna / dropna / interpolate 与业务选型
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q314 · 缺失值策略 fillna / dropna / interpolate 与业务选型

> 难度:★★★ | 标签:pandas, 缺失值

**问**:面对数据表中的 NaN,应如何选择填充、删除还是插值?各自的风险是什么?

**答**:选型取决于缺失机制和业务含义:dropna 适合缺失比例很小且随机(MCAR)的场景,但会缩小样本、可能引入偏差;fillna 适合缺失有明确业务含义的场景(金额填 0、状态填 unknown),向前/向后填充 ffill/bfill 适合时间序列;interpolate 适合连续型时序数据按线性或时间插值。风险点:对有偏分布用均值填充会压扁方差,对时间序列盲目 dropna 会打断连续性。生产上应把"缺失处理策略"作为显式配置而不是散落各处的魔法数字。

```python
# file: code/05_数据分析与工程化/q314_missing_values.py
try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({
        "ts": pd.date_range("2026-01-01", periods=6, freq="D"),
        "amount": [100, np.nan, np.nan, 160, np.nan, 200],
        "city": ["BJ", None, "SH", None, "SZ", "BJ"],
    })
    print(df.dropna(subset=["city"]).shape)          # 按关键列删
    print(df["amount"].fillna(0).tolist())           # 业务填 0
    print(df["amount"].ffill().tolist())             # 时序向前填充
    print(df["amount"].interpolate().round(1).tolist())  # 线性插值
    print(df.assign(city=df["city"].fillna("unknown")).isna().sum().to_dict())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        amounts = [100, None, None, 160, None, 200]
        filled = []
        last = None
        for v in amounts:            # ffill 的标准库等价实现
            if v is not None:
                last = v
            filled.append(last)
        print("ffill:", filled)
        print("fill 0:", [0 if v is None else v for v in amounts])
```

**追问**:
- 如何量化缺失情况?先 `df.isna().mean()` 看每列空值率,再按列分类决策:主键缺失直接拒绝,指标列按业务填,高缺失列考虑整列丢弃。
- 前向填充什么时候用错?——非时间序列数据 ffill 会把无关行的值蔓延;它只对按时间有序的列有意义。
- 均值填充的风险?——压扁方差、低估相关性,且训练/推理分布不一致;树模型可以给树「缺失作为单独分支」的能力(xgboost 原生处理)。
- 缺失本身是信号怎么办?——加 is_missing 指示列保留信息;很多业务场景「是否缺失」比填充值更有预测力。
