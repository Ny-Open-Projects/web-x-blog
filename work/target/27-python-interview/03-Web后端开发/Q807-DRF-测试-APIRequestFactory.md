---
title: [Q807] DRF 测试:APIRequestFactory 与 force_authenticate
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q807 · DRF 测试:APIRequestFactory 与 force_authenticate

> 难度:★★★☆ | 标签:DRF, 测试

**问**:DRF 的测试工具和 Django 的 Client 有什么区别?怎么模拟登录用户?

**答**:`APIRequestFactory` 构造的是** DRF Request 管线认可的请求**,直接调 ViewSet/View 可控中间层;`force_authenticate(request, user=u)` 绕过认证器直接注入用户,比伪造 token 稳定。区别于 Django Client:DRF 测试聚焦视图层行为(序列化、权限、节流),不跑完整中间件栈;要端到端时用 Django Client 配 APIClient。断言响应用 `resp.status_code` 与渲染后的 content,权限和节流场景记得检查 403/429 路径。

```python
# file: code/03_Web后端开发/q807_drf_testing.py
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
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIRequestFactory, force_authenticate

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
    permission_classes = [IsAuthenticated]

class FakeUser:
    is_authenticated = True
    username = "alice"

factory = APIRequestFactory()
view = NoteViewSet.as_view({"get": "list"})

req = factory.get("/notes")
force_authenticate(req, user=FakeUser())
r1 = view(req)
r1.render()
print("已认证:", r1.status_code)

r2 = view(factory.get("/notes"))
r2.render()
print("未认证:", r2.status_code)
```

**追问**:
- force_authenticate 和 token 认证测试怎么取舍?——单测视图逻辑用 force,认证链路本身有专门的集成测试覆盖。
- 测试要不要跑节流?——要,清空缓存后循环调用断言 429,防止有人顺手关掉限流。
