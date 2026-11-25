---
title: [Q6668] SQLAlchemy 1.4 到 2.0 迁移破坏点清单
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6668 · SQLAlchemy 1.4 到 2.0 迁移破坏点清单

难度：P6-P7 | 标签：SQLAlchemy、版本演进、ORM

**问**：SQLAlchemy 2.0 是一次大版本断代（Python 3.7+ 基线、Query 风格移除、Session.execute 全面接管）。1.4 已经内置了 2.0 风格的过渡支持，那迁移工作到底还剩什么？最常踩的破坏点有哪些？

**答**：结论：1.4 的价值是把 2.0 API 以 `future=True` 预置进来，所以正确姿势是**先在 1.4 内完成"2.0 风格改造"，再升 2.0**——升级行为差异极少。剩余破坏点集中在五类：① `Query` 对象方法（`query.filter` 返回 Query 可再链）改 `select()` + `session.execute()`；② `session.query(User).get(id)` 改 `session.get(User, id)`；③ `autocommit=True` / `subquerytransactions` 移除，隐式提交全部显式化；④ 驱动方言：2.0 默认要求 DBAPI 支持完全 DBAPI 2.0，psycopg2 需配合 psycopg3 或保持 2.8+（Q6568 迁移联动）；⑤ `Unicode/UnicodeText` 等别名与 `convert_unicode` 移除，类型声明收敛到 `String/Text`。

取舍与实战：
1. 迁移工具链：官方 `sqlalchemy2-stubs` / `sqlalchemy[asyncio]` + ruff 自定义规则（禁 `session.query(`）做静态门禁，比人工扫更可靠。
2. 事务语义收紧是行为级变化：1.4 下 `session.commit()` 后继续用 session 会隐式开新事务，2.0 的 `expire_on_commit` + 显式 `begin()` 更严格——依赖隐式新事务的老代码会在 2.0 里出现"提交后读不到自己刚写的数据"类 bug，必须有集成测试覆盖。
3. 降级基线：迁移期 pin `SQLAlchemy>=1.4.41,<2`（双风格并存）+ `SQLAlchemy-Utils` 兼容层；全绿后再放开 `<2.1`。
4. 与异步生态联动：asyncpg/psycopg 异步驱动只在 2.0 `AsyncSession` 稳定，1.4 的 asyncio 是实验态——异步服务迁移优先级最高。

```python
"""1.4 双风格对照 + 2.0 门禁规则演示（可运行；无 DB 时用内存 SQLite）"""
from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column,
                            Session, sessionmaker)

class Base(DeclarativeBase): ...

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(engine, expire_on_commit=False)

with SessionLocal() as s:
    s.add(User(name="w"))
    s.commit()

# --- 旧 1.x 风格（2.0 中 Query 移除，勿再新增）---
# s.query(User).filter(User.name == "w").one()

# --- 2.0 风格：select() + session.execute / session.get ---
with SessionLocal() as s:
    stmt = select(User).where(User.name == "w")
    u = s.execute(stmt).scalar_one()
    by_id = s.get(User, u.id)          # 替代 query.get
    print("2.0 风格 OK:", by_id.name)

# --- CI 门禁规则（ruff / 正则示意）---
BAD = ("session.query(", ".query(", "autocommit=True", "convert_unicode=")
def lint(src: str) -> list[str]:
    return [f"[阻断] {p}" for p in BAD if p in src]
print(lint("s = sessionmaker(autocommit=True)"))
```

**追问 1**：`expire_on_commit=True`（默认）下 commit 后访问属性触发什么？为什么迁移后这类问题变多？
**提示**：触发懒加载刷新，脱离事务上下文时抛 `DetachedInstanceError`；1.x 大量代码依赖"提交后对象还能用"的隐式行为，2.0 语义收紧后集中爆，迁移要显式决定每个 commit 后的刷新策略。

**追问 2**：为什么官方坚持用 `select()` 而不是保留 `Query`？
**提示**：`select()` 是与执行引擎解耦的纯语句对象，可复用于核心层/ORM 层/异步路径，类型标注友好；Query 绑定 session 的设计无法支持 2.0 的统一事务模型。

## 背诵要点
- 正确路径：1.4 `future=True` 先完成 2.0 风格改造再升 2.0；破坏点集中在 Query/get/autocommit/类型别名四类。
- 行为级雷区：commit 后隐式新事务消失、expire_on_commit 触发 DetachedInstanceError，集成测试必须覆盖。
- 门禁用静态规则禁 `session.query(`，迁移期 pin `<2` 双风格并存。

## 复盘追问
- 迁移分支上如何统计 `session.query` 的残留量并按模块排优先级？
- 异步服务先用 AsyncSession 时，同步 Session 与 AsyncSession 混用的连接池如何隔离？
