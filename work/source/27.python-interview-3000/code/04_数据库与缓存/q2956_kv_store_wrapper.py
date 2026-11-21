"""KV 封装层: 命名空间隔离 TTL 生命周期 JSON 序列化与解码容错"""
import json
import time


class KVStore:
    """后端是最简 dict, 换成 Redis 时方法签名不变"""

    def __init__(self):
        self._data = {}    # fullkey -> (expire_at, raw)
        self.stats = {"hit": 0, "miss": 0, "expired": 0, "decode_err": 0}

    @staticmethod
    def _k(ns, key):
        return "%s:%s" % (ns, key)

    def set(self, ns, key, value, ttl=60.0):
        raw = json.dumps({"v": 1, "d": value}, separators=(",", ":"))
        self._data[self._k(ns, key)] = (time.monotonic() + ttl, raw)

    def get(self, ns, key):
        full = self._k(ns, key)
        ent = self._data.get(full)
        if ent is None:
            self.stats["miss"] += 1
            return None
        exp, raw = ent
        if exp <= time.monotonic():
            del self._data[full]           # 惰性过期
            self.stats["expired"] += 1
            return None
        self.stats["hit"] += 1
        try:
            return json.loads(raw)["d"]
        except (ValueError, KeyError):
            self.stats["decode_err"] += 1  # 坏值当未命中, 不炸读路径
            del self._data[full]
            return None

    def delete(self, ns, key):
        self._data.pop(self._k(ns, key), None)

    def scan(self, ns):
        """命名空间盘点: 真实实现换 SCAN 渐进遍历, 不用 KEYS"""
        now = time.monotonic()
        return sorted(k for k, (exp, _) in self._data.items()
                      if k.startswith(ns + ":") and exp > now)


kv = KVStore()
kv.set("user", "1", {"name": "a"})
kv.set("user", "2", {"name": "b"})
kv.set("session", "t1", "abc", ttl=0.05)
print("命名空间隔离: user:1 =", kv.get("user", "1"),
      "| user 的键在 session 前缀下查不到:", kv.get("session", "1"))
print("scan user ->", kv.scan("user"), "| scan session ->", kv.scan("session"))
time.sleep(0.06)
print("TTL 到期: session:t1 =", kv.get("session", "t1"),
      "过期计数", kv.stats["expired"])
kv._data["user:3"] = (time.monotonic() + 60, "{broken-json")
print("坏值容错: user:3 =", kv.get("user", "3"),
      "容错计数", kv.stats["decode_err"])
print("统计:", kv.stats)
assert kv.stats["expired"] == 1 and kv.stats["decode_err"] == 1
