---
title: "[Q6269] TRACE/OPTIONS 与 405：Allow 头为什么是协议义务"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6269 · TRACE/OPTIONS 与 405：Allow 头为什么是协议义务

难度：P6 ｜ 标签：HTTP、TRACE、OPTIONS、405、Allow、HEAD、XST

基线：CPython 3.12.2，纯标准库；实现一个最小方法路由器，验证 HEAD 无 body、OPTIONS 的 Allow、405 必带 Allow、TRACE 关闭与 501/405 的区别。

**问**：安全扫描报告说站点开启了 `TRACE`，攻击者可以用它回显 Cookie，配合老浏览器绕过 `HttpOnly`（XST）。运维在网关禁用 TRACE 后，扫描又报"405 响应缺少 Allow 头"。另一个客户端用 `DELETE /items` 收到 404，以为"资源不存在"，其实是"方法不允许"；`OPTIONS /items` 返回 200 但 `Allow` 是空的，CORS 预检也时好时坏。TRACE 为什么危险？405 和 501 怎么分？`Allow` 头到底该由谁生成？

**答**：

- **结论**：`TRACE` 让服务器把收到的请求（含头部）原样回显，历史上可被 XST 利用读取 `HttpOnly` Cookie（老浏览器/插件），现代浏览器多已封堵，但服务端仍应**默认禁用**，返回 405 并带 `Allow`。`OPTIONS` 用于询问资源支持的方法，响应应带 `Allow`（如 `GET, HEAD, POST, OPTIONS`）；`OPTIONS *` 是服务器级能力询问，和 CORS 预检（带 `Origin`/`Access-Control-Request-Method`）不是一回事。**405 Method Not Allowed 必须带 `Allow` 头**（RFC 9110），告诉客户端"这个资源允许哪些方法"；**501 Not Implemented** 用于"服务器根本不认识这个 method"，**404** 用于"路径不存在"。405 不带 `Allow` 是协议违规，也会让客户端/扫描器无法区分"方法错"与"资源错"。
- **取舍**：严格方法白名单（每个路由显式列允许方法）最安全，但路由多时维护成本高；框架自动生成 `Allow` 能减少遗漏，但要确保 HEAD 自动跟随 GET、OPTIONS 合并所有方法、405 分支统一加头。另一个取舍是"是否暴露方法列表"：`Allow` 会告诉攻击者支持哪些方法，但这是 HTTP 语义的一部分，隐藏它并不能提升安全，反而破坏客户端兼容；真正的安全靠"不允许的方法一律拒绝 + 认证/授权"，不是靠 obscurity。TRACE 建议在网关层直接 405，应用层再兜底一次（纵深防御）。
- **实战**：事故路由对 `DELETE /items` 返回 404（因为只匹配了 GET/POST 分支），客户端重试/告警全错；`OPTIONS` 走了一个空实现，`Allow` 是空串。修复：① 路由表按 path 聚合方法集合，405 时统一 `Allow: ", ".join(sorted(allowed | {"OPTIONS"}))`；② HEAD 自动复用 GET 的 headers、body 置空、`Content-Length` 保留；③ TRACE 在网关与应用都返回 405；④ 未知 method（如 `BREW`）返回 501。上线后扫描告警归零，CORS 预检成功率从 92% 到 100%。

下面实现一个最小路由器，验证 HEAD/OPTIONS/405/501/TRACE 的行为与 `Allow` 头。

```python
# 方法路由: HEAD 无 body, OPTIONS 带 Allow, 405 必带 Allow, TRACE 禁用
ALLOWED = {
    "/items": {"GET", "POST"},
    "/health": {"GET"},
}
KNOWN_METHODS = {"GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"}


def dispatch(method, path):
    method = method.upper()
    if path not in ALLOWED:
        return 404, {}, b"not found"

    allowed = ALLOWED[path]
    allow_header = ", ".join(sorted(allowed | {"HEAD", "OPTIONS"}))

    if method == "TRACE":
        # 明确禁用, 不回显请求
        return 405, {"Allow": allow_header}, b"trace disabled"

    if method == "OPTIONS":
        return 204, {"Allow": allow_header}, b""

    if method == "HEAD":
        if "GET" not in allowed:
            return 405, {"Allow": allow_header}, b""
        status, headers, body = 200, {"Content-Type": "application/json"}, b'{"items":[]}'
        return status, {**headers, "Content-Length": str(len(body))}, b""

    if method not in KNOWN_METHODS:
        return 501, {}, b"method not implemented"

    if method not in allowed:
        return 405, {"Allow": allow_header}, b"method not allowed"

    if method == "GET":
        body = b'{"items":[]}'
        return 200, {"Content-Type": "application/json", "Content-Length": str(len(body))}, body
    if method == "POST":
        return 201, {"Location": "/items/1"}, b""

    return 500, {}, b"unreachable"


status, headers, body = dispatch("GET", "/items")
print("[1] GET:", status, headers)
assert status == 200 and body == b'{"items":[]}'

status, headers, body = dispatch("HEAD", "/items")
print("[2] HEAD:", status, headers, "body 长度:", len(body))
assert status == 200 and body == b""
assert headers["Content-Length"] == str(len(b'{"items":[]}'))

status, headers, body = dispatch("OPTIONS", "/items")
print("[3] OPTIONS:", status, headers)
assert status == 204
assert headers["Allow"] == "GET, HEAD, OPTIONS, POST"

status, headers, body = dispatch("DELETE", "/items")
print("[4] DELETE:", status, headers)
assert status == 405
assert headers["Allow"] == "GET, HEAD, OPTIONS, POST"

status, headers, body = dispatch("TRACE", "/items")
print("[5] TRACE:", status, headers, body)
assert status == 405 and body == b"trace disabled"
assert "Cookie" not in body.decode()

status, headers, body = dispatch("GET", "/missing")
print("[6] 未知路径:", status)
assert status == 404

status, headers, _ = dispatch("BREW", "/items")
print("[7] 未知方法:", status)
assert status == 501

print("[8] 结论: 405 必带 Allow; HEAD 复用 GET 头但无 body; TRACE 默认禁用")
```

**追问一**：`HEAD` 的 `Content-Length` 应该和 `GET` 一样吗？—— 应该。HEAD 的语义是"返回与 GET 相同的响应头，但不返回 body"，客户端常用它做存在性/大小/缓存探测；如果 `Content-Length` 是 0 或缺失，缓存和下载器会判断错误。实现上可以让 HEAD 复用 GET 的 header 生成逻辑，最后把 body 丢弃；不要单独写一套 HEAD 逻辑，否则容易漂移。

**追问二**：`501` 和 `405` 的边界到底怎么划？—— `501` 是"服务器不支持这个 method（全局能力缺失）"，比如自定义的 `BREW`；`405` 是"服务器认识这个 method，但当前资源不允许"，比如 `/items` 只允许 GET/POST，收到 DELETE。很多框架对未知 method 直接 405，虽不严格但可接受；关键是 **405 必须带 `Allow`**，否则客户端无法修正。`404` 只在路径不存在时用，不要用它掩盖方法错误。

## 背诵要点

- TRACE 会回显请求（含 Cookie），默认禁用并返回 405；OPTIONS 返回 `Allow`，HEAD 复用 GET 头但无 body。
- 405（方法不允许）必须带 `Allow`；501 是服务器不认识该方法；404 只表示路径不存在。
- `Allow` 由路由的方法集合统一生成（含 HEAD/OPTIONS），避免各分支漏写。

## 复盘追问

- 为什么 `DELETE /items` 返回 404 会误导客户端？（客户端会重试/认为资源被删，而不是修正方法；缓存也可能错误处理）
- CORS 预检的 OPTIONS 和普通 OPTIONS 有什么区别？（预检带 `Origin` 与 `Access-Control-Request-Method`，响应需要 CORS 头，不只是 `Allow`）
