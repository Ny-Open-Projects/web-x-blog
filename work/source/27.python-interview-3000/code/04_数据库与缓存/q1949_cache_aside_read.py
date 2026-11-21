"""旁路缓存读路径: 未命中回源 读修复写回与过期重读"""
import time

class DB:
    def __init__(self):
        self.data = {"u:1": "Alice", "u:2": "Bob"}
        self.source_reads = 0
    def get(self, key):
        self.source_reads += 1
        return self.data.get(key)

class Cache:
    def __init__(self, ttl=0.05):
        self.store = {}
        self.ttl = ttl
    def get(self, key):
        item = self.store.get(key)
        if not item:
            return None
        value, expire_at = item
        if time.monotonic() > expire_at:
            self.store.pop(key, None)   # 物理过期 回源前先清掉
            return None
        return value
    def set(self, key, value):
        self.store[key] = (value, time.monotonic() + self.ttl)

db, cache = DB(), Cache()

def read_aside(key):
    """旁路缓存标准读路径: 命中直接返回 未命中查库并写回缓存"""
    value = cache.get(key)
    if value is not None:
        return value, "hit"
    value = db.get(key)
    if value is not None:
        cache.set(key, value)     # 读修复: 回源结果写回 避免下次再打库
        return value, "miss-repaired"
    return None, "miss-empty"

print(read_aside("u:1"), "库回源", db.source_reads, "次")
print(read_aside("u:1"), "库回源", db.source_reads, "次")
time.sleep(0.06)
print(read_aside("u:1"), "库回源", db.source_reads, "次  TTL 过期后重新回源并再次写回")
print(read_aside("u:1"), "库回源", db.source_reads, "次")

# 不存在的 key: 每次都打库 这是穿透的入口 缓存 None 或布隆来堵
for _ in range(3):
    print(read_aside("u:999"), "库回源", db.source_reads, "次")
print("结论: 回源后必须写回 这是读路径的修复动作; 空结果反复打库就要用短 TTL 空值缓存或布隆过滤器")
