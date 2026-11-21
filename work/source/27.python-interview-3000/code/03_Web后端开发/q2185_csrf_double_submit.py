"""CSRF 双提交 cookie: cookie 与请求头成对校验加签名强化(纯标准库)。"""
import hmac
import secrets

KEY = b"csrf-signing-key"


def issue_pair(session_id):
    """签名的双提交令牌: nonce 绑定会话, 同时写入非 HttpOnly cookie 与页面。"""
    nonce = secrets.token_hex(16)
    mac = hmac.new(KEY, (session_id + ":" + nonce).encode(), "sha256").hexdigest()[:16]
    return "{}.{}".format(nonce, mac)


def verify(session_id, cookie_token, header_token):
    if not cookie_token or not header_token:
        return False, "缺少 cookie 或请求头"
    if not hmac.compare_digest(cookie_token, header_token):
        return False, "cookie 与请求头不一致"
    try:
        nonce, mac = cookie_token.split(".", 1)
    except ValueError:
        return False, "令牌格式错误"
    expect = hmac.new(KEY, (session_id + ":" + nonce).encode(), "sha256").hexdigest()[:16]
    if not hmac.compare_digest(mac, expect):
        return False, "签名不匹配, cookie 可能被子域注入"
    return True, "通过"


token = issue_pair("sess-1")
print("正常提交:", verify("sess-1", token, token))
print("头不匹配:", verify("sess-1", token, "attacker-value"))
forged = "deadbeef." + token.split(".", 1)[1]
print("子域伪造:", verify("sess-1", forged, forged))
assert verify("sess-1", token, token)[0]
assert not verify("sess-1", forged, forged)[0]
print("要点: 双提交把自动带 cookie 变成脚本主动回显; 加签名后才能扛住子域写 cookie 的变体")
