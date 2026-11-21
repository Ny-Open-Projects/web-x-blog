# -*- coding: utf-8 -*-
"""Condition.wait_for 的超时等待: 醒来必查谓词, 超时也要拿证据。

- wait_for(pred, timeout) 内部循环重查谓词, 帮你挡掉虚假唤醒;
- 返回值就是谓词现值: True 表示条件成立, False 表示到点仍不成立;
- 超时不是异常, 是"拿不到就带着证据返回"的快速失败。
"""
import threading
import time


class Box:
    """最小的一次性信箱: item 非空即谓词成立。"""

    def __init__(self):
        self.cv = threading.Condition()
        self.item = None

    def put(self, v):
        with self.cv:
            self.item = v
            self.cv.notify_all()

    def take(self, timeout):
        with self.cv:
            ok = self.cv.wait_for(lambda: self.item is not None, timeout)
            if ok:
                v, self.item = self.item, None
                return v, True
            # 到点仍为空: 谓词现值就是证据, 不能想当然当它有货
            return None, False


if __name__ == "__main__":
    # 场景一: 生产者迟到但赶在预算内, 消费者等到货
    box1 = Box()
    results = {}

    def late_producer():
        time.sleep(0.15)
        box1.put("包裹")

    threading.Thread(target=late_producer).start()
    t0 = time.perf_counter()
    results["s1"], results["s1_ok"] = box1.take(timeout=0.5)
    results["s1_wait"] = time.perf_counter() - t0
    print("场景一: 等到 %r, 谓词=%s, 实等 %.2fs" %
          (results["s1"], results["s1_ok"], results["s1_wait"]))

    # 场景二: 没有生产者, 到点超时, 谓词为 False
    box2 = Box()
    t0 = time.perf_counter()
    v, ok = box2.take(timeout=0.2)
    elapsed = time.perf_counter() - t0
    print("场景二: 拿到 %r, 谓词=%s, 实等 %.2fs(约等于预算)" % (v, ok, elapsed))

    # 场景三: 超时后货又到了, 证明"超时返回"不影响之后取货
    def very_late_producer():
        time.sleep(0.3)
        box2.put("迟到的包裹")

    threading.Thread(target=very_late_producer).start()
    v, ok = box2.take(timeout=0.05)      # 先超时一次
    v2, ok2 = box2.take(timeout=1.0)     # 再等一次
    print("场景三: 第一次取 %r(ok=%s), 第二次取 %r(ok=%s)" % (v, ok, v2, ok2))
