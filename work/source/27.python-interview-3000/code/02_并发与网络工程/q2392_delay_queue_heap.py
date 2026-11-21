# -*- coding: utf-8 -*-
"""延迟队列的堆实现: 到期时间在堆顶, 没到期就按最近到期点小睡。

- 堆按 (到期时刻, 序号) 排序, 堆顶永远是最近要醒的任务;
- 消费者 peek 堆顶: 没到期就 wait(剩余时间), 有新任务且更早则被推醒重算;
- 序号用来打破同刻并列, 保证同刻任务按入队顺序执行, 堆比较也不碰负载。
"""
import heapq
import threading
import time


class DelayQueue:
    def __init__(self):
        self._heap = []
        self._seq = 0
        self._cond = threading.Condition()
        self._closed = False

    def put(self, item, delay_s):
        with self._cond:
            heapq.heappush(self._heap,
                           (time.monotonic() + delay_s, self._seq, item))
            self._seq += 1
            self._cond.notify_all()          # 新任务可能比堆顶更早

    def take(self):
        """取一个到期任务, 关闭后返回 None。"""
        with self._cond:
            while True:
                if self._closed and not self._heap:
                    return None
                if self._heap:
                    remain = self._heap[0][0] - time.monotonic()
                    if remain <= 0:
                        return heapq.heappop(self._heap)[2]
                    self._cond.wait(timeout=remain)   # 睡到最近的到期点
                else:
                    self._cond.wait(timeout=0.1)

    def close(self):
        with self._cond:
            self._closed = True
            self._cond.notify_all()


def main():
    dq = DelayQueue()
    fired = []

    def consumer():
        while True:
            item = dq.take()
            if item is None:
                return
            fired.append((item, time.monotonic()))

    ct = threading.Thread(target=consumer, daemon=True)
    ct.start()
    t0 = time.monotonic()
    dq.put("慢件-0.5s", 0.5)
    dq.put("快件-0.1s", 0.1)
    dq.put("中件-0.3s", 0.3)
    dq.put("追件-0.05s", 0.05)               # 后发的最早到期, 要能顶到堆顶
    deadline = time.monotonic() + 1.5
    while len(fired) < 4 and time.monotonic() < deadline:
        time.sleep(0.01)
    dq.close()
    ct.join(timeout=1.0)

    order = [name for name, _ in fired]
    print("执行顺序:", order)
    for name, at in fired:
        print("  %s 在投递后 %.2fs 触发" % (name, at - t0))
    assert order == ["追件-0.05s", "快件-0.1s", "中件-0.3s", "慢件-0.5s"], \
        "执行顺序应按到期时刻, 而非投递顺序"


if __name__ == "__main__":
    main()
