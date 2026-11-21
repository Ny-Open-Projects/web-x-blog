"""租约续期实现:带 fencing token 的租约管理器,看门狗续期、宽限期与过期失效。"""


class LeaseManager:
    """租约中心:授予租约返回单调递增 fencing token,过期未续则可被重新授予。"""

    def __init__(self, ttl=3, grace=1):
        self.ttl, self.grace = ttl, grace
        self.leases = {}                   # resource -> {"owner","expires","fence"}
        self.clock = 0.0
        self.fence_seq = 0

    def tick(self, dt=1.0):
        self.clock += dt

    def acquire(self, resource, owner):
        cur = self.leases.get(resource)
        if cur and cur["expires"] + self.grace > self.clock:
            return None, cur["fence"]       # 有效期或宽限期内 拒绝新申请
        self.fence_seq += 1
        self.leases[resource] = {"owner": owner, "expires": self.clock + self.ttl,
                                 "fence": self.fence_seq}
        return self.fence_seq, None

    def renew(self, resource, owner, fence):
        """续期:校验持有者与 token,过期未超宽限允许补续,超宽限拒绝。"""
        cur = self.leases.get(resource)
        if not cur or cur["owner"] != owner or cur["fence"] != fence:
            return False, "not_holder"
        if self.clock > cur["expires"] + self.grace:
            return False, "expired"
        cur["expires"] = self.clock + self.ttl
        return True, "renewed"

    def fence_ok(self, resource, fence):
        """存储侧校验:旧 token 的写入必须被拒绝 防脑裂双写。"""
        cur = self.leases.get(resource)
        return bool(cur) and fence == cur["fence"]

    def release(self, resource, owner):
        cur = self.leases.get(resource)
        if cur and cur["owner"] == owner:
            if self.clock > cur["expires"] + self.grace:
                return False                # 已失效 无需也无从释放
            del self.leases[resource]
            return True
        return False


if __name__ == "__main__":
    m = LeaseManager(ttl=3, grace=1)
    fence, _ = m.acquire("db-write", "A")
    assert fence == 1
    m.tick(2)
    ok, _ = m.renew("db-write", "A", fence)
    assert ok is True, "有效期内续期成功"

    m.tick(3)                                 # 3+2=5 已过期 1 秒 仍在宽限内
    ok, why = m.renew("db-write", "A", fence)
    assert ok is True and why == "renewed", "宽限期内补续成功"

    m.tick(5)                                 # 严重超期
    ok, why = m.renew("db-write", "A", fence)
    assert ok is False and why == "expired"
    assert m.release("db-write", "A") is False, "租约已失效 释放失败"

    f2, conflict = m.acquire("db-write", "B")  # B 拿到新租约 新 fence
    assert f2 == 2 and conflict is None
    assert m.fence_ok("db-write", 2) is True
    assert m.fence_ok("db-write", 1) is False, "旧 token 写入被存储侧拒绝"

    m.tick(4)
    f3, _ = m.acquire("db-write", "C")         # B 未续期过期且超宽限 C 抢到
    assert f3 == 3
    assert m.renew("db-write", "B", 2) == (False, "not_holder")
    print("租约续期通过:续期 2 次成功 宽限补续 超期失效 B 拿新 fence 旧写入被拒")
