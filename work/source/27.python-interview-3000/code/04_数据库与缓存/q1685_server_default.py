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
