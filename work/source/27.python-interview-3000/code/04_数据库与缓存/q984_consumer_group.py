"""两个消费组独立消费同一 Stream, 组内两 worker 竞争"""
import itertools

class MiniStream:
    def __init__(self):
        self.log, self.counter = [], itertools.count(1)
        self.groups = {}

    def xadd(self, payload):
        mid = next(self.counter)
        self.log.append((mid, payload))
        return mid

    def group(self, name, start=0):
        self.groups[name] = {"pos": start, "pel": {}}

    def read(self, name, consumer, count=10):
        g = self.groups[name]
        out = [(mid, p) for mid, p in self.log if mid > g["pos"]][:count]
        for mid, _ in out:
            g["pos"] = mid
            g["pel"][mid] = consumer
        return out

if __name__ == "__main__":
    s = MiniStream()
    for t in ("下单", "支付", "发货"):
        s.xadd(t)
    s.group("库存组"), s.group("积分组")
    print("库存组 worker1:", s.read("库存组", "worker1"))
    print("积分组 worker1:", s.read("积分组", "worker1"), "<- 组间广播")
    s.group("库存组2") if False else None
    s.groups["库存组"]["pos"] = 0
    print("库存组从0重读:", s.read("库存组", "worker2"), "<- offset 可回放")
