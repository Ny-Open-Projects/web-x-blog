"""限流器: KV 接口语义下实现, DictKV 可直接跑, redis-py 用同名命令"""


class DictKV:
    """模拟 INCR 与 EXPIRE 的最小 KV 存储"""

    def __init__(self):
        self._data: dict = {}
        self._ttl: dict = {}

    def incr(self, key: str) -> int:
        self._data[key] = self._data.get(key, 0) + 1
        return self._data[key]

    def expire(self, key: str, seconds: int) -> None:
        self._data.setdefault(key, 0)
        self._ttl[key] = seconds          # 真实 Redis 到期自动删除


def is_allowed(kv: DictKV, user: str, limit: int = 5, window: int = 60) -> bool:
    """固定窗口限流: 每用户每 window 秒最多 limit 次"""
    key = f"rate:{user}:{int(window)}"
    count = kv.incr(key)
    if count == 1:
        kv.expire(key, window)
    return count <= limit


if __name__ == "__main__":
    kv = DictKV()
    for i in range(7):
        ok = is_allowed(kv, "alice")
        print(f"第 {i + 1} 次请求: {'通过' if ok else '被限流'}")
    # redis-py 等价: pipe = client.pipeline(); pipe.incr(key); pipe.expire(key, window); pipe.execute()
