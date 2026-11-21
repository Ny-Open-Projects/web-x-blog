---
title: [Q753] SQLAlchemy 异步会话依赖
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q753 · SQLAlchemy 异步会话依赖

> 难度:★★★★ | 标签:FastAPI, SQLAlchemy, 数据库

**问**:FastAPI 接异步 SQLAlchemy,session 的生命周期怎么管理?连接池参数怎么配?

**答**:标准模式:create_async_engine + async_sessionmaker,依赖里 `async with SessionLocal() as session` 用 **yield 依赖**返回,请求结束自动归还。要点:一个请求一个 session;`expire_on_commit=False` 避免提交后属性过期再触发惰性查询;连接池参数(pool_size、max_overflow、pool_recycle、pool_pre_ping)按 DB 的 max_connections 与 worker 数规划,总连接 = worker 数 ×(pool_size + max_overflow)。

```python
# file: code/03_Web后端开发/q753_async_session.py
try:
    from contextlib import asynccontextmanager
    from typing import AsyncIterator
    from sqlalchemy import text
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
except ImportError:
    print("pip install sqlalchemy aiosqlite fastapi httpx 后再运行")
    raise SystemExit(0)
try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

engine = create_async_engine("sqlite+aiosqlite://")  # 生产用 postgresql+asyncpg 并配池参数
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session

app = FastAPI()

@app.get("/ok")
async def ok(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SELECT 1"))
    return {"first": result.scalar()}

with TestClient(app) as c:
    print(c.get("/ok").json())
```

**追问**:
- session 要不要在一个请求里显式 commit?——业务写路径显式 commit,读路径自动只读,禁止把 commit 藏在依赖里造成意外提交。
- yield 依赖和 session 释放的时机?——响应发送后清理阶段归还连接,所以 handler 里不要把 session 传给后台任务。
