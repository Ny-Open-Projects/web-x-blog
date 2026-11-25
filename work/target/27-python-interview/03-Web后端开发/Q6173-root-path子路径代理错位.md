---
title: "[Q6173] root_path 缺失导致子路径代理下重定向与 OpenAPI 错位"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6173 · root_path 缺失导致子路径代理下重定向与 OpenAPI 错位

难度：P6 ｜ 标签：FastAPI、Starlette、root_path、反向代理、307、OpenAPI

**问**：应用原来挂在域名根路径 `/`，迁到 API 网关的 `/api` 前缀后，`POST /api/items`（少一个尾斜杠）返回 307，浏览器跳到 `/items/` 直接 404；Swagger 文档能打开但"Try it out"请求打到错误地址。应用代码没改，为什么所有"自己生成 URL"的地方都丢了 `/api`？`root_path` 应该配在哪一层？网关是 strip 前缀还是透传，哪种更不容易错？

**答**：
结论：反向代理把 `/api/items` **剥掉 `/api`** 后转给应用，应用看到的 `scope["path"]` 是 `/items`，它并不知道外部还有 `/api`。Starlette/FastAPI 生成绝对 URL（重定向、`url_for`、OpenAPI `servers`、docs 资源）时，会把 `root_path` 拼在 path 前；不配 `root_path`，生成的 URL 就缺 `/api`。典型表现：尾斜杠重定向 307 到 `https://host/items/`（缺前缀）→ 404；OpenAPI 的 `servers` 为空，Swagger UI 按当前页面 URL 推断，可能对也可能错；`request.url` 也只反映内部 path。

取舍：两种部署约定——a) 网关 **strip 前缀**，应用配 `root_path=/api`（FastAPI `root_path="/api"` 或 uvicorn `--root-path /api`），应用内部路由仍写 `/items`；b) 网关 **透传完整路径**，应用路由本身带 `/api`，`root_path` 留空。两种只能选一种，混用会出现双前缀 `/api/api/items`。多级代理时用 `X-Forwarded-Prefix` 由网关动态传前缀更灵活，但需要框架/中间件支持，且要防客户端伪造。`root_path` 只影响"生成 URL"，不影响路由匹配——路由仍按剥掉前缀后的 path 匹配。

实战：事故形态是"迁移当天所有带尾斜杠的 POST 变 404，前端以为接口挂了；Swagger 里点执行请求打到 `/items` 而不是 `/api/items`"。下面用最小函数模拟 Starlette 的 `build_url` 与尾斜杠重定向：无 `root_path` 时 Location 缺 `/api`；设置后正确；OpenAPI `servers` 也应反映该前缀。

```python
from urllib.parse import urlsplit


def build_url(scope, path):
    root = scope.get("root_path", "")
    host = scope["headers"].get("host") or scope["server"][0]
    return f"{scope['scheme']}://{host}{root}{path}"


def redirect_slashes(scope, path):
    # Starlette 的尾斜杠重定向：用 scope 里拼出的绝对 URL
    return 307, build_url(scope, path + "/")


scope = {
    "scheme": "http",
    "server": ("10.0.3.17", 8000),
    "headers": {"host": "api.example.com"},
    "root_path": "",
}

print("无 root_path 的 Location:", redirect_slashes(scope, "/items")[1])
print("代理挂在 /api 下时浏览器请求的是 https://api.example.com/api/items/")
print("实际跳转却缺少 /api -> 404")

scope["root_path"] = "/api"
print("设置 root_path 后     :", redirect_slashes(scope, "/items")[1])
print("OpenAPI servers       :", [{"url": scope["root_path"]}])

u = urlsplit("https://api.example.com/api/items/")
print("反向解析路径:", u.path)
```

**追问一**：为什么重定向返回的是绝对 URL，而且 host 是内部地址？——Starlette 的 `RedirectResponse` 默认把相对 path 拼成绝对 URL（基于 `scope` 的 scheme/host/root_path），方便客户端直接跳转；如果代理没传 `X-Forwarded-Host`/`Host`，host 可能是内部服务名或 Pod IP，外部不可达。生产上要么让网关重写 `Location`，要么正确配置代理头 + `root_path`，让应用生成外部可用的绝对 URL。

**追问二**：`root_path`、`X-Forwarded-Prefix`、WSGI 的 `SCRIPT_NAME` 是什么关系？——概念同源：都是"应用挂载在外部路径前缀下"的元信息。WSGI 用 `SCRIPT_NAME` 表示前缀、`PATH_INFO` 表示应用内路径；ASGI 用 `scope["root_path"]` + `scope["path"]`；`X-Forwarded-Prefix` 是代理传前缀的非标准头，需要中间件把它写进 `root_path`。三者不要重复叠加：如果网关已经 strip 并在头里传前缀，应用就不要再硬编码 `root_path`，否则双前缀。

## 背诵要点
- 代理 strip 前缀时应用只看到 `/items`；`root_path` 决定生成 URL（重定向/`url_for`/OpenAPI）是否带 `/api`。
- 路由匹配用剥前缀后的 path，`root_path` 只影响 URL 生成；strip + root_path 与透传 + 路由带前缀二选一。
- 绝对重定向依赖 scheme/host/root_path；代理头缺失会把内部地址泄露到 Location。

## 复盘追问
- 迁到 `/api` 后尾斜杠 307 全部 404、Swagger 请求打错地址，如何用 root_path 解释并修复？（strip 前缀、root_path、OpenAPI servers）
- `root_path`、`X-Forwarded-Prefix`、`SCRIPT_NAME` 如何对应？为什么会配出 `/api/api`？（同一概念的三层表达，禁止重复叠加）
