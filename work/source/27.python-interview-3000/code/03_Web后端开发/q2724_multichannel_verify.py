"""多渠道回调验签的模板化适配: 一套模板接各家头约定(纯标准库)。"""
import hashlib
import hmac


def verify_stripe_style(headers, body, secret_map, now, tolerance):
    """X-Signature: t=<ts>,v1=<hex>[,v1=<hex2>], 签名盖住 ts.body, 支持密钥轮换多签名。"""
    kid = headers.get("X-Key-Id", "default")
    secret = secret_map.get(kid)
    if secret is None:
        return False, "unknown_key_id"
    ts, sigs = None, []
    for part in headers.get("X-Signature", "").split(","):
        k, _, v = part.strip().partition("=")
        if k == "t":
            ts = int(v) if v.isdigit() else None
        elif k == "v1":
            sigs.append(v)
    if ts is None or abs(now - ts) > tolerance:
        return False, "timestamp_out_of_window"
    signed = ("%d." % ts).encode() + body
    for v in sigs:
        want = hmac.new(secret, signed, hashlib.sha256).hexdigest()
        if hmac.compare_digest(want, v):
            return True, "ok"
    return False, "bad_signature"


def verify_vcs_style(headers, body, secret_map, now, tolerance):
    """X-Signature: sha256=<hex of body>, 协议本身不带时间戳, 防重放交给 event_id 去重。"""
    sig = headers.get("X-Signature", "")
    if not sig.startswith("sha256="):
        return False, "bad_prefix"
    kid = headers.get("X-Key-Id", "default")
    secret = secret_map.get(kid)
    if secret is None:
        return False, "unknown_key_id"
    want = hmac.new(secret, body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(want, sig[7:]), "ok"


CHANNELS = {"pay": verify_stripe_style, "vcs": verify_vcs_style}
SECRETS = {"default": b"old-key", "key2": b"new-key"}


def verify_callback(channel, headers, body, now, tolerance=300):
    """模板入口: 渠道名选适配器, 输出统一的 ok/reason; 失败一律先拒后查, 不碰业务体。"""
    verifier = CHANNELS.get(channel)
    if verifier is None:
        return {"ok": False, "reason": "unknown_channel"}
    ok, reason = verifier(headers, body, SECRETS, now, tolerance)
    return {"ok": ok, "reason": reason}


body = b'{"order":"o1","amount":100}'
t = 1000000.0
ok_headers = {"X-Signature": "t=1000000,v1=%s" % hmac.new(b"old-key", b"1000000." + body, hashlib.sha256).hexdigest()}
assert verify_callback("pay", ok_headers, body, t) == {"ok": True, "reason": "ok"}
tampered = dict(ok_headers, X_Signature=ok_headers["X-Signature"])
bad = verify_callback("pay", ok_headers, body + b" ", t)
assert bad == {"ok": False, "reason": "bad_signature"}
stale = {"X-Signature": "t=999000,v1=%s" % hmac.new(b"old-key", b"999000." + body, hashlib.sha256).hexdigest()}
assert verify_callback("pay", stale, body, t)["reason"] == "timestamp_out_of_window"
new_sig = {"X-Key-Id": "key2", "X-Signature": "t=1000000,v1=%s" % hmac.new(b"new-key", b"1000000." + body, hashlib.sha256).hexdigest()}
assert verify_callback("pay", new_sig, body, t) == {"ok": True, "reason": "ok"}

vcs_sig = "sha256=" + hmac.new(b"old-key", body, hashlib.sha256).hexdigest()
assert verify_callback("vcs", {"X-Signature": vcs_sig}, body, t) == {"ok": True, "reason": "ok"}
assert verify_callback("vcs", {"X-Signature": "md5=nope"}, body, t)["reason"] == "bad_prefix"
assert verify_callback("ghost", {}, body, t)["reason"] == "unknown_channel"
print("pay: 时间戳窗口 + 多签名轮换通过; vcs: 前缀协议通过; 伪造与超窗全部拒绝")
