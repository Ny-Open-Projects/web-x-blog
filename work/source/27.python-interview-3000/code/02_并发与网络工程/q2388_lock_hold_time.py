# -*- coding: utf-8 -*-
"""锁的持有时间统计装饰器: 先知道谁持锁太久, 再谈优化。

- 装饰器把锁内工作时间记进台账, 汇出调用次数与最大持有时长;
- 等锁一方的最大等待时间, 天然被最长持有时间托底;
- 持有时间的长尾比平均值重要, 尾部就是你所有等待者被卡住的上限。
"""
import threading
import time
from functools import wraps

stats = {}


def measured_hold(name):
    """装饰锁内工作函数: 统计每次执行的持有时长。"""

    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            t0 = time.monotonic()
            try:
                return fn(*args, **kwargs)
            finally:
                cost = time.monotonic() - t0
                rec = stats.setdefault(name, {"n": 0, "total": 0.0, "max": 0.0})
                rec["n"] += 1
                rec["total"] += cost
                rec["max"] = max(rec["max"], cost)
        return wrapper
    return deco


class Store:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}
        self.observed_waits = []

    @measured_hold("store.write")
    def _write(self, key, value):
        time.sleep(value)                    # 模拟锁内真实工作耗时

    def write(self, key, value):
        with self.lock:
            self._write(key, value)

    def write_with_probe(self, key, value):
        t0 = time.monotonic()
        with self.lock:
            self.observed_waits.append(time.monotonic() - t0)
            self._write(key, value)


def main():
    store = Store()
    holds = [0.06] + [0.005] * 6             # 一长在先, 六短排队, 长尾才是主角

    threads = [threading.Thread(target=store.write_with_probe,
                                args=("k%d" % i, h))
               for i, h in enumerate(holds)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    rec = stats["store.write"]
    print("持锁台账: 次数 %d, 平均 %.1fms, 最大 %.1fms" %
          (rec["n"], rec["total"] / rec["n"] * 1000, rec["max"] * 1000))
    waits = sorted(store.observed_waits)
    print("等锁观测: 最大等待 %.1fms, 各次等待 %s" %
          (waits[-1] * 1000, ["%.0f" % (w * 1000) for w in waits]))
    assert rec["n"] == len(holds), "每次锁内工作都应入账"
    assert waits[-1] >= rec["max"] * 0.85, \
        "最大等待应接近最长持有时长, 长尾持锁拖住所有等待者"


if __name__ == "__main__":
    main()
