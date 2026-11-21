---
title: [Q1687] SAVEPOINT 嵌套事务: 局部回滚的用法
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1687 · SAVEPOINT 嵌套事务: 局部回滚的用法

> 难度:★★★☆ | 标签:事务, SAVEPOINT

**问**:批量导入一万条,第 3000 条非法,想让前 2999 条保留怎么处理?

**答**:用 SAVEPOINT 做嵌套事务:外层事务里 SAVEPOINT sp 建保存点,一段操作失败时 ROLLBACK TO sp 只回滚这段,RELEASE 后外层继续,最后整体提交;SQLAlchemy 对应 session.begin_nested()。它解决的是"失败隔离粒度"问题:不做嵌套时,一批里一条坏数据就要全批重来或全部回滚;有了保存点,按行或按片隔离,坏片跳过、好片落库。注意两点:保存点不是免费的,每层都有命名与日志成本,别嵌太深;SQLite、MySQL、PG 都支持,但 PG 里保存点内的错误会把事务标记为 aborted,必须 ROLLBACK TO 后才能继续。

```python
# file: code/04_数据库与缓存/q1687_savepoint.py
"""SAVEPOINT 嵌套事务: 局部回滚不影响外层提交"""
import sqlite3

try:
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
    HAS_SQLA = True
except ImportError:
    HAS_SQLA = False

def demo_pure():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
    conn.execute("INSERT INTO t VALUES(1, 'base')")
    conn.commit()

    conn.execute("SAVEPOINT sp1")                 # 外层事务
    conn.execute("UPDATE t SET v='outer' WHERE id=1")
    conn.execute("SAVEPOINT sp2")                 # 内层保存点
    conn.execute("UPDATE t SET v='inner-bad' WHERE id=1")
    conn.execute("ROLLBACK TO sp2")               # 只回滚内层
    conn.execute("RELEASE sp2")
    print("内层回滚后:", conn.execute("SELECT v FROM t WHERE id=1").fetchone()[0])
    conn.execute("RELEASE sp1")
    conn.commit()
    print("外层提交后:", conn.execute("SELECT v FROM t WHERE id=1").fetchone()[0])
    print("要点: 批量导入用 SAVEPOINT 按行/按片隔离失败, 坏片回滚好片继续, 整体不必推倒重来")

if HAS_SQLA:
    class Base(DeclarativeBase):
        pass

    class User(Base):
        __tablename__ = "users"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]

    def demo_sqla():
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        with Session(engine) as s:
            s.add(User(id=1, name="base"))
            s.commit()
            s.add(User(id=2, name="outer"))       # 外层事务的一部分
            nested = s.begin_nested()             # SAVEPOINT
            s.add(User(id=3, name="inner"))
            s.flush()
            nested.rollback()                     # 只回滚保存点内的对象
            s.commit()
            ids = sorted(s.scalars(select(User.id)).all())
            print("提交后存在的 id:", ids, "-> 保存点内的 id=3 被丢弃")

if __name__ == "__main__":
    if HAS_SQLA:
        demo_sqla()
    else:
        print("sqlalchemy 未安装, 用 sqlite3 原生 SAVEPOINT 演示")
        demo_pure()
```

**追问**:
- begin_nested 和 begin 的区别?——begin 开顶层事务,begın_nested 在当前事务里开保存点,必须有活事务才能嵌套。
- 保存点对死锁检测有影响吗?——死锁仍在事务层回滚整个事务,保存点不能把死锁降级成局部失败,错误重试仍要走整个外层。

---
