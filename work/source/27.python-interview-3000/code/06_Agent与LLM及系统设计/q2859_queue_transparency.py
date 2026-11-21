"""Q2859 长请求的排队透明化:队列位置 预估等待与自适应均值的校正。

长请求最怕的不是慢,是「不知道还要等多久」。入队时给出队列位置和
预估等待,预估基于近期完成耗时的滑动均值,每完成一单就校正一次,
排障时用户看到的不是黑洞,而是会收敛的倒计时。
"""

from collections import deque


class TransparentQueue:
    def __init__(self, seed_avg_ms=800.0, alpha=0.5):
        self.waiting = deque()   # (rid, enqueue_ts)
        self.avg_ms = seed_avg_ms
        self.alpha = alpha

    def enqueue(self, rid, now):
        self.waiting.append((rid, now))
        pos = len(self.waiting)
        eta = int(pos * self.avg_ms)
        return pos, eta

    def finish(self, rid, now):
        for i, (r, t0) in enumerate(self.waiting):
            if r == rid:
                self.waiting.remove((r, t0))
                waited = now - t0
                self.avg_ms = self.alpha * self.avg_ms + (1 - self.alpha) * waited
                return waited
        raise KeyError("未知请求:" + rid)


def main():
    q = TransparentQueue(seed_avg_ms=800.0)
    p1, eta1 = q.enqueue("r1", now=0)
    assert (p1, eta1) == (1, 800), (p1, eta1)
    p2, eta2 = q.enqueue("r2", now=0)
    p3, eta3 = q.enqueue("r3", now=0)
    assert (p2, eta2) == (2, 1600) and (p3, eta3) == (3, 2400)
    # r2 只等了 500ms 就完成:均值 800 -> 650
    w = q.finish("r2", now=500)
    assert w == 500, w
    assert abs(q.avg_ms - 650.0) < 1e-9, q.avg_ms
    _, eta4 = q.enqueue("r4", now=510)
    assert eta4 == 1950, eta4   # 队列剩 r1 r3 r4,预估 3 x 650
    # r1 等了 1000ms:均值 650 -> 825,预估跟着近期真实耗时走
    w2 = q.finish("r1", now=1000)
    assert w2 == 1000, w2
    assert abs(q.avg_ms - 825.0) < 1e-9, q.avg_ms
    print("入队透明化: 位置3 预估 2400ms")
    print("完成反馈校正均值 800 -> 650 -> 825")
    print("用户看到的预估会随真实耗时收敛,而不是一成不变的拍脑袋值")


if __name__ == "__main__":
    main()
