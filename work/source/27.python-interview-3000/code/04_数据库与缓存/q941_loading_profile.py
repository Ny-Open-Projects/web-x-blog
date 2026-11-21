"""画像三种加载策略: SQL 条数与返回行数"""

try:
    from sqlalchemy import create_engine, event, ForeignKey, select
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, mapped_column,
                                relationship, joinedload, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Team(Base):
    __tablename__ = "teams"
    id: Mapped[int] = mapped_column(primary_key=True)
    members: Mapped[list["Member"]] = relationship(back_populates="team")

class Member(Base):
    __tablename__ = "members"
    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team: Mapped[Team] = relationship(back_populates="members")

def profile(engine, label, options):
    stats = {"sql": 0, "rows": 0}
    def _sql(*a):
        stats["sql"] += 1
    h = event.listen(engine, "before_cursor_execute", _sql)
    with Session(engine) as s:
        q = select(Team).options(options) if options else select(Team)
        teams = s.execute(q).unique().scalars().all()
        n = sum(len(t.members) for t in teams)
        event.remove(engine, "before_cursor_execute", _sql)
        print(f"{label}: SQL {stats['sql']} 条, 团队 {len(teams)}, 成员 {n}")

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Team(members=[Member() for _ in range(10)])
                   for _ in range(100)])
        s.commit()
    profile(engine, "lazy       ", None)
    profile(engine, "joinedload ", joinedload(Team.members))
    profile(engine, "selectin   ", selectinload(Team.members))
