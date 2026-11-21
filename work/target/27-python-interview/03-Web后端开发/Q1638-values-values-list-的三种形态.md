---
title: [Q1638] values/values_list 的三种形态
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1638 · values/values_list 的三种形态

> 难度:★★☆☆ | 标签:Django ORM, 查询

**问**:values() 和 values_list() 返回的到底是什么?和直接遍历模型实例差在哪?

**答**:values() 返回字典列表,values_list() 返回元组列表,flat=True 退化为单列值列表,named=True 退化为具名元组;三者共同点是都不实例化模型——跳过模型构造开销,内存与 CPU 显著下降,这是大数据导出的标准姿势。代价:实例方法、属性、缓存过的关联全部不可用,只拿到投影字段;外键列拿到的是 author_id 主键值而不是作者对象。链式调用是整体覆盖语义,后一个 values 的字段列表完全替换前一个,不是求并集。只需要列数据(导出、聚合输入、下拉选项)用 values 系;需要模型行为(保存、方法)就必须走实例。

```python
# file: code/03_Web后端开发/q1638_values_semantics.py
"""values/values_list 的语义: dict、tuple、flat 各拿到什么(纯标准库模拟)。"""
try:
    import django
    HAS_DJANGO = True
except ImportError:
    HAS_DJANGO = False
    print("[降级] 未安装 django, 以下用内存数据模拟 QuerySet 的三种取值形态")

ROWS = [
    {"id": 1, "title": "a", "author_id": 9},
    {"id": 2, "title": "b", "author_id": 9},
]


def values(*fields):
    return [{f: r[f] for f in fields} for r in ROWS]


def values_list(*fields, flat=False, named=False):
    if flat:
        if len(fields) != 1:
            raise TypeError("flat 只能取一列")             # 由调用处捕获
        return [r[fields[0]] for r in ROWS]
    if named:
        from collections import namedtuple
        nt = namedtuple("Row", fields)
        return [nt(*(r[f] for f in fields)) for r in ROWS]
    return [tuple(r[f] for f in fields) for r in ROWS]


print("values      ->", values("id", "title"))
print("values_list ->", values_list("id", "title"))
print("flat        ->", values_list("title", flat=True))
print("named       ->", values_list("id", "title", named=True)[0].id)
try:
    values_list("id", "title", flat=True)
except TypeError as e:
    print("多列 flat:", e)
print("注意: 两种形态都不实例化模型, 实例方法与属性不可用; 外键列拿到的是主键值")
```

**追问**:
- values 后再 save 行吗?——不行,字典没有 save,类型系统帮你挡住的第一层误用。
- named 和 values 怎么选?——named 兼顾元组性能与字段名可读性,列顺序变化的回归风险更小。
