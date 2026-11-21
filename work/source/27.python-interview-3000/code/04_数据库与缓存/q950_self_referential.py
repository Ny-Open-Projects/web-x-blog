"""自引用 relationship + 递归 CTE 取整棵树"""
from typing import Optional

try:
    from sqlalchemy import (create_engine, ForeignKey, select, text)
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped,
                                mapped_column, relationship, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Dept(Base):
    __tablename__ = "depts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    parent_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("depts.id"), nullable=True)
    children: Mapped[list["Dept"]] = relationship(back_populates="parent")
    parent: Mapped[Optional["Dept"]] = relationship(
        back_populates="children", remote_side=[id])

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        ceo = Dept(name="ceo")
        cto = Dept(name="cto", parent=ceo)
        cto.children = [Dept(name="dev"), Dept(name="qa")]
        s.add(ceo); s.commit()

        # 一层: selectinload 直接子部门
        root = s.scalars(select(Dept).options(
            selectinload(Dept.children))).first()
        print("直接子部门:", [c.name for c in root.children])

        # 整树: 递归 CTE
        sql = text("""
            WITH RECURSIVE tree AS (
              SELECT id, name, 0 AS depth, name AS path FROM depts WHERE parent_id IS NULL
              UNION ALL
              SELECT d.id, d.name, t.depth + 1, t.path || '/' || d.name
              FROM depts d JOIN tree t ON d.parent_id = t.id
            )
            SELECT depth, path FROM tree ORDER BY path
        """)
        for depth, path in s.execute(sql):
            print("  " * depth + path)
