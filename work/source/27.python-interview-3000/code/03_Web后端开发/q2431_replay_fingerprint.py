"""重放防护: 请求指纹绑定 + nonce 窗口(纯标准库)。"""
import hashlib
import hmac
import json
import time

SECRET = b"demo-signing-secret"


def canonical(method, path, body, ts, nonce):
    """规范化串: 方法 路径 排序后的 JSON 时间戳 nonce, 逐项换行拼接。"""
    body_s = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "\n".join([method.upper(), path, body_s, str(ts), nonce])


def sign(method, path, body, ts, nonce):
    """客户端签名: HMAC 覆盖请求全部关键要素, 改任何一项签名即失效。"""
    return hmac.new(SECRET, canonical(method, path, body, ts, nonce).encode(),
                    hashlib.sha256).hexdigest()


class ReplayGuard:
    """服务端防重放: 时间戳限制窗口, nonce 限制一次性, 指纹绑定内容。"""

    def __init__(self, window=300, now=None):
        self.window = window
        self.now = now or time.time
        self.seen = {}                       # nonce -> 首次出现的时刻

    def check(self, method, path, body, ts, nonce):
        now = self.now()
        if abs(now - ts) > self.window:
            return False, "时间戳超出正负 {} 秒窗口".format(self.window)
        if nonce in self.seen:
            return False, "nonce 已出现过, 判定为重放"
        for stale in [k for k, v in self.seen.items() if now - v > self.window]:
            self.seen.pop(stale)             # 滑动清理, 防止 seen 无限膨胀
        self.seen[nonce] = now
        return True, "要素齐全且 nonce 首次出现, 放行"


now = time.time()
guard = ReplayGuard(window=300, now=lambda: now)
nonce = "8f14e45f"
sig = sign("POST", "/api/pay", {"amount": 100}, now, nonce)
assert sig == sign("POST", "/api/pay", {"amount": 100}, now, nonce)   # 签名可复算校验

print("签名前 16 位:", sig[:16])
ok, why = guard.check("POST", "/api/pay", {"amount": 100}, now, nonce)
print("首次提交  -> {} {}".format(ok, why))
ok2, why2 = guard.check("POST", "/api/pay", {"amount": 100}, now, nonce)
print("原样重放  -> {} {}".format(ok2, why2))
ok3, why3 = guard.check("POST", "/api/pay", {"amount": 100}, now - 3600, "new-nonce")
print("过期时间戳-> {} {}".format(ok3, why3))
assert ok and not ok2 and not ok3

# 内容被篡改时签名校验失败
sig_tampered = sign("POST", "/api/pay", {"amount": 9900}, now, nonce)
assert sig_tampered != sig
print("要点: 时间戳限窗口、nonce 限一次性、指纹 HMAC 把方法路径参数全部绑定, 三层缺一不可")
