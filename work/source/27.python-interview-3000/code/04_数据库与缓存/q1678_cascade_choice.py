"""级联策略选择: ORM cascade 谱系与数据库级联的分工"""
import sqlite3

try:
    from sqlalchemy import create_engine, ForeignKey, func, select
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, mapped_column,
                                relationship)
    HAS_SQLA = True
except ImportError:
    HAS_SQLA = False

def demo_pure():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.executescript("""
    CREATE TABLE parent(id INTEGER PRIMARY KEY, name TEXT);
    CREATE TABLE child(id INTEGER PRIMARY KEY,
        parent_id INTEGER REFERENCES parent(id) ON DELETE CASCADE, name TEXT);
    INSERT INTO parent VALUES(1, 'p1');
    INSERT INTO child VALUES(10, 1, 'c1'), (11, 1, 'c2');
    """)
    conn.execute("DELETE FROM parent WHERE id=1")
    conn.commit()
    print("数据库级 ON DELETE CASCADE 删父后子剩余:",
          conn.execute("SELECT COUNT(*) FROM child").fetchone()[0])
    print("分工: DB 级联管'行', 绕过 ORM 直改也生效; ORM cascade 管'对象图', 可挂业务钩子")
    print("ORM 谱系: save-update 与 merge 是默认; delete 管删父连带; delete-orphan 管从集合移除即删除")
    print("选型: 聚合根(订单-明细)用 all, delete-orphan; 跨聚合引用(订单-用户)绝不级联, 走业务层")
    print("坑: ORM cascade 与 DB ON DELETE 同时开启会互相踩, 二选一")

if HAS_SQLA:
    class Base(DeclarativeBase):
        pass

    class Parent(Base):
        __tablename__ = "parents"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]
        children: Mapped[list["Child"]] = relationship(cascade="all, delete-orphan")

    class Child(Base):
        __tablename__ = "children"
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str]
        parent_id: Mapped[int] = mapped_column(ForeignKey("parents.id"))

    def demo_sqla():
        engine = create_engine("sqlite://")
        Base.metadata.create_all(engine)
        with Session(engine) as s:
            s.add(Parent(id=1, name="p1",
                         children=[Child(id=10, name="c1"), Child(id=11, name="c2")]))
            s.commit()
            s.delete(s.get(Parent, 1))          # all, delete-orphan: 连带删子
            s.commit()
            print("删父后子剩余:", s.scalar(select(func.count()).select_from(Child)))
            s.add(Parent(id=2, name="p2", children=[Child(id=20, name="c20")]))
            s.commit()
            s.get(Parent, 2).children.pop()     # 从集合移除 -> delete-orphan 删除
            s.commit()
            print("从集合移除后子剩余:", s.scalar(select(func.count()).select_from(Child)))

if __name__ == "__main__":
    if HAS_SQLA:
        demo_sqla()
    else:
        print("sqlalchemy 未安装, 用 sqlite3 演示数据库级级联与 ORM 谱系对照")
        demo_pure()
