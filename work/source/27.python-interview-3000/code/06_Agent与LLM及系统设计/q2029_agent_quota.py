"""并发 Agent 的资源配额:分组信号量限并发,等待超时即拒绝,峰值不得越过限额。"""
import threading
import time


class QuotaGroup:
    def __init__(self, name, limit, wait_timeout=0.5):
        self.name = name
        self.limit = limit
        self.wait_timeout = wait_timeout
        self.sem = threading.BoundedSemaphore(limit)
        self.current = 0
        self.peak = 0
        self.rejected = 0
        self.lock = threading.Lock()

    def acquire(self, wait_timeout=None):
        wt = self.wait_timeout if wait_timeout is None else wait_timeout
        if not self.sem.acquire(timeout=wt):
            with self.lock:
                self.rejected += 1
            raise TimeoutError("配额组 %s 等待超时,拒绝进入" % self.name)
        with self.lock:
            self.current += 1
            self.peak = max(self.peak, self.current)

    def release(self):
        with self.lock:
            self.current -= 1
        self.sem.release()


if __name__ == "__main__":
    group = QuotaGroup("llm", limit=2, wait_timeout=0.5)
    in_region = []
    peak_seen = [0]
    lock = threading.Lock()
    stats = {"ok": 0, "reject": 0}

    def worker(n, hold, patience=None):
        try:
            group.acquire(patience)
        except TimeoutError:
            with lock:
                stats["reject"] += 1
            return
        with lock:
            in_region.append(n)
            peak_seen[0] = max(peak_seen[0], len(in_region))
        time.sleep(hold)
        with lock:
            in_region.remove(n)
        group.release()
        with lock:
            stats["ok"] += 1

    # 场景一:6 个短任务挤限额 2,全部应通过,峰值不越界
    ts = [threading.Thread(target=worker, args=(i, 0.1)) for i in range(6)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    assert stats["ok"] == 6 and stats["reject"] == 0
    assert peak_seen[0] <= 2 and group.peak <= 2, "并发峰值不得超过限额"

    # 场景二:两个长任务占满全部槽位,短耐心调用等待超时被拒绝而不是无限等
    blockers = [threading.Thread(target=worker, args=("hold%d" % i, 0.6))
                for i in range(2)]
    for t in blockers:
        t.start()
    time.sleep(0.05)
    impatient = threading.Thread(target=worker, args=("impatient", 0.01, 0.2))
    impatient.start()
    for t in blockers:
        t.join()
    impatient.join()
    assert stats["reject"] >= 1, "槽位被占满时应拒绝短耐心调用"
    assert group.current == 0, "全部结束后配额必须归还干净"
    print("并发配额通过:峰值不越限 全员可达 拒绝 %d 次 释放干净" % stats["reject"])
