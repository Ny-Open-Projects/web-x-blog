---
title: "[Q6258] Cookie 的 __Host- 前缀与 SameSite=None：Secure 强制、子域写入与三方上下文"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6258 · Cookie 的 __Host- 前缀与 SameSite=None：Secure 强制、子域写入与三方上下文

难度：P6 ｜ 标签：Cookie、__Host-、__Secure-、SameSite、Secure、Domain、子域、CHIPS、会话安全

**问**：一个多租户 SaaS 把会话 Cookie 命名为 `__Host-sid`，本地 HTTP 调试时浏览器根本不保存；另一个团队为了跨子域共享登录态，给 `__Host-sid` 加了 `Domain=.example.com`，结果浏览器静默丢弃，登录态全部失效。改成 `SameSite=None` 支持 iframe 嵌入后，Chrome 又不认。`__Host-` 到底强制了什么？为什么不能带 Domain？`SameSite=None` 和 `Secure`、`Partitioned` 是什么关系？

**答**：

- **结论**：`__Host-` 前缀是**浏览器强制**的写入约束，要同时满足三条才接受：①`Secure` 必须为真；②`Path=/`（必须显式写 `/`）；③**不能有 `Domain` 属性**（host-only）。任一条不满足，浏览器就当作没收到这个 Set-Cookie，**不会报错**（所以表现为"登录态莫名失效"）。它的目的是让这个 Cookie 绑定到"当前主机名"，子域无法覆盖、无法通过 DNS 劫持/子域 XSS 写入同名 Cookie（cookie tossing）。`__Secure-` 只要求 `Secure`，允许带 `Domain`，因此可以被 `.example.com` 下的任意子域覆盖——跨子域 SSO 需要共享，就得接受这个风险，或改用 token 交换。`SameSite=None` 表示"允许跨站发送"（iframe/跨域 fetch），现代浏览器同时要求 `Secure`；在三方 Cookie 逐步淘汰的背景下，还要加 `Partitioned`（CHIPS）才能在被嵌入的第三方上下文里保留，否则会被直接拦截。

- **取舍**：a) 单主机会话：用 `__Host-` + `Secure` + `Path=/` + `HttpOnly` + `SameSite=Lax`，这是最安全的默认组合；b) 跨子域 SSO：要么用 `__Secure-` + `Domain=.example.com`（接受子域可覆盖），要么每个子域各自持有 host-only Cookie（更安全但要多一次登录/ token 交换）；c) 三方嵌入：`SameSite=None; Secure` 是入场券，`Partitioned` 是三方 Cookie 限制下的"分区存储"，代价是同一用户在不同顶层站点下是不同分区，统计/会话不能直接合并；d) 本地开发：`Secure` Cookie 在 `http://localhost` 上部分浏览器允许（localhost 被视为安全上下文），但 `__Host-` 仍要求 Secure，调试时要么用 HTTPS，要么临时换不带前缀的名字。

- **实战**：事故形态是"加 `Domain` 后登录态全丢"——团队为了"让 api.example.com 和 www.example.com 共享"，把 `__Host-sid` 改成 `__Host-sid; Domain=.example.com`，浏览器按规范丢弃，服务端却一直下发，表现为"每次请求都新建会话"，session 表暴涨。修复：①确认共享范围：真需要跨子域就用 `__Secure-` 前缀 + `Domain=.example.com`，并接受子域写入风险；②不需要就保持 `__Host-`，各子域独立会话；③在测试里加一条"Set-Cookie 解析 + 前缀规则校验"，把浏览器的丢弃行为在服务端提前暴露；④iframe 场景显式设置 `SameSite=None; Secure; Partitioned`，并为不支持 CHIPS 的浏览器准备降级（顶层跳转/弹窗）。

```python
# 浏览器侧的 Cookie 前缀与 SameSite 规则(按 RFC6265bis 的写入约束模拟)
def accept_set_cookie(name, secure, path="/", domain=None, same_site="Lax"):
    # 前缀规则(大小写敏感, 必须精确匹配)
    if name.startswith("__Host-"):
        if not secure or path != "/" or domain is not None:
            return False, "violates __Host- (need Secure, Path=/, no Domain)"
    elif name.startswith("__Secure-"):
        if not secure:
            return False, "violates __Secure- (need Secure)"
    # SameSite=None 必须 Secure
    if same_site == "None" and not secure:
        return False, "SameSite=None requires Secure"
    return True, "ok"

cases = [
    ("__Host-sid", True, "/", None, "Lax", True),
    ("__Host-sid", True, "/", ".example.com", "Lax", False),
    ("__Host-sid", True, "/app", None, "Lax", False),
    ("__Host-sid", False, "/", None, "Lax", False),
    ("__Secure-sid", True, "/", ".example.com", "Lax", True),
    ("__Secure-sid", False, "/", ".example.com", "Lax", False),
    ("sid", True, "/", None, "None", True),
    ("sid", False, "/", None, "None", False),
    ("__Host-sid", True, "/", None, "None", True),
]
for name, secure, path, domain, ss, want in cases:
    ok, why = accept_set_cookie(name, secure, path, domain, ss)
    print("→", name, "domain=", domain, "path=", path, "secure=", secure, "samesite=", ss, "=>", ok, why)
    assert ok is want

# 前缀大小写敏感: __host- 不是受保护前缀
ok, _ = accept_set_cookie("__host-sid", False, "/", ".example.com", "Lax")
assert ok is True
print("→ 前缀区分大小写: __host- 不受保护")

# 子域写入: host-only Cookie 只属于设置它的主机
cookies = {}
def store(host, name, domain, value):
    key = (name, domain or host)
    cookies[key] = value

store("a.example.com", "__Host-sid", None, "A")      # host-only
store("b.example.com", "__Host-sid", None, "B")      # 另一个主机, 互不影响
assert cookies[("__Host-sid", "a.example.com")] == "A"
assert cookies[("__Host-sid", "b.example.com")] == "B"
print("→ __Host- 是 host-only, 子域之间不共享")

# 带 Domain 的 __Secure- 会被子域覆盖(cookie tossing 风险)
store("a.example.com", "__Secure-sid", ".example.com", "A")
store("evil.example.com", "__Secure-sid", ".example.com", "EVIL")
assert cookies[("__Secure-sid", ".example.com")] == "EVIL"
print("→ __Secure- + Domain 可被子域覆盖, 存在 cookie tossing 风险")

# 三方上下文: SameSite=None 只是入场券, CHIPS 需要 Partitioned
def third_party_allowed(same_site, secure, partitioned):
    return same_site == "None" and secure and partitioned

assert third_party_allowed("None", True, True)
assert not third_party_allowed("None", True, False)   # 无 Partitioned 会被拦
print("→ 三方嵌入需要 SameSite=None + Secure + Partitioned")
```

**追问一**：为什么 `__Host-` 不允许 `Domain`，而 `__Secure-` 允许？—— `Domain` 的作用是"把 Cookie 的作用域扩大到父域及所有子域"，这正好与 `__Host-` 的目标相反：它要保证"这个 Cookie 只能由当前主机写入、也只发给当前主机"，防止子域（哪怕是被人接管的测试子域）通过 `Set-Cookie` 覆盖主站的会话。`__Secure-` 的定位只是"必须走 HTTPS"，不限制作用域，所以允许 `Domain`——它防的是明文传输窃取，不防子域覆盖。二者解决的是不同威胁，不能混用。

**追问二**：`SameSite=None` 加了 `Secure` 还丢 Cookie，为什么？—— 三方 Cookie 的限制在近年收紧了：Chrome 的默认拦截、Safari 的 ITP、Firefox 的 TCP 都会阻止"未分区"的第三方 Cookie，即使你写了 `SameSite=None; Secure`。`Partitioned`（CHIPS）把 Cookie 按"顶层站点"分区存储，让嵌入方在各自的分区里拥有独立 Cookie，从而在满足隐私要求的前提下保留功能；代价是同一用户在不同顶层站点下不共享会话，跨站统计会失真。排查顺序：先看浏览器 DevTools 的 Cookie 面板是否显示 "Blocked" / "Partitioned"，再看响应头是否同时有 `Secure`、`SameSite=None`、`Partitioned`，最后确认是不是被 ITP 的"跨站跟踪"规则命中。

## 背诵要点

- `__Host-` 强制 Secure + Path=/ + 无 Domain（host-only），违反任一条浏览器静默丢弃；`__Secure-` 只强制 Secure，允许 Domain 但可被子域覆盖。
- `SameSite=None` 必须 Secure；三方嵌入还需 `Partitioned`（CHIPS），否则会被浏览器拦截。
- 跨子域共享只能在"__Secure- + Domain（有覆盖风险）"与"各子域独立 __Host-（更安全）"之间取舍。

## 复盘追问

- 给 `__Host-` 加 Domain 为什么会登录态全丢？（浏览器按前缀规则拒绝写入，服务端无感知，客户端每次都是新会话）
- iframe 里 Cookie 不生效，除了 SameSite 还差什么？（Secure、Partitioned/CHIPS，以及浏览器对三方 Cookie 的默认拦截）
