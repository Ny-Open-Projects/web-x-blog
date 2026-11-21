"""ORM 双分页: limit/offset 与 keyset 游标"""
import base64
import json

try:
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Feed(Base):
    __tablename__ = "feed"
    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[float]

def offset_page(s, page, size=3):
    return s.scalars(select(Feed).order_by(Feed.score.desc(), Feed.id)
                     .limit(size).offset(page * size)).all()

def keyset_page(s, cursor=None, size=3):
    stmt = select(Feed).order_by(Feed.score.desc(), Feed.id).limit(size)
    if cursor:
        c = json.loads(base64.b64decode(cursor))
        stmt = stmt.where((Feed.score < c["s"]) |
                          ((Feed.score == c["s"]) & (Feed.id > c["i"])))
    rows = s.scalars(stmt).all()
    next_cursor = None
    if len(rows) == size:
        last = rows[-1]
        next_cursor = base64.b64encode(json.dumps(
            {"s": last.score, "i": last.id}).encode()).decode()
    return rows, next_cursor

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Feed(score=i % 10) for i in range(20)])
        s.commit()
        print("offset 第2页:", [f.id for f in offset_page(s, 1)])
        rows, cur = keyset_page(s)
        print("keyset 第1页:", [f.id for f in rows], "cursor:", bool(cur))
        rows2, _ = keyset_page(s, cur)
        print("keyset 第2页:", [f.id for f in rows2])
