---
title: 获取股票数据：JQData 查询行情
track: basics
order: 5
summary: 认识 JoinQuant 聚宽平台与 JQData，用 Python API 查询行情数据。
---

# 获取股票数据：JQData 查询行情

## 一、JoinQuant 聚宽平台

**JoinQuant（joinquant.com）** 是国内知名的免费量化平台，提供成熟的数据接口与回测环境。其数据能力通过**数据字典**组织，涵盖：

- 股票数据：行情、财务、基本面
- 行业数据、指数数据
- 宏观经济数据
- 期货数据
- 技术分析指标

数据字典按一、二级菜单分好，每类都有说明文档，可逐项查看可调用的字段与用法。

## 二、两种取数入口

1. **数据字典**入口：按分类浏览有哪些数据、字段含义。
2. **本地 API** 入口：通过 Python 版 API（或其他语言 SDK）直接调用 `get_price`、`get_fundamentals` 等函数取数，更直观。

## 三、用 JQData 查询行情（示例）

```python
from jqdatasdk import *
auth("your_username", "your_password")   # 先用账号密码认证

# 查询日线行情：茅台，2024 年
df = get_price("600519.XSHG", start_date="2024-01-01", end_date="2024-12-31",
               frequency="daily", fields=["open", "close", "high", "low", "volume"])
print(df.tail())

# 查询基本面：市盈率、市值等
q = query(valuation).filter(valuation.code == "600519.XSHG")
fund = get_fundamentals(q, date="2024-06-30")
print(fund[["code", "pe_ratio", "market_cap"]])
```

字段说明：
- `get_price`：取行情，`frequency` 支持 `daily` / `minute` 等，`fields` 指定 OHLCV 等。
- 代码后缀：`.XSHG` 上交所、`.XSHE` 深交所。
- `get_fundamentals`：取财务与估值因子（PE、市值等）。

## 四、从取数到看板

拿到 DataFrame 后即可进入量化主线：

```text
取数(get_price) → 清洗整理(Pandas) → 计算指标(MA/MACD/RSI) → 策略信号 → 回测 → 可视化
```

> 本站「数据看板」已把这条链路的前半段跑通：实时从公开行情接口取数、计算指标、规则化综合出方向与操作指引——你可以对照本课理解每个数字是怎么来的。后续课程会带你用 Python 自己实现取数与指标。
