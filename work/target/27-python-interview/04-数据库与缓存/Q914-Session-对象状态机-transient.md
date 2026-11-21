---
title: [Q914] Session 对象状态机: transient 到 detached
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q914 · Session 对象状态机: transient 到 detached

> 难度:★★★★ | 标签:SQLAlchemy, Session

**问**:一个 ORM 对象有哪几种状态?分别在什么操作后流转?

**答**:四态:transient(刚 new,无 session 无主键)、pending(加入 session,add 之后,等待 flush)、persistent(在 session 身份映射中且数据库有对应行,flush/查询后)、detached(曾被管理,现脱离 session,如 session.close 或 expunge 后)。关键机制是 identity map:同一 session 内同主键只会有一个对象实例,重复查询返回同一引用;detached 对象访问未加载的延迟属性会报 DetachedInstanceError——这是"session 关了还能不能用对象"问题的根源。inspect(obj) 可随时查看状态,面试能画清楚 add→flush→commit 的流转即可。

```python
# file: code/04_数据库与缓存/q914_object_states.py
"""用 inspect() 追踪一个对象从 transient 到 detached 的状态流转"""

try:
    from sqlalchemy import create_engine, inspect
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

def state(obj):
    """inspect() 的状态标志位辅助"""
    i = inspect(obj)
    if i.transient: return "transient"
    if i.pending: return "pending"
    if i.detached: return "detached"
    return "persistent"

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    u = User(name="a")
    print("new 后:", state(u))

    with Session(engine) as s:
        s.add(u)
        print("add 后:", state(u))
        s.flush()
        print("flush 后:", state(u), "id=", u.id)
    print("close 后:", state(u))
```

**追问**:
- 同一 session 两次查同主键会发几条 SQL?——第二条命中 identity map 直接返回同一对象(除非该对象已过期),这是 session 的一致性缓存。
- DetachedInstanceError 何时发生?——对象已脱离 session 且访问未加载的延迟属性,解决:在 session 内访问完、用 joinedload 预取、或合理使用 expire_on_commit=False。

---
