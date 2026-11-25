---
title: "[Q6100] HTTP 多值头与重复头的语义陷阱"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6100 · HTTP 多值头与重复头的语义原理（getlist/逗号折叠）

难度：P6 | 标签：原理深挖 | HTTP 头 | 解析

**问**：网关加了 `X-Forwarded-For` 后业务取到内网 IP；`Accept` 头在有些客户端是重复多行、有些是逗号串。HTTP 头的"多值"到底有几种形态？ASGI/Starlette 怎么表示与解析，不同框架读法差在哪里会出事故？

**答**：
结论：多值头有两种**不等价**的形态：① 同名重复行（多个 `Set-Cookie`、多个 `X-Forwarded-For`）；② 单行逗号分隔（`Accept: a, b`）。规范上只有部分头（Cookie 例外！）允许逗号折叠：`Set-Cookie` 的值本身可含逗号（Expires 日期），折叠会撕碎语义；`X-Forwarded-For` 是"每代理一行追加"，网关可能合并也可能追加。ASGI 层 headers 是 `(name, value)` 的字节对列表——重复头天然保留；Starlette 的 `Headers` 提供 `headers["x"]`（取**第一个**匹配）与 `headers.getlist("x")`（全量）。事故模式：业务用 `headers["x-forwarded-for"]` 只拿到链路上**第一个**代理写的外层 IP，攻击者伪造的第一跳被当成客户端地址——必须从**最右**（最后一跳代理追加、不可伪造）取可信值。
取舍：读头的决策要区分"单值头"（Content-Type，重复即协议错误）与"列表头"（XFF/Cache-Control 指令/ Accept），用 getlist + 明确的合并策略；写头（Set-Cookie）必须逐条 add 而不能逗号拼接。
实战：XFF 解析三步：取 getlist("x-forwarded-for") 的最后一项 → 与 `X-Real-IP`/可信代理白名单交叉验证 → 中间件统一注入 `request.state.client_ip`，业务层不再自行读头。

```python
from email.message import Message
from email.parser import BytesParser
from email.policy import default as default_policy
from email.headerregistry import HeaderRegistry

# 用标准库 email.message 模拟 HTTP 头语义（其 MIME 头折叠语义与 HTTP 同源）
msg = Message()
msg["x-forwarded-for"] = "203.0.113.9, 198.51.100.7"
msg["x-forwarded-for"] = "10.0.0.5"        # 追加第二个同名头
msg["accept"] = "text/html"
msg["accept"] = "application/json"

print("重复同名头全部可见:", msg.get_all("x-forwarded-for"))
print("默认 get 取第一个:", msg.get("x-forwarded-for"), "← 事故源：可能是伪造外层")
xff = msg.get_all("x-forwarded-for")
print("正确取值：最右侧一项 =", xff[-1].split(",")[-1].strip(), "(由最后一跳可信代理写入)")

# ASGI 层：headers 是 (name, value) 字节对列表，重复天然保留
scope_headers = [
    (b"x-forwarded-for", b"203.0.113.9, 198.51.100.7"),
    (b"x-forwarded-for", b"10.0.0.5"),
    (b"content-type", b"application/json"),
]
class FakeHeaders:
    def __init__(self, raw):
        self.raw = raw
    def __getitem__(self, k):        # Starlette 语义：第一个匹配
        kk = k.lower().encode()
        for n, v in self.raw:
            if n == kk: return v.decode()
        raise KeyError(k)
    def getlist(self, k):            # Starlette 语义：全量
        kk = k.lower().encode()
        return [v.decode() for n, v in self.raw if n == kk]

h = FakeHeaders(scope_headers)
print("headers['x-forwarded-for'] =", h["x-forwarded-for"])
print("headers.getlist =", h.getlist("x-forwarded-for"))

# 逗号折叠陷阱：Set-Cookie 值内含逗号，不能合并
sc1 = "a=1; Expires=Wed, 21 Oct 2026 07:28:00 GMT"
sc2 = "b=2; Path=/"
raw_cookie = [(b"set-cookie", sc1.encode()), (b"set-cookie", sc2.encode())]
joined = ", ".join(v.decode() for _, v in raw_cookie)
print("折叠会撕碎 Expires:", joined)
print("正确：逐条 add_cookie，headers.getlist('set-cookie') 逐条解析")

# 单值头重复 = 协议错误，应拒绝而不是静默取一
if len(h.getlist("content-type")) > 1:
    print("content-type 重复 → 400（RFC 9110 单值语义）")
```

**追问 1**：为什么 Cookie 头不能按逗号折叠而 Accept 可以？
- 追问 2 层：Cookie 值允许包含逗号（历史上有 cookie2、日期字段），逗号不是无歧义分隔符；Accept 这类列表头的值本身用逗号分隔且元素不含裸逗号（q 值有分号参数）。
- 追问 3 层：通用解析策略：先 getlist 拿全部行，再逐行按"该头自己的语法"解析；别用一把逗号 split 吃所有头。

**追问 2**：代理链上 XFF 的可信边界怎么设计？
- 追问 2 层：只有"可信代理"追加的条目可信，最右第一项即客户端声称地址之前的最后一个代理视角；可信代理白名单（CIDR）之外的条目视为可伪造。
- 追问 3 层：更稳的是边缘层直接写 `X-Real-IP`/`CF-Connecting-IP` 单值头并在网关剥离外部传入的同名头，业务只读这一个头。

## 背诵要点
1. 多值头两形态：同名重复行（ASGI 列表保留）与单行逗号串；Starlette `headers[k]` 取第一个、`getlist` 全量。
2. XFF 从右往左信任：最右条目是最后可信代理写入，用 getlist[-1]+白名单，别信第一个。
3. Set-Cookie 禁止逗号折叠（值含逗号），写入方逐条 add；单值头重复应 400。

## 复盘追问
1. 为什么"取到内网 IP"的事故总在加网关后出现？——应用原来直连取 remote addr，上代理后 XFF 存在且取错了位置（第一个/没剥离外部伪造）。
2. 重复 Content-Type 为什么会静默通过某些栈？——ASGI 服务器与框架各自取头策略不同（first/last/join），要在网关层做规范化拦截。
