---
title: [Q786] 对象级权限与 get_object
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q786 · 对象级权限与 get_object

> 难度:★★★★ | 标签:DRF, 权限

**问**:用户 A 能不能访问用户 B 的订单,这个判断应该在哪做?has_object_permission 何时触发?

**答**:对象级授权两个挂点:重写 `get_object`(取数后校验归属,失败抛 PermissionDenied),或用 DRF 的 `has_object_permission`——但它**只在 retrieve/update/destroy 这类已取对象的动作触发**,list 不会调用,所以列表范围必须在 get_queryset 过滤,否则"列表泄数据、详情才拦截"。铁律:**数据隔离在 get_queryset,对象校验在取数点**,两层都要;只靠前端隐藏入口不叫权限。

```python
# file: code/03_Web后端开发/q786_obj_permission.py
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
from rest_framework.exceptions import PermissionDenied
from rest_framework.test import APIRequestFactory

class Note(models.Model):
    text = models.CharField(max_length=64)
    owner = models.CharField(max_length=32)
    class Meta:
        app_label = "demo"

with connection.schema_editor() as se:
    se.create_model(Note)

Note.objects.create(text="mine", owner="alice")
Note.objects.create(text="theirs", owner="bob")

class NoteS(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["text", "owner"]

class NoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteS

    def get_object(self):
        obj = super().get_object()
        if obj.owner != self.request.headers.get("X-User", ""):
            raise PermissionDenied("只能访问自己的笔记")
        return obj

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.headers.get("X-User", "")
        if user:
            qs = qs.filter(owner=user)   # 列表层的数据隔离
        return qs

factory = APIRequestFactory()
view = NoteViewSet.as_view({"get": "retrieve"})
r1 = view(factory.get("/notes/2", HTTP_X_USER="alice"), pk=2)
r1.render()
print("取他人笔记:", r1.status_code)
r2 = view(factory.get("/notes/1", HTTP_X_USER="alice"), pk=1)
r2.render()
print("取自己笔记:", r2.status_code)
```

**追问**:
- has_object_permission 为什么覆盖不到 list?——list 没有取单个对象的过程,DRF 只对 get_object 路径调用对象权限。
- 归属判断写在 serializer 行不行?——不行,序列化器管数据形状,授权属于访问控制,混在一起无法统一审计。
