---
title: [Q781] ViewSet 的 as_view 与请求分发源码式理解
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q781 · ViewSet 的 as_view 与请求分发源码式理解

> 难度:★★★★ | 标签:DRF, ViewSet

**问**:ViewSet.as_view({"get": "list"}) 这个映射表背后发生了什么?一次请求在 ViewSet 里走哪些步骤?

**答**:Router 或手动 as_view 把 **HTTP 方法映射到 action 名**,生成一个视图闭包;请求进来后 `initialize_request` 把 Django request 包装成 DRF Request,`initial` 依次执行 **版本协商、认证、权限检查、节流**,然后按映射调 action(如 list),list 内部走 `get_queryset → filter_queryset → paginate → get_serializer`,最后 finalize_response 包装。理解这条链就能定位:401 在认证、403 在权限、429 在节流、422 在序列化器校验。

```python
# file: code/03_Web后端开发/q781_viewset_flow.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from django.db import connection, models
from django.test import RequestFactory
from rest_framework import serializers, viewsets

class Note(models.Model):
    text = models.CharField(max_length=64)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Note)
Note.objects.create(text="n1")

class NoteS(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteS

factory = RequestFactory()
view = NoteViewSet.as_view({"get": "list", "post": "create"})
resp = view(factory.get("/notes"))
resp.render()
print(resp.status_code, resp.content.decode()[:40])
```

**追问**:
- get_queryset 什么时候被调用?——每次请求调用(不是启动时),因此可以做按请求的过滤,这也是数据隔离的切入点。
- self.action 在哪一步可用?——initialize_request 时写入,权限类和 get_serializer 常用它区分动作。
