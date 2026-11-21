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
