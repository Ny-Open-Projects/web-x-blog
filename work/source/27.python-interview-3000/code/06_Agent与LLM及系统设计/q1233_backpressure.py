"""背压传播:阻塞队列 vs 信用制对比,展示无界队列为何灾难。"""
import queue, threading, time


def producer_blocking(q, n, produced):
    for i in range(n):
        q.put(i)                       # 队列满则阻塞:背压自动生效
        produced[0] += 1


def consumer_blocking(q, n, delay):
    for i in range(n):
        time.sleep(delay)              # 慢消费者
        q.get()


class CreditFlow:
    """信用制:消费者按吞吐发放额度,生产者凭额度发送。"""

    def __init__(self, initial_credits=2):
        self.credits = initial_credits
        self.mu = threading.Lock()
        self.waited = 0

    def acquire(self):
        with self.mu:
            if self.credits <= 0:
                self.waited += 1
                return False
            self.credits -= 1
            return True

    def ack(self, n=1):
        with self.mu:
            self.credits += n


if __name__ == "__main__":
    # 1 阻塞队列:有界,生产者速度被强制对齐
    q = queue.Queue(maxsize=2)
    produced = [0]
    t1 = threading.Thread(target=producer_blocking, args=(q, 8, produced))
    t2 = threading.Thread(target=consumer_blocking, args=(q, 8, 0.01))
    t1.start(); t2.start(); t1.join(); t2.join()
    print(f"有界队列: 生产 {produced[0]} 条全部完成,峰值堆积不超过 2")
    assert produced[0] == 8

    # 2 信用制:额度 2,异步 ack 慢于生产 -> 生产者必然等待补额度
    flow = CreditFlow(initial_credits=2)

    def delayed_acks(flow, n, delay):
        for _ in range(n):
            time.sleep(delay)
            flow.ack()

    threading.Thread(target=delayed_acks, args=(flow, 10, 0.003), daemon=True).start()
    sent = 0
    for i in range(10):
        while not flow.acquire():
            time.sleep(0.001)
        sent += 1
    print(f"信用制: 发送 {sent} 条,等待补额度 {flow.waited} 次")
    assert sent == 10 and flow.waited > 0, "额度受限时生产者必须等待"
    print("背压在源头生效,任何一层都不无界堆积")
