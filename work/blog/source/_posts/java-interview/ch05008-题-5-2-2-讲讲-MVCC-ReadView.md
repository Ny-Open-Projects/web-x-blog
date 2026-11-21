---
title: "题 5.2.2：讲讲 MVCC？ReadView 是怎么生成的？RC 和 RR 的区别在哪？"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 5.2.2：讲讲 MVCC？ReadView 是怎么生成的？RC 和 RR 的区别在哪？

**【参考回答（可背，高频压轴预备题）】**
1. **隐藏列**：每行有 trx_id（最后修改事务 ID）、roll_pointer（指向 undo log 版本链）。
2. **ReadView**：一致性视图，四要素：m_ids（生成时活跃未提交事务集合）、min_trx_id、max_trx_id、creator_trx_id。
3. **可见性判断**（必背逻辑）：沿 undo 版本链从新到旧找，对每个版本的 trx_id：
   - == creator → 可见（自己改的）；
   - < min_trx_id → 可见（生成视图前已提交）；
   - ≥ max_trx_id → 不可见（视图生成后才开始）；
   - 介于 min/max 之间：在 m_ids 里 → 不可见（未提交）；不在 → 可见（已提交）。不可见就顺着 roll_pointer 找上一版本重复判断。
4. **RC 与 RR 的唯一区别**：RC **每条查询语句**生成新 ReadView（能看到别人最新已提交）；RR **事务第一次查询**生成、整个事务复用（实现可重复读）。

**【追问链】**
1. RR 下能完全避免幻读吗？→ **不能完全避免**。快照读（普通 select）靠 MVCC 防幻读；**当前读**（select ... for update / update / delete）靠**间隙锁（gap lock）+ 行锁合成 Next-Key Lock** 防幻读；但"快照读后紧跟当前读"的混用模式仍会出现幻读（经典例子：先 select 无记录，update 却更新到了别人插入的行）。
2. RR 为什么是默认？→ 历史主因：基于语句复制（statement binlog）在 RC 下会出现主从不一致（RC 没有间隙锁+binlog 顺序问题），RR 才安全；现在 row 格式复制下 RC 其实也安全，互联网公司很多业务切 RC（锁冲突更小、死锁更少）。

**【P10 加分项】**
能画出undo 版本链 + ReadView 判断过程的图，并给出工程结论："我们把交易库从 RR 切到 RC 的收益：间隙锁消失后死锁率下降一个数量级；前提是 binlog 已是 ROW 格式 + 从库 GTID 复制。选隔离级别是工程决策不是教条。"

---
