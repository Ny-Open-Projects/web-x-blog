---
title: "[Q6172] JWT 只验签不校验 aud/iss 的跨服务混用"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6172 · JWT 只验签不校验 aud/iss 的跨服务混用

难度：P6-P7 ｜ 标签：JWT、aud、iss、trust boundary、越权

**问**：内部服务都用同一套 HMAC 密钥签 JWT，网关只做"验签通过就放行"。为什么拿到一个普通业务服务的 token，就能直接调管理后台的接口？签名明明是对的，`sub` 也确实是本人。`aud` 和 `iss` 分别约束什么？为什么"共享密钥 + 只验签"等于把所有服务的权限边界抹平？改成非对称密钥就够了吗？

**答**：
结论：签名只证明"这个 token 由持有密钥的一方签发"，不证明"这个 token 是发给当前服务的"。`aud`（audience）限定接收方，`iss`（issuer）限定签发方；只验签不校验 `aud/iss`，任何持有同一密钥的服务签出的 token 都能被其他服务接受——业务服务的 token 可以调管理接口，测试环境的 token 可以调生产。共享 HMAC 密钥时更糟：每个服务都能**签发**任意服务的 token，密钥泄露面也随服务数量放大。Q6021 从架构层比较 mTLS/内部 JWT/静态 token 的取舍，本题专攻“校验方省略 aud/iss”这一具体越权。正确做法是：密钥按信任域隔离（最好每个服务一对非对称密钥），校验方强制校验 `aud` 包含自己、`iss` 等于预期签发方，并把 `typ`/`azp` 纳入判断。

取舍：非对称（RS256/ES256）让"签发"和"校验"分离，服务只拿公钥，泄露公钥无法伪造；但公钥轮换/`kid` 缓存（Q1906）和多服务多密钥管理会复杂。共享密钥只适合单一信任域内的短生命周期 token，且必须配合 `aud` 白名单。`aud` 可以是字符串或数组，多受众 token 要显式声明；不要用"把 aud 塞进自定义 claim 但校验方不看"的假动作。

实战：事故形态是"内部渗透测试用一个低权限业务的 token 调 `/admin/users` 成功，因为 admin 服务只调了 `jwt.decode(..., algorithms=['HS256'])`"。下面用同一密钥签一个 `aud=svc-billing` 的 token，展示：只验签的 search 服务接受；校验 `aud` 后拒绝；`iss` 不符也拒绝。

```python
import base64
import hashlib
import hmac
import json

KEY = b"shared-key"


def b64(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def issue(payload):
    head = b64(json.dumps({"alg": "HS256"}).encode())
    body = b64(json.dumps(payload).encode())
    sign = b64(hmac.new(KEY, f"{head}.{body}".encode(), hashlib.sha256).digest())
    return f"{head}.{body}.{sign}"


def decode(token):
    _, body, _ = token.split(".")
    return json.loads(base64.urlsafe_b64decode(body + "=" * (-len(body) % 4)))


def check(token, expect_aud=None, expect_iss=None, verify_sign=True):
    if verify_sign:
        head, body, sign = token.split(".")
        want = b64(hmac.new(KEY, f"{head}.{body}".encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(sign, want):
            return "bad-signature"
    payload = decode(token)
    if expect_aud:
        aud = payload.get("aud")
        auds = aud if isinstance(aud, list) else [aud]
        if expect_aud not in auds:
            return "bad-aud"
    if expect_iss and payload.get("iss") != expect_iss:
        return "bad-iss"
    return "ok"


token = issue({"sub": "u-1", "aud": "svc-billing", "iss": "auth.example.com"})
print("billing 服务（校验 aud）:", check(token, expect_aud="svc-billing"))
print("search  服务（只验签）  :", check(token))
print("search  服务（校验 aud）:", check(token, expect_aud="svc-search"))
print("iss 不符               :", check(token, expect_aud="svc-billing", expect_iss="evil.example.com"))
```

**追问一**：`aud` 是数组时怎么校验？多受众 token 会不会扩大攻击面？——数组表示"这张 token 同时发给多个服务"，校验方只要判断自己是否在数组里；但多受众意味着任何其中一个服务被攻破，token 都能被拿去调其他受众，违背最小权限。实践上尽量一服务一 `aud`，确需共享时用短 `exp` + 明确的信任域，并在日志里记录 `aud` 以便审计。

**追问二**：换成 RS256、每个服务独立密钥后，还需要 `aud/iss` 吗？——需要。非对称解决的是"不能伪造"，不解决"发错对象"：如果所有服务都信任同一个 IdP 的公钥，IdP 给业务 A 签的 token 在业务 B 看来签名同样有效。`aud` 是"这张票是给谁的"，`iss` 是"谁卖的票"，两者是签名之外的授权边界；此外还要校验 `alg` 不被降级（Q6120 的算法混淆）。

## 背诵要点
- 签名只证明签发者持钥，不证明 token 发给当前服务；必须校验 `aud` 包含自己、`iss` 等于预期签发方。
- 共享 HMAC 密钥 = 每个服务都能签发其他服务的 token；按信任域隔离密钥，优先非对称 + `kid` 轮换。
- `aud` 可为数组，但多受众扩大攻击面；一服务一 `aud`、短 exp，并校验 `alg` 防降级。

## 复盘追问
- 低权限业务 token 能调管理接口，如何用"只验签不校验 aud"解释并修复？（aud/iss、密钥隔离、非对称）
- 为什么换成 RS256 仍不能省掉 `aud`？（签名只证签发者，不证受众；同一 IdP 多服务共享公钥）
