---
title: [Q814] 健康检查:liveness 与 readiness 分离
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q814 · 健康检查:liveness 与 readiness 分离

> 难度:★★★☆ | 标签:健康检查, 可用性

**问**:健康检查接口应该查数据库吗?liveness 和 readiness 的语义差别?

**答**:**liveness(/healthz)只回答"进程还活着"**,失败触发重启,所以绝不能依赖外部服务——DB 抖一下把所有实例重启就是雪崩放大器。**readiness(/readyz)回答"能否接流量"**,失败只摘流不重启,可以检查关键依赖(数据库连接、缓存、配置加载)。两者分开后,依赖故障的爆炸半径是"暂时摘流"而不是"全量重启"。健康检查还要注意:不打访问日志、不计入限流、返回体要小。

```python
# file: code/03_Web后端开发/q814_health_endpoints.py
try:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

db_ok = True
app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"ok": True}                       # 进程活着就 200, 不查依赖

@app.get("/readyz")
def readyz():
    if not db_ok:                             # 依赖不可用就摘流
        return JSONResponse(status_code=503, content={"ok": False})
    return {"ok": True}

client = TestClient(app)
print("healthz:", client.get("/healthz").status_code)
print("readyz(依赖正常):", client.get("/readyz").status_code)
db_ok = False
print("readyz(依赖故障):", client.get("/readyz").status_code)
```

**追问**:
- 启动很慢的服务还需要什么探针?——startupProbe 给足启动时间,启动完成前不跑 liveness,避免被误杀。
- 健康检查挂了但业务正常是什么问题?——通常是探针实现引入了新依赖(如查了慢表),探针要最简、超时要短。
