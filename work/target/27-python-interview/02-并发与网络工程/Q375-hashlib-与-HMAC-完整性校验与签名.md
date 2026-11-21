---
title: [Q375] hashlib 与 HMAC:完整性校验与签名
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q375 · hashlib 与 HMAC:完整性校验与签名

> 难度:★★★ | 标签:hashlib, HMAC, 安全

**问**:hash 和 HMAC 有什么区别?如何设计一个标准库可跑的 API 签名方案?

**答**:hash(如 SHA-256)只有完整性能力,可被彩虹表/重放攻击;HMAC = hash + 密钥,既验完整性又验来源(只有持有密钥的双方能生成)。API 签名常见方案:客户端把 `method + path + timestamp + body` 按规则拼接,用共享密钥算 HMAC-SHA256 放进请求头;服务端用同样规则重算并 `hmac.compare_digest` 恒定时间比较;带上时间戳并在服务端校验窗口来防重放。注意密码存储要用 `hashlib.pbkdf2_hmac`/bcrypt,不能裸 hash。

```python
# file: code/02_并发与网络工程/q375_hmac_sign.py
"""HMAC-SHA256 API 签名与验签,防篡改 + 防重放。"""
import hashlib
import hmac
import json
import time

SECRET_KEY = b"shared-secret-keep-in-env"


def sign_request(method: str, path: str, body: dict, ts: float, key=SECRET_KEY) -> str:
    payload = f"{method.upper()}\n{path}\n{ts}\n" + json.dumps(body, sort_keys=True)
    return hmac.new(key, payload.encode(), hashlib.sha256).hexdigest()


def verify_request(method, path, body, ts, signature, key=SECRET_KEY,
                   window=300) -> bool:
    if abs(time.time() - ts) > window:          # 防重放:超出时间窗拒绝
        return False
    expect = sign_request(method, path, body, ts, key)
    return hmac.compare_digest(expect, signature)  # 恒定时间比较,防时序攻击


def password_digest(password: str, salt: bytes) -> bytes:
    """密码存储用 KDF,而不是裸 hash。"""
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)


if __name__ == "__main__":
    body = {"user": "alice", "amount": 100}
    ts = time.time()
    sig = sign_request("POST", "/api/pay", body, ts)
    print("签名:", sig[:16], "...")
    print("验签通过:", verify_request("POST", "/api/pay", body, ts, sig))
    print("篡改后验签:", verify_request("POST", "/api/pay", {"user": "alice", "amount": 999}, ts, sig))

    salt = b"random-salt-per-user"
    print("密码摘要:", password_digest("s3cret", salt).hex()[:16])
```

**追问**:
- 为什么用 `compare_digest` 而不是 `==`?普通 `==` 短路比较的耗时和匹配前缀长度相关,可被时序攻击逐字节爆破;`compare_digest` 恒定时间。
- MD5/SHA1 还能用吗?做非安全用途的校验和可以,安全场景一律 SHA-256 及以上。
