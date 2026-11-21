"""Q2589 队列满时按优先级拒绝:低价值请求让位或被拒。

有界优先级队列的双出口设计:高优先级到来挤掉堆里最差的,
新来的低优先级直接拒收;堆顶永远是最不值钱的请求,替换用
heapreplace 一次完成,拒绝与驱逐都要留指标。
"""
import heapq


class BoundedPQ:
    def __init__(self, capacity):
        self.cap = capacity
        self._h = []          # 存负优先级:堆顶恒为最不值钱的请求
        self._seq = 0
        self.evicted = []
        self.rejected = 0

    def push(self, item, priority):
        if len(self._h) < self.cap:
            heapq.heappush(self._h, (-priority, self._seq, item))
            self._seq += 1
            return "queued"
        worst = self._h[0]  # 堆顶是优先级数字最大即最不值钱的
        if priority < -worst[0]:
            heapq.heapreplace(self._h, (-priority, self._seq, item))
            self._seq += 1
            self.evicted.append(worst[2])
            return "evicted-lowest"
        self.rejected += 1
        return "rejected"

    def drain(self):
        raw = [(-negp, s, it)
               for negp, s, it in (heapq.heappop(self._h) for _ in range(len(self._h)))]
        raw.sort()
        return [it for _, _, it in raw]


def main():
    q = BoundedPQ(3)
    assert q.push("a-low", 9) == "queued"
    assert q.push("b-mid", 5) == "queued"
    assert q.push("c-low", 8) == "queued"
    assert q.push("d-high", 1) == "evicted-lowest"   # 挤掉 a-low
    assert q.evicted == ["a-low"], q.evicted
    assert q.push("e-worst", 10) == "rejected"
    assert q.rejected == 1
    drained = q.drain()
    assert drained == ["d-high", "b-mid", "c-low"], drained
    print("被挤掉:", q.evicted, "被拒收:", q.rejected)
    print("最终队列:", drained)


if __name__ == "__main__":
    main()
