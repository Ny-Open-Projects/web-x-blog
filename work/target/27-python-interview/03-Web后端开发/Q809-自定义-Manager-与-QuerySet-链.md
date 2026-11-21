---
title: [Q809] 自定义 Manager 与 QuerySet 链式封装
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q809 · 自定义 Manager 与 QuerySet 链式封装

> 难度:★★★☆ | 标签:Django ORM, 设计

**问**:业务查询逻辑堆在视图里,怎么用自定义 QuerySet 收编?

**答**:继承 `models.QuerySet` 写领域查询方法(`published()`、`popular(n)`),保持**返回 QuerySet** 以支持继续链式;`QuerySet.as_manager()` 挂成 objects。分工原则:QuerySet 放"查询语义",Manager 做入口与不返回集合的便捷方法,模型类放单实例行为。收益:查询可组合、可复用、可测试,视图里只剩 `Post.objects.published().popular()` 这种领域语言。

```python
# file: code/03_Web后端开发/q809_manager.py
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

class PublishedQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status="p")

    def popular(self, n: int = 3):
        return self.order_by("-views")[:n]

class Post(models.Model):
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=1, default="d")
    views = models.IntegerField(default=0)
    objects = PublishedQuerySet.as_manager()
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Post)

Post.objects.bulk_create([
    Post(title="a", status="p", views=10),
    Post(title="b", status="p", views=30),
    Post(title="c", status="p", views=20),
    Post(title="d", status="d", views=99),
])
print(list(Post.objects.published().popular(2).values_list("title", flat=True)))
```

**追问**:
- 自定义 Manager 和 QuerySet 都要实现吗?——常见做法 QuerySet 承载全部,Manager 继承 `models.Manager.from_queryset(PublishedQuerySet)` 获得同名方法。
- 领域查询和通用过滤怎么划分?——固定业务语义进 QuerySet,参数化的动态条件留给 filter_backends。
