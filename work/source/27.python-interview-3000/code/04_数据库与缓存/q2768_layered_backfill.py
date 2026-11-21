"""多级缓存的逐层回填: 每层 miss 都要把下层结果带回来, 各层 TTL 不同"""
class Layer:
    def __init__(self, name, ttl):
        self.name = name
        self.ttl = ttl
        self.data = {}
        self.hits = 0
        self.miss = 0

    def get(self, k, now):
        item = self.data.get(k)
        if item and item[0] > now:
            self.hits += 1
            return item[1]
        self.miss += 1
        return None

    def put(self, k, v, now):
        self.data[k] = (now + self.ttl, v)


L1 = Layer("L1 进程内", ttl=5)
L2 = Layer("L2 Redis", ttl=60)
db_calls = [0]

def source(k):
    db_calls[0] += 1
    return "value:" + k

def read(k, now):
    v = L1.get(k, now)
    if v is not None:
        return v, "L1"
    v = L2.get(k, now)
    if v is not None:
        L1.put(k, v, now)          # 关键: L2 命中也要回填 L1
        return v, "L2"
    v = source(k)
    L2.put(k, v, now)              # 先填远层 TTL 长
    L1.put(k, v, now)              # 再填近层 TTL 短
    return v, "DB"

for label, now in [("t=1000", 1000.0), ("t=1001", 1001.0),
                   ("t=1010 L1 已过期", 1010.0), ("t=1011", 1011.0)]:
    v, where = read("a", now)
    print("%s: %s 命中于 %s" % (label, v, where))
print("L1 命中 %d 未命中 %d | L2 命中 %d 未命中 %d | 回源 %d 次"
      % (L1.hits, L1.miss, L2.hits, L2.miss, db_calls[0]))
print("若漏掉 L2 命中回填 L1, t=1011 那次就会变成 L2 命中, 本地缓存形同虚设")
