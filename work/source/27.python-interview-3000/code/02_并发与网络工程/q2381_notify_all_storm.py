# -*- coding: utf-8 -*-
"""条件变量的广播唤醒风暴: notify_all 唤醒 N 人, 只有 1 人干成活。

- notify_all 无差别唤醒全部等待者, 每个醒来都要抢锁重查谓词;
- 一份资源被一个人拿走, 其余唤醒全是空转, 这就是惊群 herd effect;
- notify(1) 只唤醒一个, 唤醒次数等于成功次数, 系统总功最小。
"""
import threading
import time


class Slot:
    """最小可竞争资源槽: items 非空即谓词成立。"""

    def __init__(self):
        self.cond = threading.Condition()
        self.items = []
        self.wakeups = 0    # wait() 返回次数, 即被唤醒的次数
        self.success = 0    # 醒来后真的拿到资源的次数
        self.stop = False

    def consumer(self, name):
        while True:
            with self.cond:
                while not self.items and not self.stop:
                    self.cond.wait()
                    self.wakeups += 1        # 每次 wait 返回都是一次唤醒
                if self.items:
                    self.items.pop()
                    self.success += 1
                if self.stop:
                    return

    def produce_one(self, broadcast):
        with self.cond:
            self.items.append("job")
            if broadcast:
                self.cond.notify_all()
            else:
                self.cond.notify(1)

    def shutdown(self):
        with self.cond:
            self.stop = True
            self.cond.notify_all()


def run_round(n_consumers, broadcast):
    slot = Slot()
    threads = [threading.Thread(target=slot.consumer, args=(i,), daemon=True)
               for i in range(n_consumers)]
    for t in threads:
        t.start()
    time.sleep(0.2)          # 确保全部消费者已挂到 wait 上
    with slot.cond:
        assert len(slot.cond._waiters) == n_consumers, "消费者未全部挂起"
    slot.produce_one(broadcast)
    deadline = time.monotonic() + 2.0
    while slot.success < 1 and time.monotonic() < deadline:
        time.sleep(0.01)
    time.sleep(0.25)                  # 等这一轮被唤醒的消费者全部数完
    storm_wakeups = slot.wakeups      # 在 shutdown 唤醒之前快照, 只统计资源那轮
    slot.shutdown()
    for t in threads:
        t.join(timeout=1.0)
    return storm_wakeups, slot.success


def main():
    w1, s1 = run_round(5, broadcast=True)
    print("notify_all: 资源轮唤醒 %d 次, 成功 %d 次, 空转 %d 次" % (w1, s1, w1 - s1))
    w2, s2 = run_round(5, broadcast=False)
    print("notify(1) : 资源轮唤醒 %d 次, 成功 %d 次, 空转 %d 次" % (w2, s2, w2 - s2))
    assert s1 == 1 and s2 == 1, "两种方式最终都只应成功消费一份"
    assert w1 >= 5 and w2 == 1, "广播应唤醒全员, 精准通知只醒一人"


if __name__ == "__main__":
    main()
