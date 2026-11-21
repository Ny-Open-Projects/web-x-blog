---
title: [Q762] only 与 defer 的字段裁剪与隐形 N+1
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q762 · only 与 defer 的字段裁剪与隐形 N+1

> 难度:★★★★ | 标签:Django ORM, 性能

**问**:only/defer 生成的 SQL 有什么不同?它们最大的坑是什么?

**答**:`only("id","title")` 与 `defer("body")` 都让 SELECT **只取部分列**,省带宽省内存,适合大文本字段列表页。最大的坑:访问**未加载字段会触发一次额外的延迟加载查询**,写在循环里就是隐形 N+1,而且不像关联 N+1 那样显眼。与 select_related 组合时,only 的字段清单必须覆盖关联所需的连接列,否则 join 白做。

```python
# file: code/03_Web后端开发/q762_only_defer.py
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
    body = models.TextField(default="")
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Article)

Article.objects.bulk_create([Article(title=f"t{i}", body="x" * 100) for i in range(3)])

connection.queries_log.clear()
articles = list(Article.objects.only("id", "title"))
print("SQL 里取了 body 吗:", "body" in connection.queries[0]["sql"].split())
articles[0].body  # 访问未加载字段触发第二次查询
print("当前总查询数:", len(connection.queries))
```

**追问**:
- only 之后对模型实例 save 会怎样?——只更新已加载字段,Django 自动处理,但并发覆盖风险仍在。
- 怎么发现这类隐形 N+1?——测试里用 CaptureQueriesContext 断言查询数上限,或接 django-debug-toolbar/nplusone 工具。
