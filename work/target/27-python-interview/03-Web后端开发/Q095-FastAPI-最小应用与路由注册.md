---
title: [Q095] FastAPI 最小应用与路由注册
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q095 · FastAPI 最小应用与路由注册

> 难度:★☆☆ | 标签:FastAPI, 路由

**问**:写一个最小 FastAPI 应用,并说明路由有哪几种注册方式。

**答**:FastAPI 基于 Starlette(异步 web 层)+ Pydantic(数据校验)构建,原生支持类型标注驱动的参数校验和 OpenAPI 文档。路由注册方式有三种:装饰器直接挂在 app 上、`APIRouter` 按模块拆分后 `include_router` 汇总、以及 `add_api_route` 编程式注册。工程项目一般按资源拆成多个 router 文件。

```python
# file: code/03_Web后端开发/q095_fastapi_hello.py
try:
    from fastapi import FastAPI, APIRouter
    import uvicorn
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI(title='demo')
router = APIRouter(prefix='/v1', tags=['demo'])

@app.get('/')                        # 方式一:装饰器直接注册
def root():
    return {'msg': 'hello fastapi'}

@router.get('/items/{item_id}')      # 方式二:APIRouter,前缀 /v1
def read_item(item_id: int):
    return {'item_id': item_id}

app.include_router(router)           # 汇总 router

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)  # 文档: /docs
```

**追问**:
- APIRouter 拆分的好处?——按资源域组织路由与依赖前缀、tags 归组文档、便于按模块授权与测试;单一 app.py 在大项目里必然失控。
- 路由注册顺序有影响吗?——有,`/items/latest` 与 `/items/{item_id}` 冲突时先注册者命中;固定路径必须在前。
- OpenAPI 文档能关吗?——生产可设 `docs_url=None/redoc_url=None/openapi_url=None` 收敛暴露面,或挂在内网域名。
