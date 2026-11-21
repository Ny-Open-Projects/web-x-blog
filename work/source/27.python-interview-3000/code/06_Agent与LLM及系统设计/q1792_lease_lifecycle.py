"""租约生命周期状态机:获取 心跳续期 过期 接管 释放,旧 epoch 写入被 fencing 拒绝。"""


class FencedResource:
    """被保护资源桩:记录见过的最大 epoch,旧 fencing token 的写入一律拒绝。"""

    def __init__(self):
        self.epoch = 0
        self.writes = []
        self.rejected = 0

    def write(self, epoch, who, value):
        if epoch < self.epoch:
            self.rejected += 1
            return False                         # 旧 epoch 拒绝
        self.epoch = epoch
        self.writes.append((who, value))
        return True


class LeaseStateMachine:
    """free -> held -> expired -> taken 或 free,epoch 全程单调递增。"""

    def __init__(self, resource, ttl=3):
        self.resource = resource
        self.ttl = ttl
        self.state = "free"
        self.holder = None
        self.epoch = 0
        self.last_renew = 0
        self.now = 0

    def acquire(self, who):
        if self.state == "held":
            return None                          # 别人持有:获取失败
        self.epoch += 1
        self.state = "held"
        self.holder = who
        self.last_renew = self.now
        self.resource.epoch = self.epoch         # epoch 注册进资源元数据
        return self.epoch

    def renew(self, who):
        if self.state != "held" or who != self.holder:
            return False                         # 非持有者不可续
        if self.now - self.last_renew > self.ttl:
            self.state = "expired"
            return False
        self.last_renew = self.now
        return True

    def takeover(self, who):
        if self.state != "expired":
            return None                          # 只有 expired 可接管
        self.epoch += 1
        self.state = "held"
        self.holder = who
        self.last_renew = self.now
        self.resource.epoch = self.epoch         # 接管记录进资源,旧 token 从此被拒
        return self.epoch

    def release(self, who):
        if self.state == "held" and who == self.holder:
            self.state = "free"
            self.holder = None
            return True
        return False

    def tick(self):
        self.now += 1
        if self.state == "held" and self.now - self.last_renew > self.ttl:
            self.state = "expired"               # 心跳停止:自动过期


if __name__ == "__main__":
    res = FencedResource()
    lease = LeaseStateMachine(res, ttl=3)

    e1 = lease.acquire("node-a")
    assert e1 == 1 and lease.state == "held"
    assert lease.acquire("node-b") is None, "持有期他人获取失败"
    assert res.write(e1, "node-a", "v1") is True

    for _ in range(4):                           # node-a 心跳停止
        lease.tick()
    assert lease.state == "expired", "超过 TTL 未续期自动过期"
    assert lease.renew("node-a") is False, "过期后续期失败"

    e2 = lease.takeover("node-b")
    assert e2 == 2 and lease.holder == "node-b", "expired 后接管成功"
    assert res.write(e1, "node-a", "stale") is False, "旧 epoch 写入被 fencing 拒绝"
    assert res.write(e2, "node-b", "v2") is True
    assert res.rejected == 1

    assert lease.renew("node-b") is True
    assert lease.release("node-b") is True and lease.state == "free"
    assert lease.release("node-a") is False, "非持有者不能释放"
    assert lease.acquire("node-a") == 3, "释放后重新获取,epoch 继续单调"
    print("租约状态机通过:获取 续期 过期 接管 释放全链路,旧 epoch 写入被拒")
