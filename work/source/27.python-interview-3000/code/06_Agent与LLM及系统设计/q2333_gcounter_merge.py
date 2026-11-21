"""G-Counter:每个节点只增自己的槽位,合并取各槽最大值,离线增量不丢求和无重复。"""
class GCounter:
    def __init__(self, nid, peers):
        self.nid = nid
        self.slots = {p: 0 for p in peers}

    def inc(self, n=1):
        self.slots[self.nid] += n

    def value(self):
        return sum(self.slots.values())

    def merge(self, other):
        for p, v in other.slots.items():
            self.slots[p] = max(self.slots[p], v)

    def state(self):
        return dict(self.slots)


if __name__ == "__main__":
    a, b, c = GCounter("A", "ABC"), GCounter("B", "ABC"), GCounter("C", "ABC")
    a.inc(5)
    b.inc(3)
    b.inc(2)
    a.merge(b)
    assert a.value() == 10, "合并后求和 5 加 5"
    c.inc(7)
    b.merge(c)
    a.merge(b)
    assert a.value() == 17, "三方合并 5+5+7"
    before = a.value()
    a.merge(b)
    assert a.value() == before, "合并幂等 重复同步不重复计数"
    a.inc(1)
    b.merge(a)
    c.merge(a)
    assert a.state() == b.state() == c.state(), "交换律与收敛 三副本状态一致"
    assert a.value() == 18
    offline = GCounter("C", "ABC")
    offline.slots = dict(c.state())
    offline.inc(100)
    a.merge(offline)
    assert a.value() == 118, "离线增量带着原状态回来不丢"
    print("G-Counter 通过:只增己槽 逐槽取大 幂等交换 离线不丢")
