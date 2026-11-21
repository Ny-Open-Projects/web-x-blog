---
title: [Q755] 202 Accepted 异步任务接口
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q755 · 202 Accepted 异步任务接口

> 难度:★★★☆ | 标签:FastAPI, 异步模式

**问**:导出报表要跑两分钟,接口怎么设计?同步等待行吗?

**答**:同步等待会**占住 worker 两分钟**,是容量杀手。标准模式:POST 创建任务立即返回 **202 Accepted** + 任务资源 ID(Location 头指向状态地址);GET 轮询或 SSE 推进度;任务状态机 queued→running→done/failed,终态保留一段时间后清理。前端拿 done 后的下载地址取结果。配套要点:任务幂等键防重复提交、按用户限流提交频率、任务结果设 TTL。

```python
# file: code/03_Web后端开发/q755_202_pattern.py
import uuid
try:
    from fastapi import FastAPI, HTTPException
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
jobs: dict[str, dict] = {}

@app.post("/exports", status_code=202)
def create_export():
    job_id = uuid.uuid4().hex
    jobs[job_id] = {"status": "running", "progress": 40}  # 模拟异步推进
    return {"job_id": job_id, "status": "running"}

@app.get("/exports/{job_id}")
def get_export(job_id: str):
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(404)
    return job

client = TestClient(app)
r = client.post("/exports")
print(r.status_code, r.json())
print(client.get(f"/exports/{r.json()['job_id']}").json())
print(client.get("/exports/nope").status_code)
```

**追问**:
- 202 响应该带什么头?——Location 指向任务状态资源,便于通用客户端跟进。
- 轮询间隔怎么定?——前端指数退避(如 1s 起步翻倍封顶),或改用 SSE/WebSocket 由服务端推完成事件。
