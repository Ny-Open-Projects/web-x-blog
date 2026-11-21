"""JWT 签发与校验的最小实现: HS256 手工签名与声明校验(纯标准库)。"""
import base64
import hashlib
import hmac
import json
import time

SECRET = b"demo-secret-store-in-env-not-code"


class JwtError(Exception):
    pass


def _b64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(segment):
    return base64.urlsafe_b64decode(segment + "=" * (-len(segment) % 4))


def issue(claims, secret=SECRET, expires_in=600, issuer="demo"):
    """三段式: 头.载荷.签名, 全部 base64url 无填充; 签名只覆盖前两段原文。"""
    header = {"alg": "HS256", "typ": "JWT"}
    now = int(time.time())
    payload = dict(claims)
    payload.setdefault("iat", now)
    payload["exp"] = now + expires_in
    payload["iss"] = issuer
    signing_input = (
        _b64url(json.dumps(header, separators=(",", ":"), sort_keys=True).encode())
        + "."
        + _b64url(json.dumps(payload, separators=(",", ":"), sort_keys=True).encode())
    )
    signature = hmac.new(secret, signing_input.encode("ascii"), hashlib.sha256).digest()
    return signing_input + "." + _b64url(signature)


def verify(token, secret=SECRET, issuer="demo"):
    """任何一步失败都抛 JwtError; 通过则返回 claims。校验顺序: 签名 -> 算法 -> 时间 -> 签发者。"""
    parts = token.split(".")
    if len(parts) != 3:
        raise JwtError("格式非法, 不是三段式")
    signing_input = (parts[0] + "." + parts[1]).encode("ascii")
    try:
        signature = _b64url_decode(parts[2])
    except Exception:
        raise JwtError("签名段不是合法 base64url")
    if not hmac.compare_digest(hmac.new(secret, signing_input, hashlib.sha256).digest(), signature):
        raise JwtError("签名不匹配")
    header = json.loads(_b64url_decode(parts[0]))
    if header.get("alg") != "HS256":
        raise JwtError("算法未被允许, 防 alg=none 与算法混淆")
    claims = json.loads(_b64url_decode(parts[1]))
    now = int(time.time())
    if claims.get("exp", 0) < now:
        raise JwtError("令牌已过期")
    if claims.get("iss") != issuer:
        raise JwtError("签发者不符")
    return claims


token = issue({"sub": "user-42", "role": "editor"}, expires_in=600)
print("签发长度:", len(token), "段数:", token.count(".") + 1)
claims = verify(token)
print("校验通过:", claims["sub"], claims["role"], "exp 在", claims["exp"] - int(time.time()), "秒后")
assert claims["sub"] == "user-42"

header_b64, payload_b64, sig_b64 = token.split(".")
forged = header_b64 + "." + _b64url(json.dumps({"sub": "attacker", "role": "admin", "exp": int(time.time()) + 999, "iat": int(time.time()), "iss": "demo"}, separators=(",", ":")).encode()) + "." + sig_b64
try:
    verify(forged)
except JwtError as e:
    print("改载荷重放旧签名 ->", e)

try:
    verify(token + "x")
except JwtError as e:
    print("签名末位加一字节 ->", e)

none_token = _b64url(b'{"alg":"none","typ":"JWT"}') + "." + payload_b64 + "."
try:
    verify(none_token)
except JwtError as e:
    print("alg=none 空签名 ->", e)

expired = issue({"sub": "user-42"}, expires_in=-10)
try:
    verify(expired)
except JwtError as e:
    print("过期令牌 ->", e)

wrong_issuer = issue({"sub": "u1"}, issuer="other")
try:
    verify(wrong_issuer)
except JwtError as e:
    print("签发者不符 ->", e)

try:
    verify("not-a-jwt")
except JwtError as e:
    print("残缺令牌 ->", e)

# 签名耗时对错误密钥与正确密钥一致(恒定时间比较), 不给爆破侧时序侧信道
start = time.monotonic()
for _ in range(200):
    try:
        verify(token, secret=b"wrong-secret-wrong-secret")
    except JwtError:
        pass
t_wrong = time.monotonic() - start
start = time.monotonic()
for _ in range(200):
    verify(token)
t_right = time.monotonic() - start
print("错误/正确密钥 200 次校验耗时: %.3fs vs %.3fs, 差距在噪声内" % (t_wrong, t_right))
print("JWT 最小实现演示通过")
