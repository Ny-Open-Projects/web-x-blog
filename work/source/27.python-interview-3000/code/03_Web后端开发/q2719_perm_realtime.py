"""令牌内权限的实时生效: 权限版本号拒收过期声明(纯标准库)。"""


class PermAuth:
    """令牌里带 perm_version, 服务端为每个用户维护当前版本。

    版本一致才进入权限判定, 不一致返回 stale_perm 引导客户端刷新;
    bump 是权限变更的唯一写点, 改权限 = 版本加一, 全量旧令牌立即变陈旧。
    """

    def __init__(self, now=lambda: 0.0):
        self.pv = {}
        self.tokens = {}
        self._now = now

    def issue(self, user, perms, ttl=3600.0):
        version = self.pv.get(user, 1)
        self.tokens[user] = {"sub": user, "perms": list(perms), "pv": version,
                             "exp": self._now() + ttl}
        return dict(self.tokens[user])

    def bump(self, user):
        self.pv[user] = self.pv.get(user, 1) + 1

    def check(self, token, required):
        if token["exp"] <= self._now():
            return "expired"
        if self.pv.get(token["sub"], 1) != token["pv"]:
            return "stale_perm"
        return "ok" if required in token["perms"] else "forbidden"


clock = {"t": 0.0}
auth = PermAuth(now=lambda: clock["t"])
tok = auth.issue("u1", ["admin", "read"])
assert auth.check(tok, "admin") == "ok"

clock["t"] = 10.0
auth.bump("u1")  # 管理员被降权: 不等令牌过期, 立即生效
assert auth.check(tok, "admin") == "stale_perm", "未过期令牌也必须被拒收"
fresh = auth.issue("u1", ["read"])  # 客户端拿 401 后刷新, 新令牌只带 read
assert fresh["pv"] == 2
assert auth.check(fresh, "admin") == "forbidden"
assert auth.check(fresh, "read") == "ok"
clock["t"] = 3700.0
assert auth.check(fresh, "read") == "expired"
print("降权 -> 旧令牌 stale_perm -> 刷新后 admin=forbidden, read=ok")
print("兜底顺序: 过期 > 版本 > 权限; 高危操作建议再查一次存储 regardless 令牌")
