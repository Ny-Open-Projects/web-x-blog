---
title: [Q2624] operator.itemgetter 与 attrgetter:多键排序去 lambda
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2624 · operator.itemgetter 与 attrgetter:多键排序去 lambda

> 难度:★☆☆☆☆ | 标签:operator, 排序, 可读性

**问**:`key=lambda r: (r["dept"], r["age"])` 为什么要换成 itemgetter?

**答**:`operator.itemgetter("dept", "age")` 生成一个 C 实现的可调用对象,对输入依次取键返回元组,语义与 lambda 完全一致但更快、更短、无变量遮蔽风险;`attrgetter` 对属性做同样的事。二者还能接受下标(`itemgetter(0, 2)`)与点路径(`attrgetter("addr.city")`),配合 `sorted`、`min`、`groupby` 的 key 使用是标准搭配。它读起来更像「按什么排」的声明,代码评审时一眼可懂。边界:需要在取值时做转换(如 `int(r["age"])`)就得回 lambda 或先用 `map` 预处理。

```python
# file: code/01_语言核心与底层/q2624_itemgetter.py
"""itemgetter 与 attrgetter:多键排序的标准写法。"""
from operator import attrgetter, itemgetter

rows = [
    {"dept": "b", "age": 30},
    {"dept": "a", "age": 40},
    {"dept": "a", "age": 20},
]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    print("多键排序:", sorted(rows, key=itemgetter("dept", "age")))
    print("单键取值:", itemgetter("dept")(rows[0]))

    people = [Person("bob", 30), Person("amy", 25)]
    print("attrgetter:", [p.name for p in sorted(people, key=attrgetter("age"))])
    print("点路径:", attrgetter("age")(people[0]))

    # 需要转换时才回 lambda
    print("转换型 key:", sorted(rows, key=lambda r: -r["age"]))
```

**追问**:1) itemgetter 对缺键会怎样?——直接抛 KeyError,与 `r["key"]` 行为一致;想要缺省值就得写 lambda 用 `.get`。2) 两兄弟的分工?——itemgetter 取序列/映射项(C 快路径,多键返回元组);attrgetter 取属性链(obj.a.b)与调用(callable);排序 key 的 C 层实现在大数据上比 lambda 快一个量级(Q514/2092)。3) 与 operator 模块的组合?——itemgetter(1, 3) 多索引、attrgetter("x", "y") 多属性、methodcaller 调方法;SortSpec 化的多级排序。4) 生产陷阱?——缺键想容错却拿到 KeyError;itemgetter 拿属性但对象嵌套层级变;过度追求 C 路径牺牲可读性。
