"""同一 session 内混用 ORM 查询与 text() 原生 SQL"""

try:
    from sqlalchemy import create_engine, text, select
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
    score: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(name=f"u{i}", score=i) for i in range(5)])
        s.commit()

        # 原生: 排名这类窗口逻辑下放 SQL
        ranks = s.execute(text(
            "SELECT name, score, RANK() OVER (ORDER BY score DESC) AS rk "
            "FROM users")).all()
        print("原生窗口:", ranks)

        # ORM: 常规过滤回到实体世界
        top = s.scalars(select(User).where(User.score >= 3)).all()
        print("ORM 过滤:", [u.name for u in top])
        print("同一事务 同一连接, 两界共存")
