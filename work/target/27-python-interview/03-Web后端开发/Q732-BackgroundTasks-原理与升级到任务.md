---
title: [Q732] BackgroundTasks 原理与升级到任务队列的边界
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q732 · BackgroundTasks 原理与升级到任务队列的边界

> 难度:★★★☆ | 标签:FastAPI, 后台任务

**问**:BackgroundTasks 的任务什么时候执行?什么时候必须换 Celery/Arq 这类队列?

**答**:任务注册到响应对象的 background 列表,**响应发送完成后在同一进程内执行**,失败无重试、不持久化、无并发控制。适合毫秒级副作用:发确认邮件、清缓存、记埋点。一旦出现以下信号就该升级队列:任务**必须不丢**(要持久化)、**要重试**、**耗时长**(几十秒以上)、**要多机扩容**、**要延时/定时**。两者可并存:轻任务 bg,重任务在依赖里把消息投给队列。

```python
# file: code/03_Web后端开发/q732_bg_boundary.py
try:
    from fastapi import BackgroundTasks, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

done = []
app = FastAPI()

def send_email(to: str):
    done.append(f"mail->{to}")

@app.post("/signup")
def signup(email: str, bg: BackgroundTasks):
    bg.add_task(send_email, to=email)
    return {"queued": True}

client = TestClient(app)
print(client.post("/signup?email=a@b.c").json())
print("任务已执行:", done)  # TestClient 请求完成后后台任务已同步跑完
```

**追问**:
- bg 任务抛异常会怎样?——异常进服务器日志,客户端无感知且任务丢失,这正是需要队列的信号。
- bg 任务能访问请求上下文吗?——不能直接注入 Request,要在注册时把需要的值作为参数显式传入。
