---
title: "题 5.3.3：count(*)、count(1)、count(id)、count(字段) 哪个快？为什么 InnoDB 不存总行数？"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
---

### 题 5.3.3：count(*)、count(1)、count(id)、count(字段) 哪个快？为什么 InnoDB 不存总行数？

**【参考回答（可背）】**
- InnoDB 不存总行数因为 **MVCC**：不同事务看到的行数不同（并发未提交/已删除），无法全局缓存一个数。
- 四者效率：count(*) ≈ count(1) ≥ count(id) > count(字段)。count(*)/count(1) 优化器选最小索引树扫；count(id) 要取主键值；count(字段) 要判 NULL 且不能走覆盖就回表。
- 大表计数方案：explain 估算（不精确）、缓存计数（Redis，接受误差）、**计数表**（独立小表 + 事务内增减 + 定期校准）、信息表分区汇总。

**【P10 加分项】**
把 count 问题升华成"分布式计数一致性"：高并发计数（点赞数/库存显示）= 计数与明细的最终一致问题，给出"明细为准 + 异步聚合 + 展示容忍分钟级误差 + 对账兜底"的通用范式。

---
