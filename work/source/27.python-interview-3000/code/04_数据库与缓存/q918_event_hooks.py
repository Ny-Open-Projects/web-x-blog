"""before_flush 写审计表 + before_cursor_execute 统计 SQL 条数"""

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

class Audit(Base):
    __tablename__ = "audit"
    id: Mapped[int] = mapped_column(primary_key=True)
    detail: Mapped[str]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    @event.listens_for(Session, "before_flush")
    def audit(session, flush_context, instances):
        for obj in session.new:
            if isinstance(obj, User):
                session.add(Audit(detail=f"insert {obj.name}"))
        for obj in session.dirty:
            if isinstance(obj, User):
                session.add(Audit(detail=f"update {obj.name}"))

    with Session(engine) as s:
        s.add(User(name="alice"))
        s.commit()
        u = s.scalars(select(User)).one()
        u.name = "alice2"
        s.commit()
        print("审计记录:", s.scalars(select(Audit.detail)).all())
