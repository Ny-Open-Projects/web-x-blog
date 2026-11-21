"""SQLAlchemy 2.0 select 全家桶: where/order/limit/聚合"""
try:
    from sqlalchemy import create_engine, select, func
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

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(name=n, age=a) for n, a in
                   [("a", 20), ("b", 30), ("c", 30)]])
        s.commit()

        print(s.scalars(select(User).where(User.age == 30)).all())
        print(s.scalar(select(func.count()).select_from(User)))
        print(s.scalars(select(User).order_by(User.age.desc(), User.id)
                        .limit(2)).all())
