---
title: [Q127] Django 中间件栈与自定义中间件
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q127 · Django 中间件栈与自定义中间件

> 难度:★★★ | 标签:Django, 中间件

**问**:Django MIDDLEWARE 列表的顺序有什么影响?如何写一个自定义中间件?

**答**:`MIDDLEWARE` 是有序列表,第一个在最外层:请求按列表正序穿过各层的处理(如 SecurityMiddleware 先做安全检查),响应按逆序返回;process_view/异常处理/模板响应各有插入点。自定义中间件用函数式(`def mw(get_response)`)或类式(`__init__/__call__`),典型用途:Request-ID、租户识别、性能埋点。内置栈包含 Security、Session、Common、Csrf、Auth 等,顺序有官方约定,勿随意打乱。

```python
# file: code/03_Web后端开发/q127_django_middleware.py
# myapp/middleware.py (Django 模块级代码)
import time
import uuid

def request_id_middleware(get_response):
    def middleware(request):
        rid = request.headers.get('X-Request-ID', str(uuid.uuid4())[:8])
        request.rid = rid
        start = time.perf_counter()
        response = get_response(request)            # 内层处理
        response['X-Request-ID'] = rid
        response['X-Cost-Ms'] = str(round((time.perf_counter() - start) * 1000, 2))
        return response
    return middleware

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.start = time.perf_counter()
        response = self.get_response(request)
        print(f'{request.path} took {time.perf_counter() - self.start:.3f}s')
        return response

# settings.py 注册(列表第一项最外层):
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'myapp.middleware.request_id_middleware',
#     'myapp.middleware.TimingMiddleware',
#     ... 其余内置中间件 ...
# ]
```

**追问**:
- 自定义中间件放 MIDDLEWARE 哪个位置?——Request-ID/日志放最前(覆盖一切);依赖认证的中间件必须在 AuthenticationMiddleware 之后。
- 函数式和类式中间件怎么选?——简单无状态用函数式;需要构造参数与实例状态(如限流器引用)用类式 `__init__(get_response)`。
- 中间件抛异常会怎样?——向上传给外层中间件与异常处理器;中间件内部要捕获自己关心的异常,别让清理逻辑漏执行。

```mermaid
flowchart LR
    REQ[HTTP 请求] --> M1[SecurityMiddleware]
    M1 --> M2[SessionMiddleware]
    M2 --> M3[CsrfViewMiddleware]
    M3 --> M4[AuthMiddleware]
    M4 --> V[URL 路由到 View]
    V --> M5[AuthMiddleware 返回链]
    M5 --> M6[CsrfViewMiddleware]
    M6 --> M7[SessionMiddleware]
    M7 --> M8[SecurityMiddleware]
    M8 --> RES[HTTP 响应]
```
