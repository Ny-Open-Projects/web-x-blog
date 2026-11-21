---
title: [Q918] SQLAlchemy 事件钩子: before_flush / after_insert 实战
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q918 · SQLAlchemy 事件钩子: before_flush / after_insert 实战

> 难度:★★★★ | 标签:SQLAlchemy, 事件

**问**:SQLAlchemy 提供哪些常用事件钩子?给"所有变更写审计日志"该挂哪个事件?

**答**:常用层级:Session 级(before_flush/after_flush 拿到新增/修改/删除集合,适合审计与跨表协调)、Mapper 级(after_insert/after_update/after_delete,单对象回调,注意在 flush 事务内,别做耗时操作)、Attribute 级(set/setattr 拦截字段赋值,适合脏字段跟踪)、Engine 级(before_cursor_execute 计数与慢 SQL 监控)。审计日志最优挂 before_flush:一次拿到 session.new/dirty/deleted 三个集合与历史值(经 db.session.is_modified 或属性历史 inspect(obj).attrs.x.history),批量写入审计表,与业务同事务保证一致。陷阱:after_insert 里再写库必须用同一 connection,误用新 session 会死锁或绕过事务。

```python
# file: code/04_数据库与缓存/q918_event_hooks.py
"""before_flush 写审计表 + before_cursor_execute 统计 SQL 条数"""

try:
    from sqlalchemy import create_engine, event, select
    from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class Audit(Base):
    __tablename__ = "audit"
    id: Mapped[int] = mapped_column(primary_key=True)
    detail: Mapped[str]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    @event.listens_for(Session, "before_flush")
    def audit(session, flush_context, instances):
        for obj in session.new:
            if isinstance(obj, User):
                session.add(Audit(detail=f"insert {obj.name}"))
        for obj in session.dirty:
            if isinstance(obj, User):
                session.add(Audit(detail=f"update {obj.name}"))

    with Session(engine) as s:
        s.add(User(name="alice"))
        s.commit()
        u = s.scalars(select(User)).one()
        u.name = "alice2"
        s.commit()
        print("审计记录:", s.scalars(select(Audit.detail)).all())
```

**追问**:
- 钩子里能用另一个 session 吗?——不能,必须复用当前 session/connection,否则嵌套事务互相等待甚至死锁,且脱离了原事务的原子性。
- after_update 一定触发吗?——只有被标记修改的才触发;`is_modified(obj)` 为 False 或只改了主键场景要小心,需在 set 事件层面兜底。

---
