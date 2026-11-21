import threading
import time


class Scheduler:
    def __init__(self):
        self.stop_event = threading.Event()
        self.threads: list[threading.Thread] = []

    def every(self, interval: float, name: str = ""):
        def deco(fn):
            def loop():
                while not self.stop_event.is_set():
                    start = time.monotonic()
                    try:
                        fn()
                    except Exception as exc:
                        print(f"[error] task {name}: {exc}")
                    # 补齐剩余等待,执行慢于周期时自动跳过
                    self.stop_event.wait(max(0, interval - (time.monotonic() - start)))
            t = threading.Thread(target=loop, name=f"sched-{name or fn.__name__}")
            self.threads.append(t)
            t.start()
            return fn
        return deco

    def stop(self) -> None:
        self.stop_event.set()
        for t in self.threads:
            t.join()


sched = Scheduler()


@sched.every(0.2, name="heartbeat")
def heartbeat():
    print("heartbeat at", time.strftime("%H:%M:%S"))


if __name__ == "__main__":
    time.sleep(0.5)
    sched.stop()
    print("scheduler stopped")
