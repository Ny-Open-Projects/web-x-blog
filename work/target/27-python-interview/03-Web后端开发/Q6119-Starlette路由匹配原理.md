---
title: [Q6119] Starlette 路由匹配原理
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6119 · Starlette/FastAPI 路由匹配原理与注册顺序语义

> 难度:★★★★☆ | 标签:原理深挖, 路由, Starlette

**问**:`/users/{id}` 与 `/users/me` 同时注册，为什么 `me` 必须写在前面？`{id:int}` 转换器怎么实现的，405 与 404 的判定顺序是什么？FastAPI 在 Starlette 匹配之上又加了什么（依赖解析时机、响应模型）？

**答**:结论：Starlette 路由匹配是**按注册顺序的线性遍历 + 每条路由编译成正则**：`Route` 构造时把路径模板（如 `/users/{id:int}`）经 `compile_path` 转成 `^/users/(?P<id>[0-9]+)$` 正则，`Router.app` 里 `for route in self.routes: match = route.matches(scope)`——**第一条命中即停**。由此推出顺序语义：`/users/me` 若排在 `/users/{id:int}` 后面，`me` 不匹配 `[0-9]+` 会落到下一条，但如果 id 是普通字符串转换器 `{id}`，`me` 会被先匹配吃掉——所以**静态路径必须注册在动态路径之前**（或用转换器收窄）。405/404 判定：每条路由的 `matches` 返回 `Match.FULL`（路径+方法都中）/`Match.PARTIAL`（路径中但方法不中）/`Match.NONE`；**FULL 立即用，遍历完没有 FULL 但存在 PARTIAL → 405 Method Not Allowed（带 Allow 头），全 NONE → 404**——所以"405 优先于 404"是遍历语义的自然结果，方法错了能告诉你允许什么。FastAPI 在 FULL 命中后走 `route.get_route_handler()` 包装：先解析依赖（Depends 树，引 Q6088）与路径/查询/body 参数校验（Pydantic），校验失败 422 在 handler 之前——响应模型序列化在 handler 之后。性能注意：路由数大时线性正则遍历 O(n) 每请求（几十条无感，千条级要考虑 Router 分层或用 Radix 树实现的框架如 RoByndFramed/h12——工程上 FastAPI 大路由表常见做法是 APIRouter 按前缀分层，让每层遍历集合变小）。

```python
# 基线: starlette>=0.28, fastapi>=0.100；纯路由匹配部分可脱离服务运行
from starlette.routing import Route, compile_path

# 1) compile_path：路径模板 → 正则 + 参数转换器
regex, format, param_convertors = compile_path("/users/{id:int}")
print("正则:", regex.pattern)
print("转换器:", {k: v.regex for k, v in param_convertors.items()})

def handler(request):
    from starlette.responses import JSONResponse
    return JSONResponse({"id": request.path_params["id"]})

# 2) 顺序语义演示：静态路径必须在前
from starlette.routing import Router

async def me(request):
    from starlette.responses import JSONResponse
    return JSONResponse({"user": "me"})

router_wrong = Router(routes=[
    Route("/users/{id}", handler),      # 动态在前
    Route("/users/me", me),             # 静态在后 —— 被吃掉
])
router_right = Router(routes=[
    Route("/users/me", me),             # 静态在前
    Route("/users/{id:int}", handler),  # 动态在后，且转换器收窄
])

def fake_scope(path):
    return {"type": "http", "method": "GET", "path": path, "headers": [],
            "query_string": b"", "scheme": "http", "server": ("t", 80)}

# 3) 405 vs 404 判定：PARTIAL（路径中方法不中）→ 405 + Allow 头
from starlette.routing import Match
route_only_post = Route("/only-post", handler, methods=["POST"])
state, _ = route_only_post.matches(fake_scope("/only-post"))
print("GET /only-post 匹配态:", state, "| == Match.PARTIAL:", state == Match.PARTIAL)

# 4) 转换器收窄避免误吃：{id:int} 下 'me' 不会被动态路由命中
r_int, _, _ = compile_path("/users/{id:int}")
print("'me' 命中 int 正则:", bool(r_int.match("/users/me")))
r_str, _, _ = compile_path("/users/{id}")
print("'me' 命中 str 正则:", bool(r_str.match("/users/me")), "（不收窄时会吃掉静态路径）")

# 5) FastAPI 层：FULL 命中后才做依赖解析与 422 校验（验证校验先于 handler）
try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient   # 基线: httpx
    api = FastAPI()
    @api.get("/items/{item_id}")
    def read(item_id: int, q: str = "x"):
        return {"item_id": item_id}
    c = TestClient(api)
    print("FastAPI 422（校验先于 handler）:", c.get("/items/abc").status_code)
    print("FastAPI 200:", c.get("/items/42").json())
except ImportError as e:
    print("缺 fastapi/httpx，跳过集成演示:", e)
```

**追问一层**:`Match.PARTIAL` 聚合成 405 时，`Allow` 响应头的内容从哪来（多条 PARTIAL 路由怎么合并方法集合）？
**追二层**:为什么 Starlette 不用 Radix 树/Trie 而用"预编译正则线性遍历"？在大路由表（>1000 条）下这个选择的可观测症状是什么（对照 Q6099 OpenAPI 构建成本）？

**背诵要点**
- 路由 = 顺序线性遍历 + 每条预编译正则（compile_path + 转换器如 `{id:int}`），FULL 命中即停。
- 405 优先于 404：遍历完无 FULL 但有 PARTIAL（路径中方法不中）→ 405 带 Allow；全 NONE → 404。
- 静态路径注册在动态之前，或用转换器收窄动态段；FastAPI 在 FULL 后才做依赖解析与 422 校验。

**复盘追问**
- 新增 `/users/{name}` 后 `/users/me` 开始返回 404→200 且行为错乱，怎么在 CI 拦住？提示：路由表快照测试 + "静态优先" lint 规则，契约 diff（引 Q1627）。
- 千条路由的 API 每请求 P99 抬高 ~1ms，怎么分层收窄遍历集？提示：APIRouter 按前缀拆分挂载，或评估 Radix 树路由实现。
