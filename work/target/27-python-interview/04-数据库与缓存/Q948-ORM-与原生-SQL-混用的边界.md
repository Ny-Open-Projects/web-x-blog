---
title: [Q948] ORM 与原生 SQL 混用的边界
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q948 · ORM 与原生 SQL 混用的边界

> 难度:★★★☆ | 标签:SQLAlchemy, 原生 SQL

**问**:什么时候应该放弃 ORM 写原生 SQL?怎么混用才不乱?

**答**:该下放原生的场景:窗口函数/递归 CTE 等复杂分析、DB 特有语法(ON CONFLICT 细节、hint)、超大批量操作、需要精确控制计划的热点 SQL。混用纪律:原生 SQL 集中在 Repository 实现内部(上层接口不变),参数一律绑定(text().bindparams 或 raw connection 的参数化),结果映射回领域对象;SQLAlchemy 用 text() 与 session.execute 保持同一事务与连接,别另开连接破坏事务。反过来,能用 ORM 表达清楚的别手写——ORM 帮你处理方言、参数化与组合,双轨制的关键是"谁负责什么"有明确边界。

```python
# file: code/04_数据库与缓存/q948_native_sql_mix.py
"""同一 session 内混用 ORM 查询与 text() 原生 SQL"""

try:
    from sqlalchemy import create_engine, text, select
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
    score: Mapped[int]

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([User(name=f"u{i}", score=i) for i in range(5)])
        s.commit()

        # 原生: 排名这类窗口逻辑下放 SQL
        ranks = s.execute(text(
            "SELECT name, score, RANK() OVER (ORDER BY score DESC) AS rk "
            "FROM users")).all()
        print("原生窗口:", ranks)

        # ORM: 常规过滤回到实体世界
        top = s.scalars(select(User).where(User.score >= 3)).all()
        print("ORM 过滤:", [u.name for u in top])
        print("同一事务 同一连接, 两界共存")
```

**追问**:
- text() 结果怎么映射回实体?——2.0 用 `session.scalars(select(User).from_statement(text(...)))`,或取 Row 后手动构造 DTO,保持接口返回类型一致。
- 原生 SQL 的回归测试怎么做?——集中在 Repository 层就有清晰测试面:真库集成测试跑 SQL,断言行集而非实现细节。

---
