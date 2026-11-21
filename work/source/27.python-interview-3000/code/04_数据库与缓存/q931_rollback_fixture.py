"""事务回滚夹具: 外层事务 + SAVEPOINT, 内部 commit 不落库"""

try:
    from sqlalchemy import create_engine, select, text
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

def biz_create(session: Session, name: str) -> Item:
    """业务代码: 像生产一样正常 commit"""
    item = Item(name=name)
    session.add(item)
    session.commit()
    return item

def db_case(conn):
    """模拟夹具: 外层事务内嵌 SAVEPOINT, commit 后还原到 savepoint"""
    outer = conn.begin()
    s = Session(bind=conn, join_transaction_mode="create_savepoint")
    try:
        biz_create(s, "from-test")
        n = s.scalar(select(__import__("sqlalchemy").func.count()).select_from(Item))
        return f"用例内可见 {n} 行"
    finally:
        s.close()
        outer.rollback()

if __name__ == "__main__":
    with engine.connect() as conn:
        print(db_case(conn))
    with engine.connect() as conn:
        n = conn.execute(text("SELECT count(*) FROM items")).scalar()
        print("夹具结束后数据库:", n, "行  <- 回滚彻底干净")
