# -*- coding: utf-8 -*-
"""批量消费的窗口凑批: 数量到顶立即走, 时间到点也要走。

- 攒批的两个旋钮: max_batch 攒满冲刷, window 定时兜底;
- get(timeout=剩余窗口) 把两个条件统一在一个等待原语里, 不用额外的定时线程;
- 批的上限封死内存, 窗口封死单条最坏延迟, 两头都挂了保险。
"""
import queue
import threading
import time


class WindowBatcher:
    def __init__(self, max_batch, window_s):
        self.q = queue.Queue()
        self.max_batch = max_batch
        self.window_s = window_s
        self.flushed = []
        self.stop = False

    def flush(self, batch):
        if batch:
            self.flushed.append(batch)

    def run(self):
        while True:
            batch = []
            window_end = time.monotonic() + self.window_s
            while len(batch) < self.max_batch:
                remain = window_end - time.monotonic()
                if remain <= 0:
                    break                        # 窗口到点, 凑不满也走
                try:
                    item = self.q.get(timeout=remain)
                except queue.Empty:
                    break
                if item is None:                 # 关门哨兵: 停止接新件
                    self.stop = True
                    break
                batch.append(item)
            if batch:
                self.flush(batch)
            if self.stop and self.q.empty():
                return


def main():
    batches = []
    batcher = WindowBatcher(max_batch=4, window_s=0.25)
    batcher.flush = batches.append               # 观察用

    ct = threading.Thread(target=batcher.run, daemon=True)
    ct.start()

    # 场景一: 瞬时来 6 件, 应凑成 4+2, 第二批不等窗口
    for i in range(6):
        batcher.q.put(i)
    deadline = time.monotonic() + 1.0
    while len(batches) < 2 and time.monotonic() < deadline:
        time.sleep(0.01)
    print("数量驱动:", batches)
    assert batches[0] == [0, 1, 2, 3], "满 4 件立即冲刷"
    assert batches[1] == [4, 5], "剩余 2 件由窗口兜底"

    # 场景二: 只来 1 件, 等 0.25s 窗口到点也要走
    n_before = len(batches)
    batcher.q.put("孤儿件")
    t0 = time.monotonic()
    deadline = t0 + 1.5
    while len(batches) == n_before and time.monotonic() < deadline:
        time.sleep(0.01)
    cost = time.monotonic() - t0
    print("时间驱动: 单件等了 %.2fs 出批 %s" % (cost, batches[-1]))
    assert 0.2 < cost < 0.8, "单件应由窗口定时兜底, 不能无限等"
    assert batches[-1] == ["孤儿件"], "窗口出批内容正确"

    batcher.stop = True
    batcher.q.put(None)                          # 唤醒干等的循环
    ct.join(timeout=1.0)
    print("收工: 共 %d 批" % len(batches))


if __name__ == "__main__":
    main()
