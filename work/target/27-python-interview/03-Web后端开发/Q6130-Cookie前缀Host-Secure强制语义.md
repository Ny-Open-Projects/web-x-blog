---
title: [Q6130] Cookie 前缀 __Host- 与 __Secure- 的强制语义
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6130 · Cookie 前缀 `__Host-` 与 `__Secure-` 的浏览器强制语义

> 难度:★★★☆☆ | 标签:原理深挖, Cookie, 安全

**问**:Session cookie 改名成 `__Host-session` 后线上登录全挂，浏览器静默拒收——为什么？`__Host-` 与 `__Secure-` 前缀各强制什么条件？服务端"设置失败"为什么没有报错可看？Python 侧怎么在 set 前自检？

**答**:结论：Cookie 前缀是**浏览器端强制的命名契约**（RFC 6265bis），服务端只负责"按要求设置"，不合规时浏览器**静默丢弃** Set-Cookie，不会报错、也不回 4xx——所以事故表现为"登录静默失效"。两条契约：a) `__Host-` 前缀：必须 `Secure` + `Path=/` + **不得有 Domain 属性**（强制 cookie 只属于当前精确 host，子域与父域都碰不到它，防子域攻击——子域被 XSS 时抢不走主域会话）；b) `__Secure-` 前缀：只强制 `Secure`，允许 Domain（适合"跨子域共享"场景）。事故还原通常是：老代码里带着 `Domain=.example.com`（从子域共享改造而来）或没有 `Path=/`、或本地 http 环境没有 Secure——条件缺一即整条被拒。Python 侧防线：封装 set-cookie 校验函数（示例代码）在 dev 阶段断言，而不是等浏览器；配合 `SameSite=Lax/Strict` 与 `HttpOnly` 的常规属性。取舍：`__Host-` 最强但放弃子域共享；要跨子域就必须降级 `__Secure-` 并承担子域风险——这是安全与架构的显式决策，不能由"历史代码里的 Domain="顺手决定。

```python
def validate_host_prefix(name: str, attrs: dict) -> list[str]:
    """浏览器(RFC 6265bis)对 __Host-/__Secure- 的强制条件; 返回违规清单。"""
    errs = []
    if name.startswith("__Host-"):
        if not attrs.get("Secure"):
            errs.append("__Host- 必须带 Secure")
        if attrs.get("Path") != "/":
            errs.append(f"__Host- 必须 Path=/（当前 {attrs.get('Path')!r}）")
        if "Domain" in attrs:
            errs.append("__Host- 不得带 Domain 属性")
    elif name.startswith("__Secure-"):
        if not attrs.get("Secure"):
            errs.append("__Secure- 必须带 Secure")
    return errs

CASES = [
    ("__Host-session", {"Secure": True, "Path": "/", "HttpOnly": True}),   # 合规
    ("__Host-session", {"Secure": True, "Path": "/", "Domain": ".example.com"}),  # 历史残留 Domain
    ("__Host-session", {"Secure": True, "Path": "/app"}),                  # Path 不对
    ("__Host-session", {"Path": "/"}),                                     # 本地 http 无 Secure
    ("__Secure-sso",    {"Secure": True, "Domain": ".example.com"}),       # 合规: 允许子域共享
]
for name, attrs in CASES:
    errs = validate_host_prefix(name, attrs)
    print(f"{name} {attrs} -> {'合规' if not errs else '浏览器静默拒收: ' + '; '.join(errs)}")

# ---- 服务端框架层自检(Django/FastAPI 通用伪代码) ----
TEMPLATE = """
# 设置前的自检钩子(开发环境断言):
assert validate_host_prefix(name, attrs) == [], "Set-Cookie 将被浏览器静默丢弃"
# Django: settings.SESSION_COOKIE_NAME = "__Host-session"
#         SESSION_COOKIE_SECURE=True / SESSION_COOKIE_PATH="/" / 不设 DOMAIN
# FastAPI: response.set_cookie("__Host-session", v, secure=True, path="/", samesite="lax")
"""
print(TEMPLATE)
```

**追问一层**:为什么 `__Host-` 禁 Domain 属性能防子域攻击？（有 Domain 时 cookie 属于"域及子域"，子域（如 stage.example.com 或被攻破的子站）可诱导父域作用域的 cookie；禁 Domain 后作用域锁死在精确 host）。
**追问二层**:前缀改名的迁移怎么做（老 cookie 怎么办）？（双写期：同时 set 旧名与 `__Host-` 新名并读双删，登录态自然滚动；旧名若带 Domain 还要先在其作用域内显式清除）。
**追问三层**:`SameSite` 与前缀的关系？（前缀管"谁能收到"，SameSite 管"跨站请求带不带"，两者正交但都影响登录态；`__Host-` + `SameSite=Lax` 是会话 cookie 的当前推荐组合，CSRF 防线仍需 token，呼应 Q6058 Cookie 属性演进）。

## 背诵要点
- `__Host-` 强制三条件：Secure + Path=/ + 无 Domain；`__Secure-` 只强制 Secure、允许子域共享。
- 不合规时浏览器静默拒收 Set-Cookie，无任何服务端报错——必须在 set 前自检。
- `__Host-` 锁死精确 host 防子域攻击；跨子域共享是显式安全决策，迁移靠双写滚动。

## 复盘追问
- 上线新会话 cookie 后"部分用户反复被登出"，如何按浏览器/域名维度定位到前缀违规或 Domain 残留？
- 设计双写迁移方案时，旧 Domain cookie 的清除路径和时序怎么安排才能不踢掉在线用户？
