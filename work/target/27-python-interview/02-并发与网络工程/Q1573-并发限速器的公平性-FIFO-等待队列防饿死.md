---
title: [Q1573] 并发限速器的公平性:FIFO 等待队列防饿死
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1573 · 并发限速器的公平性:FIFO 等待队列防饿死

> 难度:★★★☆ | 标签:限流, 公平性, Condition

**问**:限速器在高并发下,有的线程总能拿到名额、有的线程几乎永远拿不到——这是为什么,怎么修?

**答**:常见实现是"自旋抢名额":拿不到就睡一小觉再试,睡醒时机全凭调度,运气成了分配规则,统计上出现饿死。修复是把等待者组织成显式 FIFO 队列:acquire 时入队,只有队首有资格等下一个名额,拿到才出队并唤醒下一个队首——放行顺序严格等于到达顺序。公平的代价:吞吐略降(每次放行要 notify_all),实现复杂度上升。经验法则:低频限流用自旋版无妨;名额稀缺、等待者多的场景必须公平队列。

```python
# file: code/02_并发与网络工程/q1573_fair_ratelimit.py
"""并发限速器的公平性: FIFO 等待队列防饿死。

"拿到名额才能过"的自旋实现里, 睡醒时机全凭调度运气, 运气差的线程可能
一直被插队。公平限速器把等待者排成显式队列, 每放出一个名额都从队首取,
保证先到先得。演示: 12 个线程争抢限速名额, 对比两种实现
"放行顺序 vs 到达顺序"的逆序数(逆序数越大越不公平)。
"""
import threading
import time

RATE = 8.0      # 每秒放行名额


class UnfairLimiter:
    """自旋重试版: 高并发下放行顺序被打乱。"""
    def __init__(self):
        self.lock = threading.Lock()
        self.next_slot = time.monotonic()
        self.arrival = 0
        self.grants = []            # (到达序, tag)

    def acquire(self, tag):
        with self.lock:
            self.arrival += 1
            my_seq = self.arrival
        while True:
            with self.lock:
                now = time.monotonic()
                if now >= self.next_slot:
                    self.next_slot = max(now, self.next_slot) + 1.0 / RATE
                    self.grants.append((my_seq, tag))
                    return
            time.sleep(0.002)       # 自旋: 谁抢到全凭运气


class FairLimiter:
    """FIFO 公平版: 队首优先, 先到先得。"""
    def __init__(self):
        self.cond = threading.Condition()
        self.next_slot = time.monotonic()
        self.arrival = 0
        self.queue = []             # [(到达序, tag)]
        self.grants = []            # 到达序

    def acquire(self, tag):
        with self.cond:
            self.arrival += 1
            me = (self.arrival, tag)
            self.queue.append(me)
            while self.queue[0] != me:
                self.cond.wait()        # 不是队首: 等前面的人先走
            while True:
                now = time.monotonic()
                if now >= self.next_slot:
                    break
                self.cond.wait(self.next_slot - now)   # 队首等名额
            self.next_slot = max(now, self.next_slot) + 1.0 / RATE
            self.queue.pop(0)
            self.grants.append(me[0])
            self.cond.notify_all()      # 唤醒下一个队首


def inversions(seq):
    return sum(1 for i in range(len(seq))
               for j in range(i + 1, len(seq)) if seq[i] > seq[j])


def main():
    n = 12
    arrive_barrier = threading.Barrier(n)

    def run(limiter, tag):
        arrive_barrier.wait()
        limiter.acquire(tag)

    unf = UnfairLimiter()
    ts = [threading.Thread(target=run, args=(unf, i)) for i in range(n)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    seq_unf = [s for s, _ in unf.grants]
    print("自旋版放行序(到达序):", seq_unf, "逆序数:", inversions(seq_unf))

    fair = FairLimiter()
    ts = [threading.Thread(target=run, args=(fair, i)) for i in range(n)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print("公平版放行序(到达序):", fair.grants)
    assert sorted(fair.grants) == list(range(1, n + 1)), "全员放行且按到达序"
    assert inversions(fair.grants) == 0, "公平版必须严格按到达序放行"
    print("结论: 名额稀缺时, 显式 FIFO 队列是公平性的唯一保障")


if __name__ == "__main__":
    main()
```

**追问**:1) notify_all 会不会惊群?——会唤醒全部等待者,但只有队首能拿到名额,其余重新入睡;等待者很多时可换成逐个 notify 或给每个等待者发专属 Event。2) 自旋版饿死的机制是什么?——睡眠醒来后名额可能刚被刚到的线程抢走(它没睡、抢得快),等待者越多「醒来撞上空位」的概率越低,统计上形成饥饿;FIFO 队列把「资格」从时机改成顺序,才是根治。3) 公平队列与条件变量的配合?——队首等待者在自己的 Event/Condition 上等名额,释放者把名额交给队首并 notify 它一个;每个等待者专属 Event 可以做到精确唤醒,notify_all 的惊群开销(Q573 原问)随之消失。4) 生产陷阱?——队首拿到名额后忘了出队,队列永久卡死;队列与名额计数在不同锁下更新,出现「名额有空但队首没被唤醒」的幽灵;公平模式误用于高频低争用场景,白白损失吞吐;等待者超时退出后没从队列摘除,名额发给幽灵。

---
