"""布隆过滤器:双哈希派生 k 个位置,验证假阳性率与"一定不存在"性质。"""
import hashlib, math


class BloomFilter:
    def __init__(self, n, p=0.01):
        m = int(-n * math.log(p) / (math.log(2) ** 2))
        k = max(1, int(m / n * math.log(2)))
        self.m, self.k, self.bits, self.count = m, k, bytearray(m), 0

    def _positions(self, item):
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16)
        h2 = int(hashlib.sha1(item.encode()).hexdigest(), 16)
        return [(h1 + i * h2) % self.m for i in range(self.k)]

    def add(self, item):
        for pos in self._positions(item):
            self.bits[pos] = 1
        self.count += 1

    def might_contain(self, item):
        return all(self.bits[pos] for pos in self._positions(item))


if __name__ == "__main__":
    bf = BloomFilter(n=1000, p=0.01)
    added = {f"user-{i}" for i in range(1000)}
    for u in added:
        bf.add(u)
    fp = sum(1 for i in range(10000) if (x := f"ghost-{i}") not in added and bf.might_contain(x))
    print(f"m={bf.m} bits, k={bf.k}, 实测假阳性 {fp/10000:.2%}(目标 1%)")
    assert all(bf.might_contain(u) for u in list(added)[:100]), "已加入元素绝不误判不存在"
    assert fp / 10000 < 0.03, "假阳性率应在设计值附近"

    # 缓存穿透防护场景
    def get_from_cache_or_db(key):
        if not bf.might_contain(key):
            return "blocked: 不存在的 key 不打 DB"
        return f"hit_db {key}"
    print(get_from_cache_or_db("ghost-42"))
    print("布隆过滤器为缓存穿透挡下无效查询;删除需计数布隆或布谷鸟")
