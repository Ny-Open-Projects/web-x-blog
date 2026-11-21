"""对比逐对象 add 与 insert executemany 的耗时与 SQL 条数"""
import time

try:
    from sqlalchemy import create_engine, event, insert
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Row(Base):
    __tablename__ = "rows"
    id: Mapped[int] = mapped_column(primary_key=True)
    v: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    n_sql = {"c": 0}
    event.listen(engine, "before_cursor_execute",
                 lambda *a: n_sql.__setitem__("c", n_sql["c"] + 1))
    Base.metadata.create_all(engine)
    data = [{"v": i} for i in range(20000)]

    t0 = time.perf_counter()
    with Session(engine) as s:
        s.add_all([Row(**d) for d in data])
        s.commit()
    print(f"ORM add_all: {(time.perf_counter() - t0) * 1000:.0f} ms, SQL {n_sql['c']} 条")

    n_sql["c"] = 0
    t1 = time.perf_counter()
    with Session(engine) as s:
        s.execute(insert(Row), data)
        s.commit()
    print(f"executemany: {(time.perf_counter() - t1) * 1000:.0f} ms, SQL {n_sql['c']} 条")
