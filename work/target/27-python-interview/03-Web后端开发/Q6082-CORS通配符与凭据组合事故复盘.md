---
title: "[Q6082] CORS 通配符与凭据组合的事故复盘"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6082 · CORS 通配符与凭据组合的事故复盘

难度：★★★☆☆ ｜ 标签：事故复盘 / CORS / Cookie / Web 安全

**问**：为了"前端联调方便"，服务把 `Access-Control-Allow-Origin` 配成 `*` 又保留了 Cookie 会话；后来在错误响应里直接回显请求 Origin。这两个配置各埋了什么雷？浏览器到底执行哪一侧的规则？

**答**：
- **结论**：CORS 是**浏览器执行的读取权限机制**，服务器响应头只是"许可声明"。两颗雷：1）`Allow-Origin: *` 与 `Allow-Credentials: true` 是**规范禁止组合**——浏览器会直接拒绝读取（Starlette 的 CORSMiddleware 检测到该组合会直接拒绝启动/报错），但很多人"解决"办法是把 `*` 换成**动态回显 Origin**（`allow_origin_regex` 或手动 echo），这等于对**所有网站**签发凭据许可，任意第三方页面都能带着用户 Cookie 读你的接口——CSRF 的进化版。2）正确做法是**显式白名单**（环境变量配置域名列表），未匹配的 Origin 不返回 Allow-Origin 头。
- **取舍**：为什么 `*`（不带凭据）通常无害：它只允许公开资源被跨域读；带凭据的跨域读才是核心风险。预检（OPTIONS preflight）只挡"非简单请求"，简单请求（GET/POST + 简单头）**会直接发出**——CORS 拦的是"读响应"，不是"发请求"，所以 CORS 不是 CSRF 防线，CSRF 要靠 SameSite/CSRF token（Q6058）。多环境策略：开发环境放宽（localhost 白名单），生产收紧，用配置注入而不是代码常量。
- **实战**：复盘动作：1）grep 所有 `allow_origins` 配置，`*` 与回显模式全部转显式白名单；2）错误响应/日志确认不回显 Origin（Origin 是请求方可控的，回显=反射面）；3）契约测试：对非白名单 Origin 断言**响应无** Allow-Origin 头（而不是断言有 `*`）；4）`Vary: Origin` 头必须加（缓存按 Origin 区分，否则 CDN 缓存串包）。

```python
"""CORS 组合行为核对表：白名单/通配符/凭据（FastAPI+Starlette 基线）"""
try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.testclient import TestClient
except ImportError:
    raise SystemExit("缺 fastapi：pip install 'fastapi>=0.100'（文末附标准库版核对逻辑）")

def make_app(mode: str):
    app = FastAPI()
    kw = {"allow_credentials": True, "allow_methods": ["*"], "allow_headers": ["*"]}
    if mode == "wildcard":                    # 规范禁止组合：星号 + 凭据
        kw["allow_origins"] = ["*"]
    elif mode == "echo":                      # 反模式：回显任意 Origin
        kw["allow_origin_regex"] = ".*"
    elif mode == "whitelist":                 # 正解
        kw["allow_origins"] = ["https://app.example.com"]
    app.add_middleware(CORSMiddleware, **kw)
    @app.get("/data")
    def data():
        return {"secret": "v"}
    return app

evil, legit = "https://evil.example", "https://app.example.com"
for mode in ("wildcard", "echo", "whitelist"):
    try:
        c = TestClient(make_app(mode))
        r_evil = c.get("/data", headers={"Origin": evil})
        r_legit = c.get("/data", headers={"Origin": legit})
        print(f"[{mode}] 恶意 Origin → ACO={r_evil.headers.get('access-control-allow-origin')!r} "
              f"ACAC={r_evil.headers.get('access-control-allow-credentials')!r} "
              f"| 合法 Origin → ACO={r_legit.headers.get('access-control-allow-origin')!r}")
    except Exception as e:
        print(f"[{mode}] 启动/请求受限: {type(e).__name__}")

# 断言红线：白名单模式下恶意 Origin 拿不到许可头
c = TestClient(make_app("whitelist"))
assert "access-control-allow-origin" not in c.get("/data", headers={"Origin": evil}).headers
print("红线通过：非白名单 Origin 无 Allow-Origin 头")
# 缓存红线：响应必须带 Vary: Origin，否则 CDN 按无 Origin 缓存串包
print("别忘了 Vary: Origin（CORSMiddleware 已内置；自写处理器常漏）")

# 标准库版核对逻辑（无框架也能验收）
def cors_decision(origin, whitelist, credentials):
    if origin not in whitelist:
        return "无许可头：浏览器拦截读取"
    if credentials:
        return f"ACO={origin}（凭据模式必须回具体 Origin，不能是 *）"
    return "ACO=*（公开资源可跨域读）"
print(cors_decision("https://evil.example", ["https://app.example.com"], True))
```

**追问链**
1. 为什么"回显 Origin + 凭据"比直接 `*` 更危险？
   1. `*`+凭据被浏览器硬拦（规范禁止），事故不会发生；回显模式规范合法、浏览器照单全收——任何网站的页面都能以用户身份发跨域请求并读响应，等于关掉了同源策略对凭据接口的保护，且渗透测试往往漏测这种"看起来配置了 CORS"的组合。
   2. 追问：SameSite=Lax 能兜住吗？——Lax 挡住跨站 POST 的 Cookie，但跨站 GET 顶层导航/子请求仍带 Cookie；CORS 白名单 + SameSite + CSRF token 三层各有职责，不能互相替代。
2. 预检请求的成本与缓存怎么优化？
   1. 每个非简单请求先 OPTIONS 往返（跨地域可加 100ms+），浏览器按 `Access-Control-Max-Age` 缓存预检结果（Chrome 上限 2h）——服务端务必返回较大 Max-Age 并稳定预检响应头；动态 Origin 回显在预检路径上同样要命中白名单判断。
   2. 追问：为什么"简单请求"不需要预检但仍可能被拦？——简单请求会真实发出，服务器若不给许可头，浏览器**不把响应交给页面 JS**；请求已到达服务器（副作用已发生），这就是"CORS 不防 CSRF"的机制根源。

## 背诵要点
- `*` + Allow-Credentials 是规范禁止组合；用"回显 Origin"绕过 = 对全网签发凭据许可，比 `*` 更危险。
- CORS 拦"读响应"不拦"发请求"，不能替代 CSRF 防线；简单请求直接到达服务端。
- 正解 = 显式白名单 + 未匹配不返回许可头 + Vary: Origin（防 CDN 串包）+ Max-Age 缓存预检。

## 复盘追问
- 渗透报告里"任意 Origin 均可携带 Cookie 调用"如何复现并确认影响面（哪些接口是凭据型的）？
- CDN/网关层是否也配了 CORS？双层配置不一致时浏览器行为如何排查？
