---
title: "[Q6195] DRF 该 401 却返回 403：authenticate_header 决定状态码"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6195 · DRF 该 401 却返回 403：authenticate_header 决定状态码

难度：P6 ｜ 标签：DRF、401、403、WWW-Authenticate、AuthenticationFailed、客户端跳转

**问**：接口未登录时返回 403，前端拦截器只处理 401 跳登录页，用户点页面没反应。后端说"明明抛了 `NotAuthenticated`"。为什么 DRF 会把未认证变成 403？`authenticate_header` 是什么、谁在调？RFC 对 401 有什么硬要求？

**答**：
结论：DRF 的异常处理里，`NotAuthenticated`/`AuthenticationFailed` 的状态码不是固定的 401，而是看**当前第一个认证器**有没有实现 `authenticate_header(request)`：返回非空字符串就 401 并把该字符串写进 `WWW-Authenticate` 响应头；返回 `None`（默认实现）就降级成 403。原因是 HTTP 规范要求 401 必须带 `WWW-Authenticate`，告诉客户端"用哪种方式认证"；没有这个头时，401 是不合规的，DRF 选择 403。

取舍：a) 用 JWT/OAuth 时给认证类实现 `authenticate_header`，返回 `Bearer realm="api"`，状态码自然变 401，前端拦截器也能统一处理；b) 用 Session 认证时保持 403 是合理的——浏览器会自动带 cookie，返回 401+`WWW-Authenticate` 反而会触发浏览器的 Basic 弹窗；c) 前端不要把"403 一律当无权限"，要区分"未认证"（可跳登录）与"已认证但无权限"（提示申请权限），这要求后端状态码语义准确；d) 多认证器混用时，DRF 只看**第一个**认证器的 header，顺序会影响状态码，别把 Session 放前面又期望 401。

实战：事故形态是"移动端接入 JWT 后未登录返回 403，App 的 401 拦截器不触发，用户看到空白页；后端加日志才发现认证类的 `authenticate_header` 继承了默认 `None`"。下面模拟 DRF 的状态码决策，演示无 header → 403、有 header → 401、以及多认证器顺序的影响。

```python
class BaseAuth:
    keyword = None

    def authenticate_header(self, request):
        return None          # DRF 默认：没有 challenge


class JWTAuth(BaseAuth):
    keyword = "Bearer"

    def authenticate_header(self, request):
        return 'Bearer realm="api"'


class SessionAuth(BaseAuth):
    keyword = None           # 浏览器 cookie，不发 challenge


def exception_response(authenticators, exc):
    """模拟 DRF exception_handler 的状态码分支。"""
    if exc in ("NotAuthenticated", "AuthenticationFailed"):
        auth = authenticators[0] if authenticators else None
        header = auth.authenticate_header({}) if auth else None
        if header:
            return 401, {"WWW-Authenticate": header}
        return 403, {}
    return 500, {}


print("[1] JWT 认证器:", exception_response([JWTAuth()], "NotAuthenticated"))
print("[2] Session 认证器:", exception_response([SessionAuth()], "NotAuthenticated"))
print("[3] 没有认证器:", exception_response([], "NotAuthenticated"))

# 多认证器：只看第一个
mixed = [SessionAuth(), JWTAuth()]
print("[4] Session 在前:", exception_response(mixed, "NotAuthenticated"))
print("[5] JWT 在前:", exception_response(list(reversed(mixed)), "NotAuthenticated"))

# 客户端视角：只有 401 才应该跳登录
def client_action(status, headers):
    if status == 401 and "WWW-Authenticate" in headers:
        return "跳登录 / 刷新 token"
    if status == 403:
        return "提示无权限（不跳登录）"
    return "其他"


print("[6] 403 时前端:", client_action(*exception_response([SessionAuth()], "NotAuthenticated")))
print("[7] 401 时前端:", client_action(*exception_response([JWTAuth()], "NotAuthenticated")))
```

**追问一**：`AuthenticationFailed` 和 `NotAuthenticated` 有区别吗？—— 语义上前者表示"给了凭据但无效"（token 过期、签名错），后者表示"没给凭据"；但 DRF 对两者的状态码决策走同一套 `authenticate_header` 逻辑。客户端通常都按"重新登录"处理，服务端日志要区分，否则无法判断是攻击还是 token 过期。若要在 401 里区分原因，用 `detail` 或自定义错误码，而不是改状态码。

**追问二**：为什么 Session 认证不该返回 401？—— 401 + `WWW-Authenticate` 是给"HTTP 认证方案"用的，浏览器看到 `Basic` challenge 会弹原生登录框，体验极差；Session 的登录流程是应用自己的页面，返回 403 让前端决定跳转更合适。这也是"同一套前端同时对接 Session 与 JWT"时必须分开处理的原因：状态码是协议语义，不是随便挑的。

## 背诵要点
- DRF 的 401/403 由**第一个认证器**的 `authenticate_header` 决定：非空 → 401 + `WWW-Authenticate`，`None` → 403。
- 401 必须带 challenge 头；Session 认证保持 403 才符合浏览器行为。
- 多认证器顺序影响状态码；前端要区分"未认证"与"无权限"，不能一律 403。

## 复盘追问
- 未登录返回 403 导致 App 不跳登录，如何从 `authenticate_header` 定位？（默认返回 None）
- 同时支持 Session 与 JWT 时，如何设计状态码与前端拦截？（按认证器分流、顺序、challenge 头）
