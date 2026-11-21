---
title: [Q787] DRF 节流 throttling 配置与自检
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q787 · DRF 节流 throttling 配置与自检

> 难度:★★★☆ | 标签:DRF, 限流

**问**:DRF 内置节流怎么配?AnonRateThrottle 与 ScopedRateThrottle 的区别?

**答**:节流类决定**维度**:AnonRateThrottle 按匿名 IP,UserRateThrottle 按用户,ScopedRateThrottle 按"视图声明的 throttle_scope"细分场景(登录 5/分、搜索 30/分),自定义类继承 BaseThrottle 重写 allow_request 可做租户维度。速率在 `DEFAULT_THROTTLE_RATES` 配置,超限抛 429 带 Retry-After。实现基于缓存计数(locmem/Redis),多 worker 用共享缓存才是真全局限流;测试时注意清缓存。

```python
# file: code/03_Web后端开发/q787_throttle.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django、djangorestframework:pip install django djangorestframework,原理见正文")
    raise SystemExit(0)

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=["rest_framework"],
    REST_FRAMEWORK={"DEFAULT_THROTTLE_RATES": {"anon": "3/m"}},
    CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}},
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    USE_TZ=True,
)
django.setup()

from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

class Ping(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        return Response({"ok": True})

factory = APIRequestFactory()
view = Ping.as_view()
codes = [view(factory.get("/ping")).status_code for _ in range(4)]
print(codes)  # 第 4 次被 429
```

**追问**:
- 多 worker 部署节流为什么会失效?——默认 LocMemCache 是进程内缓存,每个 worker 各算各的,必须换 Redis 等共享缓存。
- 429 响应里应该有什么?——Retry-After 头给出建议等待时间,响应体说明限流维度,客户端据此退避。
