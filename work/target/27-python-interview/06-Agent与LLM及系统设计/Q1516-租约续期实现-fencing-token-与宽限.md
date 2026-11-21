---
title: [Q1516] 租约续期实现:fencing token 与宽限期
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1516 · 租约续期实现:fencing token 与宽限期

> 难度:★★★☆ | 标签:分布式, 租约, 一致性

**问**:分布式锁讲过了,租约续期的机制细节有什么不同?

**答**:租约比锁多三层保护。续期校验归属:只有持有者凭自己的 fencing token 才能续,过期后的宽限期内允许补续,超宽限期则彻底失效,后续续期返回 expired 而不是无限拖延。fencing token 单调递增:持有者每次带着 token 写存储,存储侧只认当前 token,旧 token 的写入即使已发出也会被拒绝,这是防脑裂双写的最后防线。失效即不可释放:超期租约对原持有者来说已无从释放,新申请者无需等待,凭更高的 token 接管。三个语义合起来,把 时钟漂移 消息延迟 下的双主窗口压到最小。

```python
# file: code/06_Agent与LLM及系统设计/q1516_lease_renewal.py
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
```

**追问**:
- 宽限期为什么必须存在? 答:续期请求在途时租约可能刚好过期,一刀切失效会造成合法持有者被顶掉,宽限期容忍单次续期抖动;
- token 和 epoch 什么关系? 答:同构,epoch 是集群视角的版本号,fencing token 是资源视角的,单调性是共同的灵魂。
