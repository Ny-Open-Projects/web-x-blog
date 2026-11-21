# -*- coding: utf-8 -*-
"""监视器模式: 把不变量锁进类里。

- 不变量: balance 永远等于 history 的代数和;
- 裸类: 两个相关字段分两步写, 读者随时可能撞见"半截状态";
- 监视器: 所有读写都从同一扇门过, 不变量对外永远成立。
"""
import threading
import time

OPS = 800


class RawLedger:
    """无锁裸类: balance 与 history 分两步写, 中间是可见的半截状态。"""

    def __init__(self):
        self.balance = 0
        self.history = []

    def deposit(self, d):
        b = self.balance
        time.sleep(0)                    # 放大竞态窗口
        self.balance = b + d             # 第一步: 余额先变
        self.history.append(d)           # 第二步: 台账后记


class MonitorLedger:
    """监视器: 所有字段只被类自己的锁触碰, 不变量焊死在类内。"""

    def __init__(self):
        self._lock = threading.Lock()
        self._balance = 0
        self._history = []

    def deposit(self, d):
        with self._lock:
            self._balance += d
            self._history.append(d)      # 两步在锁内, 对外原子

    def consistent_snapshot(self):
        with self._lock:
            return self._balance, list(self._history)


def hammer_raw(ledger, done):
    d = 1
    for _ in range(OPS):
        ledger.deposit(d)
    done.set()


def check_raw(ledger, done, mismatches):
    while not done.is_set():
        bal = ledger.balance             # 读者裸读两个字段
        hist_sum = sum(ledger.history)
        if bal != hist_sum:
            mismatches[0] += 1


def hammer_monitor(ledger, done):
    for _ in range(OPS):
        ledger.deposit(1)
    done.set()


def check_monitor(ledger, done, mismatches):
    while not done.is_set():
        bal, hist = ledger.consistent_snapshot()
        if bal != sum(hist):
            mismatches[0] += 1


def run(ledger_cls, hammer_fn, check_fn):
    ledger = ledger_cls()
    done = threading.Event()
    mismatches = [0]
    ts = [threading.Thread(target=hammer_fn, args=(ledger, done))
          for _ in range(2)]
    cs = [threading.Thread(target=check_fn, args=(ledger, done, mismatches))
          for _ in range(2)]
    for t in ts + cs:
        t.start()
    for t in ts:
        t.join()
    done.set()
    for t in cs:
        t.join()
    return mismatches[0]


if __name__ == "__main__":
    raw_bad = run(RawLedger, hammer_raw, check_raw)
    mon_bad = run(MonitorLedger, hammer_monitor, check_monitor)
    print("裸类半截状态被读者撞见: %d 次" % raw_bad)
    print("监视器不变量被破坏: %d 次" % mon_bad)
    print("结论: 并发正确性是类的职责, 别指望调用方自己记得加锁")
