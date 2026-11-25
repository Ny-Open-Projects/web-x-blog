---
title: "[Q6171] JWT 时钟偏移与 leeway 的重放窗口"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6171 · JWT 时钟偏移与 leeway 的重放窗口

难度：P6 ｜ 标签：JWT、exp、nbf、时钟偏移、leeway、重放

**问**：一批 Pod 的 NTP 漂了 5 分钟，用户拿刚签发的 JWT 调接口大量 401；运维把校验的 `leeway` 调到 600 秒后恢复，但安全团队立刻反对。`exp/nbf` 用的是谁的时间？`leeway` 到底放宽了什么？为什么"调大 leeway"既是止血也是扩大重放窗口？容器环境里应该怎么治理时钟，而不是靠 leeway 兜底？

**答**：
结论：JWT 的 `exp`（过期时间）、`nbf`（生效时间）、`iat`（签发时间）都是 NumericDate（UTC 秒），校验时用**校验方自己的墙上时钟**比较；签发方和校验方时钟不一致，就会把"还没过期"判成过期（或反过来让已过期 token 继续可用）。`leeway` 给两边各加一个容差：`now > exp + leeway` 才算过期、`now + leeway < nbf` 才算未生效。它解决的是"小幅漂移"，不是"时钟坏了"：leeway=600 意味着一个已经过期 10 分钟的 token 仍被接受——如果 token 被窃取，攻击者多了 10 分钟重放窗口；如果 token 本来只有 15 分钟寿命，等于寿命延长 2/3。

取舍：leeway 一般 30~60 秒，覆盖 NTP 抖动/容器启动瞬间的偏差；同时监控 `now - iat` 的分布和节点时钟偏移（chrony/ntpd 的 offset 指标），把"漂移"当故障修，而不是把 leeway 越调越大。高安全场景用短 `exp` + refresh token + 服务端撤销列表（Q6009），不要用长 leeway 换可用性。时钟源要用 UTC 墙上时钟（`time.time()`），不能用 `time.monotonic()`——后者起点任意，和 JWT 的 Unix 时间没有可比性。

实战：事故形态是"新扩容的节点时钟慢 5 分钟，签发的 token 在旧节点看来'来自未来'（`iat`/`nbf` 不通过），登录后立刻 401"。下面用 HS256 手写一个最小 JWT，展示：服务器慢 5 秒、leeway=0 时合法 token 被判过期；leeway=30 恢复；但一个已经过期 20 秒的 token 也会被 leeway=30 放行——这就是重放窗口。

```python
import base64
import hashlib
import hmac
import json
import time

KEY = b"demo-secret"


def b64(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def issue(payload):
    head = b64(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    body = b64(json.dumps(payload, separators=(",", ":")).encode())
    sign = b64(hmac.new(KEY, f"{head}.{body}".encode(), hashlib.sha256).digest())
    return f"{head}.{body}.{sign}"


def verify(token, now, leeway=0):
    head, body, sign = token.split(".")
    want = b64(hmac.new(KEY, f"{head}.{body}".encode(), hashlib.sha256).digest())
    if not hmac.compare_digest(sign, want):
        return "bad-signature"
    payload = json.loads(base64.urlsafe_b64decode(body + "=" * (-len(body) % 4)))
    if "exp" in payload and now > payload["exp"] + leeway:
        return "expired"
    if "nbf" in payload and now + leeway < payload["nbf"]:
        return "not-yet-valid"
    return "ok"


token = issue({"sub": "u-1", "exp": 1_000, "nbf": 990})
print("服务器慢 5 秒，leeway=0 :", verify(token, now=1_005, leeway=0))
print("服务器慢 5 秒，leeway=30:", verify(token, now=1_005, leeway=30))
print("已过期 20 秒，leeway=30:", verify(token, now=1_020, leeway=30))
print("已过期 31 秒，leeway=30:", verify(token, now=1_031, leeway=30))
```

**追问一**：为什么不能直接用 token 里的 `iat` 当"当前时间"来算 `exp`？——`iat` 是签发方写的，攻击者可以伪造（在签名有效的前提下，只有签发方能改，但时钟本身可能错）；用它算 `exp - iat` 只能得到"寿命"，不能判断"现在是否过期"。过期判断必须用校验方的可信时钟。若担心签发方时钟错，应在签发侧监控 `iat` 与网关时间的偏差，而不是在校验侧用 `iat` 替代 `now`。

**追问二**：`nbf` 和 `iat` 有什么区别，为什么两个都要？——`iat` 表示"签发时刻"，`nbf` 表示"最早可用时刻"，二者可以不同（比如提前签发、延迟生效）。校验通常只强制 `exp`，`nbf` 可选；如果业务需要"延迟生效"（预约、生效窗口），必须校验 `nbf`，并给它和 `exp` 同样的 leeway。`iat` 更多用于审计/`max_age` 判断（"签发超过 N 分钟必须重新认证"），不要把它当 `nbf` 用。

## 背诵要点
- `exp/nbf/iat` 是 UTC 秒，校验用**校验方**墙上时钟；时钟漂移会导致合法 token 401 或过期 token 可用。
- `leeway` 是双向容差，30~60 秒合理；调大等于扩大重放窗口、延长 token 实际寿命。
- 用 `time.time()` 不用 `monotonic`；治理 NTP/chrony 偏移，短 exp + 撤销列表，而不是无限加 leeway。

## 复盘追问
- 新节点时钟慢 5 分钟导致登录即 401，如何用 `iat/nbf/exp` 与 leeway 解释并治理？（签发/校验时钟、容差、NTP 监控）
- 为什么把 leeway 调到 600 秒能止血但危险？（过期 token 多活 10 分钟、重放窗口、短 token 寿命被大幅延长）
