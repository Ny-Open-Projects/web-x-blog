---
title: [Q6024] 下游 HTTP 依赖的测试替身：MockTransport 与 respx
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6024 · 下游 HTTP 依赖的测试替身：MockTransport 与 respx

> 难度:★★★☆ | 标签:httpx, 测试替身, 重试

**问**：单测里怎么让"调用下游 HTTP API"的业务代码不碰真实网络？httpx 的 `MockTransport` 注入点在哪，和 respx 的路由式 mock 怎么分工？替身怎么模拟"前两次 503 第三次成功"来验证重试逻辑？与链路级 mock server（Q1878）的分工边界是什么？

**答**：三层替身策略：1) **传输层替身**——httpx 允许把 `AsyncClient(transport=MockTransport(handler))` 注入，handler 收到 `httpx.Request` 返回 `httpx.Response`，**客户端代码零改动**（仍走真实 Client 栈：超时、重试、连接池逻辑都在被测路径上），适合按"依赖"隔离的集成测试；2) **路由式 mock（respx 基线 0.21+）**——`respx.mock` 用路由匹配 URL/method/参数，按 pattern 精细返回（`route.return_value(503)` / 依调用次数变化），适合契约性断言（"必须发出这个头/这个 body"）；3) **链路级 mock server**（独立进程真端口，Q1878）——验证超时/连接复用/TLS 等真网络行为。设计要点：替身要**进依赖注入面**（客户端实例可替换，Q744 的 lifespan 共享 client），而不是让业务代码里散落 if-testing；验证重试别断言"调用了 retry 装饰器"，要断言**结果与调用次数**（行为不测实现）。

```python
# file: code/03_Web后端开发/q6024_http_test_double.py
import asyncio

async def fetch_with_retry(client, url, retries=2):
    """被测业务代码: 下游偶发 503 时重试"""
    for attempt in range(1, retries + 2):
        try:
            r = await client.get(url)
            r.raise_for_status()
            return r.json(), attempt
        except Exception:
            if attempt > retries:
                raise
            await asyncio.sleep(0.001)

try:
    import httpx
    HAVE_HTTPX = True
except ImportError:
    HAVE_HTTPX = False

async def main():
    if HAVE_HTTPX:
        calls = {"n": 0}
        def handler(request: "httpx.Request") -> "httpx.Response":
            calls["n"] += 1
            if calls["n"] < 3:                      # 前两次 503
                return httpx.Response(503)
            return httpx.Response(200, json={"ok": True})
        transport = httpx.MockTransport(handler)     # 注入点: 替换传输层
        async with httpx.AsyncClient(transport=transport) as client:
            data, used = await fetch_with_retry(client, "https://downstream/api")
        print("MockTransport:", data, "| 实际尝试次数:", calls["n"], "| 业务重试后成功于第", used, "次")
    else:
        # 降级: 无 httpx(基线 0.27+/respx 0.21+)时用假客户端演示同一契约
        class FakeClient:
            def __init__(self):
                self.n = 0
            async def get(self, url):
                self.n += 1
                if self.n < 3:
                    raise RuntimeError("503")
                return _FakeResp({"ok": True})
        class _FakeResp:
            def __init__(self, payload): self.payload = payload
            def raise_for_status(self): pass
            def json(self): return self.payload
        c = FakeClient()
        data, used = await fetch_with_retry(c, "https://downstream/api")
        print("降级假客户端:", data, "| 尝试次数:", c.n, "| 重试后成功于第", used, "次")

asyncio.run(main())
```

**追问**：1) 为什么不 monkeypatch `requests.post`？——patch 停在"函数级"，客户端超时/连接池/异常类型都不在被测路径上，测出来的是 mock 的行为不是你的行为；传输层替身保留协议栈语义。2) 录制回放（respx 的 replay/`vcr` 思路）适合什么场景？——契约快照回归：真实调用一次存 fixture，之后回放校验；要注意脱敏（token/PII）与 fixture 过期（随下游 API 演进重新录制，Q2196 相邻）。3) 替身会掩盖"下游真的改了契约"吗？——会，所以集成环境保留一条真调用冒烟（契约测试 Q1624/Q851 兜底），替身只负责单测确定性。

## 背诵要点
1. 注入传输层替身（MockTransport）：客户端零改动，超时/重试栈全在被测路径上。
2. respx 做路由式断言（URL/头/次数），链路级 mock server 验证真网络行为，三层分工。
3. 替身从依赖注入面进（client 实例可替换）；断言行为（结果+次数）不断言实现。

## 复盘追问
1. 重试逻辑用替身测过后线上仍打爆下游（退避没生效），单测漏了什么？（提示：替身模拟的是响应不模拟时间——退避要用假时钟（Q2677）或注入 sleep，超时/抖动场景补集成冒烟）
2. fixture 录制里带了真实 token 泄漏进仓库，录制方案要补什么？（提示：录制后置脱敏管道 + 仓库密钥扫描，替身层存的是结构不是凭证）
