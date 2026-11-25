---
title: "[Q6097] JWT RS256/HS256 验签的 CPU 容量账"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6097 · JWT RS256/HS256 验签的 CPU 容量账

难度：P6-P7 | 标签：容量规划 | JWT | 验签算法

**问**：认证网关把 JWT 算法从 HS256 换成 RS256 后，高峰 CPU 涨了三倍。两种算法的验证成本差多少量级？这个差怎么进容量账？在"跨服务信任"与"单服务自签自验"下应该怎么选？

**答**：
结论：HS256（HMAC-SHA256）是对称哈希，验证一次微秒级（~1-5µs）；RS256（RSA-SHA256）验证是非对称签名验证，毫秒下限的数十微秒级（2048 位 key 约 20-60µs），加上 PEM 加载与 PyJWT 的解析开销，实测常见差 10-50 倍。容量账：QPS 10k 的认证路径，HS256 验签 CPU 占比可忽略，RS256 则可能吃掉 0.3-0.6 核——算法选择直接决定网关副本数。进一步：ES256（ECDSA P-256）验证比 RS256 便宜数倍且 key 短，是"需要非对称"时的性价比选项。
取舍：HS256 要求"验证方持有签名权"，多服务共享 secret 会放大泄露面；RS256/ES256 让资源服务器只用公钥验证，信任模型更干净但 CPU 更贵。缓存维度：验签结果无法缓存（每 token 不同），但可缓存 JWKS 公钥与"token→用户"的短 TTL 映射。
实战：容量推导公式 = QPS × 单次验签 CPU 秒；选型树——单服务自签自验用 HS256（512bit+ secret、走 KMS）；跨服务/第三方接入用 ES256 优先，RS256 兼容性需要时再上；公钥热缓存（JWKS 本地化 + kid 轮换）。

```python
# 基线：标准库 hashlib(HS256 形态) + pyca/cryptography(RS256)；
# 无 cryptography 时降级为纯标准库对照演示
import hashlib, hmac, time, base64, json

def hs256_verify(token_parts, secret):
    signing_input, sig_b64 = b".".join(token_parts[:2]), token_parts[2]
    expect = hmac.new(secret, signing_input, hashlib.sha256).digest()
    got = base64.urlsafe_b64decode(sig_b64 + b"=" * (-len(sig_b64) % 4))
    return hmac.compare_digest(expect, got)

def make_hs_token(payload: dict, secret: bytes):
    b64 = lambda o: base64.urlsafe_b64encode(o).rstrip(b"=")
    header = b64(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    body = b64(json.dumps(payload).encode())
    sig = hmac.new(secret, header + b"." + body, hashlib.sha256).digest()
    return header, body, b64(sig)

secret = b"k" * 64
tok = make_hs_token({"sub": "u1", "exp": 9999999999}, secret)
t0 = time.perf_counter()
N = 100_000
for _ in range(N):
    hs256_verify(tok, secret)
hs_us = (time.perf_counter() - t0) / N * 1e6
print(f"HS256 验签: {hs_us:.2f} us/次")

rs_us = None
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.exceptions import InvalidSignature
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pub_pem = key.public_key().public_bytes(serialization.Encoding.PEM,
                                            serialization.PublicFormat.SubjectPublicKeyInfo)
    pub = serialization.load_pem_public_key(pub_pem)
    signing_input = b".".join(tok[:2])
    sig = key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    t0 = time.perf_counter()
    M = 10_000
    for _ in range(M):
        pub.verify(sig, signing_input, padding.PKCS1v15(), hashes.SHA256())
    rs_us = (time.perf_counter() - t0) / M * 1e6
    print(f"RS256(2048) 验签: {rs_us:.1f} us/次  → 差 ≈ {rs_us/hs_us:.0f}x")
except ImportError:
    print("cryptography 未安装：pip install cryptography 后可实测 RS256 段")
    rs_us = hs_us * 30   # 经验量级

# 容量账：QPS → 核数
def capacity(qps, verify_us, budget=0.3, cores_per_pod=2):
    cpu_sec = qps * verify_us / 1e6            # 每秒验签 CPU 秒
    pods = cpu_sec / (cores_per_pod * budget)
    print(f"QPS {qps:>6,} × {verify_us:6.2f}us = {cpu_sec:.2f} 核/秒 "
          f"→ 按 {int(budget*100)}% CPU 预算需 ≈{pods:.1f} pods({cores_per_pod}核)")
for qps in (1_000, 10_000):
    capacity(qps, hs_us)
    if rs_us: capacity(qps, rs_us)

# 选型树输出
def choose(cross_service: bool, compat_rs256=False):
    if not cross_service:
        return "HS256：secret 走 KMS、>=512bit、轮换有版本"
    if compat_rs256:
        return "RS256：JWKS 本地缓存 + kid 轮换，容量按 30-50us/次推导"
    return "ES256 优先：验证比 RSA 便宜数倍，key 短"
print("单服务:", choose(False))
print("跨服务+兼容:", choose(True, True))
print("跨服务新系统:", choose(True))
```

**追问 1**：为什么验签结果不能缓存而 JWKS 可以？
- 追问 2 层：签名绑定了 token 全文（每次 token 不同），无法复用；JWKS 是"公钥集合"，按 kid 缓存到本地 + 定时刷新即可消除每次取公钥的网络往返。
- 追问 3 层：更激进的优化是缓存"token jti→验证结论"的短 TTL 表，收益大但引入撤销语义复杂度，要配合 jti 清单。

**追问 2**：ES256 为什么比 RS256 验证便宜？
- 追问 2 层：ECDSA P-256 的点运算复杂度低于 RSA 2048 的模幂，验证约几微秒到十几微秒；但**签名**侧 ECDSA 反而更贵（随机数+模逆），签发多的服务要反向算账。
- 追问 3 层：Ed25519 更快更短但 JWT 生态兼容性（某些老 SDK）弱，选型时把"下游 SDK 支持矩阵"列进去。

## 背诵要点
1. HS256 验签 1-5µs，RS256(2048) 20-60µs，差 10-50 倍；ES256 验证更便宜（签名更贵）。
2. 容量公式：QPS × 验签 µs / 1e6 = 核/秒；RS256 下 10k QPS 可能要加 pods。
3. 选型树：单服务 HS256+KMS；跨服务 ES256 优先，兼容需求才 RS256；公钥本地缓存消网络往返。

## 复盘追问
1. 为什么换算法的事故总在高峰爆发？——验签 CPU 与 QPS 线性，低峰看不出，高峰先挤爆认证网关。
2. 除了换算法还有什么降压手段？——网关验签后下发短期内部票据（HS256）给下游，RS256 只在边缘验一次。
