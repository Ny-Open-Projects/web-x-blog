---
title: [Q1852] 公平性实测:条纹 streak 度量锁的霸占程度
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1852 · 公平性实测:条纹 streak 度量锁的霸占程度

> 难度:★★★★ | 标签:公平性, 基准测量, 条纹

**问**:怎么用一个可测量的指标证明一把锁是霸道的还是公平的?

**答**:公平性要拆成两层来测。微观判据是 '让位顺序':等待者先排进锁的等待队列,持有者释放后立刻重试,公平锁必须让排队的等待者先赢——这与线程调度快慢无关,可以 100% 断言。宏观观感是 '连续授权条纹':记录每次获锁的线程,统计同一线程连续获锁的最大次数,霸道锁条纹拉得很长(刚释放者立刻重入),公平锁条纹接近 1(释放后必须让队首接棒)。

- 实验一(确定性):公平锁让位 200/200 全部由等待者先赢;内建 Lock 同样协议下,等待者基本抢不赢刚释放的持有者——这就是它不公平的微观现场;

- 实验二(宏观):条纹 streak 是统计量,公平锁条纹通常只有 1-2,内建 Lock 动辄几十上百;但它受 OS 调度影响有离群值(极端时某线程可能整场独跑,连公平锁也可能出现长条纹),所以只做展示不做硬断言;

- 每线程获锁总次数两者都是满额——公平性影响的是 '顺序与延迟',不是 '最终拿没拿到'。

这个度量方法可以直接搬到自研锁的测试里,比 '感觉上公平' 可靠得多。

```python
# file: code/02_并发与网络工程/q1852_fairness_bench.py
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
```

**追问**:1) 为什么公平锁条纹偶尔会到 2-3?——公平性只约束 '已在队列里' 的线程;一个线程刚释放、其他线程还没来得及重新入队的瞬间,它重入不算插队,这是窗口期不是漏洞。2) 让位顺序实验为什么能 100% 断言?——它把「释放后谁先重试」的时序做成协议:等待者先入队、持有者才重试,公平锁的谓词(队首优先)保证让位必发生;条纹 streak 受 OS 调度影响(线程可能整场没被调度),只可展示不可断言——「把时序假设写进协议」是并发测试可断言化的通用手法(Q1852 原问的重构经验)。3) 公平性的度量还能怎么做?——获锁延迟分布(等待者从入队到拿锁的时长):公平锁的方差小;上下文切换次数(霸道锁让持有者重入,切换少吞吐高)——公平性与吞吐是光谱两端,选型看「谁在等」(交互式公平 vs 批量吞吐)。4) 生产陷阱?——条纹做硬断言(离群值假失败);公平性实验在多核+负载下跑(结果不可复现);把「公平锁」当正确性修复(它只解决饿死,竞态还得靠锁本身);度量指标只在单线程解释器上测(GIL 行为差异)。


---
