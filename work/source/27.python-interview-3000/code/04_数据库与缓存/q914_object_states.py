"""用 inspect() 追踪一个对象从 transient 到 detached 的状态流转"""

try:
    from sqlalchemy import create_engine, inspect
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

def state(obj):
    """inspect() 的状态标志位辅助"""
    i = inspect(obj)
    if i.transient: return "transient"
    if i.pending: return "pending"
    if i.detached: return "detached"
    return "persistent"

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    u = User(name="a")
    print("new 后:", state(u))

    with Session(engine) as s:
        s.add(u)
        print("add 后:", state(u))
        s.flush()
        print("flush 后:", state(u), "id=", u.id)
    print("close 后:", state(u))
