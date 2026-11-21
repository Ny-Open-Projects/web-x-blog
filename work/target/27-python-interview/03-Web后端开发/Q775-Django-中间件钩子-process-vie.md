---
title: [Q775] Django 中间件钩子:process_view 与 process_exception
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q775 · Django 中间件钩子:process_view 与 process_exception

> 难度:★★★★ | 标签:Django, 中间件

**问**:函数式中间件之外,Django 中间件类还有哪些钩子?各自的触发时机与返回值语义?

**答**:完整钩子族:`__init__`(启动时一次)、`__call__`(每请求包裹前后)、`process_view`(URL 解析后、视图执行前,返回 None 继续、返回 Response 则跳过视图与其他 process_view)、`process_exception`(视图抛异常时,返回 None 让异常继续上抛、返回 Response 则吞掉异常)、`process_template_response`(视图返回带 render 方法的对象时)。顺序敏感点:`__call__` 前半按 MIDDLEWARE 顺序、后半逆序;process_view 全部正序,process_exception 逆序。

```python
# file: code/03_Web后端开发/q775_django_middleware.py
try:
    import django
    from django.conf import settings
except ImportError:
    print("该题演示需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

def request_log(get_response):
    def middleware(request):
        request.META["X-Tenant"] = request.META.get("HTTP_X_TENANT", "public")
        response = get_response(request)
        response["X-Process-Flag"] = "ok"
        return response
    return middleware

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=["__main__.request_log", "django.middleware.common.CommonMiddleware"],
    ROOT_URLCONF="__main__",
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=[],
    USE_TZ=True,
)
django.setup()

from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse(f"tenant={request.META['X-Tenant']}")

urlpatterns = [path("", index)]

from django.test import Client

c = Client()
r = c.get("/", HTTP_X_TENANT="acme")
print(r.status_code, r.content.decode(), r["X-Process-Flag"])
```

**追问**:
- process_view 返回 Response 会发生什么?——视图与后续中间件的 process_view 被跳过,直接进入响应阶段,可用于短路的鉴权钩子。
- 钩子注册顺序和 MIDDLEWARE 列表的关系?——调用前半正序、后半逆序;process_exception 从最内层向外找第一个肯处理的。
