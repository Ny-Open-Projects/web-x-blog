---
title: [Q788] DRF 版本化机制
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q788 · DRF 版本化机制

> 难度:★★★☆ | 标签:DRF, 版本管理

**问**:DRF 的版本化 scheme 有哪几种?request.version 怎么参与序列化?

**答**:内置 scheme:URLPathVersioning(/v1/ 路径)、AcceptHeaderVersioning(Accept 头参数)、QueryParameterVersioning、HostNameVersioning、NamespaceVersioning。`determine_version` 在 initial 阶段解析出 `request.version`,序列化器据此切换字段(新版多字段、旧版裁剪),配合 reverse 的 version 参数做跨版本链接。选型惯例:C 端 API 用 URLPath(直观、可缓存、日志清晰),内部 API 用 Accept 头。ALLOWED_VERSIONS 兜住非法版本返回 404。

```python
# file: code/03_Web后端开发/q788_versioning.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    REST_FRAMEWORK={
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.HeaderVersioning",
        "DEFAULT_VERSION": "v1",
        "ALLOWED_VERSIONS": ["v1", "v2"],
    },
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class Echo(APIView):
    def get(self, request):
        return Response({"version": request.version})

factory = APIRequestFactory()
r1 = Echo.as_view()(factory.get("/echo", HTTP_ACCEPT="application/json; version=v2"))
print(r1.data)
r2 = Echo.as_view()(factory.get("/echo"))
print(r2.data)
```

**追问**:
- 版本化对缓存的影响?——URL 路径版本天然参与缓存键,Accept 头版本要确保代理层 Vary: Accept,否则缓存串版本。
- 版本之间共享代码怎么组织?——序列化器按版本目录分,业务逻辑共用 service,版本层只做形状差异。
