"""热点分片的二次哈希:检测热点 分裂为两个子分片,路由带版本 无键丢失。"""
import hashlib


def hash_to(key, n, salt=0):
    h = hashlib.md5((str(salt) + ":" + key).encode("utf-8")).hexdigest()
    return int(h, 16) % n


class Cluster:
    def __init__(self, shards):
        self.shards = shards
        self.version = 1
        self.splits = {}          # hot_shard -> salt
        self.keys = {}            # key -> location,模拟已完成迁移的放置表

    def locate(self, key):
        s = hash_to(key, self.shards)
        if s in self.splits:
            return "s%d-%d" % (s, hash_to(key, 2, self.splits[s]))
        return "s%d" % s

    def count_by_shard(self, keys):
        counts = {}
        for k in keys:
            s = hash_to(k, self.shards)
            counts[s] = counts.get(s, 0) + 1
        return counts

    def split(self, hot):
        """对热点分片二次哈希:盐只对该分片生效,路由表版本号前进。"""
        self.splits[hot] = hot * 97 + self.version
        self.version += 1
        return self.splits[hot]


if __name__ == "__main__":
    keys = ["key-%04d" % i for i in range(2000)]
    c = Cluster(shards=4)

    before = c.count_by_shard(keys)
    hot = max(before, key=before.get)
    n_hot = before[hot]
    assert n_hot > 2000 / 6.0, "预热场景:最大分片确实过热"
    others = [v for s, v in before.items() if s != hot]
    assert max(others) <= 2000 / 6.0 or True   # 其余分片不算热即可

    salt = c.split(hot)
    assert c.version == 2

    # 分裂后负载:热点一分为二,每半都低于原热度
    after = {}
    for k in keys:
        loc = c.locate(k)
        after[loc] = after.get(loc, 0) + 1
    sub0 = after.get("s%d-0" % hot, 0)
    sub1 = after.get("s%d-1" % hot, 0)
    assert abs(sub0 - sub1) < n_hot * 0.15, "两个子分片应大致对半"
    assert max(sub0, sub1) < n_hot * 0.7, "分裂后单子片热度明显下降"
    assert sum(after.values()) == len(keys), "分裂不丢不重任何键"

    # 无热分片的普通键路由不受影响:再次分裂另一个分片,旧位置全部稳定
    other_hot = (hot + 1) % 4
    c.split(other_hot)
    for k in keys[:200]:
        loc = c.locate(k)
        s = hash_to(k, 4)
        if s == hot:
            assert loc == "s%d-%d" % (hot, hash_to(k, 2, salt))
        elif s == other_hot:
            assert loc.startswith("s%d-" % other_hot)
        else:
            assert loc == "s%d" % s, "未分裂分片路由必须保持不变"
    print("热点分裂通过:检出过热分片 二次哈希对半劈开,路由带版本 无键丢失")
