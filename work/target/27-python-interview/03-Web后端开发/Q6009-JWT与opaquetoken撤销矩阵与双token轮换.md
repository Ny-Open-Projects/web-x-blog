---
title: [Q6009] JWT 与 opaque token 撤销矩阵与双 token 轮换
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6009 · JWT 与 opaque token 撤销矩阵与双 token 轮换

> 难度:★★★ | 标签:JWT, opaque token, 认证设计

**问**：JWT 无状态不可撤销，opaque token 每请求查库，两者怎么选？「双 token 轮换」具体怎么设计，refresh token 泄露怎么检测？

**答**：按撤销需求选型，先摆矩阵：| 能力 | opaque | JWT |——撤销：opaque 删存储即生效；JWT 只能等 exp，补救靠黑名单（存被撤销的 jti，集合小）或用户级版本号（`user.token_version` 进 claims，比对不一致即拒）；每请求成本：opaque 查一次缓存/库；JWT 本地验签零查库（网关友好）；泄露面：opaque 随机串无信息；JWT payload base64 可读（别放敏感字段）。**双 token 轮换**是两者的合体：access（JWT，短命 5-15min，无状态验签承担 99% 请求）、refresh（opaque，长命，有状态可撤销，承担 1% 的换发请求）。轮换规则：1) refresh 一次性消费——换发即作废旧 refresh、签发新 refresh；2) **泄露检测靠重放**：已作废的 refresh 被再次使用 = 该会话令牌泄露，处置是撤销整个 refresh 家族（用户全部会话），宁可误伤不可放过；3) 并发竞态宽容：前端多标签页同时拿旧 refresh 换发会造成误杀，给旧 refresh 一个秒级宽限期（已作废但 5s 内可重放一次并返回同一对新 token）。决策线：能接受每请求查 Redis → opaque 全套最简单可靠；必须网关本地鉴权 → JWT + 短 exp + jti 黑名单兜底。

```python
# 基线:Python 3.9+ 标准库实现(hmac 签名的 JWT-like token);生产可用 pyjwt 2.x 替换签名/验签。
import base64, hashlib, hmac, json, time

SECRET = b"demo-secret"   # 生产:从密管注入,且支持轮换(按 kid 取钥)

def b64u(d): return base64.urlsafe_b64encode(d).rstrip(b"=").decode()
def b64u_dec(s): return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))

def sign_jwt(claims):
    h, p = b64u(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()), b64u(json.dumps(claims).encode())
    sig = hmac.new(SECRET, f"{h}.{p}".encode(), hashlib.sha256).digest()
    return f"{h}.{p}.{b64u(sig)}"

def verify_jwt(token):
    h, p, s = token.split(".")
    if not hmac.compare_digest(b64u(hmac.new(SECRET, f"{h}.{p}".encode(), hashlib.sha256).digest()), s):
        return None                                     # 签名不符:恒定时间比较防 timing
    claims = json.loads(b64u_dec(p))
    if claims["exp"] < time.time(): return None         # 过期
    return claims

# ---- 双 token 轮换 + 泄露检测(重放即撤销全家) ----
refresh_store = {}     # refresh_id -> {"family": uid, "used": bool, "rotated_at": ts}
revoked_families = set()

def login(uid):
    r_id = b64u(hashlib.sha256(f"{uid}-{time.time()}".encode()).digest()[:16])
    refresh_store[r_id] = {"family": uid, "used": False, "rotated_at": 0}
    access = sign_jwt({"sub": uid, "exp": int(time.time()) + 600})   # access 10min
    return access, r_id

def rotate(r_id):
    st = refresh_store.get(r_id)
    if st is None or st["family"] in revoked_families:
        return None
    if st["used"]:                                       # 重放检测
        revoked_families.add(st["family"])               # 整个会话家族撤销
        return None
    st["used"] = True                                    # 一次性消费
    new_r = b64u(hashlib.sha256(f"rot-{time.time()}".encode()).digest()[:16])
    refresh_store[new_r] = {"family": st["family"], "used": False, "rotated_at": time.time()}
    return sign_jwt({"sub": st["family"], "exp": int(time.time()) + 600}), new_r

access, r1 = login("alice")
print("验签:", verify_jwt(access)["sub"])
res = rotate(r1); print("首次换发成功:", res is not None)
print("旧 refresh 重放(=泄露信号):", rotate(r1), "→ alice 家族已整体撤销")
print("家族撤销后整个家族的任何 refresh 均失效:", revoked_families == {"alice"})
```

**追问**：
1) 黑名单方案下网关还「零查库」吗？——退化成「正常路径查缓存黑名单（本地缓存摊薄）+验签」，仍有优势：黑名单集合极小、可本地缓存，且只查异常令牌；更进一步是 token_version 只在用户登出全部/改密时递增，正常令牌根本不进名单。
2) access token 有效期内的「撤销延迟」怎么向业务解释？——接受事实：JWT 撤销延迟 ≈ access 剩余寿命（≤15min），高危操作（改密、支付）要在资源侧二次校验（版本号或最近认证时间），而不是指望 access 立刻失效。
3) refresh token 存储放哪？——服务端加密存库（可撤销的事实源）；客户端 refresh 用 HttpOnly+Secure+SameSite cookie 或安全存储，绝不进 localStorage；多设备登录每个设备一个 family，泄露只撤销对应家族，别一刀切全登出。
