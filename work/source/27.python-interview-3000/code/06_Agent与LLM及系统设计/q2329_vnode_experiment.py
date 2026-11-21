"""一致性哈希实测:同一批 key 在不同 vnode 数下统计负载极差与迁移量,数据说话选参数。"""
import bisect, hashlib


def h(s):
    return int(hashlib.md5(s.encode()).hexdigest(), 16)


class Ring:
    def __init__(self, nodes, vnodes):
        self.nodes, self.vnodes = nodes, vnodes
        self.ring = []
        for nd in nodes:
            for v in range(vnodes):
                self.ring.append((h("%s#%d" % (nd, v)), nd))
        self.ring.sort()
        self.pos = [p for p, _ in self.ring]

    def owner(self, key):
        i = bisect.bisect(self.pos, h(key)) % len(self.ring)
        return self.ring[i][1]


def experiment(nodes, keys, vnode_levels=(1, 10, 100)):
    report = []
    for v in vnode_levels:
        ring = Ring(nodes, v)
        load = {}
        for k in keys:
            load[ring.owner(k)] = load.get(ring.owner(k), 0) + 1
        counts = [load.get(nd, 0) for nd in nodes]
        spread = (max(counts) - min(counts)) / len(keys)
        report.append({"vnodes": v, "spread": round(spread, 3), "loads": load})
    return report


if __name__ == "__main__":
    nodes = ["node-a", "node-b", "node-c", "node-d"]
    keys = ["key%d" % i for i in range(2000)]
    rep = experiment(nodes, keys)
    assert rep[0]["spread"] > rep[1]["spread"] > rep[2]["spread"], "vnode 越多负载越匀"
    assert rep[2]["spread"] < 0.05, "100 vnode 时极差应小于 5 个百分点"
    before = Ring(nodes, 100)
    after = Ring(nodes + ["node-e"], 100)
    moved = sum(1 for k in keys if before.owner(k) != after.owner(k)) / len(keys)
    assert 0.15 < moved < 0.25, "扩容一台 迁移量应接近 1/5 实测 %s" % moved
    before1 = Ring(nodes, 1)
    after1 = Ring(nodes + ["node-e"], 1)
    moved1 = sum(1 for k in keys if before1.owner(k) != after1.owner(k)) / len(keys)
    assert abs(moved - 0.2) < abs(moved1 - 0.2), "vnode 多时迁移量更接近理论值"
    print("虚拟节点实测通过:spread 递减 迁移量接近 1/N")
