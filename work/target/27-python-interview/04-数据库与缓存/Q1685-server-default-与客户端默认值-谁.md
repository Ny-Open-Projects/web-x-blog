---
title: [Q1685] server_default 与客户端默认值: 谁来填空
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1685 · server_default 与客户端默认值: 谁来填空

> 难度:★★★☆ | 标签:ORM, 建模

**问**:default 和 server_default 都写了默认值,它们分别在什么时候生效?

**答**:客户端 default 由 ORM 在 INSERT 时补上,值会立刻出现在 Python 对象上,flush 后不用回读;server_default 是数据库列的 DEFAULT 子句,INSERT 里该列缺席时由库补齐,但 ORM 对象上不会有值,要看它必须 refresh 或重查。关键风险是批量写入:bulk insert、Core insert、以及其他语言写入都会绕过 ORM 的客户端 default,重要默认值必须在库端有 server_default 兜底,两者职责是"客户端默认值方便业务立即使用,服务端默认值保证数据完整性"。

```python
# file: code/04_数据库与缓存/q1685_server_default.py
"""server_default 与客户端默认值: 谁来填空 与 可见的时机"""
import sqlite3

try:
    from sqlalchemy import create_engine, insert, select, text
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
    HAS_SQLA = True
except ImportError:
    HAS_SQLA = False

def demo_pure():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, name TEXT, bonus REAL DEFAULT 7)")
    conn.commit()

    class Order:
        def __init__(self, name, bonus=None):
            self.name = name
            self.bonus = 50.0 if bonus is None else bonus    # Python 客户端默认值

    o = Order("a")
    conn.execute("INSERT INTO orders(name, bonus) VALUES(?,?)", (o.name, o.bonus))
    conn.commit()
    print("客户端默认值随 INSERT 一起写入:",
          conn.execute("SELECT name, bonus FROM orders WHERE id=1").fetchone())

    conn.execute("INSERT INTO orders(name) VALUES('b')")     # 列缺席 -> 交给数据库 DEFAULT
    conn.commit()
    print("server_default 由库补齐:",
          conn.execute("SELECT name, bonus FROM orders WHERE id=2").fetchone())
    print("要点: 批量与 Core 写入会绕过 ORM 的 Python default, 重要默认值必须配 server_default 兜底;")
    print("      server_default 写入后对象上没有该值, 需要 refresh 才能看到")

if HAS_SQLA:
    class Base(DeclarativeBase):
        pass

    class Order(Base):
        __tablename__ = "orders"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]
        bonus: Mapped[float] = mapped_column(default=50.0, server_default=text("7"))

    def demo_sqla():
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        with Session(engine) as s:
            o = Order(name="a")                       # bonus 未赋值 -> ORM default 生效
            s.add(o)
            s.flush()
            print("ORM flush 后对象拿到 Python default:", o.bonus)
            s.execute(insert(Order).values(name="b"))  # 绕过 ORM 层
            s.commit()
            row = s.scalars(select(Order).order_by(Order.id.desc())).first()
            print("Core insert 走数据库 server_default:", row.bonus)

if __name__ == "__main__":
    if HAS_SQLA:
        demo_sqla()
    else:
        print("sqlalchemy 未安装, 用 sqlite3 等价演示两种默认值")
        demo_pure()
```

**追问**:
- created_at 这种字段两边都配可以吗?——可以且推荐:default=datetime.utcnow 方便业务立刻读,server_default=now() 防绕过,注意两个值可能有毫秒差。
- server_default 支持 onupdate 吗?——SQLAlchemy 有 server_onupdate 但多数数据库要靠触发器实现真正的库端更新时间,MySQL 可用 ON UPDATE CURRENT_TIMESTAMP。

---
