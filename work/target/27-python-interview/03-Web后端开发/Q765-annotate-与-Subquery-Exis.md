---
title: [Q765] annotate 与 Subquery/Exists 子查询
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q765 · annotate 与 Subquery/Exists 子查询

> 难度:★★★★ | 标签:Django ORM, 查询

**问**:每个作者要带"作品数"和"最新作品名",一次查询怎么做?

**答**:聚合用 `annotate(Count("book"))` 一次 GROUP BY 搞定;"每行的最新关联值"用 `Subquery`:内层 QuerySet 通过 `OuterRef` 引用外层行,`values(...)[:1]` 限定单值。相比 join 整表再聚合,Subquery 走相关子查询,大表下更可控。EXISTS 判断用 `Exists()` 包子查询配 annotate 布尔列。注意 annotate 后的聚合值参与 filter 时要用 alias,避免隐式 HAVING 语义混乱。

```python
# file: code/03_Web后端开发/q765_annotate_subquery.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.db import connection, models
from django.db.models import Count, OuterRef, Subquery

class Author(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Author)
    se.create_model(Book)

a1, a2 = Author.objects.create(name="甲"), Author.objects.create(name="乙")
Book.objects.create(title="甲一", author=a1)
Book.objects.create(title="甲二", author=a1)
Book.objects.create(title="乙一", author=a2)

latest = Book.objects.filter(author=OuterRef("pk")).order_by("-id").values("title")[:1]
qs = Author.objects.annotate(book_count=Count("book"), latest_title=Subquery(latest))
print(list(qs.values("name", "book_count", "latest_title")))
```

**追问**:
- annotate 与 aggregate 的区别?——annotate 给每行加计算列(分组到模型行),aggregate 出单个汇总值字典。
- Subquery 拿多列怎么办?——一次只取一个值列,多列要写多个 Subquery 或用 JSONArray 聚合技巧。
