"""批量失效: 版本前缀翻转代替逐键删除"""
import time

class Cache:
    def __init__(self):
        self.data = {}
        self.version = {}
    def _k(self, ns, key):
        return "%s:v%d:%s" % (ns, self.version.get(ns, 0), key)
    def get(self, ns, key):
        return self.data.get(self._k(ns, key))
    def set(self, ns, key, value):
        self.data[self._k(ns, key)] = value
    def invalidate_all(self, ns):
        """整个命名空间一键失效: 版本号加一 旧键变成不可达 等 TTL 自然回收"""
        self.version[ns] = self.version.get(ns, 0) + 1

c = Cache()
for i in range(100):
    c.set("feed", "user-%d" % i, "feed-%d" % i)
print("失效前     读 user-7 ->", c.get("feed", "user-7"), " 键总数:", len(c.data))

c.invalidate_all("feed")
print("翻转版本后 读 user-7 ->", c.get("feed", "user-7"), " 键总数:", len(c.data), " 旧键仍在但已不可达")

for i in range(100):                    # 读修复重新灌装新版本
    c.set("feed", "user-%d" % i, "feed-%d-new" % i)
print("重新灌装后 键总数:", len(c.data), " 新键 100 个 旧键 100 个等待过期")

# 失效成本对比: 一万个键逐个删与一次版本翻转
keys = ["u%d" % i for i in range(10000)]
store = {k: 1 for k in keys}
t0 = time.perf_counter()
for k in keys:
    store.pop(k, None)
t_del = time.perf_counter() - t0
t0 = time.perf_counter()
version = 1                              # 翻转只是改一个数字
t_ver = time.perf_counter() - t0
print(f"逐键删除 {t_del * 1000:.2f} ms vs 版本翻转 {t_ver * 1000:.4f} ms  差距随键数线性放大")
print("结论: 版本前缀用空间换失效速度 旧键靠 TTL 兜底回收 适合整域失效 不适合只失效单个键")
