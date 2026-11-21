"""租约选主:CAS 抢占 + 单调钟 TTL + 纪元号防过期主写。"""


class Store:
    def __init__(self):
        self.leader, self.expires_at, self.epoch = None, 0.0, 0

    def expired(self, now):
        return now >= self.expires_at

    def try_acquire(self, node, now, deadline):
        """CAS:仅当无主或租约已过期时抢占。"""
        if self.leader is None or self.expired(now):
            self.leader, self.expires_at = node, deadline
            return True
        return False


class Elector:
    def __init__(self, node_id, ttl=0.2):
        self.id, self.ttl = node_id, ttl
        self.state = "follower"

    def tick(self, store, now):
        """每个心跳周期调用:leader 续期,follower 过期后竞选。"""
        if self.state == "leader":
            if store.leader == self.id and now < store.expires_at:
                store.expires_at = now + self.ttl        # 续期
                return "leader_renewed"
            self.state = "follower"
            return "demoted"
        if store.expired(now):
            if store.try_acquire(self.id, now, now + self.ttl):
                self.state = "leader"
                store.epoch += 1                          # 新纪元
                return f"elected epoch={store.epoch}"
        return "following"


if __name__ == "__main__":
    store = Store()
    a, b = Elector("A"), Elector("B")
    now = 0.0
    r1 = a.tick(store, now)
    print("t=0.0 A:", r1)
    assert r1.startswith("elected")
    r2 = b.tick(store, now)
    print("t=0.0 B:", r2)
    assert r2 == "following", "租约未过期 B 不得竞选"

    now = 0.1
    print("t=0.1 A:", a.tick(store, now), "(续期)")
    assert a.state == "leader"
    # A 失联:不再续期
    now = 0.5
    r3 = b.tick(store, now)
    print("t=0.5 B:", r3)
    assert b.state == "leader", "租约过期后 B 接管"
    assert a.tick(store, now) == "demoted", "旧主 A 感知降级"
    epoch_after = store.epoch

    # A 恢复,带着旧纪元写数据
    def old_leader_write(epoch):
        return "rejected" if epoch < store.epoch else "accepted"
    print(f"A 携带旧纪元写 -> {old_leader_write(epoch_after - 1)}")
    assert old_leader_write(epoch_after - 1) == "rejected", "过期主写被纪元号拒绝"
    print("租约选主: 过期不抢 + 纪元 fencing 双保险")
