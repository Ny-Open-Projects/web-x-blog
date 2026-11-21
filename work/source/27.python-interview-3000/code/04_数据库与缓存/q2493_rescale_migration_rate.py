"""实例扩容的键迁移率: 取模 槽位与一致性哈希的搬家账"""
import hashlib
from bisect import bisect

N_KEYS = 100000
keys = [hashlib.md5(b"key-%d" % i).digest() for i in range(N_KEYS)]
h = [int.from_bytes(k[:8], "big") for k in keys]

def rate_mod(n_from, n_to):
    return sum(1 for x in h if x % n_from != x % n_to) / N_KEYS

SLOTS = 4096
def rate_slot(n_from, n_to):
    """Redis 风格: 槽位显式分配, 扩容时新节点从每个老节点匀出等额槽"""
    give_up = SLOTS // n_to // n_from + 1          # 每个老节点让出约 1/(N+1) 的槽
    moved = 0
    for x in h:
        s = x % SLOTS
        old = s // 1024                            # 4 节点时每节点 1024 槽
        if old < n_from and s >= (old + 1) * 1024 - give_up:
            moved += 1                             # 尾部槽被移交给新节点
    return moved / N_KEYS

def build_ring(nodes, vnodes=100):
    ring = []
    for nd in nodes:
        for v in range(vnodes):
            ring.append((int.from_bytes(
                hashlib.md5(b"node-%d-v%d" % (nd, v)).digest()[:8], "big"), nd))
    ring.sort()
    return [p for p, _ in ring], [nd for _, nd in ring]

def rate_ring(n_from, n_to):
    r1, o1 = build_ring(range(n_from))
    r2, o2 = build_ring(range(n_to))
    moved = 0
    for x in h:
        i1 = bisect(r1, x) % len(r1)
        i2 = bisect(r2, x) % len(r2)
        if o1[i1] != o2[i2]:
            moved += 1
    return moved / N_KEYS

print("从 4 实例扩到 5 实例, 10 万键需要搬家的比例:")
print("  哈希取模 mod:    %.1f%%   (几乎全部重排, 扩容即雪崩)" % (rate_mod(4, 5) * 100))
print("  固定槽位分配表:  %.1f%%   (新节点从每个老节点匀出等额槽)" % (rate_slot(4, 5) * 100))
print("  一致性哈希环:    %.1f%%   (只动受影响弧段)" % (rate_ring(4, 5) * 100))
print("结论: 扩容迁移率是选分片方案的第一账目, 取模方案把 N/(N+1) 的键搬家,")
print("      槽位与一致性哈希都把它压到约 1/(N+1); Redis Cluster 用 16384 槽就是这个道理")
