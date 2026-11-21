"""两级缓存: L1 进程内短 TTL 与 L2 共享层的分工(纯标准库模拟)。"""
import threading


class TwoLevelCache:
    """L1 进程内极短 TTL 抗热点, L2 共享层较长 TTL 抗重启; 读穿写失效。

    代际号让失效广播可数: bump 一代, 各实例丢弃自己的 L1。
    """

    def __init__(self, l1_ttl=5, l2_ttl=60, clock=None):
        self.l1, self.l2 = {}, {}
        self.l1_ttl, self.l2_ttl = l1_ttl, l2_ttl
        self.now = clock or (lambda: 0.0)
        self.generation = 0
        self.lock = threading.Lock()
        self.l2_hits = {"n": 0}

    def get(self, key, loader):
        now = self.now()
        e1 = self.l1.get(key)
        if e1 and e1["gen"] == self.generation and now < e1["until"]:
            return e1["value"], "L1"
        e2 = self.l2.get(key)
        if e2 and now < e2["until"]:
            self.l2_hits["n"] += 1
            self.l1[key] = {"value": e2["value"], "until": now + self.l1_ttl,
                            "gen": self.generation}
            return e2["value"], "L2"
        value = loader(key)                       # 双缺失, 读穿加载
        self.put(key, value)
        return value, "loader"

    def put(self, key, value):
        now = self.now()
        self.l1[key] = {"value": value, "until": now + self.l1_ttl,
                        "gen": self.generation}
        self.l2[key] = {"value": value, "until": now + self.l2_ttl}

    def invalidate(self, key):
        """写路径失效: 删 L2, 变更代际让所有实例的 L1 一并作废。"""
        with self.lock:
            self.l2.pop(key, None)
            self.generation += 1
            self.l1.clear()


clock = {"t": 0.0}
loads = {"n": 0}


def loader(key):
    loads["n"] += 1
    return "value@%d" % int(clock["t"])


cache = TwoLevelCache(l1_ttl=5, l2_ttl=60, clock=lambda: clock["t"])
print("首读 ->", cache.get("k", loader), "加载次数", loads["n"])
print("再读 ->", cache.get("k", loader), "加载次数", loads["n"])
assert loads["n"] == 1

clock["t"] = 8                       # L1 过期但 L2 仍在
print("8s 后 ->", cache.get("k", loader), "加载次数", loads["n"])
assert loads["n"] == 1

cache.invalidate("k")
loads["n"] = 0
print("失效后 ->", cache.get("k", loader), "加载次数", loads["n"])
assert loads["n"] == 1

clock["t"] = 80                      # L2 也过期
loads["n"] = 0
print("80s 后 ->", cache.get("k", loader), "加载次数", loads["n"])
assert loads["n"] == 1
print("要点: L1 用纳秒级访问抗热点键, L2 用共享存储抗重启与多实例, 失效必须穿透两层")
