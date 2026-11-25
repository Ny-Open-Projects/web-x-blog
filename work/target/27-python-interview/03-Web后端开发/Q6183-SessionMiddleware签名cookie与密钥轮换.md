---
title: "[Q6183] SessionMiddleware 的签名 cookie：轮换密钥即全员登出"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6183 · SessionMiddleware 的签名 cookie：轮换密钥即全员登出

难度：P6 ｜ 标签：Starlette、SessionMiddleware、签名、密钥轮换、SameSite

**问**：用 Starlette 的 `SessionMiddleware` 存登录态，安全扫描要求每季度轮换 `SECRET_KEY`。结果一轮换，所有用户被踢下线，客服电话被打爆。签名 cookie 为什么不能"平滑换钥"？它明明能防篡改，为什么又说"无法即时让某个会话失效"？`https_only` / `same_site` 该怎么配？

**答**：
结论：这类 session 是 `base64(payload) + HMAC 签名`，服务端**不存任何状态**，校验只依赖密钥。换密钥 → 旧 cookie 的签名全部对不上 → 全员登出，这是设计使然，不是 bug。同一个设计也带来"无法吊销"：用户登出只能删自己的 cookie，如果 cookie 被复制走（或攻击者本地保存），服务端没有任何手段让它立即失效，只能等 `max_age` 过期。payload 只是 base64，没有加密，里面的内容任何人可读。

取舍：无状态 cookie 的优点是零存储、易水平扩展、抗 Redis 故障；代价是"不可吊销 + 不可平滑轮换 + 明文可读"。需要"改密码立刻踢下线 / 禁用账号立即生效 / 权限变更即时生效"就必须服务端存储（Redis session，或只存 session id + 服务端查表），或者接受"短 TTL + refresh token"的折中。密钥轮换要平滑，得支持"新签旧验"（多密钥校验），Starlette 原生只有单密钥，要自己包一层。

实战：事故形态是"季度合规轮换密钥，凌晨全站用户掉线，监控看到 401 尖刺"。另一个隐蔽事故是"把手机号/角色塞进 session 想省一次查询"，结果角色降级后用户在 TTL 内仍是管理员。下面用 hmac 复刻签名/校验：改 payload、换密钥、伪造签名分别会怎样，以及 payload 为什么是明文。

```python
import base64
import hashlib
import hmac
import json
import time

SECRET = b"k1"


def b64e(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def b64d(txt):
    pad = "=" * (-len(txt) % 4)
    return base64.urlsafe_b64decode(txt + pad)


def sign(data, secret):
    return hmac.new(secret, data, hashlib.sha256).hexdigest()[:16]


def dump(payload, secret=SECRET):
    body = b64e(json.dumps(payload, separators=(",", ":")).encode())
    return f"{body}.{sign(body.encode(), secret)}"


def load(cookie, secret=SECRET):
    body, _, sig = cookie.rpartition(".")
    if not hmac.compare_digest(sign(body.encode(), secret), sig):
        raise ValueError("bad signature")
    return json.loads(b64d(body))


c = dump({"uid": 42, "exp": time.time() + 3600})
print("[1] cookie:", c)
print("[2] 正常校验:", load(c))

body, _, sig = c.rpartition(".")
forged_body = b64e(json.dumps({"uid": 1, "exp": time.time() + 3600},
                             separators=(",", ":")).encode())
try:
    load(f"{forged_body}.{sig}")     # 换 payload、沿用旧签名
except ValueError as e:
    print("[3] 篡改 payload 保留旧签名 ->", e)

try:
    load(c, secret=b"k2")
except ValueError as e:
    print("[4] 轮换密钥后旧 cookie 全部失效 ->", e, "（用户被迫重新登录）")

forged = dump({"uid": 1, "exp": time.time() + 3600}, secret=b"")
try:
    load(forged)
except ValueError as e:
    print("[5] 只签名不加密：payload 明文可读，空密钥伪造会被识破 ->", e)

print("[6] cookie 是签名不是加密，payload 直接可读:",
      json.loads(b64d(c.split('.')[0])))
```

**追问一**：密钥轮换怎么做才不踢人？—— 校验时依次尝试 `[新密钥, 旧密钥]`，签发一律用新密钥；等旧 cookie 的最大 TTL 过去再移除旧密钥。这要求自己实现中间件（Starlette 的 `SessionMiddleware` 只接受一个 `secret_key`），或者在网关层做双 cookie 迁移。另一种是"版本化密钥"：cookie 里带 `kid`，服务端按 kid 选密钥，轮换就是加新 kid、保留旧 kid 一段时间。

**追问二**：为什么 payload 明文可读还不算漏洞？—— 机密性靠"不放敏感数据"保证，完整性靠 HMAC。真正的风险是两类：a) 把手机号、身份证、内部角色放进去 → 等于公开；b) 把"权限"放进去 → 权限变更在 TTL 内不生效（越权窗口）。所以 cookie session 只该放 `uid` + 过期时间这类"即使泄露也不敏感、且不需要即时失效"的字段。

## 背诵要点
- 签名 cookie = base64(明文 payload) + HMAC；服务端无状态，校验只依赖密钥。
- 换密钥 = 旧 cookie 全部失效（全员登出）；无状态也意味着无法吊销单个会话，只能等过期。
- 平滑轮换需"新签旧验 + kid"，需自研中间件；敏感/权限数据不要放进去。

## 复盘追问
- 轮换 SECRET_KEY 后全员掉线，如何设计平滑轮换？（多密钥校验、kid、TTL 窗口）
- 用户改密码后旧 cookie 仍可用，如何在不改成服务端 session 的前提下缓解？（短 TTL、版本号校验、黑名单）
