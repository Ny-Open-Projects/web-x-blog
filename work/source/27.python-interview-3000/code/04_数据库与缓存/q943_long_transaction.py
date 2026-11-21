"""对比两种结构: 持事务调外部 vs 先落库再调用"""
import time

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(default="init")

def call_remote():
    time.sleep(0.2)                     # 模拟第三方 200ms

def bad_style(engine):
    t0 = time.perf_counter()
    with Session(engine) as s:
        s.add(Payment())
        call_remote()                   # 事务持锁 200ms
        s.commit()
    return time.perf_counter() - t0

def good_style(engine):
    t0 = time.perf_counter()
    with Session(engine) as s:          # 事务1: 落库立即提交
        p = Payment(status="processing")
        s.add(p)
        s.commit()
        pid = p.id
    call_remote()                        # 无事务占用
    with Session(engine) as s:          # 事务2: 确认结果
        s.get(Payment, pid).status = "done"
        s.commit()
    return time.perf_counter() - t0

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    print(f"持锁调外部: {bad_style(engine) * 1000:.0f} ms 事务持有中含 200ms 外部调用")
    print(f"短事务拆分: {good_style(engine) * 1000:.0f} ms, 两次事务各毫秒级")
