---
title: [Q789] Renderer 与内容协商
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q789 · Renderer 与内容协商

> 难度:★★★☆ | 标签:DRF, 内容协商

**问**:怎么让同一接口根据 Accept 返回裸 JSON 或带包络的 JSON?

**答**:DRF 的 `renderer_classes` 决定响应形态,内容协商按 Accept 头选择 renderer。自定义 renderer 继承 JSONRenderer 重写 render,把 data 包进统一结构;BrowsableAPIRenderer 是调试用的 HTML 形态。工程建议:**对机器客户端关掉 Browsable**(减少 XSS 面与性能开销),包络渲染器只挂在需要兼容旧前端的版本上,新版本直接裸 JSON 加标准状态码。

```python
# file: code/03_Web后端开发/q789_renderer.py
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

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class EnvelopeRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return super().render(
            {"code": 0, "data": data}, accepted_media_type, renderer_context
        )

class Ping(APIView):
    renderer_classes = [EnvelopeRenderer]

    def get(self, request):
        return Response({"hello": True})

resp = Ping.as_view()(APIRequestFactory().get("/ping"))
resp.render()
print(resp.content.decode())
```

**追问**:
- 404 也走 renderer 吗?——DRF 处理的异常响应走 renderer,统一包络要连异常处理器一起改。
- 状态码和包络 code 不一致会被前端挑战吗?——会,所以包络设计要文档化,并保证 code 与状态码的映射表唯一。
