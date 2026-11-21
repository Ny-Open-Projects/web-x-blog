---
title: [Q785] DRF 统一异常响应
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q785 · DRF 统一异常响应

> 难度:★★★☆ | 标签:DRF, 异常处理

**问**:怎么让 DRF 的 404、403、校验错误都返回同一种 JSON 结构?

**答**:自定义 `EXCEPTION_HANDLER`:先调 DRF 默认处理器拿到(响应或 None),None 表示未捕获异常交给 Django 500;有响应时把 `resp.data` 重包成统一结构并保留状态码。业务异常可自定义 APIException 子类携带错误码。注意点:未认证场景 401 要保留 WWW-Authenticate 语义;日志在 handler 里记 traceback;**不要**在 handler 里吞异常返回 200。

```python
# file: code/03_Web后端开发/q785_exception_handler.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

def envelope_handler(exc, context):
    from rest_framework.views import exception_handler as default_handler
    resp = default_handler(exc, context)
    if resp is None:
        return resp
    detail = resp.data.get("detail") if isinstance(resp.data, dict) else None
    resp.data = {
        "code": resp.status_code,
        "message": str(detail) if detail else "request failed",
        "errors": None if detail else resp.data,
    }
    return resp

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    REST_FRAMEWORK={"EXCEPTION_HANDLER": "__main__.envelope_handler"},
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.exceptions import NotFound
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class Boom(APIView):
    def get(self, request):
        raise NotFound("资源不存在")

resp = Boom.as_view()(APIRequestFactory().get("/boom"))
resp.render()
print(resp.status_code, resp.content.decode())
```

**追问**:
- default_handler 返回 None 的情况?——非 APIException/Http404/PermissionDenied 的未知异常,应记录日志后交给 Django 返回 500。
- 自定义业务异常类怎么设计?——继承 APIException,带 status_code 与 default_detail,handler 里原样透传 detail。
