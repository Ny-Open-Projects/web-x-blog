# 1234 深挖：MySQL 锁机制（三）体系与调优

> 分类：MySQL 锁 | 难度：高 | 题型：深挖 | 频率：高 | 关键词：**行锁、读类型、自增锁、间隙锁、隔离级别**
> 原文锚点：第 1~97 段「MySQL 锁全景（三）」

## 思路与架构
把「一条 SQL 怎么加锁」串成一条链：
1. **读类型定是否加锁**：一致性读（普通 SELECT，MVCC 无锁）vs 锁定读（FOR UPDATE 加 X、FOR SHARE 加 S）。
2. **写必加 X**：UPDATE/DELETE 定位后加 X 记录锁；RR 下默认 next-key（含间隙）。
3. **自增单独管**：AUTO_INCREMENT 走自增锁（传统表锁/轻量级锁），由 autoinc_lock_mode 控。
4. **幻读靠间隙**：RR 下间隙锁锁区间、只防插入，next-key 锁 = 记录锁 + 间隙锁。
5. **隔离级别定粒度**：RR 有间隙、RC 无；配置与版本（5.6.3 移除 unsafe_for_binlog）决定默认行为。

## 方案取舍
- **RR vs RC**：RR 用间隙/next-key 防幻读但锁粒度大、易阻塞插入；RC 无间隙、并发高但可能幻读——一致性要求选 RR，高并发写评估 RC。
- **autoinc_lock_mode**：2（轻量、8.0 默认）性能最高，但必须配 row 格式 binlog 保主从一致；若用 statement binlog 须降回更保守模式。
- **显式锁定读**：需要「读后改」时用 FOR UPDATE 而非先 SELECT 再改，避免二次查询间的竞态。

## 答题技巧
- 答「读加什么锁」用**二分法**：一致性读无锁、锁定读 FOR UPDATE(X)/FOR SHARE(S)，一句话定调。
- 必点 **「间隙锁只防插入不防读写、且间隙锁间不互斥」**——两个反直觉点，是区分 P6/P7 的关键。
- 被追问主从不一致：直接抛「mode=2 + statement binlog 主键错位」，并给 row binlog 解法。
- 收尾强调「走索引才能精准锁行，否则锁范围放大」，展示实战视野。

## ⚠️ 原文纠错
1. 事实核校： [经验] 一致性读/锁定读之分、FOR UPDATE(X)/FOR SHARE(S)、写加 X、自增锁与 autoinc_lock_mode、间隙锁防幻读且仅 RR 生效、5.6.3 移除 unsafe_for_binlog——均为架构性归纳，与 InnoDB 锁机制一致。
2. 崩坏词归一：源码将 InnoDB / 行锁 / 幻读 / 事务 / 排他锁 / 自增 等音译为崩坏词；本卡统一为规范术语。
