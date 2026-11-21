---
title: [Q747] OpenAPI 文档定制
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q747 · OpenAPI 文档定制

> 难度:★★☆☆ | 标签:FastAPI, OpenAPI

**问**:生成的 Swagger 文档要加服务描述、扩展字段、统一 tags,应该在哪几个层面定制?

**答**:三个层面:实例参数(`title/version/description/openapi_tags`)管全局元信息;路由参数(`tags/summary/response_model/status_code/deprecated`)管单个接口;`app.openapi` 整体覆写可以给 schema 加扩展字段(如 `x-contact`、`x-rate-limit`)或后处理 components。缓存 `app.openapi_schema` 避免每次请求重新生成。文档即契约,定制应服务于前端联调与网关配置的消费场景。

```python
# file: code/03_Web后端开发/q747_openapi_custom.py
try:
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
except ImportError:
    print("pip install fastapi 后再运行")
    raise SystemExit(0)

app = FastAPI(
    title="订单服务",
    version="2.1.0",
    description="内部订单 API",
    openapi_tags=[{"name": "orders", "description": "订单相关"}],
)

@app.get("/orders", tags=["orders"])
def list_orders():
    return []

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(title=app.title, version=app.version,
                         description=app.description, routes=app.routes)
    schema["info"]["x-contact"] = "team-orders@example.com"
    app.openapi_schema = schema
    return app.openapi_schema

app.openapi = custom_openapi
spec = app.openapi()
print(spec["info"]["title"], spec["info"].get("x-contact"))
```

**追问**:
- 怎么从 OpenAPI 文档生成客户端代码?——CI 里用 openapi-generator 或 datamodel-code-generator,把 schema 当唯一事实源。
- operation_id 有什么用?——决定生成代码的函数名,手动指定可避免自动命名在重构后漂移。
