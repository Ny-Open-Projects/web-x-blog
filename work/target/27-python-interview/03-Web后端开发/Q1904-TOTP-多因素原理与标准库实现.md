---
title: [Q1904] TOTP 多因素原理与标准库实现
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1904 · TOTP 多因素原理与标准库实现

> 难度:★★☆☆ | 标签:认证, 安全

**问**:讲讲 TOTP 的原理,为什么 30 秒一个码就能防重放?

**答**:TOTP(RFC 6238)是 HOTP 的时间版:共享密钥与当前时间除以步长(通常 30 秒)得到计数器,用 HMAC-SHA1 对计数器签名,取摘要的动态截断再模 10 的 6 次方得到 6 位码。验证端用同样的密钥与本地时间独立算码比对,全程无网络交互,所以叫离线 MFA。防重放靠时间窗:码只在当前步长内有效,验证时容忍前后各一窗以吸收手机时钟漂移(正负 30 秒),超窗即失效;严格实现还要记录"最后成功使用的计数器",拒绝同一计数器内的第二次使用。标准库三件套足够:hmac、struct、base32。工程要求:密钥按用户加密存储;验证接口必须限速防百万空间爆破;提供恢复码兜底手机丢失。

```python
# file: code/03_Web后端开发/q1904_totp.py
"""TOTP 多因素原理: RFC 6238 与标准库 hmac 的实现(纯标准库)。"""
import base64
import hashlib
import hmac
import struct
import time


def totp(secret_b32, now=None, step=30, digits=6):
    """RFC 6238: 密钥 + 时间计数器经 HMAC-SHA1 得到 6 位动态码。"""
    secret = base64.b32decode(secret_b32, casefold=True)
    counter = int((now if now is not None else time.time()) // step)
    msg = struct.pack(">Q", counter)                      # 8 字节大端计数器
    digest = hmac.new(secret, msg, hashlib.sha1).digest()
    offset = digest[-1] & 0x0F                            # 动态截断偏移
    code = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(code % 10 ** digits).zfill(digits)


def verify(secret_b32, code, now=None, window=1):
    """验证时容忍前后各 1 个时间窗, 吸收手机与服务器的小幅时钟漂移。"""
    now = now if now is not None else time.time()
    return any(totp(secret_b32, now + w * 30) == code
               for w in range(-window, window + 1))


SECRET = base64.b32encode(b"my-app-secret-key-2026!").decode("utf-8")
t0 = 1762050000.0
code = totp(SECRET, t0)
print("步长 30s, 计数器", int(t0 // 30), "动态码:", code)
assert verify(SECRET, code, t0)
print("同窗口内验证:", verify(SECRET, code, t0 + 5))
print("下一窗口验证:", verify(SECRET, code, t0 + 31), "(窗口容忍内仍通过)")
print("漂移 2 窗后:", verify(SECRET, code, t0 + 61), "(超出容忍应拒绝)")
assert not verify(SECRET, code, t0 + 61, window=1)
assert totp(SECRET, t0) == totp(SECRET, t0 + 29.9)
print("要点: TOTP 是离线可验证的共享密钥方案, 服务端只需存密钥与最后成功计数, 验证必须限速防爆破")
```

**追问**:
- 为什么用 HMAC-SHA1 而不是 SHA256?——RFC 6238 兼容 HOTP 的 SHA1,令牌器兼容性优先;协议支持 SHA256 但生态以 SHA1 为主。
- 时钟漂移大怎么办?——注册时记录偏差自适应,或引导校时;窗口不宜超过正负 2,否则降低防重放强度。
