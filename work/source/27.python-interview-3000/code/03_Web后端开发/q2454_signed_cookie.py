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
