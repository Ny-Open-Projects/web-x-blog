"""WATCH + MULTI 的 CAS 循环模拟: 竞争下重试直到成功"""
import threading
import time

class Store:
    def __init__(self):
        self.kv = {"stock": 10}
        self.version = {}
        self.lock = threading.Lock()

    def get(self, k):
        with self.lock:
            return self.kv.get(k)

    def watch_exec(self, watched_key, mutate):
        """模拟 WATCH: 版本未变才提交"""
        with self.lock:
            v0 = self.version.get(watched_key, 0)
        snapshot = self.kv[watched_key]           # 读快照
        new_val = mutate(snapshot)
        with self.lock:
            if self.version.get(watched_key, 0) != v0:
                return None                        # 被他人修改, 事务作废
            self.kv[watched_key] = new_val
            self.version[watched_key] = v0 + 1
            return new_val

def cas_decrement(store, key, want):
    for attempt in range(1, 5):
        result = store.watch_exec(key, lambda v: v - want)
        if result is not None:
            return attempt, result
        time.sleep(0.01)                           # 退避后重试
    return -1, None

if __name__ == "__main__":
    s = Store()
    out = []
    def buyer():
        out.append(cas_decrement(s, "stock", 1))
    ts = [threading.Thread(target=buyer) for _ in range(3)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("各买家(重试次数, 剩余):", out)
    print("高竞争下重试多 -> 这种场景换 Lua 一次原子扣减更优")
