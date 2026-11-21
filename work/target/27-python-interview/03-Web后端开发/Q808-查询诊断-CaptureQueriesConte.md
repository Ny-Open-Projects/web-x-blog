---
title: [Q808] 查询诊断:CaptureQueriesContext 与 N+1 断言
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q808 · 查询诊断:CaptureQueriesContext 与 N+1 断言

> 难度:★★★☆ | 标签:Django, 测试, 性能

**问**:怎么在测试里防住 N+1 回归?

**答**:用 `django.test.utils.CaptureQueriesContext(connection)` 捕获上下文内的 SQL,断言**查询条数上限**;比数条数更进一步的是断言 SQL 形态(是否含 JOIN)。配合 django-debug-toolbar 在开发环境实时看,CI 里跑查询数守卫测试。同类思路推广:每接口设"最大查询数"预算,超了要么修要么显式豁免,防止性能随业务迭代悄悄劣化。

```python
# file: code/03_Web后端开发/q808_query_debug.py
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
from django.test.utils import CaptureQueriesContext

class Book(models.Model):
    title = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

class Author(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Author)
    se.create_model(Book)

a = Author.objects.create(name="甲")
Book.objects.bulk_create([Book(title=f"b{i}", author=a) for i in range(3)])

def n_plus_one():
    for b in Book.objects.all():
        _ = b.author.name

def fixed():
    for b in Book.objects.select_related("author"):
        _ = b.author.name

with CaptureQueriesContext(connection) as ctx1:
    n_plus_one()
with CaptureQueriesContext(connection) as ctx2:
    fixed()
print("修复前查询数:", len(ctx1.captured_queries))
print("修复后查询数:", len(ctx2.captured_queries))
```

**追问**:
- 断言查询数会不会太脆?——设宽松上限(如 ≤5)并注释豁免理由,重结构断言优于精确数字。
- 生产上怎么看真实 N+1?——APM 按 trace 聚合 DB span 数,单请求 DB 查询数异常即告警。
