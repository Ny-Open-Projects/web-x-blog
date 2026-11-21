"""hybrid_property 同时服务对象读取与 SQL 过滤"""

try:
    from sqlalchemy import create_engine, select
    from sqlalchemy.ext.hybrid import hybrid_property
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first: Mapped[str]
    last: Mapped[str]

    @hybrid_property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.expression
    def full_name(cls):
        return cls.first + " " + cls.last

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(first="Ada", last="Lovelace"),
                   User(first="Alan", last="Turing")])
        s.commit()
        print("对象层:", s.scalars(select(User)).first().full_name)
        print("SQL 层:", s.scalars(select(User)
              .where(User.full_name == "Alan Turing")).one().first)
