"""配置热更新:mtime 检测 + 校验后原子替换快照(纯标准库)。"""
import json
import os
import tempfile
import threading
import time


class HotConfig:
    def __init__(self, path):
        self.path = path
        self._snapshot = self._load(path)
        self._mtime = os.stat(path).st_mtime_ns
        self._lock = threading.Lock()

    @staticmethod
    def _load(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def maybe_reload(self):
        try:
            mtime = os.stat(self.path).st_mtime_ns
        except OSError:
            return False
        if mtime == self._mtime:
            return False
        try:
            snap = self._load(self.path)
        except (ValueError, OSError) as exc:
            print("配置损坏,沿用旧值:", exc)
            self._mtime = mtime          # 避免反复报错,等待人工修复
            return False
        with self._lock:
            self._snapshot = snap
            self._mtime = mtime
        return True

    @property
    def snapshot(self):
        with self._lock:
            return self._snapshot


tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
json.dump({"timeout": 3, "retries": 2}, tmp)
tmp.close()
cfg = HotConfig(tmp.name)
print("初始:", cfg.snapshot)

time.sleep(0.02)
with open(tmp.name, "w", encoding="utf-8") as f:
    json.dump({"timeout": 5, "retries": 5}, f)
print("合法更新生效:", cfg.maybe_reload(), cfg.snapshot)

with open(tmp.name, "w", encoding="utf-8") as f:
    f.write("{bad json")
print("损坏配置沿用旧值:", cfg.maybe_reload() is False, cfg.snapshot)
os.unlink(tmp.name)
