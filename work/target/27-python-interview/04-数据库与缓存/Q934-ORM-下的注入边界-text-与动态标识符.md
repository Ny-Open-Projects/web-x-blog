---
title: [Q934] ORM 下的注入边界: text() 与动态标识符
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q934 · ORM 下的注入边界: text() 与动态标识符

> 难度:★★★★ | 标签:安全, SQLAlchemy

**问**:用了 ORM 就不会 SQL 注入了吗?哪些地方仍是边界?

**答**:ORM 的常规 where/参数都是参数化,安全;但三类位置仍是注入面:一、text() 原生 SQL 里 f-string 拼接用户输入——必须用 text().bindparams() 绑定;二、动态标识符(表名、列名、排序方向)无法参数化,只能白名单映射;三、二阶注入——存进库的恶意值在别处被拼进 SQL(如导出功能拼列名)。规则:值用绑定参数,结构用白名单,一切"拼接出来的 SQL"都要过代码评审。演示同一条查询的安全与危险两种写法。

```python
# file: code/04_数据库与缓存/q934_orm_injection.py
"""text() 的安全绑定与危险拼接对比"""

try:
    from sqlalchemy import create_engine, text
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

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add(User(name="admin")); s.commit()

        evil = "' OR '1'='1"

        # 危险: f-string 进 text()
        try:
            rows = s.execute(text(f"SELECT * FROM users WHERE name = '{evil}'")).all()
            print("危险拼接返回行数:", len(rows), "<- 被注入")
        except Exception as e:
            print("危险拼接异常:", type(e).__name__)

        # 安全: bindparams 绑定
        rows = s.execute(
            text("SELECT * FROM users WHERE name = :n").bindparams(n=evil)).all()
        print("参数化返回行数:", len(rows))

        # 动态排序: 白名单
        allowed = {"name": User.name, "id": User.id}
        key = allowed.get("name", User.id)
        print("白名单排序:", s.execute(
            text("SELECT name FROM users ORDER BY " +
                 ("name" if key is User.name else "id"))).all())
```

**追问**:
- bindparams 和直接 dict 传参区别?——等价,都是绑定参数;text() 里命名参数 + bindparams 只是显式声明,混用字符串模板才是风险。
- 白名单校验放在哪层?——数据访问层入口统一做,业务层传上来的动态字段先映射再进 SQL,不让原始字符串落到查询层。

---
