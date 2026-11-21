---
title: [Q104] yield 依赖与资源清理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q104 · yield 依赖与资源清理

> 难度:★★★ | 标签:FastAPI, 依赖注入

**问**:`yield` 形式的依赖是怎么执行的?异常会发生在哪一段?

**答**:`yield` 依赖把函数分成两段:`yield` 之前的代码在路由处理前执行并注入返回值,之后的代码在响应发送后执行,天然适合管理数据库 session、临时文件等需要清理的资源——即使路由抛异常也会执行清理部分。路由或子依赖抛出的异常会传播到 yield 之后,可在那里用 `try/except` 感知失败并回滚,但要注意此时不能再修改已发出的响应。

```python
# file: code/03_Web后端开发/q104_yield_dependency.py
try:
    from fastapi import FastAPI, Depends, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
logs: list[str] = []

def db_session():
    logs.append('session open')
    session = {'in_tx': True}
    try:
        yield session                     # 注入给路由
        session['in_tx'] = False          # 正常结束:提交
        logs.append('commit')
    except Exception:
        logs.append('rollback')           # 路由抛异常:回滚
        raise
    finally:
        logs.append('session close')      # 无论成败都清理

@app.get('/ok')
def ok(session: dict = Depends(db_session)):
    return {'data': 'ok'}

@app.get('/boom')
def boom(session: dict = Depends(db_session)):
    raise HTTPException(400, 'bad request')
# 连续请求 /ok、/boom 后 logs 依次为 open->commit->close / open->rollback->close
```

**追问**:
- yield 依赖里抛异常会怎样?——路由抛的异常先穿过依赖的 yield 处(可捕获做回滚),未捕获则继续向异常处理器传播;此时响应未发出,仍可改变结果。
- yield 依赖和 BackgroundTasks 的清理顺序?——清理段在响应发送后、后台任务执行前完成;依赖清理里不要假设响应已成功送达。
- 一个请求多个 yield 依赖的退出顺序?——与进入顺序相反(LIFO),类似栈;共享资源的依赖要按「后借先还」设计。
