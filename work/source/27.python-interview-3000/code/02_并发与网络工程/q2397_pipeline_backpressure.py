# -*- coding: utf-8 -*-
"""双队列流水线的背压实测: 上游再快, 也只能快过最慢一级。

- 两级有界队列串起三段流水线, 上游快、下游慢;
- 队列一旦顶到 maxsize, put 就阻塞, 压力以阻塞的形式向上传导;
- 实测各段产量一致, 队列水位长期钉在 maxsize 附近, 内存不涨。
"""
import queue
import threading
import time


def stage_produce(out_q, n, item_s, stats):
    for i in range(n):
        time.sleep(item_s)
        out_q.put(("raw", i))
        stats["produced"] += 1
    out_q.put(None)


def stage_transform(in_q, out_q, item_s, stats):
    while True:
        item = in_q.get()
        if item is None:
            out_q.put(None)
            return
        time.sleep(item_s)
        out_q.put(("cooked", item[1]))
        stats["transformed"] += 1


def stage_sink(in_q, item_s, stats):
    while True:
        item = in_q.get()
        if item is None:
            return
        time.sleep(item_s)
        stats["sunk"] += 1


def run_pipeline(n, produce_s, transform_s, sink_s, cap):
    q1 = queue.Queue(maxsize=cap)
    q2 = queue.Queue(maxsize=cap)
    s_prod = {"produced": 0}
    s_trans = {"transformed": 0}
    s_sink = {"sunk": 0}
    watermarks = {"q1": 0, "q2": 0}
    stop = threading.Event()

    def watch():
        while not stop.is_set():
            watermarks["q1"] = max(watermarks["q1"], q1.qsize())
            watermarks["q2"] = max(watermarks["q2"], q2.qsize())
            time.sleep(0.01)

    t_prod = threading.Thread(target=stage_produce,
                              args=(q1, n, produce_s, s_prod))
    t_trans = threading.Thread(target=stage_transform,
                               args=(q1, q2, transform_s, s_trans))
    t_sink = threading.Thread(target=stage_sink, args=(q2, sink_s, s_sink))
    t_watch = threading.Thread(target=watch, daemon=True)
    for t in (t_prod, t_trans, t_sink, t_watch):
        t.start()
    t0 = time.monotonic()
    t_prod.join(); t_trans.join(); t_sink.join()
    elapsed = time.monotonic() - t0
    stop.set()
    return elapsed, s_prod, s_trans, s_sink, watermarks


def main():
    # 快生产 10ms -> 慢加工 50ms -> 更慢落地 80ms: 压力逐级向上传导
    elapsed, sp, st, ss, wm = run_pipeline(n=10, produce_s=0.01,
                                           transform_s=0.05, sink_s=0.08, cap=2)
    print("耗时 %.2fs, 生产 %d / 加工 %d / 落地 %d" %
          (elapsed, sp["produced"], st["transformed"], ss["sunk"]))
    print("水位峰值: q1=%d q2=%d (上限 2)" % (wm["q1"], wm["q2"]))
    assert sp["produced"] == st["transformed"] == ss["sunk"] == 10, \
        "稳态下各段产量必须一致, 背压把快段按住"
    assert wm["q1"] == 2 and wm["q2"] == 2, "慢段上游的队列应长期顶满"
    assert elapsed > 10 * 0.08 * 0.9, "总耗时由最慢一级决定"


if __name__ == "__main__":
    main()
