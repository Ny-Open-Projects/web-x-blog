"""延迟双删: 两次删除 + 中间等待覆盖并发回填窗口"""
import threading
import time


class Service:
    def __init__(self, delay: float = 0.05):
        self.cache: dict = {}
        self.db: dict = {"item:1": "old"}
        self.delay = delay
        self.delete_log: list = []

    def _delete_cache(self, key: str):
        self.cache.pop(key, None)
        self.delete_log.append(round(time.time() - self.t0, 3))

    def write(self, key: str, value: str) -> None:
        self.t0 = time.time()
        self._delete_cache(key)                       # 第一次删
        self.db[key] = value                          # 更新 DB
        timer = threading.Timer(self.delay, self._delete_cache, args=(key,))
        timer.daemon = True
        timer.start()                                 # 延迟第二次删
        # 更好的替代: binlog 订阅(canal/Debezium)异步删缓存, 可靠可重试

    def read_concurrent(self, key: str) -> str:
        """模拟并发读: 先读缓存未命中, 读到 DB 后回填"""
        if key not in self.cache:
            self.cache[key] = self.db.get(key)
        return self.cache[key]


if __name__ == "__main__":
    svc = Service()
    svc.write("item:1", "new")              # 写入期间穿插一次旧读
    stale = svc.read_concurrent("item:1")   # 可能读到 old 并回填
    time.sleep(0.1)                         # 等第二次删除执行
    print("并发读回填值:", stale)
    print("两次删除时间点:", svc.delete_log)
    print("最终读:", svc.read_concurrent("item:1"), "已被第二次删除纠正")
