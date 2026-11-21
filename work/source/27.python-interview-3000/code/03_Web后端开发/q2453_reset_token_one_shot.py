"""密码重置令牌: 一次性消费与过期窗(纯标准库)。"""
import hashlib
import secrets


class ResetService:
    """库表只存令牌哈希, 消费即作废, 时间可注入便于测试过期。"""

    def __init__(self, ttl=600, now=lambda: 1000.0):
        self.ttl, self.now = ttl, now
        self.tokens = {}                         # 哈希 -> {"expires", "used"}

    def issue(self):
        token = secrets.token_urlsafe(32)
        self.tokens[self._digest(token)] = {"expires": self.now() + self.ttl,
                                            "used": False}
        return token

    def consume(self, token):
        row = self.tokens.get(self._digest(token))
        if row is None:
            return False, "令牌不存在或已被清理"
        if row["used"]:
            return False, "令牌已消费, 重放拒绝"
        if self.now() > row["expires"]:
            return False, "令牌已过期, 请重新申请"
        row["used"] = True
        return True, "校验通过, 允许设置新密码"

    @staticmethod
    def _digest(token):
        return hashlib.sha256(token.encode()).hexdigest()


clock = {"now": 1000.0}
svc = ResetService(ttl=600, now=lambda: clock["now"])

token = svc.issue()
print("签发令牌前 12 位:", token[:12], "有效期 600 秒")

ok, why = svc.consume(token)
print("首次消费   -> {} {}".format(ok, why))
assert ok

ok2, why2 = svc.consume(token)
print("重放消费   -> {} {}".format(ok2, why2))
assert not ok2 and "重放" in why2

token2 = svc.issue()
clock["now"] = 1600.0 + 1                       # 推进到过期之后
ok3, why3 = svc.consume(token2)
print("过期消费   -> {} {}".format(ok3, why3))
assert not ok3 and "过期" in why3

ok4, why4 = svc.consume("totally-forged-token")
print("伪造令牌   -> {} {}".format(ok4, why4))
assert not ok4

hashed_only = all(len(h) == 64 for h in svc.tokens)
assert hashed_only, "库里只有哈希"
print("要点: 一次性 = 消费即置 used 且判定放在同一处; "
      "过期与重放是两类失败要分开提示, 库里只存哈希, 短 TTL 限制暴露面")
