import bisect
import hashlib


def h(s: str) -> int:
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16)


class ConsistentHashRing:
    def __init__(self, vnodes: int = 100) -> None:
        self._ring = []          # 有序哈希点
        self._owner = {}         # 哈希点 -> 物理节点
        self._vnodes = vnodes

    def add(self, node: str) -> None:
        for i in range(self._vnodes):
            point = h(f"{node}#vn{i}")
            bisect.insort(self._ring, point)
            self._owner[point] = node

    def remove(self, node: str) -> None:
        for i in range(self._vnodes):
            point = h(f"{node}#vn{i}")
            idx = bisect.bisect_left(self._ring, point)
            if idx < len(self._ring) and self._ring[idx] == point:
                self._ring.pop(idx)
                del self._owner[point]

    def get(self, key: str):
        if not self._ring:
            return None
        idx = bisect.bisect(self._ring, h(key)) % len(self._ring)
        return self._owner[self._ring[idx]]


def naive_mod(key: str, n: int) -> int:
    return h(key) % n


def main() -> None:
    keys = [f"key-{i}" for i in range(2000)]

    ring = ConsistentHashRing(vnodes=100)
    for n in ("node-A", "node-B", "node-C"):
        ring.add(n)
    before = {k: ring.get(k) for k in keys}
    naive_before = {k: naive_mod(k, 3) for k in keys}

    ring.add("node-D")
    after = {k: ring.get(k) for k in keys}
    naive_after = {k: naive_mod(k, 4) for k in keys}

    moved_ring = sum(1 for k in keys if before[k] != after[k])
    moved_mod = sum(1 for k in keys if naive_before[k] != naive_after[k])
    print(f"扩容 3->4 节点: 一致性哈希迁移 {moved_ring/len(keys):.0%}, 普通取模迁移 {moved_mod/len(keys):.0%}")
    assert moved_ring / len(keys) < 0.35, "一致性哈希应只迁移约 1/N"
    assert moved_mod / len(keys) > 0.65, "普通取模几乎全部换主"

    # 负载均匀性: 虚拟节点让 3 节点各拿约 1/3
    share = {}
    for v in after.values():
        share[v] = share.get(v, 0) + 1
    print("扩容后分布:", {k: f"{v/len(keys):.0%}" for k, v in sorted(share.items())})
    assert min(share.values()) / len(keys) > 0.15

    # 摘除节点: 幸存者接管, 无 key 失踪
    ring.remove("node-C")
    assert all(ring.get(k) for k in keys)
    print("摘除 node-C 后所有 key 仍有归属")


if __name__ == "__main__":
    main()
