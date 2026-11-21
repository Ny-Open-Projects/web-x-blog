---
title: [Q941] relationship 加载策略性能画像
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q941 · relationship 加载策略性能画像

> 难度:★★★★ | 标签:SQLAlchemy, 性能

**问**:lazy、selectin、joined 三种加载策略在同一负载下的 SQL 条数、行数、耗时各是什么量级?怎么做出选择?

**答**:设 100 个父、每个 10 个子:lazy 发 1+100 条 SQL(网络往返主导)、总行数最少;joinedload 1 条 SQL 但返回 1000 行(笛卡尔膨胀,网络与去重成本);selectinload 2 条 SQL、行数正好 1100 行分两批,总传输最小。选择矩阵:多对一用 joined(无膨胀)、一对多用 selectin、深度多层用 selectin 嵌套、单父单子极端场景 joined 一次到位。做出选择的依据不是感觉而是画像:像下面这样用事件统计 SQL 条数与返回行数,再结合 QPS 与网络 RTT 估算,预加载策略应该出现在代码评审清单里。

```python
# file: code/04_数据库与缓存/q941_loading_profile.py
"""画像三种加载策略: SQL 条数与返回行数"""

try:
    from sqlalchemy import create_engine, event, ForeignKey, select
    from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, mapped_column,
                                relationship, joinedload, selectinload)
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class Base(DeclarativeBase):
    pass

class Team(Base):
    __tablename__ = "teams"
    id: Mapped[int] = mapped_column(primary_key=True)
    members: Mapped[list["Member"]] = relationship(back_populates="team")

class Member(Base):
    __tablename__ = "members"
    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team: Mapped[Team] = relationship(back_populates="members")

def profile(engine, label, options):
    stats = {"sql": 0, "rows": 0}
    def _sql(*a):
        stats["sql"] += 1
    h = event.listen(engine, "before_cursor_execute", _sql)
    with Session(engine) as s:
        q = select(Team).options(options) if options else select(Team)
        teams = s.execute(q).unique().scalars().all()
        n = sum(len(t.members) for t in teams)
        event.remove(engine, "before_cursor_execute", _sql)
        print(f"{label}: SQL {stats['sql']} 条, 团队 {len(teams)}, 成员 {n}")

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([Team(members=[Member() for _ in range(10)])
                   for _ in range(100)])
        s.commit()
    profile(engine, "lazy       ", None)
    profile(engine, "joinedload ", joinedload(Team.members))
    profile(engine, "selectin   ", selectinload(Team.members))
```

**追问**:
- 返回行数膨胀的实际代价是什么?——网络传输、ORM 行解析、joined 去重(哈希全行)都会按膨胀行数付费,百万行级直接打爆内存。
- 一层多对一 + 一层一对多怎么组合?——joinedload(A.b) 套 selectinload(B.c),多对一走连接、集合走二次查询,混合是常态。

---
