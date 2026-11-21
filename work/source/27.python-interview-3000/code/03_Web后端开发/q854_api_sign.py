from __future__ import annotations

import hashlib
import hmac
import time
from typing import Optional

SECRET = b"api-secret"

def sign_request(method: str, path: str, ts: int, nonce: str) -> str:
    msg = f"{method}\n{path}\n{ts}\n{nonce}".encode()
    return hmac.new(SECRET, msg, hashlib.sha256).hexdigest()

def verify(method, path, ts, nonce, sig, now: Optional[int] = None, window: int = 60) -> bool:
    now = now or int(time.time())
    if abs(now - ts) > window:
        return False                      # 防 replay 的时间窗
    expected = sign_request(method, path, ts, nonce)
    return hmac.compare_digest(expected, sig)

ts = int(time.time())
sig = sign_request("GET", "/v1/data", ts, "n1")
print("合法签名:", verify("GET", "/v1/data", ts, "n1", sig))
print("过期重放:", verify("GET", "/v1/data", ts - 3600, "n1", sig))
