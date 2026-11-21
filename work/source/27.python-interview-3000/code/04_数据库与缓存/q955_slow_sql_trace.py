"""before_cursor_execute 记录调用栈: 慢 SQL 直接定位到函数"""
import time
import traceback

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

SLOW_MS = 0.5
slow_log = []

def business_code(session):
    return session.scalars(select(User).where(User.name == "alice")).all()

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    @event.listens_for(engine, "before_cursor_execute")
    def _t(conn, cursor, stmt, params, *a):
        conn.info["t0"] = time.perf_counter()

    @event.listens_for(engine, "after_cursor_execute")
    def _t2(conn, cursor, stmt, params, *a):
        cost = (time.perf_counter() - conn.info["t0"]) * 1000
        if cost >= SLOW_MS:
            frames = [f.name for f in traceback.extract_stack()
                      if "sqlalchemy" not in f.filename]
            slow_log.append((stmt[:40], round(cost, 2), frames[-2:]))

    with Session(engine) as s:
        s.add(User(name="alice")); s.commit()
        business_code(s)
        print("慢 SQL 日志:", slow_log or "本次无超过阈值的 SQL")
        print("生产环境把 frames 换成完整调用栈即可定位到代码行")
