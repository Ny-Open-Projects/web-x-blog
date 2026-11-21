"""记住我的两级令牌: selector-validator 与哈希落库(纯标准库)。"""
import hashlib
import hmac
import secrets


class RememberMeStore:
    """库表只存 selector 与 validator 的哈希, Cookie 存 selector:validator。"""

    def __init__(self):
        self.rows = {}                           # selector -> {"hash", "user", "series"}

    def issue(self, user):
        selector = secrets.token_hex(8)
        validator = secrets.token_urlsafe(32)
        self.rows[selector] = {
            "hash": self._digest(validator),
            "user": user,
            "series": selector,
        }
        return selector + ":" + validator

    def consume(self, cookie_value):
        """校验并轮换: 合法则返回 (用户, 新Cookie), 失败返回 (None, 原因)。"""
        selector, sep, validator = cookie_value.partition(":")
        row = self.rows.get(selector)
        if row is None or not sep:
            return None, "selector 不存在, Cookie 无效"
        if not hmac.compare_digest(row["hash"], self._digest(validator)):
            del self.rows[selector]              # 疑似被盗用: 立即吊销整条系列
            return None, "validator 不符, 已按盗用吊销该系列"
        user = row["user"]
        new_validator = secrets.token_urlsafe(32)
        row["hash"] = self._digest(new_validator)
        return user, selector + ":" + new_validator

    @staticmethod
    def _digest(validator):
        return hashlib.sha256(validator.encode()).hexdigest()


store = RememberMeStore()
cookie1 = store.issue("alice")
print("签发 Cookie:", cookie1[:24] + "...")

user, cookie2 = store.consume(cookie1)
print("首次免登  -> user={} 轮换出新 Cookie".format(user))
assert user == "alice" and cookie2 != cookie1

user2, _ = store.consume(cookie2)
assert user2 == "alice"
print("新 Cookie 可继续使用")

user3, why = store.consume(cookie1)
print("旧 Cookie 重放 -> {} 原因: {}".format(user3, why))
assert user3 is None and "盗用" in why
selector1 = cookie1.partition(":")[0]
assert selector1 not in store.rows, "被盗系列应被吊销"

user4, why4 = store.consume("deadbeef" + ":" + "whatever")
print("伪造 Cookie -> {} 原因: {}".format(user4, why4))
assert user4 is None

# 落库内容核查: 数据库里只有 64 位十六进制哈希, 没有明文 validator
for row in store.rows.values():
    assert len(row["hash"]) == 64 and row["hash"] == row["hash"].lower()
print("要点: selector 定位行避免拿明文查库, validator 只存哈希拖库不泄令牌, "
      "每次使用即轮换, 校验失败立即吊销整个系列以检测 Cookie 被盗")
