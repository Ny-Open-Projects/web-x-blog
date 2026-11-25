---
title: "[Q6200] WebSocket 路由里依赖注入 Request：scope 不匹配直接报错"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6200 · WebSocket 路由里依赖注入 Request：scope 不匹配直接报错

难度：P7 ｜ 标签：FastAPI、WebSocket、Depends、scope、依赖注入、鉴权

**问**：同一套鉴权依赖 `def auth(request: Request)` 在 HTTP 路由工作正常，挂到 WebSocket 路由上直接报错（提示 `Request` 在 WebSocket 连接中不可用），或者干脆拿不到 token。为什么同一个依赖不能复用？`Request` 和 `WebSocket` 的 scope 差在哪？WebSocket 的鉴权该怎么写？

**答**：
结论：ASGI 的 `scope["type"]` 决定请求种类：`http` 的 scope 里才有 `method`、`headers`、`path` 等字段，`websocket` 的 scope 有 `subprotocols`、`headers` 但没有 `method`。FastAPI 在处理 `websocket` 路由时，只会把 `WebSocket` 注入为可用对象；声明 `Request` 参数时，它找不到对应的 scope 数据源，于是在解析依赖时就报错。`Depends` 本身不区分 scope，但依赖函数声明的参数类型会被解析成"从当前 scope 取 Request"，所以复用会失败。

取舍：a) 写两个依赖：HTTP 用 `Request`（读 header/cookie），WebSocket 用 `WebSocket`（读 `headers`、`query_params`、`subprotocols`），共享底层校验函数；b) 鉴权 token 优先从 header 取（`Sec-WebSocket-Protocol` 或 `Authorization`），浏览器原生 `WebSocket` API 不能自定义 header，只能退而用 query string（注意会进日志/Referer）或子协议；c) 连接建立后再发"鉴权消息"也可以，但要在 `accept` 前完成 `close(code=1008)`，别先 accept 再校验（否则已建立连接又要踢，浪费资源）；d) 不要把 HTTP 的 `request.state` 当跨协议共享状态，WebSocket 有自己的连接生命周期。

实战：事故形态是"把 REST 的 `get_current_user(request)` 直接挂到 WS 路由，测试环境用 `TestClient` 的 HTTP 覆盖不到 WS，上线后所有 WS 连接握手阶段 500"。下面用 `inspect` 模拟 FastAPI 的依赖解析：按 scope 类型检查参数注解，演示 `Request` 在 WS 下不可用、`WebSocket` 可用，以及正确的双依赖写法。

```python
import inspect


class Request:
    def __init__(self, headers=None):
        self.headers = headers or {}


class WebSocket:
    def __init__(self, headers=None, query_params=None):
        self.headers = headers or {}
        self.query_params = query_params or {}


def resolve(scope_type, fn):
    """模拟 FastAPI：按 scope 判断参数能否注入。"""
    kwargs = {}
    for name, param in inspect.signature(fn).parameters.items():
        ann = param.annotation
        if ann is Request:
            if scope_type != "http":
                raise TypeError("Request is not available in WebSocket scope")
            kwargs[name] = Request({"authorization": "Bearer t"})
        elif ann is WebSocket:
            if scope_type != "websocket":
                raise TypeError("WebSocket is not available in HTTP scope")
            kwargs[name] = WebSocket({"authorization": "Bearer t"})
        else:
            raise TypeError(f"无法注入参数 {name}: {ann}")
    return fn(**kwargs)


def get_user_http(request: Request):
    return {"user": "alice", "via": "header"}


def get_user_ws(websocket: WebSocket):
    token = websocket.headers.get("authorization", "")
    return {"user": "alice", "via": "ws-header", "token": token}


def get_user_ws_query(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if not token:
        raise PermissionError("缺少 token")
    return {"user": "alice", "via": "query"}


print("[1] HTTP 路由复用:", resolve("http", get_user_http))
try:
    resolve("websocket", get_user_http)
except TypeError as e:
    print("[2] WS 路由复用 HTTP 依赖:", e)

print("[3] WS 专用依赖:", resolve("websocket", get_user_ws))
try:
    get_user_ws_query(WebSocket())
except PermissionError as e:
    print("[4] query 无 token:", e)
print("[5] 共享校验函数、只换数据来源才是正解")

# 共享底层校验：协议适配层与业务校验分离
def verify_token(token: str):
    if not token.startswith("Bearer "):
        raise PermissionError("bad token")
    return {"user": "alice"}


def http_adapter(request: Request):
    return verify_token(request.headers.get("authorization", ""))


def ws_adapter(websocket: WebSocket):
    token = websocket.headers.get("authorization") or "Bearer " + websocket.query_params.get("token", "")
    return verify_token(token)


print("[6] HTTP 适配器:", http_adapter(Request({"authorization": "Bearer x"})))
print("[7] WS 适配器:", ws_adapter(WebSocket(query_params={"token": "x"})))
```

**追问一**：为什么 `Accept` 之后才发现鉴权失败很糟？—— WebSocket 握手只要 `accept` 就完成了协议升级，之后关闭需要发 close 帧，客户端会看到"连上又断开"，重连逻辑可能立刻重试形成风暴。正确做法是在 `accept` 之前校验，失败直接 `await websocket.close(code=1008)`（policy violation），握手阶段就拒绝，客户端拿到明确的失败。

**追问二**：浏览器为什么不能给 WebSocket 加 `Authorization` 头？—— 原生 `WebSocket` 构造器只接受 URL 与 `protocols`，没有 headers 参数（设计上防止跨站滥用）。可用替代：a) 把 token 放 query（简单但会进访问日志，需短期一次性 token）；b) 用 `Sec-WebSocket-Protocol` 传 token（合法但语义借用，代理可能改写）；c) 先 HTTP 登录拿一次性 ticket，再用 ticket 建连；d) 用支持自定义头的客户端（非浏览器）时可以直接带 header。生产上常用"短期 ticket"而不是长期 token 放 query。

## 背诵要点
- ASGI scope 按 `type` 区分，`Request` 只在 `http` scope 可用；WS 依赖必须声明 `WebSocket`。
- 共享的是"校验逻辑"，不是"参数类型"；协议适配层各自读 header/query。
- WS 鉴权要在 `accept` 前完成，失败 `close(1008)`；浏览器只能靠 query/ticket/子协议传 token。

## 复盘追问
- 同一依赖在 HTTP 正常、WS 报 `Request` 不可用，如何解释？（scope 数据源）
- 浏览器 WS 鉴权怎么做才不把长期 token 放进 URL？（一次性 ticket / 子协议 / 建连后首帧）
