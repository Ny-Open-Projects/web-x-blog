"""before_flush 对比属性历史, 写字段级变更日志"""

try:
    from sqlalchemy import create_engine, event, select
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
    from sqlalchemy import inspect as sa_inspect
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    balance: Mapped[int]

class ChangeLog(Base):
    __tablename__ = "change_log"
    id: Mapped[int] = mapped_column(primary_key=True)
    entity: Mapped[str]
    field: Mapped[str]
    old: Mapped[str]
    new: Mapped[str]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    @event.listens_for(Session, "before_flush")
    def log_changes(session, ctx, instances):
        for obj in session.dirty:
            insp = sa_inspect(obj)
            for field in ("name", "balance"):
                hist = insp.attrs[field].history
                if hist.has_changes():
                    session.add(ChangeLog(
                        entity=type(obj).__name__, field=field,
                        old=str(hist.deleted[0]), new=str(hist.added[0])))

    with Session(engine) as s:
        s.add(Account(name="alice", balance=100))
        s.commit()
        acc = s.scalars(select(Account)).one()
        acc.balance = 80
        s.commit()
        print("变更日志:", s.execute(
            select(ChangeLog.field, ChangeLog.old, ChangeLog.new)).all())
