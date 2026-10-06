# 124 undo log 与 MVCC

> 分类：MySQL 内核 | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**undo log**/**回滚**/**MVCC**/**read view**
> 原文锚点：第 41~93 段「撤销日志…回滚+MVCC、版本链、purge 清理」

## 一句话总述
**undo log** 是 InnoDB 的**逻辑日志**，记录数据修改**前的旧值**：一面用于**事务回滚**（保证原子性 A），一面构建**版本链**支持 **MVCC 快照读**（并发版本控制）；自身也受 redo 保护。

## 面试官视角
- 考察意图：是否理解 undo 的"双重身份"（回滚 + MVCC），及其与 redo 的分工。
- 分档：P5 知 undo 用于回滚；P6 知 undo 也支撑 MVCC；P7 能讲版本链、read view 与 purge 清理时机。
- 红旗答案：以为 undo 只管回滚、与 MVCC 无关。
- 惊艳点：点出 **undo 自身改动也写 redo**（undo 的持久性靠 redo 保证），且 MVCC 靠 read view 判断版本可见性 `[经验]`。

## 主问答
**Q（面试官原话）：** undo log 是什么？和 redo 什么关系？
**A：**
1. **结论**：undo 是逻辑日志，负责回滚（A）+ MVCC；redo 是物理日志，负责重放（D）——二者分工不同、互相保护。
2. **机制**：改数据前先把旧值写 undo；回滚时按 undo 做**反向操作**（insert↔delete、update 写回旧值）。MVCC 靠 undo **版本链 + read view** 让读事务看到历史版本，实现非锁定读。
3. **边界**：当某旧版本不被任何活跃 read view 需要时，由 **purge 线程**清理。这也解释了**自增 ID "断层"**——事务回滚后已分配的 ID 不回收，中间号段被预留。

**加分层：** 原文称 MVCC"是乐观锁"不严谨——MVCC 是快照读机制（配合锁实现），不是单纯的乐观锁；本卡已纠正。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | undo 干嘛？ | 基础 | 回滚 | P5 |
| L2 | 和 MVCC？ | 关联 | 版本链+read view | P6 |
| L3 | 何时清理？ | 机制 | purge/无活跃readview | P7 |
| L4 | 和 redo 关系？ | 分工 | 逻辑vs物理/互保 | P7 |
| L5 | 自增断层？ | 进阶 | 回滚不回收ID | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| InnoDB（MySQL 5.5+） | 8.0 自增持久化到数据字典 | 答"undo 回滚+MVCC；8.0 自增 ID 重启后断层减少但仍不回退已用 ID" |

## 关键代码
```sql
-- 观察当前事务与历史版本（MVCC 由 read view 控制，无直接"看历史"SQL）
SELECT * FROM information_schema.innodb_trx\G
SHOW ENGINE INNODB STATUS\G   -- 含 undo/log 相关信息
```

## 总结与追问预判
undo = 逻辑日志，回滚(A) + MVCC，自身靠 redo 保护，旧版本由 purge 清理。追问接"MySQL 日志全景"与"两阶段提交崩溃恢复"。

## ⚠️ 原文纠错
1. 机翻崩坏词归一：`andlog`/`androllog`/`安卓log`/`anroidlogo`/`安装log`/`anduallog`/`andiog`/`unddodata`→**undo log**；`inlOG`→**InnoDB**；`原则性`→**原子性**；`搜狗查询`/`circle操作`→**SQL 查询/操作**。事实正确，仅术语崩坏，本卡已归一 `[经验]`。
2. 精度补正：原文称"MVCC 是 MySQL 应对并发的乐观锁"——不准确；MVCC 是**快照读/版本链**并发控制机制（与锁配合），非单纯乐观锁；本卡已纠。另：原文"主键 ID 断层因回滚预留"准确（InnoDB 自增分配后即占用，回滚不回收）。
