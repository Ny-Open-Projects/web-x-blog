"""配置版本化快照:请求内固定一次读取(纯标准库)。"""
import threading


class ConfigCenter:
    def __init__(self, initial):
        self._data = dict(initial)
        self._version = 1
        self._lock = threading.Lock()
        self._subs = []

    def update(self, changes):
        with self._lock:
            self._data.update(changes)
            self._version += 1
            version = self._version
        for cb in self._subs:            # 锁外回调,避免死锁
            cb(version)

    def subscribe(self, cb):
        self._subs.append(cb)

    def snapshot(self):
        with self._lock:
            return self._version, dict(self._data)   # 不可变快照


center = ConfigCenter({"ratio": 0.1, "flag": True})


def handle_request():
    version, cfg = center.snapshot()     # 请求开始固定快照
    return version, cfg["ratio"]


print(handle_request())
center.update({"ratio": 0.2})
print(handle_request())
center.subscribe(lambda v: print("配置已推进到版本", v))
center.update({"flag": False})
