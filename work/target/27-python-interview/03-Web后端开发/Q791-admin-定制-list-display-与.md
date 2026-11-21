---
title: [Q791] admin 定制:list_display 与 action
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q791 · admin 定制:list_display 与 action

> 难度:★★☆☆ | 标签:Django, admin

**问**:admin 列表要显示计算列、加搜索、批量操作,怎么定制?

**答**:ModelAdmin 三件套:`list_display` 自定义列(模型方法或 ModelAdmin 方法,注意 list_select_related 防 N+1)、`search_fields`/`list_filter` 检索、`actions` 批量动作(标准签名 `(modeladmin, request, queryset)`,配 @admin.action 装饰器给描述与权限)。进阶:inlines 内联编辑关联对象、readonly_fields 保护关键字段、自定义 AdminSite 做多 admin 站点。admin 是内部工具,但**权限与审计同样不能少**,敏感数据的导出动作要走日志。

```python
# file: code/03_Web后端开发/q791_admin_custom.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[
        "django.contrib.admin", "django.contrib.auth",
        "django.contrib.contenttypes", "django.contrib.sessions",
        "django.contrib.messages",
    ],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], "APP_DIRS": True, "OPTIONS": {},
    }],
    USE_TZ=True,
)
django.setup()

from django.contrib import admin
from django.db import connection, models

class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Book)
Book.objects.create(title="Python cookbook", price=99)

site = admin.AdminSite(name="demo")

@admin.action(description="全部设为免费")
def make_free(modeladmin, request, queryset):
    queryset.update(price=0)

@admin.register(Book, site=site)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]
    search_fields = ["title"]
    actions = [make_free]

ma = BookAdmin(Book, site)
make_free(ma, None, Book.objects.filter(title="Python cookbook"))
print("action 生效:", Book.objects.get().price == 0)
print("列表列:", BookAdmin.list_display)
```

**追问**:
- list_display 自定义方法怎么加排序?——方法上设 admin.display(description=..., ordering="price") 指定可排序依据。
- admin 里怎么防误操作?——关键动作用 confirm 表单、has_delete_permission 关掉删除、重要模型 readonly。
