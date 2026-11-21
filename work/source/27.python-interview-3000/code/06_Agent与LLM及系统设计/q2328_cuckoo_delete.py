"""布谷鸟过滤器的删除语义:删一个指纹不是删一个元素,重复插入与同指纹冒名是两大坑。"""
import hashlib


def fp_hash(key, bits=8):
    v = int(hashlib.md5(key.encode()).hexdigest(), 16) % (1 << bits)
    return v or 1


def bucket_of(key, n):
    return int(hashlib.md5(("b" + key).encode()).hexdigest(), 16) % n


class Cuckoo:
    def __init__(self, n=16, slots=2, max_kick=8):
        self.n, self.slots, self.max_kick = n, slots, max_kick
        self.buckets = [[] for _ in range(n)]

    def _alts(self, key, fp):
        b1 = bucket_of(key, self.n)
        b2 = b1 ^ (int(hashlib.md5(str(fp).encode()).hexdigest(), 16) % self.n)
        return b1, b2

    def insert(self, key):
        fp = fp_hash(key)
        b1, b2 = self._alts(key, fp)
        for b in (b1, b2):
            if len(self.buckets[b]) < self.slots:
                self.buckets[b].append(fp)
                return True
        cur = b1
        for k in range(self.max_kick):
            slot = k % self.slots
            old = self.buckets[cur][slot]
            self.buckets[cur][slot] = fp
            alt = cur ^ (int(hashlib.md5(str(old).encode()).hexdigest(), 16) % self.n)
            if len(self.buckets[alt]) < self.slots:
                self.buckets[alt].append(old)
                return True
            cur, fp = alt, old
        return False

    def contains(self, key):
        fp = fp_hash(key)
        b1, b2 = self._alts(key, fp)
        return fp in self.buckets[b1] or fp in self.buckets[b2]

    def delete(self, key):
        fp = fp_hash(key)
        b1, b2 = self._alts(key, fp)
        for b in (b1, b2):
            if fp in self.buckets[b]:
                self.buckets[b].remove(fp)
                return True
        return False


if __name__ == "__main__":
    cf = Cuckoo()
    assert cf.insert("doc1") and cf.contains("doc1")
    assert cf.delete("doc1") and not cf.contains("doc1"), "删除后查不到"

    cf2 = Cuckoo()
    assert cf2.insert("dup") and cf2.insert("dup")
    assert cf2.delete("dup") and cf2.contains("dup"), "删一个指纹副本 还有留存"
    assert cf2.delete("dup") and not cf2.contains("dup"), "再删一份才真正消失"

    found = False
    for i in range(20000):
        ka, kb = "x%d" % i, "y%d" % i
        if fp_hash(ka) != fp_hash(kb) or bucket_of(ka, 16) != bucket_of(kb, 16):
            continue
        cf3 = Cuckoo()
        cf3.insert(kb)
        if cf3.contains(kb) and cf3.delete(ka):
            assert not cf3.contains(kb), "同指纹冒名删除造成假阴性"
            found = True
            break
    assert found, "应能构造出同指纹冒名案例"
    print("布谷鸟删除语义通过:先插后删 删副本语义 冒名假阴性复现")
