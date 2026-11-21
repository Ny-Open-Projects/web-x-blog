---
title: [Q6645] autocommit 与隐式事务事故复盘
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6645 · autocommit 与隐式事务事故复盘

难度：P6 | 标签：事务、autocommit、隔离级别、事故复盘

**问**："autocommit 开着就不用管事务了"这句话错在哪？一个连接从 autocommit 模式发出显式 BEGIN 后忘了 COMMIT，会发生什么？事务模式的"隐式行为"怎么变成线上事故？

**答**：
- **结论**：autocommit 只保证"单条语句自动提交"，一旦显式 BEGIN（或 ORM 开启事务），控制权回到应用，忘记 COMMIT 的后果三连：① 未提交数据在连接关闭/回滚时丢失；② 事务持有的锁一直不释放，锁队列堆积拖垮其他会话；③ 长事务阻碍 MVCC 版本回收（PG 的 vacuum、MySQL 的 undo 清理）。两种模式的边界必须在团队规范里钉死：要么全程 autocommit + 显式事务块包裹多语句，要么默认开事务、明确 commit 点，禁止混用。
- **取舍**：autocommit 模式的好处是不会忘 COMMIT、连接归还时天然干净；代价是多语句原子性要自己包 BEGIN。ORM（SQLAlchemy 2.0）默认"begin once"，commit 语义清晰，比裸驱动混用安全——事故多发生在"脚本 + 直连驱动"的场景。
- **实战**：事故复盘：跑批脚本用 autocommit 连接手工 BEGIN 后异常退出，锁挂了一夜，第二天业务全表超时。防线：① 脚本统一走 ORM/框架的事务上下文（with 块自动 commit/rollback）；② DB 侧设 `idle_in_transaction_session_timeout`（PG）兜底杀掉挂起事务；③ 巡检长事务告警（事务时长 P99）。

```python
import sqlite3, os, tempfile

db = os.path.join(tempfile.mkdtemp(), "t.db")
a = sqlite3.connect(db)                              # 默认隐式事务模式
a.execute("CREATE TABLE t (v INT)")
a.execute("INSERT INTO t VALUES (1)")                # 开启隐式事务，未 commit
b = sqlite3.connect(db, isolation_level=None)        # autocommit 连接
print("autocommit 连接看到的行数:", b.execute("SELECT COUNT(*) FROM t").fetchone()[0])
a.commit()
print("commit 后:", b.execute("SELECT COUNT(*) FROM t").fetchone()[0])

# 事故形态：autocommit 连接执行显式 BEGIN 后忘了 COMMIT 就还池
c = sqlite3.connect(db, isolation_level=None)
c.execute("BEGIN")
c.execute("INSERT INTO t VALUES (2)")
c.close()                                            # 连接关闭 -> 未提交事务回滚
print("未 COMMIT 即还池, 行数:", b.execute("SELECT COUNT(*) FROM t").fetchone()[0])
print("要点：autocommit 连接里显式 BEGIN 后必须显式 COMMIT；否则锁在手、数据丢")
```

**追问链**：
1. 追问一层：为什么"锁挂一夜"比"数据丢失"更严重？——数据丢失影响单笔业务，锁不释放会阻塞所有碰该行的会话并堆积连接池，爆炸半径是实例级。
2. 追问二层：idle_in_transaction_session_timeout 设多长合适？（略大于批处理任务的事务最大时长 P99；太短会杀掉合法长事务，太长失去兜底意义）

**背诵要点**：
1. autocommit 只管单语句；显式 BEGIN 后必须显式 COMMIT。
2. 忘 COMMIT 三连：数据丢、锁不释放、MVCC 版本堆积。
3. 防线：框架事务上下文 + idle 事务超时兜底 + 长事务告警。

**复盘追问**：
1. 事故后所有连接里都有一堆 idle in transaction，代码层怎么定位泄漏点？（连接归还路径审计 + 事务开始日志关联）
2. 为什么说"连接池掩盖了事务泄漏"？（连接不还池事务就一直挂着，池化让泄漏更隐蔽）
