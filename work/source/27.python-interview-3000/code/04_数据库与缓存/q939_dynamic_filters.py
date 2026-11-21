"""字典驱动的动态过滤构造器: 白名单 + 统一组装"""

try:
    from sqlalchemy import create_engine, and_, select
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
    age: Mapped[int]
    active: Mapped[bool] = mapped_column(default=True)

FILTERS = {
    "name": lambda v: User.name.like(f"%{v}%"),
    "age_gte": lambda v: User.age >= v,
    "age_lte": lambda v: User.age <= v,
    "active": lambda v: User.active == bool(v),
}

def build_query(params: dict):
    conds = [FILTERS[k](v) for k, v in params.items() if k in FILTERS]
    return select(User).where(and_(*conds)) if conds else select(User)

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(name="alice", age=30), User(name="bob", age=20),
                   User(name="alan", age=40)])
        s.commit()
        for p in ({"name": "a", "age_gte": 25}, {"active": True}, {}):
            print(p, "->", [u.name for u in s.scalars(build_query(p))])
        print("未知参数被忽略:", [u.name for u in
              s.scalars(build_query({"evil": "1' OR '1'='1"}))])
