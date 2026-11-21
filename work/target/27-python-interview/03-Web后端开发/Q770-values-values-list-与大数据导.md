---
title: [Q770] values/values_list 与大数据导出
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q770 · values/values_list 与大数据导出

> 难度:★★★☆ | 标签:Django ORM, 性能

**问**:导出百万行数据到 CSV,怎么不把进程内存打爆?

**答**:三个组合拳:`values_list` 只要需要的列(跳过模型实例化开销,省一半内存与 CPU);`iterator(chunk_size)` 分块拉取避免结果集整体驻留;流式写出到响应或文件,而不是攒成大字符串。模板层不要套上 deferring 之外的逻辑;真正海量导出走异步任务生成文件再给下载链接,HTTP 请求里同步导出百万行本身就是反模式。

```python
# file: code/03_Web后端开发/q770_export.py
import csv
import io
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

Article.objects.bulk_create([Article(title=f"t{i}") for i in range(5)])

buf = io.StringIO()
writer = csv.writer(buf)
writer.writerow(["id", "title"])
rows = Article.objects.values_list("id", "title").iterator(chunk_size=100)
for row in rows:
    writer.writerow(row)
print("导出行数:", len(buf.getvalue().strip().splitlines()))
```

**追问**:
- iterator 在 SQLite 和 PostgreSQL 上行为一样吗?——PG 有服务端游标真流式,SQLite 是客户端分块取,语义近似内存表现不同。
- 导出要过滤敏感列怎么办?——values_list 白名单列,或在序列化层统一脱敏,导出路径也要过权限。
