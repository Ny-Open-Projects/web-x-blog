"""Unit of Work: 跨仓储操作一个事务, 失败整体回滚"""
import contextlib

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str]

class Stock(Base):
    __tablename__ = "stocks"
    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str]
    qty: Mapped[int]

class UoW:
    def __init__(self, engine):
        self.engine = engine
        self.session = None
    def __enter__(self):
        self.session = Session(self.engine)
        return self
    def __exit__(self, exc_type, *_):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

def place_order(uow, sku):
    stock = uow.session.get(Stock, 1)
    if stock.qty <= 0:
        raise ValueError("库存不足, 整体回滚")
    stock.qty -= 1
    uow.session.add(Order(sku=sku))

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add(Stock(sku="x", qty=1)); s.commit()

    with UoW(engine) as uow:               # 成功: 两个表一起提交
        place_order(uow, "x")
    with Session(engine) as s:
        print("成功后库存:", s.get(Stock, 1).qty, "订单数:",
              len(s.query(Order).all()))

    try:
        with UoW(engine) as uow:           # 失败: 整体回滚
            place_order(uow, "x")
            raise ValueError("下游支付失败")
    except ValueError as e:
        print("失败:", e)
    with Session(engine) as s:
        print("回滚后库存:", s.get(Stock, 1).qty)
