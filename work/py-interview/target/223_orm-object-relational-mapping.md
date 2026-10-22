# 223. ORM：对象关系映射

> 分类：Web 框架 | 难度：L2 | 题型：概念+权衡 | 频率：中 | 关键词：**ORM** / **Object Relational Mapping** / **SQLAlchemy** / **Peewee** / **优缺点**
> 原文锚点：第9章 9-1「ORM=Object Relational Mapping(对象到关系映射); 流行实现 SQLAlchemy(事实标准), Django内置ORM, 轻量 Peewee; 为何用ORM: 代码更面向对象, 用业务模型操作数据表而非手写SQL」

## 一句话总述
**ORM（Object Relational Mapping）把数据库表/行映射成程序里的对象**，让"用业务模型操作数据"取代"手写 SQL"；Python 里 SQLAlchemy 已成事实标准，另有 Django 内置 ORM、轻量 Peewee。

## 面试官视角
- **考察意图**：是否理解 ORM 解决什么问题、有什么代价，而非只说"不用写 SQL"。
- **P5** 能说出 ORM 是"对象到关系映射"及常见实现（SQLAlchemy/Django ORM） / **P6** 能讲清 ORM 优势（面向对象、少写胶水 SQL、易维护）与代价（复杂查询性能/灵活性受限） / **P7** 能补充"何时该绕过 ORM 直接写 SQL（报表/复杂 join/性能敏感）"。
- **红旗**：认为 ORM 能完全替代 SQL、不需要懂 SQL；或不知道 SQLAlchemy 是独立库（以为只有 Django ORM）。
- **惊艳点**：能点出"ORM 生成的 SQL 可能低效，性能关键点仍要 EXPLAIN/原生 SQL" `[经验]`。

## 主问答
**Q（面试官原话）：** 什么是 ORM？为什么要用 ORM？

**A · 标准答案骨架：**
1. **定义**：ORM（Object Relational Mapping）实现"业务对象"与"关系数据库表/字段"之间的映射——表→类、行→对象、字段→属性。
2. **常见实现**：Python 里 **SQLAlchemy** 是事实标准（Flask 生态用 Flask-SQLAlchemy），Django 有**内置 ORM**，还有轻量的 **Peewee**。
3. **为什么用**：让代码更**面向对象**——直接操作业务模型而非手写 SQL 字符串；减少胶水代码、易维护、跨库可移植。

**加分层**：ORM 也有代价——复杂查询（多表 join、窗口函数、报表）下生成 SQL 未必最优，性能敏感处应**回退到原生 SQL**；所以"懂 SQL"是用好 ORM 的前提，而非替代。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | ORM 是什么 | 基本认知 | 对象-关系映射 | 换题 → 不及格 |
| L2 | 常见实现 | 是否用过 | SQLAlchemy/Django/Peewee | 判 P5 |
| L3 | 为什么用 | 权衡 | 面向对象/少写SQL | 判 P6 |
| L4 | ORM 代价 | 深入 | 复杂查询性能受限 | 判 P6+ |
| L5 | 何时不用 ORM | 实战 | 报表/复杂join回退原生SQL | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| SQLAlchemy/Django ORM/Peewee 长期为主流 | 无版本翻转 | 仍按此答；可补"异步 ORM（SQLAlchemy 1.4+ async、Tortoise-ORM）" |

## 关键代码
```python
# SQLAlchemy 声明模型（ORM 示例）[实测, python]
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, Session
Base = declarative_base()
class User(Base):                      # 表 → 类
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))         # 字段 → 属性
engine = create_engine("sqlite:///db.sqlite3")
with Session(engine) as s:
    u = s.get(User, 1)                # 行 → 对象，无需手写 SQL
    print(u.name)
```

## ⚠️ 原文纠错
- 机翻还原：「circleargument」→ **SQLAlchemy**；「将果自」→ **Django（内置）ORM**；「PV对 / 轻量量的」→ **Peewee（轻量 ORM）**；「objectrelationalmapping」→ **Object Relational Mapping**；「circle」→ **SQL**（"直接写 circle"=直接写 SQL）；「surfatomy / flashsufatomy」→ **SQLAlchemy / Flask-SQLAlchemy**。
- 原文"ORM 让代码更面向对象，用业务模型操作数据表而非直接写 SQL"准确；"SQLAlchemy 成事实标准、Peewee 轻量"准确。
- 原文未提 ORM 代价与回退原生 SQL，已补（权衡考点）。

## 总结与追问预判
ORM = 对象-关系映射，Python 以 SQLAlchemy 为事实标准；优势是面向对象、易维护，代价是复杂查询需回退原生 SQL。可衔接：**MVC（见 222 卡）**、**WSGI（见 220 卡）**。
