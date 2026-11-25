---
title: "[Q6156] 测试数据库 fixture 的 CI 成本账"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6156 · 测试数据库 fixture 的 CI 成本账

难度：P6 ｜ 标签：测试、fixture、CI、事务回滚、成本工程

**问**：测试套件里"每个测试建库建表灌数据"为什么让 CI 时间随测试数线性爆炸？事务回滚（每测试包一个事务后回滚）、内存库（SQLite in-memory）、快照恢复（模板库 clone）三种策略的成本与保真度怎么权衡？迁移文件在测试库初始化里占了 2 分钟怎么治？

**答**：
结论：fixture 初始化成本 = `建连接 + DDL（迁移）+ 数据灌入` × 测试数，其中 DDL 最贵（真实 PG 每张表带系统目录写入）。三种策略的成本阶梯：① **事务回滚**：迁移只跑一次（会话级），每个测试包 BEGIN…ROLLBACK，建表零重复——最快但"测试内代码调 COMMIT/TRUNCATE/独立连接"会破功，且测不出真实提交行为；② **SQLite in-memory**：零 IO 微秒级，但方言与 PG 不一致（JSON 操作符、并发行为、迁移兼容性靠 alembic/sqlalchemy 适配层），保真度低，适合单元级不适合集成级；③ **快照/模板库**（PG `CREATE DATABASE TEMPLATE` 或每 worker clone）：迁移一次成模板，N 个并行 worker 各 clone 一份，恢复秒级且保真度高——CI 规模化后的主流。治理迁移占 2 分钟：测试库用"迁移基线快照"（迁移只在基线变化时重跑），或合并迁移（squash）。

取舍：速度与保真度必须分层——单元/服务层测试用事务回滚+内存库追求秒级反馈；端到端/迁移验证用真实 PG+快照；**禁止**把"生产等价"当作全量要求，那等于把集成测试数量当成 CI 成本上限。并行度要配套：xdist 多 worker × 各自模板 clone，同时盯连接数预算（worker × pool）。

实战：CI 成本账三张表——总时长（对 MR 反馈延迟）、总机器分钟（对账单）、失败重跑率（对稳定性）；用 `--durations` 找 fixture 热点，把"每测试重建"改为"模块级 session fixture + 事务回滚"通常直接砍掉 60-80%。

```python
import sqlite3, time, contextlib

# 1) 三种策略的成本实测（SQLite 演示，PG 同构思路）
def cost_of_recreate(n_tests=50):
    start = time.perf_counter()
    for _ in range(n_tests):
        conn = sqlite3.connect(":memory:")
        conn.executescript("""
            CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
            CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amount INT);
        """)
        conn.close()
    return time.perf_counter() - start

def cost_of_rollback(n_tests=50):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    start = time.perf_counter()
    for _ in range(n_tests):
        conn.execute("BEGIN")
        conn.execute("INSERT INTO users (name) VALUES ('a')")
        conn.execute("ROLLBACK")              # 回滚代替重建
    return time.perf_counter() - start

t1, t2 = cost_of_recreate(), cost_of_rollback()
print("recreate-per-test : %.1fms" % (t1 * 1000))
print("begin/rollback    : %.1fms  (%.0fx faster)" % (t2 * 1000, t1 / max(t2, 1e-9)))

# 2) 事务回滚 fixture 的 pytest 风格骨架（含"测试内 COMMIT 破功"演示）
@contextlib.contextmanager
def rollback_fixture(migrations):
    conn = sqlite3.connect(":memory:")
    for ddl in migrations:
        conn.execute(ddl)
    conn.commit()                              # 基线
    try:
        conn.execute("BEGIN")
        yield conn
    finally:
        conn.rollback()                        # 测试产物全部丢弃
        conn.close()

MIGRATIONS = ["CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)"]
with rollback_fixture(MIGRATIONS) as conn:
    conn.execute("INSERT INTO t (v) VALUES ('dirty')")
    print("inside test sees dirty:", conn.execute("SELECT count(*) FROM t").fetchone()[0])
with rollback_fixture(MIGRATIONS) as conn:     # 新测试拿到干净库
    print("next test is clean    :", conn.execute("SELECT count(*) FROM t").fetchone()[0])

# 3) 快照思路演示：模板库 -> clone（PG 用 CREATE DATABASE ... TEMPLATE；SQLite 用 backup API）
src = sqlite3.connect(":memory:")
src.execute("CREATE TABLE big (id INTEGER PRIMARY KEY)"); src.commit()
import os, tempfile
snap = os.path.join(tempfile.mkdtemp(), "snap.db")
src.backup(sqlite3.connect(snap))              # 模板快照
for worker in range(4):                        # N worker 各 clone 一份
    w = sqlite3.connect(snap)
    assert w.execute("SELECT count(*) FROM sqlite_master").fetchone()[0] > 0
    w.close()
print("snapshot cloned for 4 workers ok")
```

**追问一**：事务回滚策略为什么测不出"提交后的唯一约束冲突在并发下"这类问题？——回滚把测试限制在单连接单事务视图，看不到锁等待、可见性（READ COMMITTED 下的幻读）与提交路径的行为；这类断言必须落在真实提交的集成层，两层各测各的边界。

**追问二**：并行 worker 共享一个真实 PG 时的隔离怎么做、风险是什么？——schema-per-worker（每 worker 一个 schema 或 database）+ 连接串注入；风险是全局状态（序列、扩展对象、跨 schema 触发器）互相污染，以及连接数 = worker × pool 超出 PG max_connections——这也是"并行度要进容量账"的原因。

## 背诵要点
- fixture 成本 = 迁移 DDL × 测试数是 CI 爆炸主因；治理主线：迁移跑一次成基线，测试用事务回滚/快照 clone。
- 三策略权衡：事务回滚最快但测不到提交行为，SQLite 快但方言失真，PG 模板 clone 秒级且保真。
- 并行要配套 schema-per-worker 与连接数预算；CI 账看总时长/机器分钟/重跑率三指标。

## 复盘追问
- CI 从 8 分钟涨到 40 分钟，--durations 显示 70% 在 fixture，如何分层改造并验证不降低覆盖？（热点迁移、session+回滚、快照，讨论保真度分层标准）
- 为什么"每个测试都用真实 PG 并全量迁移"是反模式？从事故成本与反馈延迟角度论述。（线性爆炸 + 迁移耦合，讨论测试金字塔预算）
