---
title: [Q800] 行级多租户实现:中间件 + Manager 过滤
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q800 · 行级多租户实现:中间件 + Manager 过滤

> 难度:★★★★ | 标签:Django, 多租户

**问**:行级租户在 Django 里怎么落地,才能保证"开发者不可能忘加过滤"?

**答**:三件套:**中间件/认证层**把租户放进 contextvar;**自定义 Manager** 的 get_queryset 恒定追加 `filter(tenant=当前租户)`,模型默认用它;`all_objects` 作为显式逃生口供后台任务与运维脚本用。配合:所有含租户表建 (tenant, ...) 复合索引;跨租户访问(客服)走显式授权接口并审计;迁移与回填脚本用 all_objects。原则:**默认安全,越权显式**。

```python
# file: code/03_Web后端开发/q800_tenant_manager.py
import contextvars
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

CURRENT_TENANT: contextvars.ContextVar = contextvars.ContextVar("tenant", default="public")

class TenantManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tenant=CURRENT_TENANT.get())

class Invoice(models.Model):
    tenant = models.CharField(max_length=32)
    amount = models.IntegerField(default=0)
    objects = TenantManager()      # 默认隔离
    all_objects = models.Manager() # 显式逃生口
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Invoice)

with connection.schema_editor() as se:
    pass
Invoice.all_objects.bulk_create([
    Invoice(tenant="acme", amount=100),
    Invoice(tenant="globex", amount=200),
])

token = CURRENT_TENANT.set("acme")
print("租户内可见:", Invoice.objects.count())
CURRENT_TENANT.reset(token)
print("逃生口全量:", Invoice.all_objects.count())
```

**追问**:
- contextvar 在异步视图下可靠吗?——可靠,ASGI 每请求独立 context,Django 3.x 起支持;同步 WSGI 用线程本地等价。
- 外键关联到租户表要注意什么?——关联查询走隔离 manager 天然带过滤,但 raw SQL 和 values 聚合要人工复查租户条件。
