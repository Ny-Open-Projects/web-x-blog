"""带 TTL 与写锁的会话状态存储,模拟 Redis 行为(纯内存实现)。"""
import threading
import time


class SessionStore:
    def __init__(self, ttl_seconds: float = 1.0):
        self.ttl = ttl_seconds
        self._data: dict[str, dict] = {}
        self._expire: dict[str, float] = {}
        self._locks: dict[str, threading.Lock] = {}

    def _alive(self, sid: str) -> bool:
        return sid in self._data and time.time() < self._expire[sid]

    def get(self, sid: str) -> dict:
        if not self._alive(sid):
            self._data.pop(sid, None)
            return {"messages": [], "tasks": []}
        return self._data[sid]

    def save(self, sid: str, state: dict):
        self._data[sid] = state
        self._expire[sid] = time.time() + self.ttl

    def update(self, sid: str, fn):
        """同一 session 的更新串行化,避免并发交错。"""
        lock = self._locks.setdefault(sid, threading.Lock())
        with lock:
            state = self.get(sid)
            fn(state)
            self.save(sid, state)


if __name__ == "__main__":
    store = SessionStore(ttl_seconds=1.0)

    def append(state):
        state["messages"].append({"role": "user", "content": "hi"})

    store.update("s1", append)
    store.update("s1", append)
    print("读取:", store.get("s1"))
    time.sleep(1.1)
    print("过期后:", store.get("s1"))
