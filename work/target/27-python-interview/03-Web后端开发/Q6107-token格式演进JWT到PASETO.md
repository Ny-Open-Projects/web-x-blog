---
title: [Q6107] token 格式演进：JWT 到 PASETO
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6107 · token 格式演进：JWT 到 PASETO

> 难度:★★★★☆ | 标签:版本演进, JWT, PASETO

**问**:JWT 已经 ubiquity 了，为什么还有人推 PASETO？选型与迁移怎么考虑？

**答**:结论：JWT（RFC 7519）的痛点来自 JOSE 家族的"算法协商"设计——header 里声明算法，实现又支持一大堆，历史漏洞全是"alg 混淆"（none 算法、RS256→HS256 把公钥当 HMAC 密钥）与库实现坑（可引 Q6009/Q114 的验签面）。PASETO（RFC 8417? 实为规范 draft）的思路相反：**版本即协议**，`v4.local`/`v4.public` 明确写死唯一算法（对称 AEAD / Ed25519 签名），没有可选项就没有混淆面。取舍矩阵：继续 JWT 的理由是生态（认证中间件、网关、多方互操作）成熟；选 PASETO 的理由是自建体系内消灭算法协商与默认不安全模式（如 unsigned payload）。迁移务实路径：新 token 用 PASETO（或"收紧版 JWT"——白名单 alg、强制校验 aud/exp）、双读校验、旧 token 自然过期。基线：Python 生态 `pyjwt`（JWT）与 `pypaseto`/`py-paseto`（PASETO，基线 3.9+，缺库降级示意见代码）。

```python
import base64, json, hmac, hashlib, os

# 原理演示：PASETO v4.public 的思想 = 固定算法（Ed25519），此处用 HMAC 模拟"无协商"
SECRET = os.urandom(32)

def paseto_style_sign(payload: dict) -> str:
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=")
    sig = hmac.new(SECRET, body, hashlib.sha256).digest()      # 算法写死，无 header 协商
    return b"v4.public." + body + b"." + base64.urlsafe_b64encode(sig).rstrip(b"=")

def paseto_style_verify(token: bytes) -> dict | None:
    _, body, sig = token.rsplit(b".", 2)
    pad = b"=" * (-len(sig) % 4)
    if not hmac.compare_digest(hmac.new(SECRET, body, hashlib.sha256).digest(),
                               base64.urlsafe_b64decode(sig + pad)):
        return None                                            # 恒定时间比较（Q2455 同源纪律）
    return json.loads(base64.urlsafe_b64decode(body + b"=" * (-len(body) % 4)))

t = paseto_style_sign({"sub": "u1", "exp": 9999999999})
print("payload:", paseto_style_verify(t))
print("篡改后:", paseto_style_verify(t.replace(b"u1", b"u9")))

# JWT 侧的收紧清单：alg 白名单 + 必校验声明
JWT_RULES = {"allowed_algs": {"RS256"}, "must_verify": ["exp", "aud"]}
print("JWT 收紧规则:", JWT_RULES)
```

**追问一层**:JWT 的 `none` 算法与 RS256→HS256 混淆攻击的具体成因？为什么 PASETO 结构上免疫？
**追二层**:PASETO `local`（对称）与 `public`（非对称）的选型边界？多服务共享验证时用哪个？

**背诵要点**
- JWT 的风险来自算法协商与宽松默认；PASETO 用版本锁定唯一算法。
- 收紧 JWT 的底线：alg 白名单、强制 exp/aud、恒定时间验签比较。
- 迁移走双读+自然过期，而不是全量重签。

**复盘追问**
- 历史上因为"库默认不校验 exp"造成的越权事故如何系统性防？提示：验签中间件集中化 + 合同测试。
- 内部服务互信需要非对称吗？提示：local（对称）够用且更快，public 用于跨信任域（Q6021）。
