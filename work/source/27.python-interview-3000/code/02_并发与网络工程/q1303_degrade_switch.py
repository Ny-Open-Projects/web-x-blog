import threading
import time


class DegradeSwitch:
    """开关面板: 整体替换不可变快照, 请求粒度取一次、全程一致。"""

    def __init__(self, features: dict) -> None:
        self._lock = threading.Lock()
        self._snapshot = dict(features)   # {功能名: 是否可用}

    def snapshot(self) -> dict:
        with self._lock:
            return dict(self._snapshot)   # 请求开始时取一次

    def set_all(self, features: dict) -> None:
        with self._lock:
            self._snapshot.update(features)


def serve_request(snap: dict, feature: str, stats: dict) -> None:
    if snap.get(feature, True):
        stats["normal"] += 1              # 正常路径
    else:
        stats["degraded"] += 1            # 兜底路径: 返回缓存/默认值


def main() -> None:
    switch = DegradeSwitch({"recommend": True, "search": True})
    stats = {"normal": 0, "degraded": 0}
    stats_lock = threading.Lock()
    stop = threading.Event()

    def worker() -> None:
        while not stop.is_set():          # 持续服务, 覆盖翻转前后的所有阶段
            snap = switch.snapshot()      # 每个请求取一次快照
            with stats_lock:
                serve_request(snap, "recommend", stats)

    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()

    time.sleep(0.3)
    print("运维翻转开关: recommend -> 关闭")
    switch.set_all({"recommend": False})
    time.sleep(0.3)
    print("恢复: recommend -> 开启")
    switch.set_all({"recommend": True})
    time.sleep(0.3)
    stop.set()

    for t in threads:
        t.join()
    print(f"正常服务 {stats['normal']} 次, 降级兜底 {stats['degraded']} 次")
    assert stats["degraded"] > 0 and stats["normal"] > 0, "两个阶段都应出现"


if __name__ == "__main__":
    main()
