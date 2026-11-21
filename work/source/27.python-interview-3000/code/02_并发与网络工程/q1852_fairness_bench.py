# -*- coding: utf-8 -*-
"""公平性实测: 公平锁的让位协议 vs 内建 Lock 的先到先得。

- 确定性判据是 "让位顺序": 等待者先排队, 持有者释放后立刻重试,
  公平锁必须让等待者先赢——与线程调度快慢无关, 可 100% 断言;
- 条纹 streak(同一线程连续获锁次数)是宏观观感: 公平锁条纹通常只有 1-2,
  内建 Lock 条纹动辄几十上百; 但它受 OS 调度影响会有离群值, 只做展示;
- 公平锁条纹偶发略长: 其它线程恰好都处在两次获取之间, 队列短暂为空。
"""
import collections
import sys
import threading
import time

sys.setswitchinterval(1e-6)           # 高频切换, 让线程真正咬在一起争锁
ROUNDS = 200
THREADS = 5
TRIALS = 200


class FairLock:
    def __init__(self):
        self._cond = threading.Condition()
        self._queue = collections.deque()
        self._owner = None

    def acquire(self, timeout=10.0):
        me = threading.get_ident()
        with self._cond:
            self._queue.append(me)
            deadline = time.monotonic() + timeout
            while self._owner is not None or self._queue[0] != me:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("公平锁等待超时")
                self._cond.wait(remain)
            self._queue.popleft()
            self._owner = me

    def release(self):
        with self._cond:
            self._owner = None
            self._cond.notify_all()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *exc):
        self.release()


def max_streak(seq):
    best = 0
    cur = 0
    prev = None
    for x in seq:
        cur = cur + 1 if x == prev else 1
        prev = x
        best = max(best, cur)
    return best


def bench(lock, seq):
    start = threading.Event()

    def worker(tag):
        start.wait()                          # 全员在同一瞬间起跑
        for _ in range(ROUNDS):
            with lock:
                seq.append(tag)

    ts = [threading.Thread(target=worker, args=("t%d" % i,)) for i in range(THREADS)]
    for t in ts:
        t.start()
    time.sleep(0.05)                          # 确保全员都堵在起跑线上
    t0 = time.monotonic()
    start.set()
    for t in ts:
        t.join()
    return time.monotonic() - t0


def handoff_trial(lock, fair):
    """等待者先排队, 持有者释放后立刻重试: 记录谁先拿到。"""
    order = []

    def waiter():
        lock.acquire()
        order.append("waiter")
        time.sleep(0.0005)                # 让持有者的重试申请先撞上队列
        lock.release()

    lock.acquire()                        # 主线程扮演持有者
    t = threading.Thread(target=waiter)
    t.start()
    if fair:
        while len(lock._queue) == 0:      # 公平锁可直接确认等待者已入队
            time.sleep(0.0005)
    else:
        time.sleep(0.02)                  # 内建锁无内省, 留足时间让它 park 在 acquire
    lock.release()                        # 释放后立刻重试
    lock.acquire()
    order.append("holder")
    lock.release()                        # 放开锁, 让仍在排队的等待者完成收尾
    t.join()
    return order[0]                       # "waiter"=让位给排队者, "holder"=持有者抢回


def main():
    # 实验一: 让位顺序(确定性判据, 可断言)
    fair_wins = sum(handoff_trial(FairLock(), fair=True) == "waiter" for _ in range(TRIALS))
    print("公平锁让位: 等待者先赢 %d/%d" % (fair_wins, TRIALS))
    assert fair_wins == TRIALS, "公平锁必须让已排队的等待者先赢, 一次都不许抢回"

    unfair_wins = sum(handoff_trial(threading.Lock(), fair=False) == "waiter"
                      for _ in range(TRIALS))
    print("内建 Lock 让位: 等待者先赢 %d/%d —— 释放者立刻重试通常能抢回, 这就是不公平的微观现场"
          % (unfair_wins, TRIALS))

    # 实验二: 条纹 streak(宏观观感, 受调度影响, 只做展示)
    seq_unfair, seq_fair = [], []
    cost_unfair = bench(threading.Lock(), seq_unfair)
    cost_fair = bench(FairLock(), seq_fair)
    counts = collections.Counter(seq_unfair)
    counts_fair = collections.Counter(seq_fair)
    assert all(c == ROUNDS for c in counts.values()), "每个线程都应拿到 ROUNDS 次"
    assert all(c == ROUNDS for c in counts_fair.values())
    print("内建 Lock: 最长条纹=%d 分布=%s 耗时=%.2fs"
          % (max_streak(seq_unfair), dict(counts), cost_unfair))
    print("公平锁  : 最长条纹=%d 分布=%s 耗时=%.2fs"
          % (max_streak(seq_fair), dict(counts_fair), cost_fair))
    print("结论: 公平由让位协议保证(实验一), 条纹(实验二)是它的宏观表现; 公平锁耗时更长, 用唤醒开销换无人饥饿")


if __name__ == "__main__":
    main()
