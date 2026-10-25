---
title: 第5课 · Pandas 高阶操作
track: quant
order: 5
summary: 批量导入、HDF 存取、K 线周期转换（resample）、groupby 分组——策略实战的常用高阶技巧。
---

# 第5课 · Pandas 高阶操作

> 第五课打基础，本课通过真实任务练高阶：批量导入、持久化、周期转换、分组统计——都是策略里天天要用的操作。

## 5.1 批量导入数据

交易所有多个品种、多日文件，需批量读入汇总成一张表：

```python
import pandas as pd, glob, os

frames = []
for f in glob.glob("data/bittrex/EOSUSD/*.csv"):
    frames.append(pd.read_csv(f))
df = pd.concat(frames, ignore_index=True)   # 汇总成一张 DataFrame
print(df.shape)
```

## 5.2 用 HDF 存取数据

个人量化**不必一上来就用 MySQL**：数据量不大时 CSV 即可；要更强功能又比数据库简单，推荐 **HDF**（与 pandas 高度集成、读写快）。

```python
df.to_hdf("data/eosusd_1min.h5", key="df", mode="w")   # 保存
df = pd.read_hdf("data/eosusd_1min.h5", key="df")       # 读取
```

## 5.3 转换数据周期（resample）

策略可能用 1 分钟、5 分钟、1 小时或日线；用 `resample` 把细粒度合成粗粒度 K 线：

```python
df = pd.read_hdf("data/eosusd_1min.h5", key="df")
df = df.set_index("candlebegintime")           # 以时间为索引

rule = "5T"    # 5 分钟；"1H"=小时，"1D"=日
kline = df["close"].resample(rule).agg({
    "open": "first", "high": "max", "low": "min",
    "close": "last", "volume": "sum",
})
kline.dropna(inplace=True)
print(kline.head())
```

## 5.4 groupby 分组处理

按某一列把数据分组，对每组分别统计/计算——非常强大：

```python
# 例：按品种分组，统计每个品种的平均成交量
df = pd.read_csv("data/bittrex_1h.csv")
g = df.groupby("symbol")["volume"].mean()
print(g)

# 例：按品种 + 按小时分组求均值
df.groupby(["symbol", df["candlebegintime"].dt.hour])["close"].mean()
```

> 小结：批量导入解决「多文件」，HDF 解决「存与取」，resample 解决「周期切换」，groupby 解决「分组统计」。掌握这四招，数据处理环节基本通畅。下一课进入交易所接口，把真实数据接进来。
