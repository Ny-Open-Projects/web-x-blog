---
title: 第4课 · Pandas 入门操作
track: quant
order: 4
summary: 用真实行情数据上手 pandas：导入、查看、列操作、筛选、排序、时间与滚动——后续所有策略的地基。
---

# 第4课 · Pandas 入门操作

> `pandas` 是量化数据处理的核心库，之后所有策略都建立在它之上。本课不照本宣科，直接拿一份行情数据「玩会」它。

## 4.1 数据导入

```python
import pandas as pd
df = pd.read_csv("data/coin.csv", nrows=15)   # 读 CSV，nrows 限制行数
print(type(df))   # <class 'pandas.core.frame.DataFrame'>
```

## 4.2 查看与选取

```python
df.shape            # (行数, 列数)，如 (1440, 6)
df.shape[0]         # 只取行数
df.head()           # 前 5 行
df.tail(3)          # 后 3 行
df["close"]         # 取「收盘价」这一列（Series）
df[["open", "close"]]   # 取多列
```

## 4.3 列操作（整列向量化）

```python
# 字符串列：整体拼接
df["北京时间"] = "2018-01-24 " + df["时间"]

# 数值列：整体运算（向量化，无需 for 循环）
df["close_x100"] = df["close"] * 100
```

## 4.4 筛选与缺失处理

```python
# 布尔筛选：只留收盘价 > 100 的行
up = df[df["close"] > 100]

# 处理缺失值
df.isnull().sum()        # 每列缺失数量
df2 = df.dropna()        # 删含缺失的行
df3 = df.fillna(0)       # 用 0 填充
```

## 4.5 合并、去重、排序

```python
df.sort_values(by="candlebegintime", ascending=True)  # 按时间升序
df.drop_duplicates()                                   # 去重
pd.concat([df1, df2])                                  # 上下拼接多张表
```

## 4.6 字符串与时间、滚动操作

```python
# 时间列常是字符串，需转成时间类型才能按时间运算
df["candlebegintime"] = pd.to_datetime(df["candlebegintime"])

# 滚动窗口：如 5 周期移动平均
df["ma5"] = df["close"].rolling(5).mean()
```

> 小结：导入 → 查看/选取 → 列操作 → 筛选/缺失 → 排序/合并 → 时间/滚动，这一套覆盖了量化数据预处理 80% 的场景。下一课讲批量导入、HDF 存储、周期转换与分组等高阶操作。
