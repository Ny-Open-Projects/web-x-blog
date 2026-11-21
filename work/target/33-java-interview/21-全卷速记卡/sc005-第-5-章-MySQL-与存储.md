---
title: "第 5 章 MySQL 与存储"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

## 第 5 章 MySQL 与存储

1. B+ 树：矮胖省 IO、叶子链表扫范围；主键自增防页分裂。
2. 二级索引存主键，回表是成本；覆盖索引免回表；ICP 引擎层先过滤。
3. MVCC 四要素 ReadView + 版本链；RC 每语句、RR 每事务一次视图。
4. RR 防幻读：快照读靠 MVCC，当前读靠 Next-Key；混用仍有幻读。
5. 两阶段提交：redo prepare → binlog → redo commit；崩溃看 binlog 定夺。
6. 双 1 最安全；组提交提吞吐；参数翻译成业务风险再定。
7. 死锁预防：固定顺序、小事务、热点分段、RC 减间隙锁。
8. 主从延迟：关键读走主库；并行复制 writeset；半同步保不丢；GTID 必开。
9. 分库分表：先榨干单库，分片键选 user_id，扩容用双写四步，基因法兜底。
10. 资金三道闸：幂等 → 条件更新 → 对账冲正。
11. 索引评审十条：趋势递增主键、覆盖高频模式、区分度、单表≤5、每索引有主。
12. Buffer Pool 双 LRU 防污染；命中率骤降=查新增大扫描。
13. 大表 DDL 走 gh-ost：binlog 流+cut-over，DDL 平台化。
