"""SQLAlchemy 2.x Core 最小示例: sqlite3 可直接运行"""

try:
    from sqlalchemy import (
        create_engine, MetaData, Table, Column, Integer, String, insert, select,
    )
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(32), nullable=False),
    Column("age", Integer),
)

if __name__ == "__main__":
    metadata.create_all(engine)          # 建表
    with engine.begin() as conn:         # begin 自动提交事务
        conn.execute(insert(users), [
            {"name": "alice", "age": 30},
            {"name": "bob", "age": 25},
        ])

    stmt = select(users.c.name).where(users.c.age >= 26).order_by(users.c.name)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(dict(row._mapping))
