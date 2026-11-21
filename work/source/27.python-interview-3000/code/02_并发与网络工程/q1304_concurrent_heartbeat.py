import concurrent.futures
import threading
import time


class HeartbeatScheduler:
    """调度线程只派发, 真正的探测在线程池里隔离执行。"""

    def __init__(self, interval: float) -> None:
        self._interval = interval
        self._targets = {}          # name -> probe 函数
        self._lateness = {}         # name -> [迟到秒数]
        self._fails = {}
        self._pool = concurrent.futures.ThreadPoolExecutor(max_workers=8)
        self._stop = threading.Event()

    def register(self, name: str, probe) -> None:
        self._targets[name] = probe
        self._lateness[name] = []
        self._fails[name] = 0

    def _beat(self, name: str, probe, due: float) -> None:
        self._lateness[name].append(max(0.0, time.monotonic() - due))
        try:
            probe()
        except Exception:
            self._fails[name] += 1  # 异常隔离在任务内, 不影响调度

    def run(self) -> None:
        while not self._stop.is_set():
            due = time.monotonic()
            for name, probe in list(self._targets.items()):
                self._pool.submit(self._beat, name, probe, due)
            self._stop.wait(self._interval)

    def stop(self) -> None:
        self._stop.set()
        self._pool.shutdown(wait=True)


def main() -> None:
    def broken_probe() -> None:
        time.sleep(0.5)               # 坏目标: 每拍卡 0.5 秒
        raise ConnectionError("下游挂了")

    def good_probe() -> None:
        time.sleep(0.001)

    sched = HeartbeatScheduler(interval=0.1)
    sched.register("broken", broken_probe)
    sched.register("good-1", good_probe)
    sched.register("good-2", good_probe)

    t = threading.Thread(target=sched.run, daemon=True)
    t.start()
    time.sleep(1.0)
    sched.stop()

    fails = sched._fails["broken"]
    worst_good = max(max(v) for k, v in sched._lateness.items() if k != "broken")
    print(f"坏目标失败 {fails} 次(被隔离), 好目标最大迟到 {worst_good*1000:.1f} ms")
    assert worst_good < 0.05, "好目标不应被坏目标拖垮"
    print("故障隔离验证通过")


if __name__ == "__main__":
    main()
