"""模拟惰性删除与定期抽样删除"""
import random
import time


class MiniRedis:
    def __init__(self):
        self.data: dict = {}
        self.expire_at: dict = {}

    def setex(self, key: str, value: str, ttl: float) -> None:
        self.data[key] = value
        self.expire_at[key] = time.time() + ttl

    def _expired(self, key: str) -> bool:
        return key in self.expire_at and time.time() > self.expire_at[key]

    def get(self, key: str):
        """惰性删除: 访问时检查并清理"""
        if self._expired(key):
            self.data.pop(key, None)
            self.expire_at.pop(key, None)
            return None
        return self.data.get(key)

    def active_cycle(self, samples: int = 5) -> int:
        """定期删除: 每轮从带 TTL 的 key 中抽样, 模拟每 100ms 一次"""
        keys = list(self.expire_at)
        removed = 0
        for key in random.sample(keys, min(samples, len(keys))):
            if self._expired(key):
                self.data.pop(key, None)
                self.expire_at.pop(key, None)
                removed += 1
        return removed


if __name__ == "__main__":
    r = MiniRedis()
    r.setex("k1", "v", 0.05)   # 很快过期
    r.setex("k2", "v", 100)
    print("立即读 k1:", r.get("k1"))
    time.sleep(0.1)
    print("0.1s 后读 k1:", r.get("k1"), " 已被惰性删除")
    print("主动抽样清理数量:", r.active_cycle())
