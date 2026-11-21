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
