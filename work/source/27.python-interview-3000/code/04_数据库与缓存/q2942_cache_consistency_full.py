"""缓存与 DB 一致性完整方案: 旁路读路径 + 版本入键写路径"""
import time

TTL = 60.0


class System:
    """db 行自带 ver, 缓存键带 ver: 失效不追删, 旧键自然不可达"""

    def __init__(self):
        self.db = {1: {"price": 10, "ver": 1}, 2: {"price": 20, "ver": 1}}
        self.meta = {}    # id -> 缓存住的当前版本号, 未命中才回库点查
        self.cache = {}   # "item:{id}:v{ver}" -> (expire_at, row)
        self.log = []

    def _meta_ver(self, i):
        if i in self.meta:
            return self.meta[i]
        v = self.db[i]["ver"]
        self.meta[i] = v
        return v

    def read(self, i):
        v = self._meta_ver(i)
        key = "item:%d:v%d" % (i, v)
        ent = self.cache.get(key)
        if ent and ent[0] > time.monotonic():
            self.log.append("hit  %s" % key)
            out = dict(ent[1])
            out.pop("ver", None)
            return out
        row = self.db[i]                      # 回源: 行里带权威 ver
        self.cache[key] = (time.monotonic() + TTL, dict(row))
        self.meta[i] = row["ver"]             # 顺手刷新 meta
        self.log.append("miss %s -> 回源" % key)
        out = dict(row)
        out.pop("ver", None)
        return out

    def write(self, i, price):
        row = self.db[i]
        old_key = "item:%d:v%d" % (i, row["ver"])
        row["price"] = price
        row["ver"] += 1
        self.meta.pop(i, None)                # meta 一删, 新读者自然走新键
        self.cache.pop(old_key, None)         # 尽力而为删旧键, 删失败也无害
        self.log.append("write id=%d ver -> %d" % (i, row["ver"]))


s = System()
print("首次读:", s.read(1))
print("再次读:", s.read(1))
s.write(1, 12)
print("写后读:", s.read(1))

# 经典竞态回放: 读者在写前拿到旧行, 写者提交后其回源才迟到落缓存
old_row = dict(s.db[2])                     # 读者 T1: 回源读到 ver=1 旧行
s.write(2, 99)                              # 写者 T2: ver -> 2, meta 已翻
s.cache["item:2:v1"] = (time.monotonic() + TTL, dict(old_row))  # T1 迟到回填 v1 键
got = s.read(2)                             # 新读者按 meta 走 v2 键
assert got["price"] == 99
print("竞态回放: 旧值被隔离在 v1 键, 读者拿到", got)
print("\n".join(s.log))
assert s.read(1)["price"] == 12 and s.read(2)["price"] == 99
print("结论: 版本入键把删除竞态变成结构性不可达, 残留旧键等 TTL 自然回收")
