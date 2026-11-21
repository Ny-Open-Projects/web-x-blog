"""对比 expire_on_commit 两种设置与 expunge 的对象出层行为"""

try:
    from sqlalchemy import create_engine
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

def demo(expire_on_commit, use_expunge):
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine, expire_on_commit=expire_on_commit) as s:
        u = User(name="a")
        s.add(u)
        s.commit()
        if use_expunge:
            s.expunge(u)
        try:
            return f"expire={expire_on_commit} expunge={use_expunge} -> {u.name}"
        except Exception as e:
            return f"expire={expire_on_commit} expunge={use_expunge} -> {type(e).__name__}"

if __name__ == "__main__":
    print(demo(True, False))
    print(demo(False, False))
    print(demo(True, True))
