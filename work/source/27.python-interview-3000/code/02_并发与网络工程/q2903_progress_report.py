# -*- coding: utf-8 -*-
"""跨线程的进度上报: 工作线程干活, 主线程看板。

- 进度账本一把锁: 工作线程 step 加数, 主线程 snapshot 拿只读快照;
- 快照是一次字典拷贝, 渲染进度条时不会与工作线程互相阻塞;
- 每个任务单独计数, 汇总口径随时可算 (完成数 / 总数 / 完成率)。
"""
import threading
import time


class Progress:
    """线程安全的进度账本。"""

    def __init__(self, totals):
        self._lock = threading.Lock()
        self._done = dict.fromkeys(totals, 0)
        self._total = dict(totals)

    def step(self, task, n=1):
        with self._lock:
            self._done[task] += n

    def finish(self, task):
        with self._lock:
            self._done[task] = self._total[task]

    def snapshot(self):
        with self._lock:
            return {k: (v, self._total[k]) for k, v in self._done.items()}

    def total_of(self, task):
        with self._lock:
            return self._total[task]


def render_bar(done, total, width=20):
    filled = int(width * done / total)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def worker(prog, task, per_item):
    """工作线程: 每做完一件就上报一次。"""
    total = prog.total_of(task)
    for _ in range(total):
        time.sleep(per_item)
        prog.step(task)


if __name__ == "__main__":
    totals = {"下载": 30, "转码": 18, "上传": 12}
    prog = Progress(totals)
    ts = [threading.Thread(target=worker, args=(prog, name, speed), daemon=True)
          for name, speed in (("下载", 0.004), ("转码", 0.007), ("上传", 0.010))]
    for t in ts:
        t.start()

    polls = 0
    while any(t.is_alive() for t in ts):
        snap = prog.snapshot()
        line = " | ".join("%s %s %d/%d" % (name, render_bar(d, n), d, n)
                          for name, (d, n) in snap.items())
        polls += 1
        if polls % 4 == 1:             # 每 4 个轮询打一行, 输出别刷屏
            print("t=%.2fs %s" % (polls * 0.05, line))
        time.sleep(0.05)

    for t in ts:
        t.join()
    snap = prog.snapshot()
    print("最终:", " | ".join("%s %d/%d" % (n, d, t) for n, (d, t) in snap.items()))
    assert all(d == t for d, t in snap.values()), "进度账本与实际不符"
    print("轮询 %d 次, 账实相符" % polls)
    print("要点: 上报是加法, 展示是快照, 两边各走各的锁互不拖累")
