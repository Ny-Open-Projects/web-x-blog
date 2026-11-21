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
