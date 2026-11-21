"""lazy=raise_on_sql 演示: 未预加载就访问属性立即报错"""

try:
    from sqlalchemy import create_engine, ForeignKey, select
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, mapped_column,
                                relationship, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user", lazy="raise_on_sql")

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="orders")

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add(User(orders=[Order(), Order()]))
        s.commit()

        u = s.scalars(select(User).options(selectinload(User.orders))).one()
        print("预加载后访问:", len(u.orders), "个订单")

        u2 = s.scalars(select(User)).one()
        try:
            _ = u2.orders
        except Exception as e:
            print("未预加载访问被拦截:", type(e).__name__)
