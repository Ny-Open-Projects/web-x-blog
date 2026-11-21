# -*- coding: utf-8 -*-
"""有界队列满策略三选一实测: 阻塞、丢最老、丢最新。

- 队满时只有三种回答: 阻塞等、丢最老留新、丢最新保旧;
- 丢最老适合监控指标类数据, 新值永远比旧值有信息量;
- 丢最新适合任务队列, 排队的活不能凭空消失, 宁可拒绝新请求。
"""
import queue
import threading
import time


def consume_slowly(q, n, item_s):
    """慢消费者: 每件耗时 item_s 秒。"""
    got = []
    for _ in range(n):
        try:
            got.append(q.get(timeout=2.0))
        except queue.Empty:
            break
        time.sleep(item_s)
    return got


def policy_block(cap, items, item_s):
    q = queue.Queue(maxsize=cap)
    out = []

    def producer():
        for it in items:
            q.put(it)                        # 队满就睡, 天然背压
        q.put(None)

    t = threading.Thread(target=producer, daemon=True)
    t.start()
    out = consume_slowly(q, len(items) + 1, item_s)
    t.join(timeout=5)
    return out


def policy_drop(q, item, side):
    """side='old' 丢最老, side='new' 丢最新。"""
    if side == "old":
        try:
            q.get_nowait()                   # 挤掉队头
        except queue.Empty:
            pass
        q.put_nowait(item)
    else:
        try:
            q.put_nowait(item)               # 放不进就算了
        except queue.Full:
            pass
    return q


def run_drop(cap, items, item_s, side):
    q = queue.Queue(maxsize=cap)
    dropped = []

    def producer():
        for it in items:
            if side == "old":
                if q.full():
                    dropped.append(q.get_nowait())
                q.put_nowait(it)
            else:
                if q.full():
                    dropped.append(it)
                else:
                    q.put_nowait(it)
        q.put(None)

    threading.Thread(target=producer, daemon=True).start()
    out = consume_slowly(q, len(items) + 1, item_s)
    return out, dropped


def main():
    items = ["m%d" % i for i in range(8)]

    out = policy_block(3, items, 0.05)
    print("阻塞  : 收到 %d 件, 顺序完整, 一件不丢但生产者被拖住" %
          len([x for x in out if x]))
    assert [x for x in out if x] == items, "阻塞策略不该丢数据"

    out, dropped = run_drop(3, items, 0.05, "old")
    print("丢最老: 收到 %s" % out[:-1])
    print("       被挤掉 %s" % dropped)
    assert "m0" in dropped and "m7" not in dropped, "丢最老应保住新数据"

    out, dropped = run_drop(3, items, 0.05, "new")
    print("丢最新: 收到 %s" % out[:-1])
    print("       被拒收 %s" % dropped)
    assert "m0" not in dropped and "m7" in dropped, "丢最新应保住旧数据"


if __name__ == "__main__":
    main()
