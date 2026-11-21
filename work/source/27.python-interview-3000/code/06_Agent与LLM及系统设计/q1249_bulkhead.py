"""舱壁隔离:按依赖分区资源池,慢依赖打满只牺牲自己的功能。"""
import threading, time
from collections import defaultdict


class Bulkhead:
    def __init__(self, capacities):
        self.cap = dict(capacities)
        self.in_use = defaultdict(int)
        self.mu = threading.Lock()
        self.rejected = defaultdict(int)

    def try_acquire(self, pool):
        with self.mu:
            if self.in_use[pool] < self.cap[pool]:
                self.in_use[pool] += 1
                return True
            self.rejected[pool] += 1
            return False

    def release(self, pool):
        with self.mu:
            self.in_use[pool] = max(0, self.in_use[pool] - 1)

    def call(self, pool, fn):
        if not self.try_acquire(pool):
            raise RuntimeError(f"{pool} 舱壁已满,快速失败")
        try:
            return fn()
        finally:
            self.release(pool)


if __name__ == "__main__":
    bw = Bulkhead({"payment": 3, "recommend": 3})
    # payment 变慢:占满自己的池
    def slow_payment():
        time.sleep(0.15)
        return "paid"
    ok, fails = [], []
    threads = []
    for i in range(8):
        def run(i=i):
            try:
                ok.append(bw.call("payment", slow_payment))
            except RuntimeError as e:
                fails.append(str(e))
        threads.append(threading.Thread(target=run))
    for t in threads: t.start()
    # 同时推荐服务完全不受影响
    for _ in range(10):
        bw.call("recommend", lambda: "rec-ok")
    for t in threads: t.join()
    print("payment 成功:", len(ok), "快速失败:", len(fails), "recommend 全部成功")
    assert len(ok) == 3 and len(fails) == 5, "payment 池容量 3,超出快速失败"
    assert bw.rejected["recommend"] == 0, "健康依赖零影响"

    # 池大小按 Little 定律核算
    qps, latency = 100, 0.03
    need = qps * latency
    print(f"recommend 池需求 = {qps}×{latency}s = {need} 并发,设池 3 有余量" if need < 3 else "池偏小")
    print("舱壁: 故障被限制在自己的分区,全服务不雪崩")
