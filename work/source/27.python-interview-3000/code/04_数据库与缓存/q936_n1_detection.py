"""SQL 计数器: 用事件自动发现 N+1, 对比修复前后"""

try:
    from sqlalchemy import create_engine, event, ForeignKey, select
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped,
                                mapped_column, relationship, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    books: Mapped[list["Book"]] = relationship(back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped[Author] = relationship(back_populates="books")

class SqlCounter:
    def __init__(self, engine):
        self.n = 0
        event.listen(engine, "before_cursor_execute", self._inc)
    def _inc(self, *a):
        self.n += 1
    def __enter__(self):
        self.n = 0
        return self
    def __exit__(self, *a):
        pass

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    counter = SqlCounter(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Author(books=[Book()]) for _ in range(8)])
        s.commit()

        with counter as c:
            authors = s.scalars(select(Author)).all()
            total = sum(len(a.books) for a in authors)
        print(f"N+1: {total} 本, SQL {c.n} 条")

        with counter as c:
            authors = s.scalars(select(Author)
                                .options(selectinload(Author.books))).all()
            total = sum(len(a.books) for a in authors)
        print(f"selectinload: {total} 本, SQL {c.n} 条")
