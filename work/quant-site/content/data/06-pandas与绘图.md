---
title: 高效数据处理与绘图（pandas / matplotlib）
track: data
order: 6
summary: 用 pandas 做清洗、运算、分组，用 matplotlib 绘图，数据分析的主战场，也是量化因子计算的核心。
---

# 高效数据处理与绘图

> 拿到数据后进入预处理与分析。`pandas` 是处理表格的利器，`matplotlib` 负责把结果画出来。

## pandas：处理与分析表格

```python
import pandas as pd

df = pd.read_csv("data/kline.csv")          # 读取
df.shape; df.head(); df.info()               # 概览

# 清洗
df.isnull().sum()                            # 缺失统计
df = df.dropna()                             # 删缺失
df = df.drop_duplicates()                    # 去重

# 运算：向量化，无需 for 循环
df["ma5"] = df["close"].rolling(5).mean()    # 5 日均线
df["ret"] = df["close"].pct_change()         # 收益率

# 分组：按维度聚合
df.groupby("industry")["ret"].mean()
```

核心：`read_csv/read_excel`、`shape/head/info`、缺失与去重、**列运算与滚动窗口**、`groupby` 分组、`merge/concat` 合并。

## matplotlib：绘图

```python
import matplotlib.pyplot as plt

df["close"].plot(figsize=(10, 4), title="收盘价")
plt.xlabel("date"); plt.ylabel("price")
plt.show()

# 常见图：折线(趋势)/柱状(对比)/散点(关系)/直方图(分布)
```

## 迁移到量化

- **缺失/异常/去重**：行情数据同样有停牌、坏点，必须先清洗。
- **滚动窗口 `rolling`**：均线、波动率、RSI 都靠它。
- **`groupby`**：按行业/板块/因子分组统计。
- **重采样 `resample`**：分钟线合成日线。

> pandas 是数据分析与量化因子计算的共同主战场；会清洗、会运算、会分组、会画图，就具备了从数据到结论的完整能力。
