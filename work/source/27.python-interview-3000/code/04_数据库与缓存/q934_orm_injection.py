"""text() 的安全绑定与危险拼接对比"""

try:
    from sqlalchemy import create_engine, text
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

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add(User(name="admin")); s.commit()

        evil = "' OR '1'='1"

        # 危险: f-string 进 text()
        try:
            rows = s.execute(text(f"SELECT * FROM users WHERE name = '{evil}'")).all()
            print("危险拼接返回行数:", len(rows), "<- 被注入")
        except Exception as e:
            print("危险拼接异常:", type(e).__name__)

        # 安全: bindparams 绑定
        rows = s.execute(
            text("SELECT * FROM users WHERE name = :n").bindparams(n=evil)).all()
        print("参数化返回行数:", len(rows))

        # 动态排序: 白名单
        allowed = {"name": User.name, "id": User.id}
        key = allowed.get("name", User.id)
        print("白名单排序:", s.execute(
            text("SELECT name FROM users ORDER BY " +
                 ("name" if key is User.name else "id"))).all())
