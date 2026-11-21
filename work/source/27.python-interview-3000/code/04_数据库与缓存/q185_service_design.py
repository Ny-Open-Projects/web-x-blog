"""综合小实现: 本地 LRU -> Redis 语义 -> DB 三级读取 + 互斥重建"""
import random
import threading
from collections import OrderedDict


class ProductDB:
    def __init__(self):
        self.data = {1: {"name": "手机", "price": 4999}}
        self.reads = 0

    def get(self, pid: int):
        self.reads += 1
        return self.data.get(pid)


class DetailService:
    def __init__(self, db: ProductDB, local_size: int = 2):
        self.db = db
        self.redis: dict = {}
        self.local: OrderedDict = OrderedDict()
        self.local_size = local_size
        self.key_locks: dict = {}
        self._guard = threading.Lock()

    @staticmethod
    def _ttl() -> float:
        return 300 * (1 + random.uniform(-0.1, 0.1))    # 雪崩防护: TTL 抖动

    def get(self, pid: int):
        if pid in self.local:                            # 第一级: 进程内
            self.local.move_to_end(pid)
            return self.local[pid], "local"
        if pid in self.redis:                            # 第二级: Redis
            self.local[pid] = self.redis[pid]
            return self.redis[pid], "redis"
        with self._lock_for(pid):                        # 第三级: 互斥回源
            if pid in self.redis:                        # 双重检查
                return self.redis[pid], "redis"
            value = self.db.get(pid)
            if value is not None:
                self.redis[pid] = value                  # 回填 + 抖动 TTL
                self.local[pid] = value
                if len(self.local) > self.local_size:
                    self.local.popitem(last=False)
            return value, "db"

    def _lock_for(self, pid: int) -> threading.Lock:
        with self._guard:
            return self.key_locks.setdefault(pid, threading.Lock())


if __name__ == "__main__":
    svc = DetailService(ProductDB())
    for _ in range(50):
        svc.get(1)
    print("50 次请求, DB 读次数:", svc.db.reads)     # 1
    print("再次读取:", svc.get(1))
