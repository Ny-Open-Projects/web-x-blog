---
title: [Q102] FastAPI 依赖注入基础 Depends
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q102 · FastAPI 依赖注入基础 Depends

> 难度:★★☆ | 标签:FastAPI, 依赖注入

**问**:什么是 FastAPI 的依赖注入系统?相比手动调用函数有什么好处?

**答**:`Depends(func)` 声明依赖后,FastAPI 在进入路由前自动执行依赖函数并把返回值注入参数,依赖本身也可再声明依赖,形成依赖树。好处:复用业务逻辑(认证、分页、DB session)、参数自动校验、便于测试时用 `dependency_overrides` 替换实现。依赖是"声明式"的,与路由解耦,还能在 `dependencies=[...]` 中作为不注入返回值的副作用依赖使用。

```python
# file: code/03_Web后端开发/q102_depends_basic.py
try:
    from fastapi import FastAPI, Depends, HTTPException, Query
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

def pagination(page: int = Query(1, ge=1), size: int = Query(10, le=100)):
    return {'page': page, 'size': size}

def fake_db():
    return {'conn': 'db-conn'}

def get_current_user(token: str = Query(...), db: dict = Depends(fake_db)):
    if token != 'abc':
        raise HTTPException(401, 'invalid token')
    return {'user': 'alice', 'db': db}

@app.get('/items')
def list_items(pager: dict = Depends(pagination), user=Depends(get_current_user)):
    return {'pager': pager, 'user': user['user']}

@app.get('/admin', dependencies=[Depends(get_current_user)])  # 只校验不注入
def admin():
    return {'msg': 'ok'}
```

**追问**:
- 依赖函数可以是 async 的吗?——可以,且与 async 路由共用事件循环;注意不要在 async 依赖里写阻塞调用。
- dependencies=[Depends(...)] 不接收返回值的用法?——副作用依赖(鉴权、限流、审计),返回值丢弃;把「必须先做某事」声明在路由装饰器上。
- 依赖注入和中间件怎么分工?——横切全站流量(日志/限流)用中间件;按路由组合的业务前置(认证、分页、DB)用依赖,粒度更细且可复用。
- 依赖抛异常怎么变成 4xx?——依赖内 raise HTTPException,FastAPI 走正常异常处理返回;依赖失败路由不会执行。
