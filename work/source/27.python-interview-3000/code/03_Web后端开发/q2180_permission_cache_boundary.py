"""权限缓存的失效边界: 变更角色后旧缓存何时说谎(纯标准库)。"""


class AuthzService:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.cache = {}                             # user_id -> (perms, cached_at, role)
        self.roles = {"viewer": {"read"}}

    def permissions(self, user_id, role, now):
        hit = self.cache.get(user_id)
        if hit and now - hit[1] <= self.ttl and hit[2] == role:
            return hit[0], "cache"
        perms = frozenset(self.roles.get(role, set()))
        self.cache[user_id] = (perms, now, role)
        return perms, "computed"

    def grant_role(self, role, perms):
        """授权变更只改角色表; 键里没有角色版本, 旧缓存继续说谎到 TTL 过期。"""
        self.roles[role] = set(perms)


svc = AuthzService()
p1 = svc.permissions("u1", "viewer", now=0)
print("首次查询        :", p1)
svc.grant_role("viewer", {"read", "export"})
p2 = svc.permissions("u1", "viewer", now=10)
p3 = svc.permissions("u1", "viewer", now=61)
print("变更后 10s 命中  :", p2)
print("TTL 过后 61s     :", p3)
assert p2 == (frozenset({"read"}), "cache")                        # 旧权限仍被命中
assert p3 == (frozenset({"read", "export"}), "computed")           # TTL 过后才重算
print("要点: 缓存键只含 user_id 时, 角色变更就是失效盲区; TTL 只是错多久的上界, 不是失效手段")
