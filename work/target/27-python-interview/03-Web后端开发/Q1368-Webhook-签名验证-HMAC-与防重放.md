---
title: [Q1368] Webhook 签名验证:HMAC 与防重放
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1368 · Webhook 签名验证:HMAC 与防重放

> 难度:★★★★ | 标签:Webhook, 签名

**问**:第三方回调你的 Webhook,怎么确认请求真来自对方而不是伪造?

**答**:标准三件套:双方约定签名密钥;对方用密钥对 **`时间戳.原始字节体`** 计算 HMAC-SHA256 放进头(如 `X-Signature`);你方验证时做三件事——用**原始请求体字节**重算(不能反序列化再拼,字段顺序会变)、`hmac.compare_digest` 恒定时间比较、检查时间戳在容忍窗口内(常见 ±5 分钟)防重放。密钥按渠道隔离并支持轮换(头里带 key id)。另外把验证结果当安全事件记录,验证失败立即 401 且不解析业务体,避免解析器漏洞被利用。

```python
# file: code/03_Web后端开发/q1368_webhook_sig.py
"""Webhook 签名验证:HMAC-SHA256 加时间戳防重放(纯标准库)。"""
import hashlib
import hmac
import time

SECRET = b"whsec_demo_key"


def sign(timestamp, body):
    return hmac.new(SECRET, f"{timestamp}.".encode() + body, hashlib.sha256).hexdigest()


def verify(timestamp, body, signature, tolerance=300):
    try:
        ts = int(timestamp)
    except (TypeError, ValueError):
        return False, "时间戳非法"
    if abs(time.time() - ts) > tolerance:
        return False, "超出重放容忍窗口"
    if not hmac.compare_digest(sign(timestamp, body), signature):
        return False, "签名不符"
    return True, "ok"


body = b'{"event": "payment.succeeded"}'
ts = str(int(time.time()))
sig = sign(ts, body)
print("正常回调:", verify(ts, body, sig))
print("体被篡改:", verify(ts, b'{"event": "payment.failed"}', sig))
print("重放旧包:", verify("1600000000", body, sign("1600000000", body)))
```

**追问**:
- 为什么要签时间戳而不只签 body?——只签 body 的签名永久有效,截获即可无限重放;时间戳把有效窗压到分钟级。
- 验证失败要重试吗?——不要回执任何细节,统一 401 并告警;对方平台自己有重试机制。
