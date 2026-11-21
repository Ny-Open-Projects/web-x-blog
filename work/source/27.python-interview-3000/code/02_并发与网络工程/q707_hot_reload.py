import json
import os
import tempfile
import threading
import time


class HotConfig:
    """mtime 轮询 + 原子快照替换的热更新配置。"""

    def __init__(self, path: str, poll: float = 0.1) -> None:
        self._path = path
        self._poll = poll
        self._mtime = 0.0
        self._snapshot: dict = {}
        self._lock = threading.Lock()  # 只保护加载过程, 读端无锁
        self.reload()
        self._stop = threading.Event()
        threading.Thread(target=self._watch, daemon=True).start()

    def reload(self) -> bool:
        try:
            with open(self._path) as f:
                data = json.load(f)
            self._validate(data)  # 校验失败 → 保留旧版
        except (OSError, json.JSONDecodeError, ValueError) as e:
            print(f"[config] 加载失败, 保留旧版: {e}")
            return False
        with self._lock:
            self._snapshot = data          # 原子引用替换
            self._mtime = os.path.getmtime(self._path)
        print(f"[config] 生效: {data}")
        return True

    @staticmethod
    def _validate(data: dict) -> None:
        if not isinstance(data.get("rate_limit"), int) or data["rate_limit"] <= 0:
            raise ValueError("rate_limit 必须是正整数")
        if data.get("log_level") not in ("DEBUG", "INFO", "WARNING", "ERROR"):
            raise ValueError("log_level 非法")

    def _watch(self) -> None:
        while not self._stop.is_set():
            try:
                mtime = os.path.getmtime(self._path)
                if mtime != self._mtime:
                    self.reload()
            except OSError:
                pass
            time.sleep(self._poll)

    def get(self) -> dict:
        return self._snapshot  # 不可变约定: 读端拿到的永远是完整版本

    def close(self) -> None:
        self._stop.set()


if __name__ == "__main__":
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"rate_limit": 100, "log_level": "INFO"}, f)
        path = f.name

    try:
        cfg = HotConfig(path)
        print("读取:", cfg.get()["rate_limit"])

        print("\n--- 正常更新 ---")
        with open(path, "w") as f:
            json.dump({"rate_limit": 500, "log_level": "DEBUG"}, f)
        time.sleep(0.3)
        print("读取:", cfg.get()["rate_limit"], cfg.get()["log_level"])

        print("\n--- 非法配置 → 保留旧版 ---")
        with open(path, "w") as f:
            json.dump({"rate_limit": -1, "log_level": "DEBUG"}, f)
        time.sleep(0.3)
        print("读取(应仍为 500):", cfg.get()["rate_limit"])

        print("\n--- 坏 JSON → 保留旧版 ---")
        with open(path, "w") as f:
            f.write("{broken")
        time.sleep(0.3)
        print("读取(应仍为 500):", cfg.get()["rate_limit"])
        cfg.close()
    finally:
        os.unlink(path)
