"""权限缓存失效的版本号方案: 角色版本进键, 变更即失效(纯标准库)。"""


class VersionedAuthz:
    def __init__(self):
        self.role_version = {"viewer": 1}
        self.roles = {"viewer": frozenset({"read"})}
        self.cache = {}

    def permissions(self, user_id, role):
        key = (user_id, role, self.role_version[role])
        hit = self.cache.get(key)
        if hit is not None:
            return hit, "cache"
        perms = self.roles.get(role, frozenset())
        self.cache[key] = perms
        return perms, "computed"

    def grant_role(self, role, perms):
        """递增版本号使旧键全部自然失效; 旧条目留给 LRU/TTL 兜底清理。"""
        self.roles[role] = frozenset(perms)
        self.role_version[role] += 1


svc = VersionedAuthz()
print("变更前        :", svc.permissions("u1", "viewer"))
svc.grant_role("viewer", {"read", "export"})
print("变更后立即查  :", svc.permissions("u1", "viewer"))
print("同版本再查    :", svc.permissions("u1", "viewer")[1])
assert svc.permissions("u1", "viewer")[0] == frozenset({"read", "export"})
print("要点: 版本号把删一批缓存变成换一个键, 失效是 O(1) 写操作; 全局 epoch 适合授权大改的一键失效")
