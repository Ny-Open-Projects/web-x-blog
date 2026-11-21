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
