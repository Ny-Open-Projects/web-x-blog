---
title: "[Q6095] Starlette TestClient 从 requests 到 httpx 的迁移演进"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6095 · TestClient 从 requests 到 httpx 的迁移演进

难度：P6 | 标签：版本演进 | TestClient | httpx

**问**：升级 Starlette 后 CI 里 TestClient 相关用例大量报错。为什么 TestClient 的底层从 requests 换成了 httpx？迁移中常见的破坏点有哪些？测试"客户端断开"这类新场景 httpx 又带来了什么能力？

**答**：
结论：Starlette 0.21 起 `TestClient` 基于 `httpx.Client` 重建（此前是 requests）。动因：requests 不支持 ASGI 传输层的同步封装改造与流式 API 的统一，httpx 的 `transport=ASGITransport` 架构天然适配"进程内调用应用"，且 API 设计（`httpx.Client`/`AsyncClient` 对称）支持同步与异步测试统一。迁移破坏点：① `client.post(..., json=)` 行为基本一致，但 `data=` 与 `params=` 的编码细节、响应对象的属性差异（`resp.json()` 相同、`resp.text` 相同，`resp.cookies` 类型变化）；② 旧的 `requests.exceptions` 异常不再出现，换成 `httpx` 异常；③ portal/context 语义变化——旧版 `TestClient` 支持嵌套 with 模拟 lifespan，新版同样支持但内部是 anyio portal；④ `requests` 的 `session` 属性移除。
取舍：httpx 化带来真正的收益是**异步测试与流式断开**：`AsyncClient(transport=ASGITransport(app))` 无需真实端口即可测应用，`client.stream()` 可模拟"收到一半断开"，覆盖取消路径。
实战：迁移清单按报错分三类处理（导入异常、属性改名、lifespan 用法）；CI 加 httpx 版本基线（Starlette 0.21+ / httpx 0.22+），并在 conftest 里封装统一的 `make_client()` 隔离底层差异。

```python
# 基线：Starlette >= 0.21 / httpx >= 0.22；未安装时降级退出并打印装法
try:
    from starlette.applications import Starlette
    from starlette.responses import JSONResponse
    from starlette.routing import Route
    from starlette.testclient import TestClient
    import httpx
except ImportError as e:
    print(f"缺依赖({e})：pip install 'starlette>=0.21' 'httpx>=0.22' 后重跑")
    import sys; sys.exit(0)

import json, threading, time

async def state(request):
    return JSONResponse({"ok": True, "method": request.method})

async def echo(request):
    body = await request.json()
    return JSONResponse({"got": body})

async def slow(request):
    await asyncio.sleep(1.0)           # 若被取消则不会返回
    return JSONResponse({"done": True})

app = Starlette(routes=[
    Route("/state", state, methods=["GET"]),
    Route("/echo", echo, methods=["POST"]),
    Route("/slow", slow, methods=["GET"]),
])

# 同步 TestClient（httpx 底层，进程内 ASGI 传输）
with TestClient(app) as client:        # with 进入 = lifespan 启动，退出 = 关闭
    r = client.get("/state")
    print("同步:", r.status_code, r.json())
    r = client.post("/echo", json={"x": 1})
    print("POST:", r.json())
    # httpx 异常体系：不再是 requests.exceptions
    print("异常基类:", httpx.HTTPError.__mro__[1].__name__)

# 异步 Client：无需端口、可测取消/断开路径
import asyncio
from httpx import AsyncClient, ASGITransport

async def async_tests():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.get("/state")
        print("异步:", r.status_code)

        # 断开模拟：客户端超时取消 → 应用侧协程被取消（ASGITransport 不缓冲）
        t0 = time.perf_counter()
        try:
            await asyncio.wait_for(ac.get("/slow"), timeout=0.1)
        except asyncio.TimeoutError:
            print(f"客户端 0.1s 放弃（服务端 1s 任务被隔离，耗时 {time.perf_counter()-t0:.2f}s）")

if __name__ == "__main__":
    async_tests_run = asyncio.new_event_loop()
    async_tests_run.run_until_complete(async_tests())

    # 迁移破坏点清单（陈述式自检）
    checks = {
        "requests 异常类消失": "except httpx.HTTPError",
        "resp.cookies 类型变化": "httpx.Cookies",
        "lifespan 用 with TestClient(app)": "不再需要 portal 细节",
        "异步测试用 AsyncClient+ASGITransport": "免端口",
    }
    for k, v in checks.items():
        print(f"迁移要点 - {k}: {v}")
```

**追问 1**：ASGITransport 与"真实端口起服务再测"的差别？
- 追问 2 层：ASGITransport 在进程内直接调用应用，没有网络栈（超时/重传/真实断开都不存在），快且稳但覆盖不了网络层行为；E2E 用 uvicorn+真实客户端补。
- 追问 3 层：取消语义也不同——ASGITransport 下客户端放弃会把应用任务留在 loop 里跑完（除非应用自己响应 disconnect），真实 uvicorn 会收到 http.disconnect；断开相关断言要谨慎。

**追问 2**：httpx 化对 mock 下游 HTTP 的影响？
- 追问 2 层：应用内部若也用 httpx，可用 `MockTransport` 整链路进程内化；requests 时代的 monkeypatch `requests.get` 手法要改成注入 transport。
- 追问 3 层：统一 transport 注入面让"测试替身"从 patch 变成依赖注入，这才是 httpx 化最大红利。

## 背诵要点
1. Starlette 0.21+ TestClient 底层 requests→httpx：异常类、cookie 类型、lifespan 用法是三大破坏点。
2. 新能力：AsyncClient + ASGITransport 免端口异步测试、stream 模拟流式，取消路径可测。
3. ASGITransport 没有真实网络栈，断开/超时语义与生产不同，E2E 需补真实服务测试。

## 复盘追问
1. 为什么迁移选在 Starlette 0.21 而不是更早？——等 httpx 的 transport 抽象成熟，且要同步迁移内部测试生态。
2. 升级后"测试全绿但生产断开行为异常"怎么解释？——ASGITransport 不发 http.disconnect，断开路径只有真网络测试覆盖。
