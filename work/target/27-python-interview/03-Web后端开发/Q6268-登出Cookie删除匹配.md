---
title: "[Q6268] 登出为什么没清掉 Cookie：domain/path 匹配与 Clear-Site-Data"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6268 · 登出为什么没清掉 Cookie：domain/path 匹配与 Clear-Site-Data

难度：P6 ｜ 标签：Cookie、登出、Path/Domain、Max-Age、Clear-Site-Data、会话失效

基线：CPython 3.12.2，纯标准库；用 `(domain, path, name)` 键的最小 Cookie Jar 复现"删错 path 没删掉"，并验证 `__Host-` 前缀与服务端会话吊销。

**问**：用户在 `/app` 下登录，服务端下发 `sid=...; Domain=.example.com; Path=/app`。登出接口在 `/` 下返回 `Set-Cookie: sid=; Max-Age=0; Path=/`，前端显示"已退出"，但用户刷新 `/app` 仍然是登录态；换一台共用电脑，下一个人直接进了上一个账号。另一个版本用 `Domain=www.example.com` 删 `.example.com` 的 Cookie，同样无效。Cookie 删除到底按什么匹配？`Clear-Site-Data` 能兜底吗？删了 Cookie 就安全了吗？

**答**：

- **结论**：Cookie 的唯一键是 **(name, domain, path)**，删除时必须用**完全相同的 name/domain/path** 再发一次 `Set-Cookie`，并把 `Max-Age=0`（或 `Expires` 设为过去时间）；只匹配 name 不够。`Path=/` 删不掉 `Path=/app` 的 Cookie，`Domain=www.example.com` 也删不掉 `Domain=.example.com` 的 Cookie——浏览器会把它们当成不同的 Cookie 同时保存。`__Host-` 前缀还要求 `Secure`、`Path=/`、**不能带 Domain**，删除时同样不能带 Domain。`Clear-Site-Data: "cookies", "storage"` 可以让浏览器清掉该 origin 的 Cookie/存储，但它是"尽力而为"、支持度不一，且**不能替代服务端会话失效**：Cookie 只是客户端凭证，攻击者偷走的 `sid` 在服务端仍然有效，必须在服务端删除 session/加入黑名单。
- **取舍**：最简单的修复是"登录和登出用同一个 helper 生成 Cookie 属性"，保证 path/domain 一致；但历史系统可能已经存在多个 path 的旧 Cookie，登出时要**枚举并逐个删除**（`/`、`/app`、`/api` 等），或者干脆换一个全新的 Cookie 名（旧的自然失效）。`Clear-Site-Data` 适合作息"一键清空"，但不要把它当唯一手段；服务端会话吊销是必须的，尤其是"登出所有设备"场景。另一个取舍是 `Max-Age=0` vs 过期时间：两者都可，`Max-Age=0` 更明确；某些老客户端只认 `Expires`，可以同时发。
- **实战**：事故的登录 helper 写死 `Path=/app`，登出 helper 写死 `Path=/`，两个函数各自维护字符串，谁也没发现不匹配。修复：① 抽出 `cookie_attrs()` 返回统一的 `domain/path/secure/samesite`，登录/登出共用；② 登出时对已知的历史 path 列表逐个发删除头；③ 服务端 `sessions.pop(sid)`，并把 `sid` 加入短期黑名单（防并发请求复用）；④ 响应加 `Clear-Site-Data: "cookies", "storage"` 作为纵深防御。上线后共用电脑串号归零。

下面用最小 Jar 验证：错误 path 删除无效、正确 path 删除生效、`__Host-` 拒绝 Domain、`Clear-Site-Data` 清空、以及服务端 session 吊销后旧 sid 失效。

```python
# Cookie 删除: (name, domain, path) 必须完全匹配; 服务端 session 必须同时吊销
from http.cookies import SimpleCookie


class CookieJar:
    def __init__(self):
        self.store = {}

    def set(self, name, value, domain, path):
        self.store[(name, domain, path)] = value

    def delete(self, name, domain, path):
        self.store.pop((name, domain, path), None)

    def get_for(self, host, request_path):
        result = {}
        for (name, domain, path), value in self.store.items():
            domain_ok = domain.startswith(".") and host.endswith(domain) or host == domain
            path_ok = request_path == path or request_path.startswith(path.rstrip("/") + "/")
            if domain_ok and path_ok:
                result[name] = value
        return result


jar = CookieJar()
jar.set("sid", "s3cr3t", ".example.com", "/app")
print("[1] 登录后 /app 可见:", jar.get_for("www.example.com", "/app"))
assert jar.get_for("www.example.com", "/app") == {"sid": "s3cr3t"}

# 错误 path: 删不掉
jar.delete("sid", ".example.com", "/")
print("[2] 用 Path=/ 删除后:", jar.get_for("www.example.com", "/app"))
assert jar.get_for("www.example.com", "/app") == {"sid": "s3cr3t"}

# 错误 domain: 也删不掉
jar.delete("sid", "www.example.com", "/app")
assert jar.get_for("www.example.com", "/app") == {"sid": "s3cr3t"}
print("[3] 用 www.example.com 删除仍无效")

# 正确匹配: 删除生效
jar.delete("sid", ".example.com", "/app")
print("[4] 正确 domain/path 删除后:", jar.get_for("www.example.com", "/app"))
assert jar.get_for("www.example.com", "/app") == {}


def build_cookie(name, value, domain=None, path="/", max_age=None, secure=False):
    parts = [f"{name}={value}", f"Path={path}"]
    if domain:
        parts.append(f"Domain={domain}")
    if max_age is not None:
        parts.append(f"Max-Age={max_age}")
    if secure:
        parts.append("Secure")
    return "; ".join(parts)


delete_header = build_cookie("sid", "", domain=".example.com", path="/app", max_age=0)
print("[5] 删除头:", delete_header)
assert "Max-Age=0" in delete_header and "Path=/app" in delete_header


def valid_host_prefix(header):
    cookie = SimpleCookie()
    cookie.load(header)
    morsel = next(iter(cookie.values()))
    return not morsel["domain"] and morsel["path"] == "/" and bool(morsel["secure"])


print("[6] __Host- 合法:", valid_host_prefix(build_cookie("__Host-sid", "x", path="/", secure=True)))
assert valid_host_prefix(build_cookie("__Host-sid", "x", path="/", secure=True)) is True
assert valid_host_prefix(build_cookie("__Host-sid", "x", domain=".example.com", path="/", secure=True)) is False

# Clear-Site-Data 解析
def clear_site_data(header):
    return {item.strip().strip('"') for item in header.split(",")}

cleared = clear_site_data('"cookies", "storage"')
print("[7] Clear-Site-Data:", cleared)
assert cleared == {"cookies", "storage"}

# 服务端会话必须同时吊销
sessions = {"sid-1": "alice"}
sessions.pop("sid-1", None)
print("[8] 旧 sid 服务端是否有效:", "sid-1" in sessions)
assert "sid-1" not in sessions

print("[9] 结论: 删除按 (name, domain, path) 精确匹配; 客户端删除 + 服务端吊销缺一不可")
```

**追问一**：`Max-Age=0` 和 `Expires=Thu, 01 Jan 1970` 有什么区别？—— 语义上都表示"立即过期"，`Max-Age` 是相对时间、优先级更高，`Expires` 是绝对时间、受客户端时钟影响。老浏览器/某些 SDK 只认 `Expires`，所以生产上常同时发两个。注意 `Expires` 必须是合法的 HTTP-date（GMT），时区/格式错了会被忽略，Cookie 反而删不掉。

**追问二**：为什么删了 Cookie 还要在服务端删 session？—— Cookie 只是"客户端愿意不再发送"，攻击者可以保留/重放旧的 `sid`；如果服务端 session 还在，登出形同虚设。正确登出是"服务端先失效 session（或把 token 加入黑名单）→ 再让客户端删 Cookie"；顺序反过来会有窗口期：客户端删了，但服务端还没失效，旧 token 仍可用。对 JWT 这类无状态 token，需要短期 access token + 可吊销的 refresh token，或维护 `jti` 黑名单。

## 背诵要点

- Cookie 唯一键是 `(name, domain, path)`；删除必须完全匹配并带 `Max-Age=0` 或过去的 `Expires`。
- `Path=/` 删不掉 `Path=/app`，`www.example.com` 删不掉 `.example.com`；`__Host-` 不能带 Domain。
- 登出必须"服务端 session 失效 + 客户端删除 Cookie"，`Clear-Site-Data` 只是纵深防御。

## 复盘追问

- 为什么登录/登出用不同 helper 容易出这种 bug？（属性字符串各写一份，path/domain 漂移，测试只测"接口 200"没测 Cookie 是否真的消失）
- `Clear-Site-Data` 能替代服务端吊销吗？（不能；它只清客户端存储，旧 token 仍可被重放）
