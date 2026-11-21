"""最小服务注册中心:注册 + 心跳续期 + TTL 剔除 + 发现。"""
import threading
import time


class Registry:
    def __init__(self, ttl=5.0):
        self.ttl = ttl
        self._services: dict[str, dict[str, float]] = {}  # svc -> {inst: 心跳时间}
        self._lock = threading.Lock()
        self._stop = threading.Event()
        threading.Thread(target=self._evict_loop, daemon=True).start()

    def register(self, svc: str, instance: str):
        with self._lock:
            self._services.setdefault(svc, {})[instance] = time.monotonic()

    def heartbeat(self, svc: str, instance: str) -> bool:
        with self._lock:
            return self._services.get(svc, {}).update({instance: time.monotonic()}) or True

    def discover(self, svc: str) -> list:
        now = time.monotonic()
        with self._lock:
            return [i for i, t in self._services.get(svc, {}).items()
                    if now - t < self.ttl]

    def deregister(self, svc: str, instance: str):
        with self._lock:
            self._services.get(svc, {}).pop(instance, None)

    def _evict_loop(self):
        while not self._stop.wait(1.0):
            now = time.monotonic()
            with self._lock:
                for svc in list(self._services):
                    stale = [i for i, t in self._services[svc].items()
                             if now - t >= self.ttl]
                    for i in stale:
                        del self._services[svc][i]
                        print(f"[evict] {svc}/{i} 心跳超时剔除")


if __name__ == "__main__":
    reg = Registry(ttl=2.0)
    reg.register("user-svc", "10.0.0.1:8001")
    reg.register("user-svc", "10.0.0.2:8002")
    print("发现:", reg.discover("user-svc"))
    reg.heartbeat("user-svc", "10.0.0.1:8001")   # 实例1 心跳续期
    time.sleep(2.5)                               # 实例2 停止心跳
    print("TTL 后存活:", reg.discover("user-svc"))
    reg.deregister("user-svc", "10.0.0.1:8001")
    print("主动注销后:", reg.discover("user-svc"))
