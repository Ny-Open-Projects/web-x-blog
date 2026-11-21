"""exists 与 count 的正确写法 vs 反模式"""

try:
    from sqlalchemy import create_engine, select, func, exists
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Order(user_id=1) for _ in range(100)])
        s.commit()

        # 正确: exists 谓词, 找到一行即短路
        has = s.scalar(select(exists().where(Order.user_id == 1)))
        print("EXISTS 判存在:", has)

        # 正确: 数据库端 count
        n = s.scalar(select(func.count()).select_from(Order)
                     .where(Order.user_id == 1))
        print("COUNT:", n)

        # 反模式对照(仅演示, 禁止上线):
        rows = s.scalars(select(Order).where(Order.user_id == 1)).all()
        print("反模式 len(rows):", len(rows), "<- 拉回 100 行只为判断 0/1")
