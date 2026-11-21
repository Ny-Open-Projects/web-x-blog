# -*- coding: utf-8 -*-
"""任务窃取 work stealing 概念模拟: 自己的队列尾取, 偷别人的队列头。

- 每个 worker 拥有双端队列: 自己从尾部取(局部性好), 饿了从别人头部偷(最老的先跑);
- 偷是逐个试探别人的锁, 不加全局锁, 争用被限制在单个 victim 上;
- 负载天然倾斜时, 饿汉 worker 只能靠偷活下来, 这就是窃取的负载均衡作用。
"""
import collections
import threading
import time

WORKERS = 4


class StealingPool:
    def __init__(self, n):
        self._own = [collections.deque() for _ in range(n)]
        self._locks = [threading.Lock() for _ in range(n)]
        self._exec = collections.defaultdict(list)   # worker -> task ids
        self._steals = []                            # (thief, victim)
        self._lock = threading.Lock()

    def seed(self, idx, task_ids):
        with self._locks[idx]:
            self._own[idx].extend(task_ids)

    def _pop_own(self, idx):
        with self._locks[idx]:
            return self._own[idx].pop() if self._own[idx] else None

    def _steal_one(self, idx):
        n = len(self._own)
        for step in range(1, n + 1):
            victim = (idx + step) % n
            with self._locks[victim]:
                if self._own[victim]:
                    t = self._own[victim].popleft()   # 偷最老的
                    with self._lock:
                        self._steals.append((idx, victim))
                    return t
        return None

    def worker(self, idx):
        while True:
            t = self._pop_own(idx)
            if t is None:
                t = self._steal_one(idx)
            if t is None:
                time.sleep(0.003)
                with self._lock:
                    total = sum(len(v) for v in self._exec.values())
                if total >= EXPECTED_TOTAL:
                    return
                continue
            time.sleep(0.002)                     # 模拟执行
            with self._lock:
                self._exec[idx].append(t)


EXPECTED_TOTAL = 19


def main():
    pool = StealingPool(WORKERS)
    pool.seed(0, ["t%02d" % i for i in range(12)])
    pool.seed(1, ["s%02d" % i for i in range(6)])
    pool.seed(2, ["u00"])
    pool.seed(3, [])                              # 饿汉, 只能偷

    ts = [threading.Thread(target=pool.worker, args=(i,)) for i in range(WORKERS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=10.0)
        assert not t.is_alive(), "窃取池应正常收敛退出"

    done = []
    for idx in range(WORKERS):
        done.extend(pool._exec[idx])
    print("各 worker 执行分布:", {("w%d" % i): len(pool._exec[i]) for i in range(WORKERS)})
    print("窃取事件数:", len(pool._steals), "样例:", pool._steals[:5])
    assert len(done) == EXPECTED_TOTAL and len(set(done)) == EXPECTED_TOTAL, \
        "所有任务恰好执行一次"
    assert len(pool._exec[3]) >= 1, "空队列的饿汉 worker 必须靠窃取获得任务"
    assert len(pool._steals) >= 1, "至少发生一次窃取"
    print("结论: 自队尾取自队头偷, 无全局锁也完成了负载均衡")


if __name__ == "__main__":
    main()
