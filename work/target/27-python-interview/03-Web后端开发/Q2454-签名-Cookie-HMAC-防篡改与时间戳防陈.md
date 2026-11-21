---
title: [Q2454] 签名 Cookie:HMAC 防篡改与时间戳防陈旧
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2454 · 签名 Cookie:HMAC 防篡改与时间戳防陈旧

> 难度:★★★★ | 标签:Cookie, HMAC, 会话

**问**:把会话数据放进客户端 Cookie,怎么保证它不被篡改?签名应该盖住哪些内容?

**答**:签名 Cookie 的格式是 "base64(payload)|timestamp|hmac",HMAC 的输入必须同时覆盖 payload 与时间戳——只签 payload 的实现会让攻击者保留合法签名而把时间戳改到未来,绕过过期检查。校验四步:格式拆分、重算 HMAC 并用 compare_digest 比较、检查时间戳在 max_age 内、才解析 payload。密钥只在服务端,这是整个方案的安全根,泄露即全线失守,所以要支持密钥轮换(同时验新旧两把)。与 JWT 的关系:这就是最小化的不透明 JWT——去掉头与标准声明,保留"声明加签名"的内核;区别在 JWT 有标准化生态与算法协商,签名 Cookie 更简单也少了协商带来的算法混淆攻击面。Cookie 里永远不要放敏感明文,签名保证完整性不保密,需要机密性得再加密。

```python
# file: code/03_Web后端开发/q2454_signed_cookie.py
"""签名 Cookie: HMAC 防篡改与时间戳防陈旧(纯标准库)。"""
import base64
import hashlib
import hmac
import json
import time

SECRET = b"demo-signing-key-change-me"


def encode_cookie(payload, ts, secret=SECRET):
    """格式: base64(payload)|timestamp|hmac(payload|timestamp)。"""
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    mac = hmac.new(secret, raw + b"|" + str(ts).encode(),
                   hashlib.sha256).hexdigest()
    return "{}|{}|{}".format(base64.urlsafe_b64encode(raw).decode(), ts, mac)


def decode_cookie(cookie, secret=SECRET, max_age=3600, now=None):
    """返回 (payload, 原因); 签名不符 过期 格式错都不还原数据。"""
    now = time.time() if now is None else now
    try:
        b64, ts_s, mac = cookie.split("|")
    except ValueError:
        return None, "格式非法"
    try:
        raw = base64.urlsafe_b64decode(b64.encode())
        expected = hmac.new(secret, raw + b"|" + ts_s.encode(),
                            hashlib.sha256).hexdigest()
    except (ValueError, TypeError):
        return None, "解码失败"
    if not hmac.compare_digest(mac, expected):
        return None, "签名不符, 内容被篡改或密钥不对"
    if now - int(ts_s) > max_age:
        return None, "签名过期, 需重新登录"
    return json.loads(raw.decode()), "ok"


good = encode_cookie({"uid": 7, "role": "member"}, ts=1700000000)
print("签发:", good[:40] + "...")

payload, why = decode_cookie(good, now=1700000000 + 100)
print("正常校验  -> {} {}".format(payload, why))
assert payload == {"uid": 7, "role": "member"}

# 篡改演示: 攻击者把 role 改成 admin, 没有 HMAC 密钥签不出新签名
parts = good.split("|")
import base64 as _b64
tampered_raw = _b64.urlsafe_b64decode(parts[0].encode()).decode()
tampered_raw = tampered_raw.replace("member", "admin")
evil = "{}|{}|{}".format(
    _b64.urlsafe_b64encode(tampered_raw.encode()).decode(), parts[1], parts[2])
payload2, why2 = decode_cookie(evil, now=1700000000 + 100)
print("篡改校验  -> {} {}".format(payload2, why2))
assert payload2 is None and "签名不符" in why2

# 篡改时间戳同样会破坏签名, 因为 ts 参与了 HMAC 计算
evil_ts = "{}|{}|{}".format(parts[0], "1600000000", parts[2])
payload3, why3 = decode_cookie(evil_ts, now=1700000000 + 100)
assert payload3 is None
print("改时间戳  -> {}".format(why3))

payload4, why4 = decode_cookie(good, now=1700000000 + 7200)
print("过期校验  -> {} {}".format(payload4, why4))
assert payload4 is None and "过期" in why4
print("要点: 值放客户端的前提是 HMAC 盖住 payload 与时间戳, "
      "密钥只在服务端, 校验用 compare_digest, max_age 控制签名有效期")
```

**追问**:
- 过期检查为什么在服务端做而不是信任 payload 里的 exp?——payload 是客户端可读的,exp 只能作为签名输入由服务端判定,任何"客户端声明"都必须重验。
- 撤销一个签名 Cookie 怎么做?——无状态签名天然无法撤销,要么缩短 max_age,要么加服务端黑名单或版本号校验,退化为半有状态。
