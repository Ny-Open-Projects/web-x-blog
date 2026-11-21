"""信号量资源池的租约设计: 超时借出 + 泄漏回收线程。

要点:
- threading.Semaphore 只回答"还有几个空位", 不回答"谁借了没还";
- 每次借出登记 Lease(借出人/时刻/槽位), 正常归还时注销;
- 守护回收线程周期扫描: 租约超过 TTL 视为泄漏, 强制回收槽位。
"""
import threading
import time

LEASE_TTL = 0.4        # 租约超过该时长视为泄漏
REAP_INTERVAL = 0.1


class Lease:
    def __init__(self, pool, slot_id):
        self.pool = pool
        self.slot_id = slot_id
        self.taken_at = time.monotonic()
        self.owner = threading.current_thread().name
        self.returned = False

    def release(self):
        if self.returned:
            return                      # 幂等: 重复归还无害
        self.returned = True
        self.pool._give_back(self.slot_id, self)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.release()


class LeasePool:
    def __init__(self, size):
        self.size = size
        self.slots = list(range(size))
        self.free_sem = threading.Semaphore(size)   # 管"数量"
        self.mu = threading.Lock()
        self.cond = threading.Condition(self.mu)
        self.leases = {}                            # 管"责任"
        self.reclaimed = []

    def acquire(self, timeout=1.0):
        if not self.free_sem.acquire(timeout=timeout):
            raise TimeoutError("资源池已满且等待超时")
        with self.cond:
            slot_id = self.slots.pop()
            lease = Lease(self, slot_id)
            self.leases[lease] = slot_id
        return lease

    def _give_back(self, slot_id, lease):
        with self.cond:
            if lease in self.leases:
                del self.leases[lease]
                self.slots.append(slot_id)
                self.cond.notify()
        self.free_sem.release()

    def reap_loop(self):
        while True:
            time.sleep(REAP_INTERVAL)
            now = time.monotonic()
            with self.cond:
                leaked = [x for x in self.leases if now - x.taken_at > LEASE_TTL]
                for lease in leaked:
                    slot_id = self.leases.pop(lease)
                    lease.returned = True
                    # 泄漏槽位的底层资源状态不可信, 生产中应重建或标记待检
                    self.slots.append(slot_id)
                    self.reclaimed.append((lease.owner, slot_id))
                    self.cond.notify()
            for _ in leaked:
                self.free_sem.release()


def main():
    pool = LeasePool(2)
    threading.Thread(target=pool.reap_loop, daemon=True).start()
    log = []
    log_lock = threading.Lock()

    def borrower(name, leak):
        lease = pool.acquire(timeout=1.0)
        with log_lock:
            log.append((name, "borrow", lease.slot_id))
        if leak:
            return                  # 故意不归还: 模拟持有人"卡死"
        time.sleep(0.05)
        lease.release()
        with log_lock:
            log.append((name, "give-back", lease.slot_id))

    ts = [threading.Thread(target=borrower, args=(f"t{i}", i == 0), daemon=True)
          for i in range(4)]
    for t in ts:
        t.start()

    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline and len(pool.reclaimed) < 1:
        time.sleep(0.05)

    ok = []
    def late_borrower():
        try:
            lease = pool.acquire(timeout=1.5)
            ok.append(lease.slot_id)
            lease.release()
        except TimeoutError as e:
            ok.append(str(e))

    t = threading.Thread(target=late_borrower)
    t.start()
    t.join()

    for item in log:
        print("事件:", *item)
    print("回收记录:", pool.reclaimed)
    print("迟到借出者结果:", ok)
    assert pool.reclaimed, "泄漏租约应被回收线程收回"
    assert ok and isinstance(ok[0], int), "回收后新借出应成功"
    print("结论: Semaphore 管数量, 租约表管责任, 回收线程管兜底")


if __name__ == "__main__":
    main()
