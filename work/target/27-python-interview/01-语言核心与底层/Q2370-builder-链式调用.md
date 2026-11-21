---
title: [Q2370] builder 链式调用
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2370 · builder 链式调用

> 难度:★★★☆☆ | 标签:builder, 链式调用, API 设计

**问**:builder 模式的核心契约是什么?复用 builder 实例有什么坑?

**答**:builder 的契约两条:每个配置方法返回 self,让调用可以链下去;build() 做完整性校验并产出不可变的成品,构造非法状态在 build 时集中报错(如「没指定 table」)。它适合「多可选配置 + 构建过程有顺序依赖 + 成品应当验证」的对象——SQL 构造器、HTTP 请求、复杂报告都是典型。最大的坑是 builder 本身的可变状态:同一个 builder 链完再链,where 条件会累积,第二次 build 混入上一轮的配置。两种对策:文档声明「一链一用」,每次新建;或提供不可变变体,每个配置方法返回深拷贝/新实例,线程安全可缓存,代价是每次拷贝的开销。与 kwargs 大参数列表相比,builder 把「哪个方法配哪类东西」变成签名的一部分,配合 IDE 提示,可发现性远好于记参数名。

```python
# file: code/01_语言核心与底层/q2370_builder.py
"""builder 链式调用:每步返回 self,build 时校验并冻结成品。"""
import copy


class QueryBuilder:
    def __init__(self):
        self._table = None
        self._wheres = []
        self._limit = None

    def table(self, name):
        self._table = name
        return self

    def where(self, cond):
        self._wheres.append(cond)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        if not self._table:
            raise ValueError("必须先指定 table")
        sql = "SELECT * FROM " + self._table
        if self._wheres:
            sql += " WHERE " + " AND ".join(self._wheres)
        if self._limit is not None:
            sql += " LIMIT " + str(self._limit)
        return sql


class FrozenBuilder(QueryBuilder):
    """不可变变体:每个配置方法返回副本,可复用可缓存。"""

    def table(self, name):
        new = copy.deepcopy(self)
        new._table = name
        return new

    def where(self, cond):
        new = copy.deepcopy(self)
        new._wheres.append(cond)
        return new


if __name__ == "__main__":
    sql = QueryBuilder().table("users").where("age > 18").where("active = 1").limit(10).build()
    print(sql)

    base = QueryBuilder().table("orders")
    print(base.where("paid = 1").build())
    print("可变 builder 会累积:", base.where("paid = 0").build())

    fb = FrozenBuilder().table("a")
    print("不可变链互不影响:", fb.table("b")._table, "与", fb._table)
```

**追问**:1) builder 与直接用 dataclass 关键字构造怎么选?——配置项少、无构建顺序依赖时 dataclass 足够;配置方法携带语义(table/where/limit 各有约束)或构建过程分阶段时 builder 才有增量价值。2) 链式调用的实现要点?——每个 with_x 返回 self(Signature 用 typing.Self 标,Q1269);构建分阶段时 build() 收口;不可变派生风格则返回新副本(与 frozen dataclass 组合)。3) 与 kwargs 演化的关系?——builder 让「新增配置项」不破坏调用方(方法追加);签名演化(Q2373)的风险被封装。4) 生产陷阱?——链式返回 None 忘 self;builder 半成品被误用(未 build 先用);配置语义重复(方法名与字段名双套真相)。
