---
title: 数据处理：Excel 与 SQL
track: data
order: 2
summary: 用 Excel 做清洗整合，用 SQL 从数据库提取数据，数据预处理的两把基础利器。
---

# 数据处理：Excel 与 SQL

## 一、Excel：最基础的数据预处理

电子表格是最普遍的数据处理工具。核心是**预处理**三件事：

| 操作 | 含义 |
|---|---|
| 清洗 | 处理缺失值、异常值 |
| 提取 | 删除不需要的字段/行 |
| 整合 | 把其他表/数据源的维度合并进来 |

常用能力：数学/统计函数（SUM、AVERAGE、VLOOKUP）、排序筛选、数据透视表、条件格式。**量化里同样适用**：拿到行情 CSV 第一件事就是查缺失、查异常、去重。

## 二、SQL：从数据库提取数据

互联网企业的数据存在数据库里（主流 MySQL / Oracle）。SQL 是与数据库对话的语言：

```sql
-- 查询某标的最新 30 条日线，按日期倒序
SELECT trade_date, open, high, low, close, volume
FROM kline_daily
WHERE symbol = '510300'
ORDER BY trade_date DESC
LIMIT 30;

-- 聚合：每天的平均价与总成交量
SELECT trade_date, AVG(close) AS avg_close, SUM(volume) AS total_vol
FROM kline_daily
GROUP BY trade_date;
```

关键语法：`SELECT`（选列）/ `FROM`（选表）/ `WHERE`（行过滤）/ `GROUP BY`（分组）/ `ORDER BY`（排序）/ `LIMIT`（限量）/ 聚合函数 `COUNT/SUM/AVG/MAX/MIN`。

> Excel 适合小数据手工清洗，SQL 适合从数据库批量提取与聚合。量化的历史行情、因子表都存在数据库里，SQL 是取数的基本功。
