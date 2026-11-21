"""布谷鸟过滤器简化版:双桶候选 + 指纹踢脸 + 支持删除。"""
import hashlib, random


def fp_of(x, bits=16):
    return int(hashlib.md5(x.encode()).hexdigest(), 16) % (1 << bits) or 1


def idx_of(x, n):
    return int(hashlib.md5(x.encode()).hexdigest(), 16) % n


class CuckooFilter:
    def __init__(self, n_buckets=64, bucket_size=4, max_kicks=32):
        self.buckets = [[] for _ in range(n_buckets)]
        self.n, self.bs, self.mk = n_buckets, bucket_size, max_kicks

    def _cands(self, x):
        fp = fp_of(x)
        i1 = idx_of(x, self.n)
        i2 = (i1 ^ idx_of(str(fp), self.n)) % self.n
        return fp, i1, i2

    def insert(self, x):
        fp, i1, i2 = self._cands(x)
        for _ in range(self.mk):
            for i in (i1, i2):
                if len(self.buckets[i]) < self.bs:
                    self.buckets[i].append(fp)
                    return True
            # 两个候选桶都满:随机踢一个,被踢者迁往自己的另一候选桶
            victim_b = random.choice([i1, i2])
            pos = random.randrange(len(self.buckets[victim_b]))
            fp, self.buckets[victim_b][pos] = self.buckets[victim_b][pos], fp
            i1 = victim_b
            i2 = (i1 ^ idx_of(str(fp), self.n)) % self.n
        return False

    def contains(self, x):
        fp, i1, i2 = self._cands(x)
        return fp in self.buckets[i1] or fp in self.buckets[i2]

    def delete(self, x):
        fp, i1, i2 = self._cands(x)
        for i in (i1, i2):
            if fp in self.buckets[i]:
                self.buckets[i].remove(fp)
                return True
        return False


if __name__ == "__main__":
    random.seed(3)
    cf = CuckooFilter()
    for i in range(40):
        assert cf.insert(f"k{i}")
    assert all(cf.contains(f"k{i}") for i in range(40)), "已插入必须查到"
    assert cf.delete("k7"), "支持删除"
    assert not cf.contains("k7")
    ghost = sum(1 for i in range(5000) if cf.contains(f"g{i}"))
    print(f"40 个元素后,幽灵误判 {ghost}/5000,已删项返回 False")
    assert ghost < 30
    print("布谷鸟: 定长 2 桶查询 + 踢脸重试 + 真删除")
