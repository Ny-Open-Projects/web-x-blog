---
title: [Q944] Django ORM: select_related 与 prefetch_related
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q944 · Django ORM: select_related 与 prefetch_related

> 难度:★★★☆ | 标签:Django, ORM

**问**:Django 的 select_related 和 prefetch_related 区别是什么?分别对应什么 SQL?

**答**:select_related 用 SQL JOIN 一次取回关联对象,适用于 ForeignKey/OneToOne(多对一/一对一),参数写关系路径 `Book.objects.select_related("author")`;prefetch_related 分两条 SQL——先查主对象,再用 IN 批量查关联表,在 Python 层拼装,适用于 ManyToMany 与反向外键(一对多)。选错的表现:对一对多用 select_related 会行数膨胀(与 SQLAlchemy joinedload 同理),对 FK 用 prefetch 多一次查询但不错。配套工具:only/defer 控制字段、values 列表瘦身、prefetch_related(Prefetch("books", queryset=...)) 定制子查询,debug 时用 connection.queries 或 django-debug-toolbar 看 SQL。

```python
# file: code/04_数据库与缓存/q944_django_loading.py
"""用原生 SQL 演示 select_related 与 prefetch_related 的形态差异"""
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE author (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE book (id INTEGER PRIMARY KEY, author_id INT, title TEXT);
        INSERT INTO author VALUES (1, 'Ada'), (2, 'Alan');
        INSERT INTO book VALUES (1, 1, 'Notes'), (2, 1, 'Engine'),
                                (3, 2, 'Machine');
    """)
    print("select_related 形态: 一条 JOIN")
    for r in conn.execute(
            "SELECT b.title, a.name FROM book b "
            "LEFT JOIN author a ON a.id = b.author_id"):
        print("  ", r)
    print("prefetch_related 形态: 两条 SQL + 内存拼装")
    authors = conn.execute("SELECT id, name FROM author").fetchall()
    books = conn.execute(
        f"SELECT id, author_id, title FROM book "
        f"WHERE author_id IN ({','.join(str(a[0]) for a in authors)})").fetchall()
    print("   作者:", authors, "\n   批量书籍:", books)
    print("Django: FK/OneToOne 用 select_related, M2M/反向用 prefetch_related")
```

**追问**:
- Prefetch 对象解决什么问题?——默认 prefetch 拉全量关联再过滤会破坏对应关系,用 Prefetch 指定带过滤的 queryset,保证"预加载且只取需要的"。
- only/defer 的坑?——只取部分字段后再访问未取字段会触发再查询,与懒加载叠加又变 N+1,清单要与序列化字段对齐。

---
