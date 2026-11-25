---
title: "[Q6267] Cookie 的 4KB 上限：Set-Cookie 截断、分片与 431"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6267 · Cookie 的 4KB 上限：Set-Cookie 截断、分片与 431

难度：P6 ｜ 标签：Cookie、4KB、431、分片、Session、请求头

基线：CPython 3.12.2，纯标准库；用 `http.cookies.SimpleCookie` 与字节长度计算，验证单 Cookie 超限、分片重组与请求头总大小触发的 431。

**问**：一个 SaaS 把用户的权限列表、租户配置、feature flags 全塞进 JWT，再整个写进 Cookie；某企业客户权限多，Cookie 涨到 6.2KB。浏览器**静默丢弃**了这条 `Set-Cookie`，用户登录成功后立刻又变回未登录；服务端日志里没有任何错误。另一个内部系统把 40KB 的配置写进 Cookie，Nginx 直接返回 431，前端只看到空白页。Cookie 到底限制多大？超了是服务端报错还是浏览器丢？为什么"分片"不是长久之计？

**答**：

- **结论**：主流浏览器对**单个 Cookie**（name + value + 属性）的限制约 **4096 字节**，超出通常**静默丢弃**，不会给服务端任何反馈；对每个域名还有数量限制（约 180 个）和总大小限制。服务端/网关则限制**整个请求头**的大小（Nginx `large_client_header_buffers` 默认 8KB 左右，超了返回 **431 Request Header Fields Too Large**，有的实现返回 400）。所以"Set-Cookie 超 4KB"表现为"偶发登录态丢失"，"Cookie 总量超 8KB"表现为"整站 431/400"。`Cookie` 头会在**每个同域请求**上重复发送，4KB 的 Cookie 乘以静态资源/API 请求数就是带宽与延迟的净损失。
- **取舍**：分片（`sid.0`、`sid.1`，每片 <3800 字节）能绕过单 Cookie 限制，但会：① 增加 Cookie 数量，逼近每域 180 个的上限；② 每片都带属性，总开销更大；③ 分片之间可能不一致（并发响应覆盖一半），需要版本号/校验；④ 仍然要受请求头总大小限制。更根本的解法是**服务端会话**：Cookie 只放一个高熵、不透明的 session id（32～43 字节），权限/配置放 Redis/DB，按 id 查；或者用 `__Host-` 前缀 + `HttpOnly; Secure; SameSite=Lax` 保护。JWT 适合"无状态、跨服务"场景，但不适合把大对象塞进 Cookie。
- **实战**：事故的 JWT 里塞了 `permissions`（200 条）、`tenant`、`features`，6.2KB；Chrome 丢弃后，前端仍以为登录成功。修复：① Cookie 只保留 `session_id`（`secrets.token_urlsafe(32)`，43 字符）；② 权限/配置放服务端缓存，按 `session_id` 查，TTL 30 分钟；③ 登出时删 session 并 `Clear-Site-Data`；④ 网关把请求头上限从 8KB 调到 16KB 只是临时缓解，长期靠瘦身。上线后登录态丢失归零，首屏请求头从 7.8KB 降到 0.9KB。

下面验证单 Cookie 超 4096 的判断、分片/重组、以及 Cookie 头总量超过 8KB 时返回 431 的闸门。

```python
# Cookie 大小: 单条 ~4096 字节, 请求头总量超限 -> 431
from http.cookies import SimpleCookie

MAX_COOKIE = 4096
CHUNK = 3800


def set_cookie_header(name, value, path="/", extra=""):
    header = f"{name}={value}; Path={path}"
    if extra:
        header += "; " + extra
    return header


def cookie_size(header):
    return len(header.encode("latin-1"))


# 1) 单条 5000 字节: 超过浏览器上限
big_value = "a" * 5000
big_header = set_cookie_header("sid", big_value, extra="HttpOnly; Secure")
print("[1] 单条大小:", cookie_size(big_header))
assert cookie_size(big_header) > MAX_COOKIE


def chunk_cookie(name, value, limit=CHUNK):
    return [
        (f"{name}.{i // limit}", value[i:i + limit])
        for i in range(0, len(value), limit)
    ]


chunks = chunk_cookie("sid", big_value)
print("[2] 分片:", [(n, len(v)) for n, v in chunks])
assert all(len(n) + len(v) + len("; Path=/") <= MAX_COOKIE for n, v in chunks)
assert "".join(v for _, v in chunks) == big_value

# 用 SimpleCookie 解析分片并重组
jar = SimpleCookie()
for name, value in chunks:
    jar[name] = value
restored = "".join(jar[name].value for name in sorted(jar))
print("[3] 分片数:", len(jar), "| 重组一致:", restored == big_value)
assert restored == big_value


def request_status(cookie_headers, limit=8192):
    raw = "; ".join(cookie_headers)
    size = len(raw.encode("latin-1"))
    return (431 if size > limit else 200), size


# 2) 20 条 500 字节 Cookie: 总量超 8KB -> 431
headers = [f"k{i}=" + "x" * 500 for i in range(20)]
status, size = request_status(headers)
print("[4] 请求头总大小:", size, "-> 状态:", status)
assert status == 431

# 3) 服务端会话: 只放 43 字符的 session id
session_id = "s" * 43
small = set_cookie_header("__Host-sid", session_id, extra="HttpOnly; Secure; SameSite=Lax")
print("[5] 服务端会话 Cookie 大小:", cookie_size(small))
assert cookie_size(small) < 200
assert request_status([small])[0] == 200

print("[6] 结论: 单条超 4KB 浏览器静默丢; 总量超 8KB 网关 431; 根本解是瘦身/服务端会话")
```

**追问一**：`__Host-` 前缀有什么额外约束？—— `__Host-` 前缀的 Cookie 必须满足：`Secure`、`Path=/`、且**不能**带 `Domain` 属性（只能绑定当前 host，不能共享给子域）。这能防止子域覆盖父域的同名 Cookie（session fixation 的一种）。`__Secure-` 只要求 `Secure`，约束更弱。命名时注意浏览器对前缀是强制校验的，不满足会被拒绝。

**追问二**：为什么不在 Cookie 里存压缩后的 JWT？—— 压缩能减小体积，但：① 压缩后的二进制需要 Base64，膨胀 33%；② 解压需要 CPU，且压缩炸弹可能被恶意构造；③ Cookie 仍会在每个请求上发送，带宽/延迟问题没解决；④ JWT 的签名/过期/吊销语义在服务端会话里更容易控制。如果确实需要无状态，控制 claims 数量（只放 `sub`、`exp`、`jti`），权限按需查；不要把"无状态"理解成"把所有状态塞进客户端"。

## 背诵要点

- 单 Cookie 约 4096 字节，超出浏览器**静默丢弃**；请求头总量超网关上限（约 8KB）返回 431。
- 分片能绕过单条限制，但增加数量/属性开销、受总量限制、可能不一致；不是长久方案。
- 根本解：服务端会话 + 不透明 session id；`__Host-` 要求 Secure、Path=/、无 Domain。

## 复盘追问

- 为什么 Cookie 超限时服务端日志没有错误？（浏览器侧丢弃，响应已成功发出，服务端无感知）
- 分片 Cookie 在并发响应下会出什么问题？（两个响应各自更新部分分片，可能拼出混合版本；需要版本号/原子写）
