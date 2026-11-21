---
title: [Q6021] 服务间认证：mTLS 底座 + 内部 JWT 授权的组合
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6021 · 服务间认证：mTLS 底座 + 内部 JWT 授权的组合

> 难度:★★★★☆ | 标签:服务间认证, mTLS, 内部 JWT

**问**：内网"环境隔离=安全"在零信任模型下为什么不成立？服务间认证的三层方案——静态共享 token、网关签发的内部 JWT、mTLS——在轮换/撤销/授权粒度上怎么比较？为什么成熟架构是"mTLS 做身份底座 + 内部 JWT 做授权"，而不是二选一？mTLS 终结点（网关/sidecar）把证书身份传给业务服务时，最大的坑是什么？

**答**：内网一台失陷，"无认证内网"就是横向移动的高速路。三层方案对比：1) **静态共享 token**：实现最简，但轮换=全量发版、撤销=殃及所有调用方、无身份粒度——只防"陌生人"，防不了"已进网的邻居"；2) **内部 JWT**（调用方向 auth 服务换发短效 service token，含 sub/scope/exp/aud）：轮换=换签发密钥（kid 轮换，Q1906）、撤销靠短 TTL+黑名单（Q6009）、scope 可细到接口级（Q1909）——但它是**bearer 凭据**，被抓即可重放，传输层要 TLS 兜底；3) **mTLS**：身份绑定到密钥对（私钥不出配置、不在网络上传输任何可被抓的字符串），撤销=短有效期证书自动重签或吊销（cert-manager/SPIFFE 是成熟运维面），握手机制本身见 Q695——但它只有"服务身份"，**授权粒度到不了接口级**。所以成熟组合是两层互补：**mTLS 证明"这条连接来自哪个服务"（身份底座），内部 JWT 证明"这次调用被授权做什么"（scope/用户上下文）**。最大的坑在**身份透传**：网关终结 mTLS 后必须**重新签发**内部令牌（把证书里的服务身份写进 sub），绝不能透传"调用方自报身份"的头——那等于允许伪造（与 X-Forwarded-For 信任链同理，Q2186）。

```python
# file: code/03_Web后端开发/q6021_service_auth.py
import base64, hashlib, hmac, json, time

def b64u(d) -> str:
    raw = json.dumps(d, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()

def issue_internal_jwt(sub: str, scope: str, ttl: int = 300, key: bytes = b"k1-secret"):
    """auth 服务在 mTLS 连接上签发内部令牌: 身份底座之上再给授权粒度"""
    body = b64u({"alg": "HS256", "typ": "JWT", "kid": "k1"}) + "." + \
           b64u({"sub": sub, "scope": scope, "aud": "internal",
                 "exp": int(time.time()) + ttl})
    sig = hmac.new(key, body.encode(), "sha256").digest()
    return body + "." + base64.urlsafe_b64encode(sig).rstrip(b"=").decode()

def gateway_relay(cert_identity: str, scope: str) -> str:
    """mTLS 终结点(网关/sidecar)把证书身份转为内部令牌:
       必须重新签发,绝不能透传调用方自报的头(伪造注入点)"""
    if not cert_identity.startswith("spiffe://"):
        raise ValueError("拒绝: 不是内部 CA 证书里的 SAN URI 身份")
    return issue_internal_jwt(cert_identity, scope)

token = gateway_relay("spiffe://prod/ns/app/sa/orders", "orders:read orders:write")
print("内部令牌(前 48 字符):", token[:48], "...")
print("方案矩阵:")
for name, rotate, revoke, granularity in [
    ("静态 token", "轮换=全量发版", "撤销=殃及全体", "无"),
    ("内部 JWT", "换签发密钥", "短 TTL+黑名单", "scope 接口级"),
    ("mTLS", "证书自动重签", "吊销/短 TTL", "服务级(握手见 Q695)"),
]:
    print(f"  {name:<10} {rotate:<14} {revoke:<14} {granularity}")
print("结论: mTLS 身份底座(证明连接来自谁) + 内部 JWT 授权(证明被允许做什么)")
```

**追问**：1) 内部 JWT 为什么不直接用 HS256 长效密钥？——HS256 的验签方必须持有签名密钥，任何一个验证服务失陷即可伪造所有人的令牌；内部规模上去后换 RS256/ES256 非对称（验签方只持公钥，Q114），kid 管理轮换。2) mTLS 下 token 被抓还能重放吗？——抓到的是"内部 JWT"（授权层）而非身份：短 TTL（5 分钟）+ audience 限定 + mTLS 层要求重放者自己也得有证书；敏感操作再加 nonce 窗口（Q2178）。3) 从"无认证内网"迁移到这套组合的节奏？（提示：先观测→静态 token（止血红框）→ mTLS 双轨（CERT_OPTIONAL）→ 内部 JWT 授权收口，每步都有独立回滚开关，参考灰度放量节奏）

## 背诵要点
1. 静态 token 只防"陌生人"：轮换=发版、撤销=殃及全体、无粒度。
2. mTLS 身份绑密钥对（私钥不出网、可自动重签），但只有服务级身份；握手机制见 Q695。
3. 组合拳：mTLS 证明连接身份 + 内部 JWT（短 TTL/aud/scope）证明授权；网关必须重签令牌、禁止透传自报身份头。

## 复盘追问
1. 两个服务间已经 mTLS 了，审计发现某服务越权调用了另一服务的管理接口——问题出在哪一层？（提示：mTLS 只证明"是谁"，越权是授权层缺 scope 校验——内部 JWT 的 scope 判定（Q1909/Q1908）没有落地）
2. sidecar 接管 mTLS 后，业务进程拿到的"对端身份"还可信吗？（提示：取决于 sidecar 注入头的方式——mesh 需要保证注入头不可被 pod 内进程伪造（如通过 loopback 元数据/重新签名），业务层把它当"可信输入"前先验证信任链）
