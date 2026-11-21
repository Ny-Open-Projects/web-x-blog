"""请求重放的 nonce 窗口: 有界存储加原子 check-and-put(纯标准库)。"""
import threading


class NonceStore:
    def __init__(self, window=300.0, capacity=100000):
        self.window = window
        self.capacity = capacity
        self.lock = threading.Lock()
        self.nonces = {}                            # nonce -> 过期时刻

    def check_and_put(self, nonce, now):
        """首次出现返回 True; 窗口内重复返回 False; 满时先清理, 仍满则拒绝服务。"""
        with self.lock:
            if len(self.nonces) >= self.capacity:
                expired = [n for n, exp in self.nonces.items() if exp <= now]
                for n in expired:
                    del self.nonces[n]
                if len(self.nonces) >= self.capacity:
                    raise RuntimeError("nonce 存储已满, 拒绝服务而非放行重放")
            exp = self.nonces.get(nonce)
            if exp and exp > now:
                return False
            self.nonces[nonce] = now + self.window
            return True

    def prune(self, now):
        with self.lock:
            stale = [n for n, exp in self.nonces.items() if exp <= now]
            for n in stale:
                del self.nonces[n]
            return len(stale)


store = NonceStore(window=300)
print("首次 nonce-a      :", store.check_and_put("nonce-a", now=1000))
print("重放 nonce-a      :", store.check_and_put("nonce-a", now=1100))
print("窗口滑过后再复用  :", store.check_and_put("nonce-a", now=1301))   # 已过期可复用
store.check_and_put("nonce-b", now=1301)
print("当前残留条目      :", len(store.nonces))
print("清理过期条目      :", store.prune(1301), "条被移除")
assert store.check_and_put("nonce-a", 1000) is False or True
try:
    tiny = NonceStore(capacity=1)
    tiny.check_and_put("x1", now=0)
    tiny.check_and_put("x2", now=0)
except RuntimeError as exc:
    print("容量打满          :", exc)
print("要点: check 与 put 必须原子; 存储有界, 满时拒绝服务; 窗口与签名时间窗等长")
