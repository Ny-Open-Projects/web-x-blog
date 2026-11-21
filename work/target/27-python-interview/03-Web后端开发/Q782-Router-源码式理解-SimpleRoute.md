---
title: [Q782] Router 源码式理解:SimpleRouter 生成了什么
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q782 · Router 源码式理解:SimpleRouter 生成了什么

> 难度:★★★☆ | 标签:DRF, Router

**问**:router.register 之后 urlpatterns 里到底多了什么?list 与 retrieve 的 URL 怎么来的?

**答**:SimpleRouter 内部维护 routes 模板:标准动作生成 `{prefix}`(list/create)与 `{prefix}/{lookup}`(retrieve/update/destroy),额外动作由 `@action(detail=...)` 追加;每条 URL 配上 name(如 `note-list`)供 reverse。DefaultRouter 在此基础上加 API root 视图与 format 后缀。理解模板就能解释:lookup_value_regex 控制主键匹配形态、自定义 action 的 url_path/name 如何反向解析。

```python
# file: code/03_Web后端开发/q782_router_urls.py
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

from rest_framework import routers, serializers, viewsets

class NoteS(serializers.Serializer):
    text = serializers.CharField()

class NoteViewSet(viewsets.ModelViewSet):
    queryset = []
    serializer_class = NoteS

    from rest_framework.decorators import action

    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        pass

router = routers.SimpleRouter()
router.register(r"notes", NoteViewSet)
for url in router.urls:
    print(str(url.pattern), url.name)
```

**追问**:
- detail=False 的 action URL 长什么样?——挂在集合上,如 /notes/recent/;detail=True 挂在实例上 /notes/{pk}/publish/。
- 两个 ViewSet 注册同名前缀会怎样?——URL name 冲突,reverse 失败,要用不同的 basename。
