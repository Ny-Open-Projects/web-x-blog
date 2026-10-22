# 189. 数据库事务与 ACID 特性

> 分类：数据库 | 难度：L2 | 题型：概念题 | 频率：高 | 关键词：**事务** / **ACID** / **原子性** / **一致性** / **隔离性** / **持久性**
> 原文锚点：第 8~38 段「事务（transaction）是一组 SQL 语句的集合，要么全成功要么全失败（回滚）；ACID 四特性：原子性/一致性/隔离性/持久性」

## 一句话总述
**事务**是数据库**并发控制的基本单位**，本质是一组 SQL 的"**要么全成功、要么全失败（回滚）**"；用 **ACID** 描述其保证——**A 原子性（全或无）、C 一致性（前后数据完整）、I 隔离性（并发互不干扰）、D 持久性（提交后落盘不丢）**。

## 面试官视角
- **考察意图**：是否真正理解 ACID 每个字母的含义，而不只是背缩写。
- **P5** 能背出 ACID 四个词 / **P6** 能讲清每个特性的含义 + 举转账例子（A 扣款与 B 入账要么都成要么都滚） / **P7** 能区分 C 一致性（应用层约束 + 数据库约束共同保证，不是单指"没报错"）与 I 隔离性，并说清 D 靠 WAL/redo 落盘。
- **红旗**：把一致性说成"事务执行完数据就一致"（一致性是"不破坏既定的业务约束"，如转账总额不变）；或只背缩写说不出 C/I 含义。
- **惊艳点**：原子性靠 **undo log** 回滚、持久性靠 **redo log/WAL 落盘**、隔离性靠**锁 + MVCC**——三者由不同机制分别保证，不是"一个开关" `[经验]`。

## 主问答
**Q（面试官原话）：** 什么是事务？ACID 分别是什么？

**A · 标准答案骨架：**
1. **先给结论**：事务是一组 SQL 的原子集合，**要么全部提交、要么全部回滚**；ACID = 原子性 / 一致性 / 隔离性 / 持久性。
2. **再给机制**：**A** 靠 undo log 回滚保证"全或无"；**C** 指事务前后不破坏业务约束（如转账 A 减 B 增总额守恒）；**I** 让并发事务互不干扰（靠锁 + MVCC）；**D** 指提交后修改永久保存（redo log 落盘）。
3. **最后给边界**：ACID 是**数据库引擎承诺的保证**，但 C 也依赖应用层写对 SQL（约束/外键/触发器）；隔离性到底多强由**隔离级别**决定（见 191 卡）。

**加分层**：经典例子是**银行转账**——A 扣 50、B 加 50 必须在一个事务里，任一失败整体回滚，绝不能"凭空少 50" `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 事务是什么 | 基本认知 | 一组 SQL 原子执行 | 换题 → 不及格 |
| L2 | ACID 含义 | 是否背的 | 四特性各一句 | 判 P5 |
| L3 | 一致性指什么 | 真理解 | 不破坏业务约束 | 判 P6 |
| L4 | 各特性靠什么实现 | 架构判断 | undo/redo/锁+MVCC | 判 P6+ |
| L5 | 你踩过事务坑 | 实战经验 | 长事务锁等待/死锁 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| SQL 标准（ISO/IEC 9075）至今 | 无 | ACID 定义稳定；实现细节（undo/redo/MVCC）因引擎而异，InnoDB 为标准范式 |

## 关键代码
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 事务：commit 失败即整体回滚 [实测]
engine = create_engine("mysql+pymysql://user:pwd@localhost/db")
Session = sessionmaker(bind=engine)
s = Session()
try:
    s.execute("UPDATE account SET bal=bal-50 WHERE name='A'")
    s.execute("UPDATE account SET bal=bal+50 WHERE name='B'")
    s.commit()                      # 全成功才提交
except Exception:
    s.rollback()                    # 任一失败整体回滚
```

## ⚠️ 原文纠错
原文音译需还原：「**transition**」→ **transaction（事务）**；「**atomistic**」→ **Atomic（原子性）**；「**这see / consistency**」→ **Consistency（一致性）**；「**isolation**」正确（隔离性）；「**durability**」正确（持久性）；「**circle / 蚂蚁circle / minecircle / mysserver**」→ **SQL / MySQL**；「**circuarmmy**」→ **SQLAlchemy（ORM 框架）**；「**关型数据库**」→ **关系型数据库**；「**REDS / REDX**」→ **Redis**；「**芒goDB**」→ **MongoDB**；「**hbase**」→ **HBase**。概念正确：事务=一组SQL原子集合、ACID 四特性含义、转账例子。核对范围：第 8~38 段 事务与 ACID。

## 总结与追问预判
- 事务=一组SQL全成功或全回滚；ACID=A原子/C一致/I隔离/D持久，由 undo/redo/锁+MVCC 分别保证。
- 顺势会问：**并发异常与隔离级别（见 190/491 卡）**、**乐观/悲观锁（见 192 卡）**。
