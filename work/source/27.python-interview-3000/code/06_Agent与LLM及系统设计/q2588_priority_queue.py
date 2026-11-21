"""Q2588 请求优先级队列的实现:heapq 加序列号保稳定。

优先级队列的核心实现细节:heapq 是最小堆,数字越小越先出;
同优先级时元组比较会落到第三项 item 上,顺序由字典序决定,
这是运气不是契约——必须补一个单调递增 seq 保证 FIFO 稳定。
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._h = []
        self._seq = 0

    def push(self, item, priority):
        heapq.heappush(self._h, (priority, self._seq, item))
        self._seq += 1

    def pop(self):
        if not self._h:
            raise IndexError("queue empty")
        _, _, item = heapq.heappop(self._h)
        return item

    def __len__(self):
        return len(self._h)


def main():
    q = PriorityQueue()
    q.push("low-1", 5)
    q.push("high-1", 1)
    q.push("low-2", 5)
    q.push("high-2", 1)
    out = [q.pop() for _ in range(4)]
    assert out == ["high-1", "high-2", "low-1", "low-2"], out
    # 对照:无 seq 的堆,同优先级按 item 字典序出队,语义不可控
    h = []
    for name, p in [("zz", 5), ("aa", 5)]:
        heapq.heappush(h, (p, name))
    assert heapq.heappop(h)[1] == "aa"   # 字典序,不是到达序
    try:
        q.pop()
        raise SystemExit(1)
    except IndexError as exc:
        print("空队列弹出被拒:", exc)
    print("带 seq 的出队序:", out, "← 同级按到达序,跨级按优先级")


if __name__ == "__main__":
    main()
