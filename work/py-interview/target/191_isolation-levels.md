# 191. 事务隔离级别：RU/RC/RR/Serializable

> 分类：数据库 | 难度：L2 | 题型：对比题 | 频率：高 | 关键词：**隔离级别** / **Read Uncommitted** / **Read Committed** / **Repeatable Read** / **Serializable** / **MySQL默认RR**
> 原文锚点：第 52~59 段「数据库定义四种隔离级别：读未提交/读已提交/可重复读/串行化；MySQL 默认 Repeatable Read；串行化效率最低」

## 一句话总述
SQL 标准定义四级隔离：**Read Uncommitted（读未提交）**→**Read Committed（读已提交）**→**Repeatable Read（可重复读）**→**Serializable（串行化）**，级别越高并发异常越少但性能越差；**MySQL/InnoDB 默认是 Repeatable Read**。

## 面试官视角
- **考察意图**：是否记得四级顺序、各级解决哪些异常，以及 MySQL 的默认值。
- **P5** 能背出四级 + 说 MySQL 默认 RR / **P6** 能讲清每级解决哪些异常（RC 解决脏读、RR 解决不可重复读、Serializable 解决全部） / **P7** 能说清 RR 下 InnoDB 靠 MVCC+Next-Key Lock 已防幻读，且 RC 是多数互联网（如 PostgreSQL、Oracle）的默认级别。
- **红旗**：说"Serializable 才防幻读"而忽略 InnoDB RR 已用间隙锁防住；或记错 MySQL 默认级别（不是 RC）。
- **惊艳点**：PostgreSQL/Oracle 默认 **Read Committed**，而 MySQL 默认 **Repeatable Read**——公司里常主动调成 RC 以降低间隙锁带来的锁冲突 `[经验]`。

## 主问答
**Q（面试官原话）：** 事务隔离级别有哪些？MySQL 默认是哪个？

**A · 标准答案骨架：**
1. **先给结论**：四级——**读未提交 < 读已提交 < 可重复读 < 串行化**；**MySQL 默认 Repeatable Read**。
2. **再给机制**：**RU** 能读未提交数据（有脏读）；**RC** 只能读已提交（解决脏读，但有不可重复读）；**RR** 同一事务内重复读一致（解决不可重复读，InnoDB 还防幻读）；**Serializable** 完全串行（解决全部异常，但并发最低）。
3. **最后给边界**：级别越高越安全但**锁/快照开销越大、并发越低**；实际选型在"安全"与"性能"间权衡，互联网常基于 RC/RR；Serializable 仅用于强一致且低并发场景。

**加分层**：隔离级别本质是**在一致性强度与并发性能之间取舍**；调级别比改业务代码便宜，是排障第一步 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 四级隔离 | 基本认知 | RU/RC/RR/SR | 换题 → 不及格 |
| L2 | 各级解决啥 | 是否背的 | RC防脏读/RR防不可重复 | 判 P5 |
| L3 | MySQL 默认 | 真理解 | Repeatable Read | 判 P6 |
| L4 | RR 防幻读吗 | 架构判断 | InnoDB MVCC+间隙锁 | 判 P6+ |
| L5 | 为何调成 RC | 实战经验 | 降低间隙锁冲突 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| SQL:2011 至今 | InnoDB RR 用 Next-Key Lock 防幻读（超出标准） | MySQL 默认 RR；PostgreSQL/Oracle 默认 RC；生产可按需调 RC |

## 关键代码
```sql
-- 查看与设置隔离级别（MySQL 8） [实测]
SELECT @@transaction_isolation;
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

## ⚠️ 原文纠错
原文音译需还原：「**readcommcommitted**」→ 原文用以指**读未提交（Read Uncommitted）**，标准术语 **Read Uncommitted** 对应"读未提交"、Read Committed 对应"读已提交"，原文此处术语拼写与级别错位，已按语义纠正；「**repeabebleread**」→ **Repeatable Read（可重复读）**；「**串行化**」正确（Serializable）。概念正确：四级隔离顺序、MySQL 默认 RR、串行化效率最低。核对范围：第 52~59 段 隔离级别。

## 总结与追问预判
- 四级：RU→RC→RR→Serializable；MySQL 默认 RR；级别越高越安全越慢。
- 顺势会问：**并发异常（见 190 卡）**、**乐观/悲观锁（见 192 卡）**、**InnoDB 引擎（见 195 卡）**。
