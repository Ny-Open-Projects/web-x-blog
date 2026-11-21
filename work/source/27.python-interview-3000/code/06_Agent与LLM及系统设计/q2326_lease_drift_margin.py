"""租约时钟漂移:节点间时钟有漂移时,名义到期时刻必须减去最大漂移才是安全过期点。"""
class LeaseWithDrift:
    def __init__(self, ttl=10.0, max_drift=1.0):
        self.ttl = ttl
        self.max_drift = max_drift
        self.holder = None
        self.nominal_expire = 0.0
        self.safe_expire = 0.0

    def grant(self, holder, now):
        self.holder = holder
        self.nominal_expire = now + self.ttl
        self.safe_expire = self.nominal_expire - self.max_drift
        return self.safe_expire

    def renew(self, holder, now):
        if holder != self.holder:
            return False
        self.nominal_expire = now + self.ttl
        self.safe_expire = self.nominal_expire - self.max_drift
        return True

    def local_allow(self, node_now, margin=True):
        limit = self.safe_expire if margin else self.nominal_expire
        return node_now < limit


if __name__ == "__main__":
    lm = LeaseWithDrift(ttl=10.0, max_drift=1.0)
    lm.grant("A", now=0.0)
    assert lm.safe_expire == 9.0, "安全过期点比名义早一个最大漂移"
    assert lm.local_allow(8.0), "安全期内允许"
    assert not lm.local_allow(9.0), "慢钟节点在提前量内被拦下"
    assert lm.local_allow(9.0, margin=False), "不留漂移余量同一时刻就会放行"
    assert lm.renew("A", now=5.0)
    assert lm.safe_expire == 14.0
    assert lm.local_allow(13.0) and not lm.local_allow(14.0), "续期后重新计算安全点"
    assert not lm.renew("B", now=6.0), "非持有者不能续"
    print("租约漂移通过:安全过期点提前 慢钟被拦 续期重算")
