"""登出的令牌失效列表: jti 黑名单与到期自动出列(纯标准库)。"""
import hashlib
import hmac
import json


def token_jti(payload, secret):
    """无状态令牌的 jti: 对 payload 做带密钥哈希即可, 不必真发 UUID。"""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hmac.new(secret, raw, hashlib.sha256).hexdigest()[:16]


class DenyList:
    """登出即写 jti, TTL 取令牌剩余寿命, 到点自动出列, 存储只增不减是错的。"""

    def __init__(self, now=lambda: 0.0):
        self._banned = {}
        self._now = now

    def revoke(self, jti, exp):
        t = self._now()
        if exp <= t:
            return False  # 已过期令牌天然失效, 不占黑名单
        self._banned[jti] = exp
        self._banned = {k: v for k, v in self._banned.items() if v > t}  # 顺手清扫
        return True

    def is_denied(self, jti):
        exp = self._banned.get(jti)
        if exp is None:
            return False
        if exp <= self._now():
            del self._banned[jti]
            return False
        return True


class Auth:
    """校验顺序固定: 先验签名与过期, 再查黑名单, 黑名单命中立即拒绝。"""

    def __init__(self, secret, deny, now=lambda: 0.0):
        self.secret, self.deny, self._now = secret, deny, now

    def check(self, payload):
        if payload["exp"] <= self._now():
            return "expired"
        if self.deny.is_denied(token_jti(payload, self.secret)):
            return "revoked"
        return "ok"


SECRET = b"k"
clock = {"t": 0.0}
now = lambda: clock["t"]
deny = DenyList(now)
auth = Auth(SECRET, deny, now)

tok = {"sub": "u1", "exp": 100.0}
jti = token_jti(tok, SECRET)
assert auth.check(tok) == "ok"
deny.revoke(jti, tok["exp"])
assert auth.check(tok) == "revoked", "登出后令牌必须被拒"
clock["t"] = 101.0
assert auth.check(tok) == "expired"
assert not deny.is_denied(jti), "过期的黑名单条目应自动出列"
deny.revoke(token_jti({"sub": "u2", "exp": 90.0}, SECRET), 90.0)  # 已过期令牌拒绝入列
assert len(deny._banned) == 0
print("登出即拒 -> 到期转 expired -> 黑名单条目自动清空, 存储有界")
