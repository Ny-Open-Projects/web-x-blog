---
title: "[Q7256] 测试内存库第二个连接查不到表：SQLite :memory: 的连接生命周期"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7256 · 测试内存库第二个连接查不到表：SQLite :memory: 的连接生命周期

难度：P6 ｜ 标签：SQLite、:memory:、测试隔离、连接管理、fixture 设计

基线：Python 3.12 + sqlite3；实测内存库"每连接独立"的语义与三种修复路径，全标准库实跑。

**问**：测试里用 SQLite `:memory:` 建库跑用例，快是快，但夹具里建的表在业务代码自己 `connect(':memory:')` 时报 `no such table`。为什么两个连接连的"内存库"不是同一个？有没有办法让多个连接共享内存库？什么时候该用内存库、什么时候用文件库？

**答**：
- **结论**：`:memory:` 的语义是**每个连接打开一个全新的、私有的内存数据库**——连接关闭即销毁，两个连接各开各的，表当然互相看不见。这不是 bug 是设计：它保证测试天然隔离。修复三条路：① **单连接贯穿**：夹具创建一个连接，业务代码不接受自己的连接参数而复用同一个（最常见，配合事务回滚夹具 Q1092 天衣无缝）；② **共享内存库**：用 URI `file:testdb?mode=memory&cache=shared` 让多个连接共享同一内存库（注意池化行为：所有连接都关后库即消失，连接池要至少留一条活连接）；③ **临时文件库**：`tmp_path` 下的文件库，多连接天然共享，用完即删。内存库的价值是快（无磁盘 IO），文件库的价值是多连接与持久化调试。选型口诀：**单连接用 :memory:，多连接用共享内存或临时文件**。
- **取舍**：① 共享内存库 + 连接池的经典坑：连接池把"最后一条连接"归还后关掉，库随之消失，下一个用例又建空库——测试用池要么禁用要么保活；② 共享内存库的写锁与文件库一致（同一时刻一个写者），并行测试下会串行化，性能优势打折（Q7146）；③ 内存库调试性差：用例挂了库就没了，要现场就得用文件库留现场（与 Q7262 失败现场留存呼应）；④ schema 初始化成本：每个测试夹具建表，用"模块级建库 + 每用例事务回滚"摊平。
- **实战**：① 夹具分层：模块级 fixture 建库建 schema（慢，一次），用例级 fixture 开事务包住、用例结束回滚（Q1092）；② 共享内存 URI 的库名要唯一（按测试会话生成），防同进程内不同测试模块互相串库；③ CI 并行时每 worker 独立内存库名或文件路径，防共享缓存冲突（Q7246 的教训）；④ 内存库的 `PRAGMA foreign_keys`、时间函数等行为与真实库一致性要抽测——测试替身与生产库的方言差异是隐藏事故源（Q907 适用边界）。

```python
"""SQLite :memory: 连接生命周期实测：私有语义与三种修复路径。"""
import sqlite3
import tempfile
import os


def try_table(conn: sqlite3.Connection) -> bool:
    try:
        conn.execute("SELECT * FROM t_users").fetchall()
        return True
    except sqlite3.OperationalError:
        return False


if __name__ == "__main__":
    # 场景1: 两个独立 :memory: 连接 -> 互相看不见 (默认语义)
    c1 = sqlite3.connect(":memory:")
    c1.execute("CREATE TABLE t_users (id INTEGER)")
    c1.commit()
    c2 = sqlite3.connect(":memory:")
    print(f"场景1 独立内存库: 连接1建表, 连接2可见? {try_table(c2)}  <- 每连接私有库")
    c1.close()
    c2.close()

    # 场景2: 共享内存库 (URI + shared cache) -> 多连接同库
    uri = "file:unittest_shared_2026?mode=memory&cache=shared"
    s1 = sqlite3.connect(uri, uri=True)
    s1.execute("CREATE TABLE t_users (id INTEGER)")
    s1.execute("INSERT INTO t_users VALUES (1)")
    s1.commit()
    s2 = sqlite3.connect(uri, uri=True)
    n = s2.execute("SELECT COUNT(*) FROM t_users").fetchone()[0]
    print(f"场景2 共享内存库: 连接2可见? {try_table(s2)} (行数 {n})")
    # 坑: 所有连接都关后库消失
    s1.close()
    s2.close()
    s3 = sqlite3.connect(uri, uri=True)
    print(f"  全部连接关闭后新连接: 表还在? {try_table(s3)}  <- 库随最后一条连接销毁")
    s3.close()

    # 场景3: 临时文件库 -> 多连接 + 可留现场
    with tempfile.TemporaryDirectory() as d:
        db_path = os.path.join(d, "test.db")
        f1 = sqlite3.connect(db_path)
        f1.execute("CREATE TABLE t_users (id INTEGER)")
        f1.execute("INSERT INTO t_users VALUES (7)")
        f1.commit()
        f2 = sqlite3.connect(db_path)
        n2 = f2.execute("SELECT COUNT(*) FROM t_users").fetchone()[0]
        print(f"场景3 临时文件库: 连接2可见? {try_table(f2)} (行数 {n2}), "
              f"现场可留: {os.path.exists(db_path)}")
        f1.close()
        f2.close()

    ok = True
    print("\n结论：:memory: 是每连接私有库; 单连接贯穿用 :memory:,")
    print("      多连接用共享内存 URI(保活一条)或临时文件库(可留现场)")
```

**追问一**：共享内存库和事务回滚夹具（Q1092）怎么配合？

→ 解析：完全兼容且互补：模块级 fixture 用共享内存 URI 建库建 schema（一次）；每个用例的 fixture 在该库上 `BEGIN`，用例内所有操作跑在事务里，用例结束 `ROLLBACK`——数据零残留，连"清理表"都不用。注意两点：一是被测代码自己开事务时会嵌套（SQLite 无真正的嵌套事务），要么被测代码接受"传入连接已开事务"的约定（外层 SAVEPOINT 包住，Q1687），要么被测代码只用传入连接不许自己 connect；二是共享缓存下的写锁：用例串行时无感，xdist 并行时每 worker 用**不同库名**的共享内存 URI，天然隔离（Q7257 的 worker 独立资源原则）。

**追问二**：什么时候该放弃内存库换文件库？

→ 解析：三个信号：① 需要"多连接且池化行为要被真实测试"（比如测连接泄漏、事务超时），内存库的"最后连接销毁"语义会让测试失真；② 调试需要现场——flaky 用例挂了要 dump 库文件分析，内存库转瞬即逝（Q7262 现场留存）；③ 用到 SQLite 的磁盘特性（WAL 行为、文件锁、页缓存），内存库根本不触发这些路径。反过来，纯逻辑验证（函数返回值、SQL 语句正确性）留在内存库，速度优势保留。本质是"测试要模拟生产路径的哪一段"：模拟到磁盘行为就用文件库（tmp_path），不模拟就用内存库——别为了统一用一种而失真。
