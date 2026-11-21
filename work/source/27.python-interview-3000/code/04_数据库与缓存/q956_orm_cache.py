"""主键级薄缓存: 读走缓存 写后失效"""
import time

class FakeCache:
    def __init__(self):
        self._data = {}

    def get(self, key):
        item = self._data.get(key)
        if item and item[0] > time.monotonic():
            return item[1]
        return None

    def set(self, key, value, ttl):
        self._data[key] = (time.monotonic() + ttl, value)

    def delete(self, key):
        self._data.pop(key, None)

class UserRepo:
    def __init__(self, db, cache):
        self.db, self.cache = db, cache
        self.hits = self.miss = 0

    def get(self, uid):
        key = f"user:{uid}"
        if (v := self.cache.get(key)) is not None:
            self.hits += 1
            return v
        self.miss += 1
        row = self.db.get(uid)                    # 模拟 DB 查询
        if row:
            self.cache.set(key, row, ttl=60)
        return row

    def save(self, uid, row):
        self.db[uid] = row
        self.cache.delete(f"user:{uid}")          # 写后失效

if __name__ == "__main__":
    db = {1: {"name": "alice"}}
    repo = UserRepo(db, FakeCache())
    print(repo.get(1), "miss")
    print(repo.get(1), "hit")
    repo.save(1, {"name": "alice2"})
    print(repo.get(1), "失效后回源")
    print(f"命中率统计: {repo.hits} hit / {repo.miss} miss")
