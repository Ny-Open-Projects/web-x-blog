---
title: [Q6040] JWT 验签的 CPU 成本账与公钥验签优化
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6040 · JWT 验签的 CPU 成本账与公钥验签优化

> 难度:★★★★ | 标签:成本工程, JWT, 验签, 容量

**问**：每个请求验一次 JWT，CPU 账有多大？RS256 与 HS256 的成本差多少？公钥验签能缓存吗——缓存了还怎么撤销？什么场景下验签成本会变成事故？

**答**：成本账：HS256（HMAC-SHA256）约 1-3µs/次（对称，几乎免费），RS256（RSA-2048 验签）约 50-100µs/次，ES256（ECDSA）约 100-200µs 验签但签名更小——RS256/ES256 是"每请求 5-10% CPU"的量级：单核 1000 QPS 的服务若每请求验 RSA，验签独占约 50-100ms/秒 ≈ 5-10% 单核，网关类服务（纯转发+鉴权）占比更高。事故触发面：1) 网关把验签做成每请求无缓存 + 高峰 QPS 翻倍 → 鉴权层 CPU 先满（鉴权是串行前置，满了整站挂）；2) jwks 远端拉取没有缓存/限频 → 上游 JWKS 端点抖动时每请求同步拉取（网络 IO + CPU 双炸）；3) token 很长（权限塞进 claims）→ Base64 解码 + JSON 解析成本叠加。优化矩阵：a) **公钥缓存**：jwks 按 kid 缓存（本地内存 + TTL/被动刷新），验签算法本身无状态可缓存结果吗？——**按 token 缓存验签结果（token 串 → 校验通过时的 exp 前有效）**是网关级优化，缓存 key 就是 token 本身（应用侧一般不做，防内存滥用）；b) **HS256 换算**：内网自签发+自验的服务可降级 HMAC（成本 1/50），代价是密钥分发与撤销面；c) **验签前置收敛**：网关验一次传递身份头（mTLS/内部签名，Q6021），业务服务免重复验签；d) claims 瘦身：token 只放 sub+scope 版本号。撤销与缓存的矛盾：结果缓存 TTL 必须 ≤ 撤销容忍窗口，配合黑名单/版本号（Q6009）。

```python
# file: code/03_Web后端开发/q6040_jwt_verify_cost.py
"""验签成本基准(纯 hashlib 近似) + jwks 公钥缓存 + 验签结果缓存.
真实 RS256 用 cryptography/pbjwt; 缺库时以 HMAC 量级对比演示."""
import hashlib
import hmac
import json
import time

def bench(fn, n: int = 10_000) -> float:
    t0 = time.perf_counter()
    for _ in range(n):
        fn()
    return (time.perf_counter() - t0) / n * 1e6   # µs/次

secret = b"k" * 32
payload = json.dumps({"sub": "u1", "scope": "read", "exp": 9999999999}).encode()

t_hmac = bench(lambda: hmac.new(secret, payload, hashlib.sha256).digest())
print(f"HMAC-SHA256(HS256 同量级): {t_hmac:.2f} µs/次")

# RS256 量级参考(实测请用 cryptography>=41): RSA-2048 verify ≈ 50-100µs
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    sig = key.sign(payload, padding.PKCS1v15(), hashes.SHA256())
    pub = key.public_key()
    t_rsa = bench(lambda: pub.verify(sig, payload, padding.PKCS1v15(),
                                     hashes.SHA256()), n=2000)
    print(f"RSA-2048 验签(RS256 同量级): {t_rsa:.1f} µs/次  -> 比对称贵 ~{t_rsa/t_hmac:.0f} 倍")
    HAS_ASYM = True
except ImportError:
    HAS_ASYM = False
    print("(cryptography 未安装, 以参考值 RSA-2048≈50-100µs 计算容量账)")

# --- jwks 公钥缓存: 按 kid, TTL + 被动刷新 ---
class JWKSCache:
    def __init__(self, ttl: float = 300.0) -> None:
        self.keys: dict[str, object] = {}
        self.fetched_at = 0.0
        self.ttl = ttl

    def get(self, kid: str, fetch) -> object:
        now = time.monotonic()
        if not self.keys or now - self.fetched_at > self.ttl:
            self.keys = fetch()                       # 远端 jwks(带限频)
            self.fetched_at = now
        key = self.keys.get(kid)
        if key is None:                               # 未知 kid: 强刷一次(轮换)
            self.keys = fetch()
            self.fetched_at = now
            key = self.keys.get(kid)
        if key is None:
            raise ValueError("unknown kid")
        return key

# --- 验签结果缓存: token -> exp 前有效 (网关级优化) ---
class VerifyResultCache:
    def __init__(self, cap: int = 10_000) -> None:
        self.cache: dict[str, float] = {}    # token -> 通过时的 exp
        self.cap = cap

    def check(self, token: str, exp: float, verify) -> bool:
        now = time.monotonic()
        hit = self.cache.get(token)
        if hit is not None and hit > now:
            return True
        ok = verify(token)
        if ok:
            if len(self.cache) >= self.cap:  # 简单容量护栏(生产用 LRU)
                self.cache.clear()
            self.cache[token] = min(exp, now + 30)  # TTL<=撤销容忍窗口
        return ok

cache = JWKSCache(ttl=300)
cache.get("k1", lambda: {"k1": "pubkey-object"})     # 首次拉取
print("jwks 缓存命中(kid=k1):", cache.get("k1", lambda: {"k1": "pubkey-object"}))

vc = VerifyResultCache(cap=100)
verify_fn = lambda tok: tok == "good-token"
print("结果缓存首次验签:", vc.check("good-token", exp=time.time() + 60,
                                      verify=verify_fn))
print("结果缓存二次(免验签):", vc.check("good-token", exp=time.time() + 60,
                                        verify=verify_fn))
print(f"容量账: 单核 1000QPS x RSA 100µs ≈ 10% 单核只做验签; HS256≈0.3%")
```

**追问**：1) 为什么验签结果可以缓存而撤销语义不破？——缓存的 TTL 是"撤销容忍窗口"的显式选择：接受最多 N 秒的撤销延迟换 N 倍 CPU；黑名单/版本号（Q6009）要在缓存命中路径里检查，否则缓存把撤销也缓存了。2) ES256 与 RS256 怎么选？——ES256 验签略贵但密钥/token 更小、算力抗量子前向性讨论不同；移动端/嵌入设备在意 token 体积选 ES256，纯服务端选 RS256 差别不大，**成本敏感选 HS256（同信任域）**。3) 验签成本怎么进监控？——把"鉴权层 CPU 占比""jwks 拉取次数"做成独立指标，与总 CPU 配额对账；jwks 拉取次数异常=上游抖动或 kid 轮换风暴的前兆。

## 背诵要点
- 成本量级：HS256 ≈1-3µs、RSA-2048 验签 ≈50-100µs（约 50 倍）；每请求验 RSA 占单核 5-10%。
- 优化链：jwks 按 kid+TTL 缓存 → 网关验一次传身份头 → 结果缓存（TTL≤撤销容忍窗）→ HS256 同域降级。
- 事故面：鉴权层 CPU 先满、jwks 无限频拉取、超长 token 解码叠加；拉取次数要独立监控。

## 复盘追问
- 你的鉴权中间件 CPU 占比是多少？超过多少就该启动"网关统一验签"的改造？
- 撤销容忍窗口从 0 秒放宽到 30 秒，业务侧哪些场景（支付/权限变更）会反对？怎么分级？
