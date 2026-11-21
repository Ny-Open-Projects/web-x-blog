---
title: [Q916] flush 与 autoflush: 何时真正发 SQL
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q916 · flush 与 autoflush: 何时真正发 SQL

> 难度:★★★★ | 标签:SQLAlchemy, Session

**问**:flush 和 commit 的关系?autoflush 会造成什么意外查询?

**答**:commit = flush(把 pending 变更写成 INSERT/UPDATE/DELETE)+ 提交事务;flush 只发 SQL 不提交,失败可回滚重试。autoflush=True(默认)时,任何查询执行前 session 先自动 flush 未决变更,保证"查到自己的修改"——副作用是查询可能意外触发写入,常见坑:查询抛 IntegrityError 而你以为是查询问题,其实是 autoflush 把脏对象刷出去了。批量导入可关 autoflush 降开销,但要自己管理 flush 节奏;flush 顺序按 mapper 依赖拓扑(先父后子),同一表内按主键排序,理解它才能解释外键顺序错误。

```python
# file: code/04_数据库与缓存/q916_autoflush.py
"""演示 autoflush: 查询前自动 flush 脏对象, 观察发出与未发出的 SQL"""

try:
    from sqlalchemy import create_engine, event, select
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    sqls = []
    @event.listens_for(engine, "before_cursor_execute")
    def _log(conn, cursor, stmt, *a):
        sqls.append(stmt[:40])
    Base.metadata.create_all(engine)

    with Session(engine) as s:                     # autoflush 默认开
        s.add(User(name="a"))
        s.execute(select(User))                    # 查询前自动 flush
        print("autoflush 开, SQL 序列:", sqls)
        print("行数:", s.scalar(select(__import__('sqlalchemy').func.count())
                                 .select_from(User)))

    sqls.clear()
    with Session(engine, autoflush=False) as s:
        s.add(User(name="b"))
        s.execute(select(User))
        print("autoflush 关, 查询不触发写入, 此刻行数:",
              s.scalar(select(__import__('sqlalchemy').func.count()).select_from(User)))
        s.flush()
        print("手动 flush 后行数:",
              s.scalar(select(__import__('sqlalchemy').func.count()).select_from(User)))
```

**追问**:
- 为什么查询前要自动 flush?——保证 session 内"读己之写":你刚改的对象立刻可见,避免同一事务内新旧混用。
- flush 顺序错了会怎样?——先插入子表会因外键为空/违反约束报错,SQLAlchemy 按 mapper 依赖自动排序,自引用表需显式 order_by 或分两次 flush。

---
