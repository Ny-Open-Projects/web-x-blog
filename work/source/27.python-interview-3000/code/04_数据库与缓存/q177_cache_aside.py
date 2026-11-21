"""Cache Aside 读写路径的最小实现"""


class CacheAsideService:
    def __init__(self):
        self.cache: dict = {}
        self.db: dict = {"item:1": "v1"}
        self.db_reads = 0

    def read(self, key: str):
        if key in self.cache:
            return self.cache[key], "cache"
        self.db_reads += 1
        value = self.db.get(key)
        if value is not None:
            self.cache[key] = value
        return value, "db"

    def write(self, key: str, value: str) -> None:
        self.db[key] = value        # 第一步: 更新 DB
        self.cache.pop(key, None)   # 第二步: 删除缓存, 而不是更新


if __name__ == "__main__":
    svc = CacheAsideService()
    print(svc.read("item:1"))        # cache 未建, 读 DB
    print(svc.read("item:1"))        # 命中缓存
    svc.write("item:1", "v2")
    print(svc.read("item:1"), "写后读到新值, 缓存已被删除并重载")
    print("DB 读次数:", svc.db_reads)
