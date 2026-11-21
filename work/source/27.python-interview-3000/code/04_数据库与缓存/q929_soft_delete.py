"""do_orm_execute + with_loader_criteria 全局注入软删过滤"""

try:
    from sqlalchemy import create_engine, select, event
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, mapped_column,
                                with_loader_criteria)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Doc(Base):
    __tablename__ = "docs"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    deleted: Mapped[bool] = mapped_column(default=False)

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    @event.listens_for(Session, "do_orm_execute")
    def _soft_delete(execute_state):
        if not execute_state.is_column_load and not execute_state.is_relationship_load:
            execute_state.statement = execute_state.statement.options(
                with_loader_criteria(Doc, lambda cls: cls.deleted == False,  # noqa
                                     include_aliases=True))

    with Session(engine) as s:
        s.add_all([Doc(title="a"), Doc(title="b")])
        s.commit()
        s.query(Doc).filter(Doc.title == "a").update({"deleted": True})
        s.commit()
        print("自动过滤后可见:", [d.title for d in s.scalars(select(Doc))])
        raw = s.execute(select(Doc).execution_options(
            include_deleted=True) if False else select(Doc.title)).all()
        print("普通 select 也被过滤:", raw)
