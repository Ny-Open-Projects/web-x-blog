import threading
import time


def naive_upgrade_demo() -> None:
    """裸升级: 两个读者同时 acquire_write, 互相等待读者归零 -> 死锁。"""
    lock = {"readers": 0, "writer": False}
    cond = threading.Condition()
    results = []

    def reader_want_upgrade(name: str) -> None:
        with cond:
            lock["readers"] += 1          # 双方都拿到了读锁
        with cond:
            lock["readers"] -= 1          # 裸升级: 先放掉自己再等对方
            while lock["readers"] > 0 or lock["writer"]:
                cond.wait()
            lock["writer"] = True
            results.append(name)
            lock["writer"] = False
            cond.notify_all()

    # 两个线程真正同时进入临界区, 制造竞态死锁
    barrier = threading.Barrier(2)
    threads = []
    for name in ("A", "B"):
        t = threading.Thread(target=lambda n=name: (barrier.wait(),
                                                    naive_step(cond, lock, results, n)),
                             daemon=True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join(timeout=0.5)
    hung = any(t.is_alive() for t in threads)
    print("裸升级并发两个线程 ->", "死锁复现(线程仍挂起)" if hung else "侥幸未死锁")


def naive_step(cond: threading.Condition, lock: dict, results: list, name: str) -> None:
    with cond:
        lock["readers"] += 1
        lock["readers"] -= 1
        while lock["readers"] > 0 or lock["writer"]:
            cond.wait()
        lock["writer"] = True
        results.append(name)
        lock["writer"] = False
        cond.notify_all()


class UpgradableRWLock:
    """预留名额的升级读写锁: 声明 upgrade 后新读者/新写者全部被挡住。"""

    def __init__(self) -> None:
        self._cond = threading.Condition()
        self._readers = 0
        self._writer = False
        self._reserved = False  # 升级预留名额

    def acquire_read(self, upgrade: bool = False) -> None:
        with self._cond:
            while self._writer or self._reserved:
                self._cond.wait()
            if upgrade:
                self._reserved = True
            self._readers += 1

    def upgrade(self) -> None:
        with self._cond:
            assert self._reserved, "upgrade 必须先 acquire_read(upgrade=True)"
            self._readers -= 1
            while self._readers > 0:      # 等现存读者退出, 预留挡住了新读者
                self._cond.wait()
            self._reserved = False
            self._writer = True

    def release_read(self) -> None:
        with self._cond:
            self._readers -= 1
            if self._readers == 0:
                self._cond.notify_all()

    def release_write(self) -> None:
        with self._cond:
            self._writer = False
            self._cond.notify_all()


def safe_upgrade_demo() -> None:
    lock = UpgradableRWLock()
    log = []

    def upgrader() -> None:
        lock.acquire_read(upgrade=True)
        log.append("读到旧值, 发现要改")
        lock.upgrade()
        log.append("升级成功, 独占写入")
        lock.release_write()

    def plain_reader() -> None:
        time.sleep(0.05)
        lock.acquire_read()
        log.append("普通读者被预留挡住, 升级完才进来")
        time.sleep(0.05)
        lock.release_read()

    u = threading.Thread(target=upgrader)
    r = threading.Thread(target=plain_reader, daemon=True)
    r.start()
    u.start()
    u.join(timeout=2)
    r.join(timeout=2)
    assert not u.is_alive(), "预留升级不应死锁"
    for line in log:
        print(line)


if __name__ == "__main__":
    naive_upgrade_demo()
    print("---")
    safe_upgrade_demo()
