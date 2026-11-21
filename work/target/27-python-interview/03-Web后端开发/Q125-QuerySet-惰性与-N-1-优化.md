---
title: [Q125] QuerySet 惰性与 N+1 优化
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q125 · QuerySet 惰性与 N+1 优化

> 难度:★★★ | 标签:Django, ORM 性能

**问**:QuerySet 是懒加载的吗?如何解决模板中遍历外键导致的 N+1 问题?

**答**:QuerySet 创建时不发 SQL,在迭代、切片、len()/list() 等"求值"时才查询,且结果有缓存(同一 queryset 二次迭代不再查库)。N+1 指循环访问外键字段时每行触发一次额外查询:`select_related('author')` 用 SQL JOIN 一次取回外键/一对一关联,`prefetch_related('tags')` 对多对多/反向关系分两条查询后在 Python 层拼装;`only/defer` 控制列加载,`exists/count` 替代无谓的全量取回。

```python
# file: code/03_Web后端开发/q125_queryset_nplus1.py
# 自包含演示:用内存对象 + SQL 计数器模拟 QuerySet,对比 N+1 与两种预取策略
class QueryStats:
    """模拟 django.db.connection.queries:记录"数据库"被查询的次数"""
    count = 0

    @classmethod
    def hit(cls, sql):
        cls.count += 1

class Author:
    def __init__(self, name):
        self.name = name

class Tag:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author, tags):
        self.title = title
        self._author = author
        self._tags = list(tags)
        self._author_loaded = False   # False 时访问 author/tags 属性会"再查一次库"
        self._tags_loaded = False

    @property
    def author(self):
        if not self._author_loaded:   # N+1 的 N:每本书触发一次额外查询
            QueryStats.hit(f"SELECT * FROM author WHERE id = {id(self._author) % 100}")
            self._author_loaded = True
        return self._author

    @property
    def tags(self):
        if not self._tags_loaded:
            QueryStats.hit(f"SELECT * FROM tag WHERE book_id = '{self.title}'")
            self._tags_loaded = True
        return self._tags

BOOKS = [
    Book("三体", Author("刘慈欣"), [Tag("科幻"), Tag("小说")]),
    Book("呐喊", Author("鲁迅"), [Tag("文学")]),
    Book("朝花夕拾", Author("鲁迅"), [Tag("文学")]),
]

def bad_nplus1():
    QueryStats.count = 0
    QueryStats.hit("SELECT * FROM book")        # 迭代求值:第 1 条
    return [f'{b.title} by {b.author.name}' for b in BOOKS]
    # 每本书额外查询一次 author -> 1 + N 条 SQL(N=3 时共 4 条)

def good_select_related():
    # 模拟 select_related('author'):JOIN 一次取回,关联对象迭代前已装填
    QueryStats.count = 0
    for b in BOOKS:
        b._author_loaded = True
    QueryStats.hit("SELECT ... JOIN author ON author.id = book.author_id")
    return [f'{b.title} by {b.author.name}' for b in BOOKS]

def good_prefetch_related():
    # 模拟 prefetch_related('tags'):书 1 条 + 标签 1 条,共 2 条 SQL
    QueryStats.count = 0
    for b in BOOKS:
        b._tags_loaded = True
    QueryStats.hit("SELECT * FROM book")
    QueryStats.hit("SELECT * FROM tag WHERE book_id IN (...)")
    return [{b.title: [t.name for t in b.tags]} for b in BOOKS]
    # 注意:先 prefetch 再 all(),不要再写 b.tags.filter(...) 产生新查询

print(bad_nplus1(), "SQL 条数:", QueryStats.count)             # 4 条(1+N,N=3)
print(good_select_related(), "SQL 条数:", QueryStats.count)    # 1 条
print(good_prefetch_related(), "SQL 条数:", QueryStats.count)  # 2 条
```

**追问**:
- prefetch_related 的 Prefetch 对象有什么用?——自定义子查询与过滤:`Prefetch('tags', queryset=Tag.objects.filter(active=True))`,避免取回无用关联。
- select_related 能接多深?——跨多级外键 `select_related('a__b__c')` 一次 JOIN 取回;JOIN 过多会让单查询变慢,按访问路径权衡。
- 怎么在开发期发现 N+1?——`connection.queries` 计数、django-debug-toolbar、nplusone 检测库;测试断言查询次数是更硬的防线。
