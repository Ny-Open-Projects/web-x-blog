---
title: [Q769] QuerySet 求值时机与结果缓存
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q769 · QuerySet 求值时机与结果缓存

> 难度:★★★☆ | 标签:Django ORM, QuerySet

**问**:QuerySet 的惰性求值具体指什么?什么时候会"偷偷"再查一次库?

**答**:QuerySet 构造时只记录描述,**首次迭代/len/list/bool 判断才发 SQL**,并把结果缓存在 `._result_cache`;之后再次迭代同一 QuerySet 用缓存。任何**链式调用(filter/orderby/切片生成新对象)都返回新 QuerySet、缓存为空,必再查库**。另一类易错点:`if qs:` 触发完整求值,`qs.exists()`、`qs.count()` 是替代的轻量判断;模板里两次遍历同一变量有缓存,遍历两个"看起来一样"的变量就是两次查询。

```python
# file: code/03_Web后端开发/q769_queryset_cache.py
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

class Article(models.Model):
    title = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Article)

Article.objects.bulk_create([Article(title=f"t{i}") for i in range(3)])

connection.queries_log.clear()
qs = Article.objects.all()
print("count 触发查询:", len(connection.queries) == 1)
list(qs)
print("迭代触发查询:", len(connection.queries) == 2)
list(qs)
print("二次迭代走缓存:", len(connection.queries) == 2)
list(qs.order_by("-id"))
print("链式后重新查询:", len(connection.queries) == 3)
```

**追问**:
- exists() 和 count() 谁更快?——判断有无用 exists(短路 LIMIT 1),需要数字才用 count,两者都不读全行。
- 迭代大表怎么省内存?——iterator(chunk_size) 分块拉取,让缓存不驻留全量结果。
