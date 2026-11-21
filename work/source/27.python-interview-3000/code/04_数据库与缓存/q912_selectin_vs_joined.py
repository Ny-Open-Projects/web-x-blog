"""统计两种加载策略的 SQL 条数, 直观对比 joinedload 与 selectinload"""

try:
    from sqlalchemy import create_engine, ForeignKey, select, event
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped,
                                mapped_column, relationship, joinedload, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="orders")

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    count = {"n": 0}

    @event.listens_for(engine, "before_cursor_execute")
    def _c(*a):
        count["n"] += 1

    Base.metadata.create_all(engine)
    with Session(engine) as s:
        for u in range(10):
            s.add(User(name=f"u{u}", orders=[Order() for _ in range(5)]))
        s.commit()

        for label, opt in (("joinedload", joinedload(User.orders)),
                           ("selectinload", selectinload(User.orders))):
            count["n"] = 0
            users = s.execute(select(User).options(opt)).unique().scalars().all()
            n_orders = sum(len(u.orders) for u in users)
            print(f"{label}: SQL {count['n']} 条, 取回 {n_orders} 个订单")
