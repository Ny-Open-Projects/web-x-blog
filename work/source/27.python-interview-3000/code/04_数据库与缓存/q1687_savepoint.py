"""SAVEPOINT 嵌套事务: 局部回滚不影响外层提交"""
import sqlite3

try:
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
    HAS_SQLA = True
except ImportError:
    HAS_SQLA = False

def demo_pure():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
    conn.execute("INSERT INTO t VALUES(1, 'base')")
    conn.commit()

    conn.execute("SAVEPOINT sp1")                 # 外层事务
    conn.execute("UPDATE t SET v='outer' WHERE id=1")
    conn.execute("SAVEPOINT sp2")                 # 内层保存点
    conn.execute("UPDATE t SET v='inner-bad' WHERE id=1")
    conn.execute("ROLLBACK TO sp2")               # 只回滚内层
    conn.execute("RELEASE sp2")
    print("内层回滚后:", conn.execute("SELECT v FROM t WHERE id=1").fetchone()[0])
    conn.execute("RELEASE sp1")
    conn.commit()
    print("外层提交后:", conn.execute("SELECT v FROM t WHERE id=1").fetchone()[0])
    print("要点: 批量导入用 SAVEPOINT 按行/按片隔离失败, 坏片回滚好片继续, 整体不必推倒重来")

if HAS_SQLA:
    class Base(DeclarativeBase):
        pass

    class User(Base):
        __tablename__ = "users"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]

    def demo_sqla():
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        with Session(engine) as s:
            s.add(User(id=1, name="base"))
            s.commit()
            s.add(User(id=2, name="outer"))       # 外层事务的一部分
            nested = s.begin_nested()             # SAVEPOINT
            s.add(User(id=3, name="inner"))
            s.flush()
            nested.rollback()                     # 只回滚保存点内的对象
            s.commit()
            ids = sorted(s.scalars(select(User.id)).all())
            print("提交后存在的 id:", ids, "-> 保存点内的 id=3 被丢弃")

if __name__ == "__main__":
    if HAS_SQLA:
        demo_sqla()
    else:
        print("sqlalchemy 未安装, 用 sqlite3 原生 SAVEPOINT 演示")
        demo_pure()
