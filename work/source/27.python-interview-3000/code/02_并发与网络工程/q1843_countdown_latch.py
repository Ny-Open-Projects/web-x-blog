# -*- coding: utf-8 -*-
"""倒计时闩锁 CountDownLatch: 一次性计数到零的汇聚点。

- 与 Event 的差别: Event 是二态开关且天然可重置, Latch 表达 "还差几个" 的量化语义;
- count_down 只减不增, 到零后对所有人永久放行, wait 支持 timeout 非阻塞探测;
- 典型用途: 主流程等 n 个子系统就绪、汇聚多个并行任务的完成信号。
"""
import threading
import time


class CountDownLatch:
    def __init__(self, n):
        assert n >= 0
        self._cond = threading.Condition()
        self._count = n

    def count_down(self):
        with self._cond:
            if self._count > 0:
                self._count -= 1
                if self._count == 0:
                    self._cond.notify_all()   # 到零广播放行

    def wait(self, timeout=None):
        with self._cond:
            deadline = None if timeout is None else time.monotonic() + timeout
            while self._count > 0:
                if deadline is None:
                    self._cond.wait(0.5)
                else:
                    remain = deadline - time.monotonic()
                    if remain <= 0:
                        return False
                    self._cond.wait(remain)
            return True

    @property
    def count(self):
        with self._cond:
            return self._count


def main():
    # 场景一: 主线程等 3 个子系统就绪
    latch = CountDownLatch(3)
    ready_log = []

    def subsystem(name, cost):
        time.sleep(cost)
        ready_log.append(name)
        latch.count_down()

    for name, cost in [("db", 0.05), ("cache", 0.03), ("config", 0.08)]:
        threading.Thread(target=subsystem, args=(name, cost)).start()

    t0 = time.monotonic()
    ok = latch.wait(timeout=2.0)
    print("三个子系统就绪:", ready_log, "等待耗时: %.2fs" % (time.monotonic() - t0))
    assert ok and latch.count == 0, "latch 应当计数到零"

    # 场景二: 只有一个倒计时者, 探测超时返回 False 而不是抛异常
    latch2 = CountDownLatch(2)
    threading.Thread(target=latch2.count_down).start()
    ok2 = latch2.wait(timeout=0.2)
    print("缺一个倒计时者, 带超时 wait 返回:", ok2, "剩余计数:", latch2.count)
    assert ok2 is False and latch2.count == 1, "超时应返回 False 且计数不变"

    # 对照: Event 无法表达 "还差几个", 只能表达 "发生了没有"
    ev = threading.Event()
    print("对照 Event: 只有 set/clear 两态, 数不了进度")
    print("结论: Latch = 带计数的单次汇聚点, 超时探测返回 False 不抛异常")


if __name__ == "__main__":
    main()
