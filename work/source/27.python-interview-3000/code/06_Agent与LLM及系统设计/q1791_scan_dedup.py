"""分布式扫描去重:分片先认领再扫描,完成登记后重扫跳过,崩溃片租约过期回收重派。"""


class ScanCoordinator:
    def __init__(self, ranges, lease_ttl=3):
        self.ranges = list(ranges)
        self.claims = {}                         # range -> {owner, at}
        self.done = set()
        self.scanned = []                        # (worker, range)
        self.lease_ttl = lease_ttl
        self.now = 0

    def claim(self, worker):
        for r in self.ranges:
            if r in self.done:
                continue
            c = self.claims.get(r)
            if c is None or self.now - c["at"] > self.lease_ttl:
                self.claims[r] = {"owner": worker, "at": self.now}
                return r                         # 未认领或租约过期:认领成功
        return None

    def complete(self, worker, r):
        c = self.claims.get(r)
        if c is None or c["owner"] != worker:
            return False                         # 不是你的片,不能替登记
        self.done.add(r)
        self.scanned.append((worker, r))
        return True

    def tick(self):
        self.now += 1


if __name__ == "__main__":
    coord = ScanCoordinator(["r1", "r2", "r3", "r4", "r5", "r6"], lease_ttl=3)

    got = {}
    for w in ("w1", "w2", "w3"):
        got[w] = coord.claim(w)
    assert got == {"w1": "r1", "w2": "r2", "w3": "r3"}, "认领互斥,一人一片"
    assert coord.claim("w1") == "r4", "已持有的不再重复认领"

    assert coord.complete("w1", "r1") and coord.complete("w2", "r2")
    assert coord.complete("w1", "r4")
    assert coord.complete("w2", "r3") is False, "别人的分片不能替其登记完成"

    for _ in range(5):                           # w3 崩溃:不再认领也不再完成
        coord.tick()
    assert coord.claim("w4") == "r3", "租约过期后 r3 可被安全重新认领"
    coord.complete("w4", "r3")
    while True:
        r = coord.claim("w4")
        if r is None:
            break
        coord.complete("w4", r)

    assert coord.claim("w4") is None, "全部完成后再认领返回空"
    assert sorted(r for _, r in coord.scanned) == ["r1", "r2", "r3", "r4", "r5", "r6"]
    assert len(coord.scanned) == len(set(r for _, r in coord.scanned)), "每分片恰好有效扫描一次"
    print("扫描去重通过:认领互斥 租约过期回收重派,完成登记后绝不重扫")
